import json, urllib.request

data = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/object_info', timeout=10).read())
cc = data.get('CharacterCreatorV2', {})
print("Input required:", cc.get('input', {}).get('required'))
print("Input optional:", cc.get('input', {}).get('optional'))
print("Output:", cc.get('output'))
print("Output node:", cc.get('output_node'))
print("Full keys:", list(cc.keys()))
