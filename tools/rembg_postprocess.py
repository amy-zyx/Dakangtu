"""
批量抠图脚本：把 output/rita_yuzu_local/*.png 用 isnet-anime 抠成透明 PNG
输出到 output/rita_yuzu_transparent/
"""
import os, sys
from pathlib import Path
from PIL import Image

# 让 rembg 用 CPU 或 GPU
try:
    from rembg import remove, new_session
    session = new_session("isnet-anime")
    print("[rembg] isnet-anime session ready (GPU)")
except Exception as e:
    print(f"[rembg] GPU failed ({e}), fallback to CPU")
    from rembg import remove, new_session
    session = new_session("isnet-anime", providers=["CPUExecutionProvider"])

IN_DIR = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\output\rita_yuzu_local")
OUT_DIR = Path(r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\rita_yuzu_transparent")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 收集输入图
inputs = sorted(IN_DIR.glob("*.png"))
if not inputs:
    # 兜底：搜全 output 目录
    fallback = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\output")
    inputs = sorted(fallback.glob("rita_yuzu_*.png"))
    inputs = [p for p in inputs if "transparent" not in p.name]

print(f"[scan] {len(inputs)} inputs from {IN_DIR}")
if not inputs:
    print("[ERR] no PNGs found, run the workflow first")
    sys.exit(1)

for i, src in enumerate(inputs, 1):
    img = Image.open(src).convert("RGBA")
    print(f"[{i}/{len(inputs)}] {src.name}  size={img.size}", flush=True)
    out_bytes = remove(img, session=session, only_mask=False, post_process_mask=True)
    out = Image.open(__import__("io").BytesIO(out_bytes)).convert("RGBA")
    dst = OUT_DIR / src.name.replace(".png", "_rmbg.png")
    out.save(dst, "PNG", optimize=True)
    print(f"   -> {dst}  ({dst.stat().st_size//1024} KB)", flush=True)

print(f"\n[done] {len(inputs)} sprites written to {OUT_DIR}")
