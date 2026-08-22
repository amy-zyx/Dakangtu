"""
Rita 基础角色生成 - 提交到 AutoDL ComfyUI
目标: qwen-image-edit-2511 + Lightning 4steps + Flux 采样
"""
import urllib.request, ssl, json, time, uuid, os
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
BASE = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_rita_v1'
os.makedirs(OUT_DIR, exist_ok=True)

# ============================================================
# Rita 基础 prompt（与本地项目文档一致）
# ============================================================
POSITIVE = """masterpiece, best quality, 2D galgame style, anime, cel shading,
flat color blocks, clean line art, black outlines, soft lighting,

1girl, solo, 19 years old, asian female,
petite build, slim body, slender long legs, 163cm height impression,
small oval face, delicate features, porcelain skin, fair skin,

long straight black hair, pure black hair no purple tint,
hair down to chest length, center part, middle part bangs,
hair on both sides of face framing face,

large almond eyes, gentle eyes, quiet gaze, slightly downcast,
thin natural eyebrows, small nose, soft thin lips, light pink lips,

expression: gentle, calm, slightly shy, reserved, delicate and moving,

wearing: mustard yellow wool coat, double-breasted long coat,
knee-length, beige turtleneck underneath,
wearing: opaque black velvet tights, fleece-lined tights, warm texture,
wearing: black ankle boots, low heel,

full body standing, front view, hands at sides,
slight smile, looking at viewer,
plain white background, character reference sheet
"""

NEGATIVE = """3D, semi-realistic, photorealistic, photo, photographic,
gradient heavy shading, complex background, scenery, indoor, outdoor,
purple hair tint, blue hair tint, brown hair tint,
lolita, sexy, seductive, revealing, nsfw, nude, naked, exposed skin,
chibi, loli, child,
deformed, bad anatomy, extra fingers, mutated hands, blurry, low quality,
text, watermark, signature, multiple girls, crowd,
sheer stockings, transparent stockings, silk stockings, nylon,
shorts, skirt, miniskirt, summer clothes, sleeveless
"""

# ============================================================
# 构造 ComfyUI 工作流
# ============================================================
workflow = {
    "1": {  # UNETLoader
        "class_type": "UNETLoader",
        "inputs": {
            "unet_name": "qwen_image_edit_2511_bf16.safetensors",
            "weight_dtype": "default"
        }
    },
    "2": {  # CLIPLoader (单口，type=qwen_image)
        "class_type": "CLIPLoader",
        "inputs": {
            "clip_name": "qwen/qwen_2.5_vl_7b.safetensors",
            "type": "qwen_image"
        }
    },
    "3": {  # VAELoader
        "class_type": "VAELoader",
        "inputs": {
            "vae_name": "qwen_image_vae.safetensors"
        }
    },
    "4": {  # LoraLoader (Lightning 4-steps)
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["1", 0],
            "clip": ["2", 0],
            "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors",
            "strength_model": 1.0,
            "strength_clip": 1.0
        }
    },
    "5": {  # ModelSamplingFlux
        "class_type": "ModelSamplingFlux",
        "inputs": {
            "model": ["4", 0],
            "max_shift": 3.5,
            "base_shift": 1.0,
            "width": 1024,
            "height": 1536
        }
    },
    "6": {  # TextEncodeQwenImageEdit positive
        "class_type": "TextEncodeQwenImageEdit",
        "inputs": {
            "clip": ["4", 1],
            "prompt": POSITIVE
        }
    },
    "7": {  # TextEncodeQwenImageEdit negative
        "class_type": "TextEncodeQwenImageEdit",
        "inputs": {
            "clip": ["4", 1],
            "prompt": NEGATIVE
        }
    },
    "8": {  # EmptyLatentImage
        "class_type": "EmptyLatentImage",
        "inputs": {
            "width": 1024,
            "height": 1536,
            "batch_size": 1
        }
    },
    "9": {  # KSampler
        "class_type": "KSampler",
        "inputs": {
            "model": ["5", 0],
            "positive": ["6", 0],
            "negative": ["7", 0],
            "latent_image": ["8", 0],
            "seed": 42,
            "steps": 4,
            "cfg": 1.0,
            "sampler_name": "euler",
            "scheduler": "simple",
            "denoise": 1.0
        }
    },
    "10": {  # VAEDecode
        "class_type": "VAEDecode",
        "inputs": {
            "samples": ["9", 0],
            "vae": ["3", 0]
        }
    },
    "11": {  # SaveImage
        "class_type": "SaveImage",
        "inputs": {
            "images": ["10", 0],
            "filename_prefix": "rita_base_v1"
        }
    }
}

# ============================================================
# 提交
# ============================================================
client_id = str(uuid.uuid4())
payload = json.dumps({"prompt": workflow, "client_id": client_id}).encode('utf-8')
req = urllib.request.Request(BASE + '/prompt', data=payload,
                              headers={'Content-Type': 'application/json'})
print(f'>>> 提交工作流 (client_id={client_id[:8]})')
try:
    resp = urllib.request.urlopen(req, timeout=30, context=ctx)
    result = json.loads(resp.read())
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', 'ignore')
    print(f'!! HTTP {e.code} {e.reason}')
    print(f'!! 响应体: {body}')
    # 把工作流 dump 到文件方便排查
    with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\last_workflow.json', 'w', encoding='utf-8') as f:
        json.dump(workflow, f, ensure_ascii=False, indent=2)
    print('!! 工作流已保存到 output/last_workflow.json')
    raise SystemExit(1)
prompt_id = result.get('prompt_id')
print(f'    prompt_id = {prompt_id}')
if not prompt_id:
    print('!! 提交失败，响应：', result)
    raise SystemExit(1)

# ============================================================
# 轮询
# ============================================================
print('>>> 等待生成完成...')
for i in range(120):  # 最多等 4 分钟
    time.sleep(2)
    try:
        hr = urllib.request.urlopen(BASE + f'/history/{prompt_id}', timeout=8, context=ctx)
        hist = json.loads(hr.read())
    except Exception as e:
        print(f'    轮询异常 (i={i}): {e}')
        continue
    if prompt_id in hist:
        entry = hist[prompt_id]
        # 检查是否完成
        if entry.get('outputs') or entry.get('status', {}).get('completed'):
            print(f'    完成 (用时 ~{(i+1)*2}s)')
            outputs = entry.get('outputs', {})
            for node_id, node_out in outputs.items():
                if 'images' in node_out:
                    for img in node_out['images']:
                        fn = img['filename']
                        sub = img.get('subfolder', '')
                        tp = img.get('type', 'output')
                        url = f'{BASE}/view?filename={urllib.parse.quote(fn)}&subfolder={urllib.parse.quote(sub)}&type={tp}'
                        local = os.path.join(OUT_DIR, fn)
                        print(f'    下载: {fn} <- {url}')
                        with urllib.request.urlopen(url, timeout=30, context=ctx) as r:
                            with open(local, 'wb') as f:
                                f.write(r.read())
                        print(f'    保存到: {local}')
            break
    if i % 5 == 0:
        # 检查 queue
        try:
            qr = urllib.request.urlopen(BASE + '/queue', timeout=5, context=ctx)
            qd = json.loads(qr.read())
            print(f'    队列剩余: {qd.get("exec_info", {}).get("queue_remaining", "?")}')
        except Exception:
            pass
else:
    print('!! 超时未完成')
