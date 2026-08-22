# -*- coding: utf-8 -*-
"""查 ComfyUI 实际 custom nodes"""
import json, urllib.request

COMFYUI = "http://127.0.0.1:8188"

# ComfyUI /object_info 端点能列出所有可用节点
req = urllib.request.Request(f"{COMFYUI}/object_info")
try:
    data = json.loads(urllib.request.urlopen(req, timeout=10).read())
    # 找 VNCCS 节点
    vnccs_nodes = [k for k in data.keys() if "vnccs" in k.lower() or "VNCCS" in k]
    print(f"=== VNCCS 节点 ({len(vnccs_nodes)}) ===")
    for n in vnccs_nodes:
        print(f"  {n}")
    print()
    # 找 LoRA 相关
    lora_nodes = [k for k in data.keys() if "lora" in k.lower() or "LoRA" in k]
    print(f"=== LoRA 节点 ({len(lora_nodes)}) ===")
    for n in lora_nodes:
        print(f"  {n}")
    print()
    # 找 CharacterCreator
    char_nodes = [k for k in data.keys() if "character" in k.lower() or "Character" in k]
    print(f"=== Character 节点 ({len(char_nodes)}) ===")
    for n in char_nodes:
        print(f"  {n}")
except Exception as e:
    print(f"ERR: {e}")
