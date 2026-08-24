import json, urllib.request

data = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/object_info', timeout=10).read())
for n in ['CharacterCreatorV2', 'VNCCS_CharacterGenerator', 'VNCCS_PoseStudio', 'VNCCS_ControlCenter']:
    if n not in data:
        print(f"=== {n} (NOT FOUND) ===")
        continue
    print(f"=== {n} ===")
    info = data[n]
    print("  input.required:")
    for k, v in info['input']['required'].items():
        print(f"    {k}: {v[0] if isinstance(v, list) else v}")
    print("  input.optional:")
    for k, v in info['input'].get('optional', {}).items():
        print(f"    {k}: {v[0] if isinstance(v, list) else v}")
    print()
