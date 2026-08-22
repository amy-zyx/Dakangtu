"""云端 Yuzu 测试 - 不用 DMD2, 28 步"""
import socket, ssl, json, os, time

def http_post(host, path, body, port=443, timeout=300):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    data = json.dumps(body).encode('utf-8')
    req = f'POST {path} HTTP/1.0\r\nHost: {host}\r\nContent-Type: application/json\r\nContent-Length: {len(data)}\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode() + data)
    chunks = []
    while True:
        d = s.recv(65536)
        if not d: break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks).decode('utf-8','ignore')
    body_text = raw.split('\r\n\r\n',1)[1] if '\r\n\r\n' in raw else raw
    return body_text

def http_get(host, path, port=443, timeout=15, binary=False):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f'GET {path} HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode())
    chunks = []
    while True:
        d = s.recv(65536)
        if not d: break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks)
    if b'\r\n\r\n' in raw:
        return raw.split(b'\r\n\r\n', 1)[1]
    return raw

host = '8188-cpod-1ud2p6nylymq.pod.compshare.cn'

POSITIVE = """masterpiece, best quality, yuzusoft style, yuzu soft style,
anime, 2D galgame style, illustration,
1girl, solo, 19 years old, asian female,
petite build, slim body, slender long legs, 163cm,
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
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "perfectdeliberate_v70.safetensors"}},
        "2": {"class_type": "LoraLoader", "inputs": {
            "model": ["1", 0], "clip": ["1", 1],
            "lora_name": "Yuzu Soft[style]-Illus.safetensors",
            "strength_model": 0.85, "strength_clip": 0.85
        }},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 1], "text": POSITIVE}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 1], "text": NEGATIVE}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 768, "height": 1152, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {
            "model": ["2", 0], "positive": ["3", 0], "negative": ["4", 0],
            "latent_image": ["5", 0], "seed": seed, "steps": 28, "cfg": 7,
            "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0
        }},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": f"cloud_yuzu_s{seed}"}}
    }

seed = 101
print(f'submitting seed={seed}...')
r = http_post(host, '/prompt', {"prompt": build(seed), "client_id": "cloud-yuzu-1"})
print('submit response:', r[:200])
try:
    pid = json.loads(r)['prompt_id']
    print(f'prompt_id={pid}')
except Exception as e:
    print('parse fail:', e)
    raise SystemExit(1)

# 等待完成
print('waiting...', flush=True)
t0 = time.time()
last_size = 0
for i in range(180):  # 最多 9 分钟
    time.sleep(3)
    try:
        h = json.loads(http_get(host, '/history').decode('utf-8','ignore'))
    except Exception as ex:
        print(f'  poll err: {ex}'); continue
    if pid in h:
        out = h[pid].get('outputs', {})
        for nid, nv in out.items():
            for img in nv.get('images', []):
                fn = img['filename']
                sub = img.get('subfolder','')
                tp = img.get('type','output')
                url = f'/view?filename={fn}&subfolder={sub}&type={tp}'
                data = http_get(host, url, timeout=60)
                if len(data) > 1000:
                    out_path = rf'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_yuzu\cloud_yuzu_s{seed}_{fn}'
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    with open(out_path, 'wb') as f:
                        f.write(data)
                    print(f'  [OK] {out_path} ({len(data)//1024} KB) after {time.time()-t0:.1f}s')
                    raise SystemExit(0)
    print(f'  [{i}] {time.time()-t0:.0f}s', flush=True)
print('timeout')
