"""
Yuzu Soft 纯风格 v1 - 不锁脸，看风格是否到位
栈: Illustrious 底模 + Yuzu Soft[style]-Illus LoRA
"""
import urllib.request, json, urllib.parse, time, os
BASE = 'http://127.0.0.1:8188'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_v1'
os.makedirs(OUT_DIR, exist_ok=True)

POSITIVE = """masterpiece, best quality, yuzusoft style, yuzu soft style,
anime, 2D galgame style, illustration,
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
normal quality, jpeg artifacts, signature, watermark, username, blurry,
3d, realistic, photorealistic, photo, gradient heavy shading,
multiple girls, crowd, busy background,
purple hair, violet hair, magenta hair, lavender hair, blue hair, pink hair,
purple eyes, violet eyes, pink eyes, lavender eyes,
sheer stockings, transparent stockings, silk stockings, nylon,
shorts, skirt, miniskirt, summer clothes, sleeveless
"""

def build(seed):
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "Illustrious\\ILFlatMix.safetensors"}},
        "2": {"class_type": "LoraLoader", "inputs": {
            "model": ["1", 0], "clip": ["1", 1],
            "lora_name": "Yuzu Soft[style]-Illus.safetensors",
            "strength_model": 0.85, "strength_clip": 0.85
        }},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 1], "text": POSITIVE}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 1], "text": NEGATIVE}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {
            "model": ["2", 0], "positive": ["3", 0], "negative": ["4", 0],
            "latent_image": ["5", 0], "seed": seed, "steps": 28, "cfg": 7.0,
            "sampler_name": "euler_ancestral", "scheduler": "normal", "denoise": 1.0
        }},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": f"yuzu_v1_s{seed}"}}
    }

def submit(wf):
    payload = json.dumps({"prompt": wf, "client_id": "yuzu-v1"}).encode('utf-8')
    req = urllib.request.Request(BASE + '/prompt', data=payload, headers={'Content-Type': 'application/json'})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        return json.loads(r.read()).get('prompt_id')
    except urllib.error.HTTPError as e:
        return f'ERR:{e.code}:' + e.read().decode('utf-8', 'ignore')[:300]

def wait(pid):
    for i in range(180):
        time.sleep(2)
        try:
            r = urllib.request.urlopen(BASE + f'/history/{pid}', timeout=8)
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
                    with urllib.request.urlopen(url, timeout=60) as rr:
                        with open(local, 'wb') as f:
                            f.write(rr.read())
                    print(f'  [OK] {fn} ({os.path.getsize(local)//1024} KB)')
            return True
    return False

for s in [11, 22, 33, 44]:
    print(f'\n--- seed={s} ---')
    pid = submit(build(s))
    if isinstance(pid, str) and pid.startswith('ERR'):
        print('  提交失败:', pid)
        continue
    print(f'  prompt_id={pid}')
    if wait(pid):
        print(f'  seed={s} 完成')

print(f'\n=== 结果: {OUT_DIR} ===')
for f in sorted(os.listdir(OUT_DIR)):
    print(' ', f)
