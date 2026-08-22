# -*- coding: utf-8 -*-
"""查 CharacterCreatorV2 + CharacterAssetSelector 完整字段"""
import json, urllib.request

COMFYUI = "http://127.0.0.1:8188"
data = json.loads(urllib.request.urlopen(f"{COMFYUI}/object_info", timeout=10).read())

for node_name in ["CharacterCreator", "CharacterCreatorV2", "CharacterAssetSelector", "CharacterAssetSelectorQWEN", "CharacterCloner", "VNCCS_CharacterGenerator", "VNCCS_CharacterCloneGenerator", "VNCCS_ClothesGenerator"]:
    print(f"\n{'='*70}")
    print(f"=== {node_name} ===")
    print('='*70)
    node = data.get(node_name, {})
    if not node:
        print("节点不存在")
        continue

    inputs = node.get("input", {})

    # 必填
    for k, v in inputs.get("required", {}).items():
        if isinstance(v, list) and len(v) > 0:
            t = v[0]
            if isinstance(t, list):
                opts = [o[0] for o in t[:8]]
                print(f"  [必填] {k}: 枚举({len(t)}): {opts}{'...' if len(t)>8 else ''}")
            else:
                default = v[1].get("default", "?") if len(v) > 1 else "?"
                print(f"  [必填] {k}: {t} 默认={default!r}")
        else:
            print(f"  [必填] {k}: {v}")

    # 可选
    for k, v in inputs.get("optional", {}).items():
        if isinstance(v, list) and len(v) > 0:
            t = v[0]
            if isinstance(t, list):
                opts = [o[0] for o in t[:8]]
                print(f"  [可选] {k}: 枚举({len(t)}): {opts}{'...' if len(t)>8 else ''}")
            else:
                default = v[1].get("default", "?") if len(v) > 1 else "?"
                print(f"  [可选] {k}: {t} 默认={default!r}")
        else:
            print(f"  [可选] {k}: {v}")

    print(f"  [输出]: {node.get('output', [])}")
