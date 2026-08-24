import json
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_tennis_preview.json', encoding='utf-8') as f:
    d = json.load(f)
for n in d['nodes']:
    nid = n.get('id')
    typ = n.get('type') or n.get('class_type','-')
    print(f"=== id={nid} type={typ} ===")
    for k in n.keys():
        if k in ('widgets_values',):
            v = n[k]
            if isinstance(v, list):
                for i, item in enumerate(v):
                    print(f"  widgets_values[{i}]: {repr(item)[:200]}")
            else:
                print(f"  {k}: {repr(v)[:200]}")
        elif k in ('inputs', 'links'):
            print(f"  {k}: {n[k]}")
        else:
            print(f"  {k}: {repr(n[k])[:80]}")
    print()
