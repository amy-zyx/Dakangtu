"""本地 8188 健康 + 关键模型/节点检查"""
import urllib.request, json
BASE = 'http://127.0.0.1:8188'
out = []

# 1. system_stats
try:
    r = urllib.request.urlopen(BASE + '/system_stats', timeout=5)
    out.append(f'/system_stats: {r.status}')
    out.append('  body: ' + r.read().decode('utf-8', 'ignore')[:300])
except Exception as e:
    out.append(f'/system_stats ERR: {e}')

# 2. object_info 找 Yuzusoft / Qwen 相关
try:
    r = urllib.request.urlopen(BASE + '/object_info', timeout=10)
    data = json.loads(r.read())
except Exception as e:
    data = {}
    out.append(f'/object_info ERR: {e}')

def list_models(node_key, widget_name):
    if node_key not in data: return []
    spec = data[node_key]['input']['required'].get(widget_name)
    if spec is None: return None
    if isinstance(spec, list) and spec and isinstance(spec[0], list):
        return spec[0]
    return []

# 3. LoRA 中搜 yuzu
loras = list_models('LoraLoader', 'lora_name') or []
yuzu = [l for l in loras if 'yuzu' in l.lower()]
out.append(f'\nLoraLoader 总数: {len(loras)}, 含 yuzu: {yuzu}')

# 4. Checkpoints
ckpts = list_models('CheckpointLoaderSimple', 'ckpt_name') or []
out.append(f'\nCheckpoints: {ckpts}')

# 5. UNET
unets = list_models('UNETLoader', 'unet_name') or []
out.append(f'\nUNETLoader: {unets}')

# 6. CLIPLoader 支持的 type
clip_info = data.get('CLIPLoader', {}).get('input', {}).get('required', {}).get('type')
if clip_info:
    out.append(f'\nCLIPLoader.type: {clip_info[0]}')

# 7. TextEncode 节点
encode_nodes = [k for k in data.keys() if 'TextEncode' in k or 'Qwen' in k]
out.append(f'\nTextEncode 类节点: {encode_nodes[:15]}')

# 8. SDXL base / anime 模型
all_files = set(loras) | set(ckpts) | set(unets)
patterns = ['yuzu', 'sdxl', 'animagine', 'pony', 'anima', 'qwen']
for p in patterns:
    matches = [f for f in all_files if p in f.lower()]
    if matches:
        out.append(f'\n匹配 "{p}": {matches}')

# 9. ControlNet
cn = list_models('ControlNetLoader', 'control_net_name') or []
out.append(f'\nControlNet ({len(cn)}): {cn[:5]}')

# 10. IPAdapter 节点
ip_nodes = [k for k in data.keys() if 'IPAdapter' in k or 'IPAdapter' in k.lower()]
out.append(f'\nIPAdapter 节点: {ip_nodes}')

# 11. InsightFace 节点
if_nodes = [k for k in data.keys() if 'InsightFace' in k or 'FaceID' in k.lower()]
out.append(f'\nFaceID/InsightFace 节点: {if_nodes}')

text = '\n'.join(str(x) for x in out)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\local_probe.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('OK, wrote output/local_probe.txt, len=', len(text))
