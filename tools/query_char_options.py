# -*- coding: utf-8 -*-
"""查 CharacterAssetSelector 的 character 和 costume 枚举完整列表"""
import json, urllib.request

COMFYUI = "http://127.0.0.1:8188"
data = json.loads(urllib.request.urlopen(f"{COMFYUI}/object_info", timeout=10).read())

# 查所有 Character* 节点的 character 选项
for node_name in ["CharacterAssetSelector", "CharacterAssetSelectorQWEN", "CharacterCreator"]:
    print(f"\n=== {node_name} ===")
    node = data.get(node_name, {})
    inputs = node.get("input", {})

    for section in ["required", "optional"]:
        for param_name, param_val in inputs.get(section, {}).items():
            if isinstance(param_val, list) and len(param_val) > 0 and isinstance(param_val[0], list):
                # 枚举
                options = [str(o[0]) for o in param_val[0]]
                if "character" in param_name.lower() or "costume" in param_name.lower():
                    print(f"  [{param_name}] 共 {len(options)} 个选项:")
                    for opt in options:
                        print(f"    - {opt}")
                    print()
