"""
下 IPAdapter Plus SDXL (weight=0.8, PLUS high strength) 需要的两个文件。

注意: comfyui_ipadapter_plus 的 utils.get_clipvision_file() 对 "PLUS (high strength)"
预设走的是 ViT-H 分支 (不是 bigG) -- 即使 ipadapter 权重文件名里带 "sdxl"，
配套的 CLIP Vision 编码器实际上是 h94/IP-Adapter 仓库 models/ 目录下的 ViT-H 版本，
不是 sdxl_models/ 目录下的 bigG 版本。装错会导致 "ClipVision model not found"。
"""
import os
os.environ["HF_HUB_DISABLE_XET"] = "1"

from huggingface_hub import hf_hub_download
from pathlib import Path
import time

clip_vision_dst = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\models\clip_vision")
ipadapter_dst = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\models\ipadapter")
clip_vision_dst.mkdir(parents=True, exist_ok=True)
ipadapter_dst.mkdir(parents=True, exist_ok=True)

TARGETS = [
    ("h94/IP-Adapter", "models/image_encoder/model.safetensors", clip_vision_dst,
     clip_vision_dst / "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"),
    ("h94/IP-Adapter", "sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors", ipadapter_dst,
     ipadapter_dst / "ip-adapter-plus_sdxl_vit-h.safetensors"),
]

for repo, fn, local_dir, final_path in TARGETS:
    print(f"\n[downloading] {repo}/{fn} -> {final_path}")
    if final_path.exists() and final_path.stat().st_size > 10 * 1024 * 1024:
        print(f"  already exists ({final_path.stat().st_size // 1024 // 1024} MB), skipping")
        continue
    ok = False
    for attempt in range(3):
        try:
            p = hf_hub_download(repo_id=repo, filename=fn, local_dir=local_dir)
            sz = Path(p).stat().st_size
            print(f"  OK: {p}  ({sz // 1024 // 1024} MB)")
            if Path(p) != final_path:
                import shutil
                shutil.copy(p, final_path)
                print(f"  copied to: {final_path}")
            ok = True
            break
        except Exception as e:
            print(f"  attempt {attempt+1}/3 FAIL: {type(e).__name__}: {str(e)[:200]}")
            time.sleep(2)
    if not ok:
        print(f"  === FAILED after 3 attempts: {repo}/{fn} ===")

print("\n=== clip_vision 目录 ===")
for f in sorted(clip_vision_dst.iterdir()):
    if f.is_file():
        print(f"  {f.name}  ({f.stat().st_size // 1024 // 1024} MB)")

print("\n=== ipadapter 目录 ===")
for f in sorted(ipadapter_dst.iterdir()):
    if f.is_file():
        print(f"  {f.name}  ({f.stat().st_size // 1024 // 1024} MB)")
