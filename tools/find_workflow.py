# -*- coding: utf-8 -*-
"""查 ComfyUI 浏览器里保存的 workflow 列表"""
import json, urllib.request, os

COMFYUI = "http://127.0.0.1:8188"

# 1. 查 settings 看保存路径
try:
    settings = json.loads(urllib.request.urlopen(f"{COMFYUI}/settings", timeout=10).read())
    print("=== ComfyUI Settings ===")
    # 找用户保存 workflow 的目录
    for k, v in settings.items():
        if "user" in k.lower() or "workflow" in k.lower() or "default" in k.lower():
            print(f"  {k}: {v}")
except Exception as e:
    print(f"settings err: {e}")

# 2. 查可能的 workflow 文件位置
print("\n=== 查可能的 workflow 文件 ===")
possible_dirs = [
    r"C:\Users\jwu40\Documents\ComfyUI\user\default\workflows",
    r"C:\Users\jwu40\AppData\Local\Programs\ComfyUI\user\default\workflows",
    r"C:\Users\jwu40\AppData\Roaming\ComfyUI\user\default\workflows",
]
for d in possible_dirs:
    if os.path.exists(d):
        print(f"FOUND: {d}")
        for f in os.listdir(d):
            if "vnccs" in f.lower() or "new_char" in f.lower() or "creator" in f.lower():
                print(f"  - {f}")
    else:
        print(f"  not exist: {d}")
