# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
"""把背景图拉大到 1920x1080 (全屏)"""
from PIL import Image
import os, shutil

BG_DIR = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\game\images\backgrounds"
TARGET = (1920, 1080)

files = ["airport_hall.png", "wellington_airport.png"]

for fname in files:
    src = os.path.join(BG_DIR, fname)
    if not os.path.exists(src):
        print(f"  [SKIP] {fname} (不存在)")
        continue
    img = Image.open(src)
    w, h = img.size
    print(f"  [INFO] {fname}: {w}x{h}")
    if (w, h) == TARGET:
        print(f"         已是目标尺寸, 跳过")
        continue
    # 拉大 (高质量)
    img_resized = img.resize(TARGET, Image.LANCZOS)
    # 覆盖原图
    img_resized.save(src, "PNG", optimize=True)
    new_size = os.path.getsize(src)
    print(f"  [OK]  {fname} -> 1920x1080 ({new_size//1024}KB)")

print("\nDone!")
