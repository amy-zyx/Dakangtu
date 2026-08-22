# -*- coding: utf-8 -*-
"""查 VNCCS_CharacterGenerator 节点的参数"""
import json, urllib.request

COMFYUI = "http://127.0.0.1:8188"
data = json.loads(urllib.request.urlopen(f"{COMFYUI}/object_info", timeout=10).read())

node = data.get("VNCCS_CharacterGenerator", {})
print("=== VNCCS_CharacterGenerator 参数 ===\n")
print(f"输入 ({len(node.get('input', {}).get('required', {}))} 个必填):")
for k, v in node.get('input', {}).get('required', {}).items():
    print(f"  {k}: {v}")
print(f"\n输入 ({len(node.get('input', {}).get('optional', {}))} 个可选):")
for k, v in node.get('input', {}).get('optional', {}).items():
    print(f"  {k}: {v}")
print(f"\n输出: {list(node.get('output', []))}")
print(f"返回类型: {node.get('return_names', [])}")

# 同时查 CharacterCreator 跟它配对
print("\n\n=== CharacterCreator（V1）参数 ===\n")
cc = data.get("CharacterCreator", {})
for k, v in cc.get('input', {}).get('required', {}).items():
    print(f"  {k}: {v}")
for k, v in cc.get('input', {}).get('optional', {}).items():
    print(f"  {k}: {v}")
