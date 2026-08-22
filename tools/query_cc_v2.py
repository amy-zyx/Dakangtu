# -*- coding: utf-8 -*-
"""查 CharacterCreatorV2 节点的参数"""
import json, urllib.request

COMFYUI = "http://127.0.0.1:8188"
data = json.loads(urllib.request.urlopen(f"{COMFYUI}/object_info", timeout=10).read())

for node_name in ["CharacterCreatorV2", "CharacterCloner", "CharacterAssetSelector", "CharacterAssetSelectorQWEN", "CharacterSheetCropper"]:
    print(f"\n{'='*60}")
    print(f"=== {node_name} ===")
    print('='*60)
    node = data.get(node_name, {})
    if not node:
        print("节点不存在")
        continue
    print(f"\n[必填] {len(node.get('input', {}).get('required', {}))} 个:")
    for k, v in node.get('input', {}).get('required', {}).items():
        if isinstance(v, list) and len(v) > 0 and isinstance(v[0], list):
            opts = [o[0] for o in v[0][:10]]
            default = v[1].get('default', '?') if len(v) > 1 else '?'
            extra = []
            for key in ['min', 'max', 'multiline', 'forceInput']:
                if len(v) > 1 and key in v[1]:
                    extra.append(f"{key}={v[1][key]}")
            print(f"  {k}: 枚举={opts[:8]}{'...' if len(opts)>8 else ''}, 默认={default} {' '.join(extra)}")
        elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], str) and v[0] in ('INT', 'FLOAT', 'BOOLEAN', 'STRING'):
            t = v[0]
            default = v[1].get('default', '?') if len(v) > 1 else '?'
            extra = []
            for key in ['min', 'max', 'multiline', 'forceInput']:
                if len(v) > 1 and key in v[1]:
                    extra.append(f"{key}={v[1][key]}")
            print(f"  {k}: {t} 默认={default} {' '.join(extra)}")
        else:
            print(f"  {k}: {v}")
    print(f"\n[可选] {len(node.get('input', {}).get('optional', {}))} 个:")
    for k, v in node.get('input', {}).get('optional', {}).items():
        print(f"  {k}: {v}")
    print(f"\n输出: {list(node.get('output', []))}")
