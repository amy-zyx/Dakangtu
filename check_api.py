import json
d = json.load(open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_tennis_preview_api.json', encoding='utf-8'))
for k, v in d['prompt'].items():
    print(f"{k} ({v['class_type']}): {list(v['inputs'].keys())}")
