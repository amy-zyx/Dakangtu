"""
Rita v2 - 加强 anti-purple，锁眼色，一次出 4 张
"""
import urllib.request, ssl, json, urllib.parse, time, os
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
BASE = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_rita_v2'
os.makedirs(OUT_DIR, exist_ok=True)

POSITIVE = """masterpiece, best quality, 2D galgame style, anime, cel shading,
flat color blocks, clean line art, black outlines, soft lighting,

1girl, solo, 19 years old, asian female,
petite build, slim body, slender long legs, 163cm height impression,
small oval face, delicate features, porcelain skin, fair skin,

HAIR_COLOR_LOCK: jet black hair, true black hair, ink black hair, charcoal black hair,
NO purple, NO violet, NO magenta, NO lavender, NO blue, NO highlights,
pure solid black hair color throughout, no colored hair highlights, monochrome hair,
hair shine must be GRAY or WHITE only, never any color tint,

long straight black hair, hair down to chest length, center part, middle part bangs,
hair on both sides of face framing face, side-swept long strands,

EYE_COLOR_LOCK: dark brown eyes, black-brown eyes, deep brown irises,
NO purple eyes, NO violet eyes, NO magenta eyes, NO pink eyes,
solid dark brown iris, black pupil,
large almond eyes, gentle eyes, quiet gaze, slightly downcast,
thin natural eyebrows, small nose, soft thin lips, light pink lips,

expression: gentle, calm, slightly shy, reserved, delicate and moving,

wearing: mustard yellow wool coat, double-breasted long coat,
knee-length, beige turtleneck underneath,
wearing: opaque black velvet tights, fleece-lined tights, warm texture, thick tights,
wearing: black ankle boots, low heel,

full body standing, front view, hands at sides,
slight smile, looking at viewer,
plain white background, character reference sheet
"""

NEGATIVE = """3D, semi-realistic, photorealistic, photo, photographic,
gradient heavy shading, complex background, scenery, indoor, outdoor,
purple, violet, magenta, lavender, blue, pink, teal, green, red hair highlights,
purple hair, violet hair, magenta hair, lavender hair, blue hair, pink hair,
hair color tint, colored hair, dyed hair, highlighted hair, gradient hair,
purple eyes, violet eyes, magenta eyes, pink eyes, lavender eyes, blue eyes,
lolita, sexy, seductive, revealing, nsfw, nude, naked, exposed skin,
chibi, loli, child,
deformed, bad anatomy, extra fingers, mutated hands, blurry, low quality,
text, watermark, signature, multiple girls, crowd,
sheer stockings, transparent stockings, silk stockings, nylon,
shorts, skirt, miniskirt, summer clothes, sleeveless
"""

def build_workflow(seed):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_edit_2511_bf16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen/qwen_2.5_vl_7b.safetensors", "type": "qwen_image"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
        "4": {"class_type": "LoraLoader", "inputs": {"model": ["1", 0], "clip": ["2", 0], "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors", "strength_model": 1.0, "strength_clip": 1.0}},
        "5": {"class_type": "ModelSamplingFlux", "inputs": {"model": ["4", 0], "max_shift": 3.5, "base_shift": 1.0, "width": 1024, "height": 1536}},
        "6": {"class_type": "TextEncodeQwenImageEdit", "inputs": {"clip": ["4", 1], "prompt": POSITIVE}},
        "7": {"class_type": "TextEncodeQwenImageEdit", "inputs": {"clip": ["4", 1], "prompt": NEGATIVE}},
        "8": {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1536, "batch_size": 1}},
        "9": {"class_type": "KSampler", "inputs": {"model": ["5", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0], "seed": seed, "steps": 4, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
        "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 0]}},
        "11": {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": f"rita_v2_s{seed}"}}
    }

def submit(workflow):
    client_id = str(uuid.uuid4())
    payload = json.dumps({"prompt": workflow, "client_id": client_id}).encode('utf-8')
    req = urllib.request.Request(BASE + '/prompt', data=payload, headers={'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        return json.loads(resp.read()).get('prompt_id')
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'ignore')
        print(f'!! 400: {body[:500]}')
        return None

def wait_and_download(prompt_id, prefix):
    for i in range(180):
        time.sleep(3)
        try:
            hr = urllib.request.urlopen(BASE + f'/history/{prompt_id}', timeout=8, context=ctx)
            hist = json.loads(hr.read())
        except Exception:
            continue
        if hist and prompt_id in hist:
            outputs = hist[prompt_id].get('outputs', {})
            for node_out in outputs.values():
                if 'images' in node_out:
                    for img in node_out['images']:
                        fn = img['filename']
                        sub = img.get('subfolder', '')
                        tp = img.get('type', 'output')
                        url = f'{BASE}/view?filename={urllib.parse.quote(fn)}&subfolder={urllib.parse.quote(sub)}&type={tp}'
                        local = os.path.join(OUT_DIR, fn)
                        with urllib.request.urlopen(url, timeout=60, context=ctx) as r:
                            with open(local, 'wb') as f:
                                f.write(r.read())
                        print(f'  [OK] {fn} ({os.path.getsize(local)//1024} KB)')
            return True
    return False

import uuid
seeds = [101, 202, 303, 404]
print('=== Rita v2 批量提交 (4 张) ===')
for s in seeds:
    print(f'\n--- seed={s} ---')
    wf = build_workflow(s)
    pid = submit(wf)
    if not pid:
        continue
    print(f'  prompt_id={pid}')
    if wait_and_download(pid, f's{s}'):
        print(f'  seed={s} 完成')
    else:
        print(f'  seed={s} 超时')

print(f'\n=== 全部完成，结果在 {OUT_DIR} ===')
for f in sorted(os.listdir(OUT_DIR)):
    print(' ', f)
