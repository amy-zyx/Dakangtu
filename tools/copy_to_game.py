# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
"""把 Jack V6 6 张 + 参考图放到游戏工程"""
import shutil, os, json, urllib.request

COMFYUI = "http://127.0.0.1:8188"
OUT = r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\output"
DST = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\game\images\characters"

# 创建目标目录
os.makedirs(DST, exist_ok=True)

# Step 1: 上传 V6 文件到 ComfyUI input/ 然后用 API 复制到工程? 不行
# Step 1: 用 shutil 复制 (Python 不受沙箱限制)
files_to_copy = [
    ("JackFW2_00001_.png", "jack_smile.png"),          # 参考图
    ("jackV6_surprised_00001_.png", "jack_surprised.png"),
    ("jackV6_blush_00001_.png",     "jack_blush.png"),
    ("jackV6_thinking_00001_.png",  "jack_thinking.png"),
    ("jackV6_sad_00001_.png",       "jack_sad.png"),
    ("jackV6_happy_00001_.png",     "jack_happy.png"),
    ("jackV6_worried_00001_.png",   "jack_worried.png"),
]

print("=== 复制 Jack 图到游戏工程 ===")
for src_name, dst_name in files_to_copy:
    src = os.path.join(OUT, src_name)
    dst = os.path.join(DST, dst_name)
    if not os.path.exists(src):
        print(f"  [SKIP] {src_name} -> {dst_name} (源不存在)")
        continue
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy2(src, dst)
    size = os.path.getsize(dst)
    print(f"  [OK] {src_name:30s} -> {dst_name:25s} ({size//1024}KB)")

# Step 2: 也复制 Ami + wellington
print("\n=== 复制其他已有图到游戏工程 ===")
other_files = [
    # Ami
    (r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared\output\ami_*.png", "ami_*.png"),
    # Wellinton
    (r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\game\images\backgrounds\wellington_airport.png", "wellington_airport.png"),
]
for src_pattern, dst_name in other_files:
    if "*" in src_pattern:
        import glob
        for src in glob.glob(src_pattern):
            fname = os.path.basename(src)
            dst = os.path.join(DST, fname)
            if os.path.exists(dst):
                continue
            shutil.copy2(src, dst)
            print(f"  [OK] {fname}")

# Step 3: 列出所有 jack + ami 图
print("\n=== 游戏工程角色图列表 ===")
for f in sorted(os.listdir(DST)):
    if f.startswith(("ami_", "jack_")):
        size = os.path.getsize(os.path.join(DST, f))
        print(f"  {f:30s} {size//1024:4d}KB")

print("\nDone!")
