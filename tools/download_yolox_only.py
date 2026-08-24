"""
单独重下 yolox_l.onnx（SSL 握手断，加 retry + 镜像源）
"""
import os
os.environ["HF_HUB_DISABLE_XET"] = "1"

from huggingface_hub import hf_hub_download
from pathlib import Path
import time

ckpts = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\comfyui_controlnet_aux\ckpts")
target = ckpts / "hr16" / "yolox-onnx" / "yolox_l.onnx"
target.parent.mkdir(parents=True, exist_ok=True)

REPOS = [
    ("hr16/yolox-onnx", "yolox_l.onnx", "official"),
    ("jameslahm/yolox", "yolox_l.onnx", "mirror"),
    ("Bingsu/yolox_l.onnx", "yolox_l.onnx", "huggingface"),
]

for repo, fn, note in REPOS:
    print(f"\n[trial: {note}] {repo}/{fn}")
    for attempt in range(3):
        try:
            p = hf_hub_download(
                repo_id=repo,
                filename=fn,
                local_dir=ckpts / Path(repo).parent / Path(repo).name,
            )
            sz = Path(p).stat().st_size
            print(f"  OK: {p}  ({sz//1024//1024} MB)")
            # 复制到标准位置
            import shutil
            if p != str(target):
                shutil.copy(p, target)
                print(f"  copied to: {target}")
            break
        except Exception as e:
            print(f"  attempt {attempt+1}/3 FAIL: {type(e).__name__}: {str(e)[:200]}")
            time.sleep(3)
    else:
        continue
    if target.exists() and target.stat().st_size > 10*1024*1024:
        print(f"\n=== SUCCESS ===  {target}  ({target.stat().st_size//1024//1024} MB)")
        break

if not target.exists() or target.stat().st_size < 10*1024*1024:
    print("\n=== ALL TRIALS FAILED, trying direct curl with resume ===")
    import urllib.request
    urls = [
        ("https://huggingface.co/hr16/yolox-onnx/resolve/main/yolox_l.onnx", "official"),
        ("https://hf-mirror.com/hr16/yolox-onnx/resolve/main/yolox_l.onnx", "mirror-cn"),
    ]
    for url, note in urls:
        print(f"[curl: {note}] {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                with open(target, "wb") as f:
                    while True:
                        chunk = r.read(1<<20)
                        if not chunk: break
                        f.write(chunk)
            sz = target.stat().st_size
            print(f"  OK: {target}  ({sz//1024//1024} MB)")
            if sz > 10*1024*1024:
                print("\n=== SUCCESS via curl ===")
                break
        except Exception as e:
            print(f"  FAIL: {type(e).__name__}: {str(e)[:200]}")

print("\n=== final ckpts 目录 ===")
for f in sorted(ckpts.rglob("*.onnx")) + sorted(ckpts.rglob("*.torchscript.pt")):
    print(f"  {f}  ({f.stat().st_size//1024//1024} MB)")
