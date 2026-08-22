"""
云端备用方案：用 PanelPainter_v3_Qwen2511 试 Yuzu 类似风格
栈: Qwen-Image-Edit 2511 + Lightning 4 步 + PanelPainter v3
"""
import urllib.request, json, urllib.parse, time, os
BASE = 'https://8188-cpod-1ud2p6nylymq.pod.compshare.cn'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_panel_v1'
os.makedirs(OUT_DIR, exist_ok=True)

POSITIVE = """masterpiece, best quality, yuzusoft style, yuzu soft style,
anime, 2D galgame style, illustration, panel art,
1girl, solo, 19 years old, asian female,
petite build, slim body, slender long legs, 163cm height,
small oval face, delicate features, porcelain skin, fair skin,

HAIR: jet black hair, ink black hair, charcoal black hair, no purple tint,
pure solid black hair, no highlights, monochrome black hair,
long straight hair, hair down to chest length,
center part, middle part bangs, no fringe,
hair on both sides of face framing face, side-swept long strands,

EYES: dark brown eyes, black-brown eyes, deep brown irises,
large almond eyes, gentle eyes, quiet gaze, slightly downcast,
thin natural eyebrows, small nose, soft thin lips, light pink lips,

expression: gentle, calm, slightly shy, reserved, delicate and moving,

wearing: mustard yellow wool coat, double-breasted long coat, knee-length,
beige turtleneck underneath,
wearing: opaque black velvet tights, fleece-lined tights, warm texture,
wearing: black ankle boots, low heel,

full body standing, front view, hands at sides,
slight smile, looking at viewer,
plain white background, character reference sheet
"""

NEGATIVE = """lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
jpeg artifacts, signature, watermark, username, blurry,
3d, realistic, photorealistic, photo, gradient heavy shading,
multiple girls, crowd, busy background,
purple hair, violet hair, magenta hair, lavender hair, blue hair, pink hair,
purple eyes, violet eyes, pink eyes, lavender eyes,
sheer stockings, transparent stockings, silk stockings, nylon,
shorts, skirt, miniskirt, summer clothes, sleeveless
"""

def build(seed):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_edit_2511_bf16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors", "type": "qwen_image"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
        "4": {"class_type": "LoraLoader", "inputs": {
            "model": ["1", 0], "clip": ["2", 0],
            "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors",
            "strength_model": 1.0, "strength_clip": 1.0
        }},
        "5": {"class_type": "LoraLoader", "inputs": {
            "model": ["4", 0], "clip": ["4", 1],
            "lora_name": "PanelPainter_v3_Qwen2511.safetensors",
            "strength_model": 0.7, "strength_clip": 0.7
        }},
        "6": {"class_type": "ModelSamplingFlux", "inputs": {"model": ["5", 0], "max_shift": 3.5, "base_shift": 1.0, "width": 1024, "height": 1536}},
        "7": {"class_type": "TextEncodeQwenImageEdit", "inputs": {"clip": ["5", 1], "prompt": POSITIVE}},
        "8": {"class_type": "TextEncodeQwenImageEdit", "inputs": {"clip": ["5", 1], "prompt": NEGATIVE}},
        "9": {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1536, "batch_size": 1}},
        "10": {"class_type": "KSampler", "inputs": {
            "model": ["6", 0], "positive": ["7", 0], "negative": ["8", 0],
            "latent_image": ["9", 0], "seed": seed, "steps": 4, "cfg": 1.0,
            "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0
        }},
        "11": {"class_type": "VAEDecode", "inputs": {"samples": ["10", 0], "vae": ["3", 0]}},
        "12": {"class_type": "SaveImage", "inputs": {"images": ["11", 0], "filename_prefix": f"cloud_panel_v1_s{seed}"}}
    }

def submit(wf):
    payload = json.dumps({"prompt": wf, "client_id": "panel-v1"}).encode('utf-8')
    req = urllib.request.Request(BASE + '/prompt', data=payload, headers={'Content-Type': 'application/json'})
    try:
        r = urllib.request.urlopen(req, timeout=30, context=__import__('ssl').create_default_context())
        return json.loads(r.read()).get('prompt_id')
    except urllib.error.HTTPError as e:
        return f'ERR:{e.code}:' + e.read().decode('utf-8', 'ignore')[:300]

def wait(pid):
    import ssl
    ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    for i in range(60):
        time.sleep(1)
        try:
            r = urllib.request.urlopen(BASE + f'/history/{pid}', timeout=5, context=ctx)
            hist = json.loads(r.read())
        except Exception:
            continue
        if hist and pid in hist:
            outputs = hist[pid].get('outputs', {})
            for node_out in outputs.values():
                for img in node_out.get('images', []):
                    fn = img['filename']
                    sub = img.get('subfolder', '')
                    tp = img.get('type', 'output')
                    url = f'{BASE}/view?filename={urllib.parse.quote(fn)}&subfolder={urllib.parse.quote(sub)}&type={tp}'
                    local = os.path.join(OUT_DIR, fn)
                    with urllib.request.urlopen(url, timeout=60, context=ctx) as rr:
                        with open(local, 'wb') as f:
                            f.write(rr.read())
                    print(f'  [OK] {fn} ({os.path.getsize(local)//1024} KB)')
            return True
    return False

import ssl
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
for s in [101, 202, 303]:
    print(f'\n--- seed={s} ---')
    pid = submit(build(s))
    if isinstance(pid, str) and pid.startswith('ERR'):
        print('  提交失败:', pid); continue
    print(f'  prompt_id={pid}')
    t0 = time.time()
    if wait(pid):
        print(f'  用时 {time.time()-t0:.1f}s')
    else:
        print(f'  超时')

print(f'\n=== 结果: {OUT_DIR} ===')
for f in sorted(os.listdir(OUT_DIR)):
    print(' ', f)
