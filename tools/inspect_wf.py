import json
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_tennis_preview.json', encoding='utf-8') as f:
    d = json.load(f)
for n in d['nodes']:
    nid = n.get('id')
    typ = n.get('type') or n.get('class_type','-')
    wv = n.get('widgets_values')
    if isinstance(wv, list):
        w0 = repr(wv[0])[:200] if wv else None
        wn = len(wv)
    else:
        w0 = f"type={type(wv).__name__}"
        wn = 1
    print(f"id={nid} type={typ} | wv_count={wn} | wv0={w0}")
