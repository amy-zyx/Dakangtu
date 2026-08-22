"""本地 8188 跑 Yuzu SDXL workflow (4 步加速)"""
import urllib.request, json, urllib.parse, time, os
BASE = 'http://127.0.0.1:8188'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_local_sdxl'
os.makedirs(OUT_DIR, exist_ok=True)

POSITIVE = """masterpiece, best quality, yuzusoft style, yuzu soft style,
official art, sophisticated, elegant, refined, intricate detail, sharp focus, detailed face,
anime, 2D galgame visual novel style, PC game CG, high resolution illustration,
1girl, solo, single character, 19 years old, asian female,
petite build, slim body, slender long legs, 163cm,
small oval face, delicate mature features, porcelain skin, fair skin,

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
wearing: opaque jet black solid tights, opaque pitch black tights, NOT sheer, NOT silk, NOT transparent, fleece-lined, warm texture,
wearing: black ankle boots, low heel, short boots,

full body standing, front view, hands at sides,
slight smile, looking at viewer,
plain white background
"""

NEGATIVE = """lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
jpeg artifacts, signature, watermark, username, blurry,
3d, realistic, photorealistic, photo, gradient heavy shading,
multiple girls, two girls, twin, mirror image, side by side,
character sheet, character reference sheet, reference sheet, multiple views, turnaround, concept art, turnaround sheet, model sheet,
crowd, busy background,
chibi, kawaii, super deformed, SD, deformed, childlike, loli, child, young child, baby, toddler, simple shading, flat shading, sticker, mascot,
purple hair, violet hair, magenta hair, lavender hair, blue hair, pink hair, brown hair,
purple eyes, violet eyes, pink eyes, lavender eyes,
brown tights, tan tights, beige tights, brown legs, tan legs, olive legs, khaki legs,
sheer stockings, transparent stockings, silk stockings, nylon, fishnet,
shorts, skirt, miniskirt, summer clothes, sleeveless
"""

def build(seed):
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "Illustrious\\ILFlatMix.safetensors"}},
        "2": {"class_type": "LoraLoader", "inputs": {
            "model": ["1", 0], "clip": ["1", 1],
            "lora_name": "Yuzu Soft[style]-Illus.safetensors",
            "strength_model": 1.05, "strength_clip": 1.05
        }},
        "3": {"class_type": "LoraLoader", "inputs": {
            "model": ["2", 0], "clip": ["2", 1],
            "lora_name": "DMD2\\dmd2_sdxl_4step_lora_fp16.safetensors",
            "strength_model": 0.85, "strength_clip": 0.85
        }},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["3", 1], "text": POSITIVE}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["3", 1], "text": NEGATIVE}},
        "6": {"class_type": "EmptyLatentImage", "inputs": {"width": 768, "height": 1152, "batch_size": 1}},
        "7": {"class_type": "KSampler", "inputs": {
            "model": ["3", 0], "positive": ["4", 0], "negative": ["5", 0],
            "latent_image": ["6", 0], "seed": seed, "steps": 4, "cfg": 1.5,
            "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0
        }},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["1", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": f"yuzu_local_s{seed}"}}
    }

def submit(wf):
    payload = json.dumps({"prompt": wf, "client_id": "yuzu-local"}).encode('utf-8')
    req = urllib.request.Request(BASE + '/prompt', data=payload, headers={'Content-Type': 'application/json'})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        return json.loads(r.read()).get('prompt_id')
    except urllib.error.HTTPError as e:
        return f'ERR:{e.code}:' + e.read().decode('utf-8', 'ignore')[:300]
    except Exception as e:
        return f'EXC:{type(e).__name__}:{e}'

def wait(pid):
    for i in range(120):
        time.sleep(1.5)
        try:
            r = urllib.request.urlopen(BASE + f'/history/{pid}', timeout=5)
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

print('=== Health check ===')
try:
    r = urllib.request.urlopen(BASE + '/system_stats', timeout=5)
    s = json.loads(r.read())
    print(f'  ComfyUI {s["system"]["comfyui_version"]}  GPU: {[d.get("name") for d in s.get("devices",[])]}')
except Exception as e:
    print(f'  NOT REACHABLE: {e}')
    raise SystemExit(1)

for s in [101, 202, 303]:
    print(f'\n--- seed={s} ---')
    pid = submit(build(s))
    if isinstance(pid, str) and pid.startswith(('ERR', 'EXC')):
        print('  提交失败:', pid); continue
    print(f'  prompt_id={pid}')
    t0 = time.time()
    if wait(pid):
        print(f'  seed={s} 用时 {time.time()-t0:.1f}s')
    else:
        print(f'  seed={s} 超时')

print(f'\n=== 结果: {OUT_DIR} ===')
for f in sorted(os.listdir(OUT_DIR)):
    print(' ', f)
