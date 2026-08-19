# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
"""Ami 文件名跟 Jack 一致: Ami_<emotion>_00001_.png -> ami_<emotion>.png"""
import shutil, os

DST = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\game\images\characters"

renames = [
    ("Ami_smile_00001_.png",     "ami_smile.png"),
    ("Ami_surprised_00001_.png", "ami_surprised.png"),
    ("Ami_blush_00001_.png",     "ami_blush.png"),
    ("Ami_thinking_00001_.png",  "ami_thinking.png"),
    ("Ami_sad_00001_.png",       "ami_sad.png"),
]

print("=== Ami 文件名规范化 (跟 jack 一致) ===")
for old, new in renames:
    src = os.path.join(DST, old)
    dst = os.path.join(DST, new)
    if not os.path.exists(src):
        print(f"  [SKIP] {old} (源不存在)")
        continue
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy2(src, dst)
    print(f"  [OK] {old} -> {new}")

# 删除旧的 Ami 命名文件 (保留新命名)
print("\n=== 删除旧命名 ===")
for old, _ in renames:
    src = os.path.join(DST, old)
    if os.path.exists(src):
        os.remove(src)
        print(f"  [DEL] {old}")

# 最终列表
print("\n=== 最终角色图 ===")
for f in sorted(os.listdir(DST)):
    if f.endswith(".png"):
        size = os.path.getsize(os.path.join(DST, f))
        print(f"  {f:30s} {size//1024:4d}KB")
