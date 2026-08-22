"""Generate a simple Ami tennis preview using cloud ComfyUI's native nodes only (no VNCCS)."""
import json, base64, urllib.request, urllib.error, time, os
from pathlib import Path

CRED = "XT11TL:bCu5w26jSI"
BASE = "https://wp08.unicorn.org.cn:11274"
AUTH = "Basic " + base64.b64encode(CRED.encode()).decode()


def http_json(path, body=None, method="GET"):
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(
        BASE + path, data=data, method=method,
        headers={"Content-Type": "application/json", "Authorization": AUTH},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "body": e.read().decode("utf-8", errors="replace")[:1500]}


def download(filename, out_path, subfolder="", type_="output"):
    qs = f"filename={urllib.parse.quote(filename)}&type={type_}"
    if subfolder: qs += f"&subfolder={urllib.parse.quote(subfolder)}"
    req = urllib.request.Request(BASE + "/view?" + qs, headers={"Authorization": AUTH})
    with urllib.request.urlopen(req, timeout=30) as r:
        out_path.write_bytes(r.read())


# Use Qwen-Image-Edit-2511 (the model your local workflow was using).
# But Qwen-Image-Edit needs a different pipeline — for a quick smoke test
# we'll use the Anima model with a strong prompt to match the tennis outfit.
prompt = {
    "1": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {"ckpt_name": "xl/animaPencilXL_v500.safetensors"},
    },
    "2": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": (
                "masterpiece, best quality, score_7, anime, 2d flat illustration, "
                "cel shading, visual novel style, "
                "1girl, 20 years old chinese girl, soft feminine features, round face, "
                "slightly chubby cheeks, kind gentle expression, large expressive brown eyes, "
                "soft eyelashes, small nose, light pink lips, natural minimal makeup, "
                "long straight black hair, very long hair, side parting, hair reaching waist, dark black color, "
                "slim thick body type, curvy figure, well-endowed bust, large breasts, narrow waist, wide hips, "
                "feminine curves, 165cm, healthy voluptuous physique, "
                "wearing tennis outfit, white tennis dress, short pleated tennis skirt, "
                "white sleeveless polo shirt, sporty fashion, exposed cleavage, "
                "waist-up portrait, looking at viewer, smile"
            ),
            "clip": ["1", 1],
        },
    },
    "3": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": (
                "bad quality, worst quality, low quality, score_1, score_2, score_3, "
                "blurry, jpeg artifacts, 3d, realistic, photorealistic, gradient, "
                "complex shading, mature, old, dark skin, male, flat chest, skinny"
            ),
            "clip": ["1", 1],
        },
    },
    "4": {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 768, "height": 1024, "batch_size": 4},  # 4 images to compare
    },
    "5": {
        "class_type": "KSampler",
        "inputs": {
            "model": ["1", 0],
            "positive": ["2", 0],
            "negative": ["3", 0],
            "latent_image": ["4", 0],
            "seed": 12345,
            "steps": 28,
            "cfg": 7,
            "sampler_name": "euler_ancestral",
            "scheduler": "normal",
            "denoise": 1.0,
        },
    },
    "6": {
        "class_type": "VAEDecode",
        "inputs": {"samples": ["5", 0], "vae": ["1", 2]},
    },
    "7": {
        "class_type": "SaveImage",
        "inputs": {"images": ["6", 0], "filename_prefix": "ami_tennis_cloud"},
    },
}

print("Submitting to cloud (Qwen-free smoke test)...")
res = http_json("/prompt", {"prompt": prompt, "client_id": "ami-ami-1"}, method="POST")
if "error" in res:
    print("ERROR:", json.dumps(res, indent=2, ensure_ascii=False)[:1500])
    raise SystemExit(1)
pid = res["prompt_id"]
print(f"  prompt_id: {pid}, queue #{res.get('number')}")

# Wait
print("Waiting for completion...")
deadline = time.time() + 600
while time.time() < deadline:
    h = http_json(f"/history/{pid}")
    e = h.get(pid)
    if e and e.get("status", {}).get("completed"):
        print("  completed!")
        # Show any errors
        for m in e.get("status", {}).get("messages", []):
            if m[0] == "execution_error":
                print("ERROR:", json.dumps(m[1], indent=2)[:1500])
        out_dir = Path("outputs/cloud")
        out_dir.mkdir(parents=True, exist_ok=True)
        n = 0
        for nid, node_out in e.get("outputs", {}).items():
            for k, v in node_out.items():
                if isinstance(v, list):
                    for img in v:
                        if isinstance(img, dict) and "filename" in img:
                            fn = img["filename"]
                            sub = img.get("subfolder", "")
                            try:
                                download(fn, out_dir / fn, sub)
                                print(f"  ↓ {out_dir / fn}")
                                n += 1
                            except Exception as ex:
                                print(f"  ! {ex}")
        print(f"Done: {n} files")
        break
    time.sleep(5)
else:
    print("Timeout")
