import json, urllib.request
d = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/object_info', timeout=10).read())
for n in ['CharacterCreatorV2','VNCCS_CharacterGenerator','VNCCS_PoseStudio','VNCCS_ControlCenter']:
    print(f"=== {n} ===")
    print("  input_order:", d[n].get('input_order'))
    print("  required:", list(d[n].get('input', {}).get('required', {}).keys()))
    print("  optional:", list(d[n].get('input', {}).get('optional', {}).keys()))
    print()
