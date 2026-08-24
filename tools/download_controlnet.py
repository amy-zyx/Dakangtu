"""
下标准 ControlNet OpenPose SDXL（1.5GB）
"""
import os
os.environ["HF_HUB_DISABLE_XET"] = "1"

from huggingface_hub import hf_hub_download
from pathlib import Path
import time

dst = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\models\controlnet")
dst.mkdir(parents=True, exist_ok=True)

# 试多个源
REPOS = [
    ("xinsir/controlnet-openpose-sdxl-1.0", "diffusion_pytorch_model.safetensors", "official"),
    ("thibaud/controlnet-openpose-sdxl-1.0", "diffusion_pytorch_model.safetensors", "thibaud"),
    ("ckpt/controlnet-openpose-sdxl-1.0", "diffusion_pytorch_model.safetensors", "ckpt"),
]

for repo, fn, note in REPOS:
    print(f"\n[trial: {note}] {repo}/{fn}")
    for attempt in range(3):
        try:
            p = hf_hub_download(
                repo_id=repo,
                filename=fn,
                local_dir=dst,
            )
            print(f"  OK: {p}  ({Path(p).stat().st_size//1024//1024} MB)")
            if Path(p).stat().st_size > 100*1024*1024:
                print(f"\n=== SUCCESS ===")
                break
        except Exception as e:
            print(f"  attempt {attempt+1}/3 FAIL: {type(e).__name__}: {str(e)[:200]}")
            time.sleep(2)
    if (dst / "diffusion_pytorch_model.safetensors").exists() and \
       (dst / "diffusion_pytorch_model.safetensors").stat().st_size > 100*1024*1024:
        break

# 兜底 curl
final = dst / "diffusion_pytorch_model.safetensors"
if not final.exists() or final.stat().st_size < 100*1024*1024:
    print("\n=== curl fallback ===")
    import urllib.request
    urls = [
        ("https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors", "thibaud"),
        ("https://hf-mirror.com/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors", "mirror-cn"),
    ]
    for url, note in urls:
        print(f"[curl: {note}] {url[:80]}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                with open(final, "wb") as f:
                    total = 0
                    while True:
                        chunk = r.read(1<<20)
                        if not chunk: break
                        f.write(chunk)
                        total += len(chunk)
                        if total % (50*1024*1024) == 0:
                            print(f"  {total//1024//1024} MB ...")
            sz = final.stat().st_size
            print(f"  OK: {final}  ({sz//1024//1024} MB)")
            if sz > 100*1024*1024:
                break
        except Exception as e:
            print(f"  FAIL: {type(e).__name__}: {str(e)[:200]}")

print("\n=== final controlnet 目录 ===")
for f in sorted(dst.iterdir()):
    if f.is_file() and f.stat().st_size > 1MB:
        print(f"  {f.name}  ({f.stat().st_size//1024//1024} MB)")
