"""查本地 8188 资源：节点 + LoRA + 底模"""
import urllib.request, json
BASE = 'http://127.0.0.1:8188'

def get(path):
    return json.loads(urllib.request.urlopen(BASE + path, timeout=10).read())

oi = get('/object_info')
out = []

# LoraLoader 选项
ll = oi.get('LoraLoader', {}).get('input', {}).get('required', {}).get('lora_name')
loras = ll[0] if isinstance(ll, list) and isinstance(ll[0], list) else []
out.append(f'=== LoraLoader ({len(loras)}) ===')
for l in loras:
    mark = ' <-- VNCCS' if 'VNCCS' in l or 'vnccs' in l else ''
    mark += ' <-- YUZU' if 'Yuzu' in l or 'yuzu' in l else ''
    out.append(f'  {l}{mark}')

# CheckpointLoaderSimple 选项
ckpt = oi.get('CheckpointLoaderSimple', {}).get('input', {}).get('required', {}).get('ckpt_name')
ckpts = ckpt[0] if isinstance(ckpt, list) and isinstance(ckpt[0], list) else []
out.append(f'\n=== CheckpointLoaderSimple ({len(ckpts)}) ===')
for c in ckpts:
    out.append(f'  {c}')

# 所有节点类型（找 VNCCS、Pose、IPAdapter）
out.append('\n=== 节点类型（按关键字）===')
for n in sorted(oi.keys()):
    nl = n.lower()
    if 'vnccs' in nl or 'pose' in nl or 'ipadapter' in nl or 'faceid' in nl or 'reference' in nl or 'yuzu' in nl:
        out.append(f'  {n}')

# /queue + /history
q = get('/queue')
h = get('/history')
out.append(f'\n=== queue_running: {len(q.get("queue_running",[]))} pending: {len(q.get("queue_pending",[]))}')
out.append(f'=== history: {len(h)} entries')

text = '\n'.join(out)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\local_8188.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(text)
