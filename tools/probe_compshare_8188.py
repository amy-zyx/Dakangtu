"""compshare 8188 完整模型盘点"""
import urllib.request, json, ssl
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
BASE = 'https://8188-cpod-1ud2p6nylymq.pod.compshare.cn'

r = urllib.request.urlopen(BASE + '/system_stats', timeout=30, context=ctx)
sys = json.loads(r.read())
print('=== system_stats ===')
devs = sys.get('devices', [])
for d in devs:
    print(f'  GPU: {d.get("name")} (vram_total={d.get("memory_total")})')
print(f'  RAM: {sys.get("system",{}).get("ram_total",0)//(1024**3)} GB')
print(f'  ComfyUI: {sys.get("system",{}).get("comfyui_version")}')

r = urllib.request.urlopen(BASE + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

def list_models(node, key):
    if node not in data: return None
    spec = data[node]['input']['required'].get(key)
    if isinstance(spec, list) and spec and isinstance(spec[0], list):
        return spec[0]
    return None

print('\n=== Checkpoints ===')
for m in list_models('CheckpointLoaderSimple','ckpt_name') or []:
    print(' ', m)

print('\n=== UNET ===')
for m in list_models('UNETLoader','unet_name') or []:
    print(' ', m)

print('\n=== VAE ===')
for m in list_models('VAELoader','vae_name') or []:
    print(' ', m)

loras = list_models('LoraLoader','lora_name') or []
print(f'\n=== LoRA ({len(loras)}) ===')
for m in loras:
    print(' ', m)

print('\n=== 双/单 CLIPLoader type 选项 ===')
cliploader_types = data.get('CLIPLoader',{}).get('input',{}).get('required',{}).get('type', [None])[0]
if cliploader_types:
    print('  CLIPLoader.type:', cliploader_types)

# 找 Qwen / Yuzu / 角色一致性 节点
print('\n=== 关键节点存在性 ===')
for n in ['IPAdapter', 'IPAdapterFaceID', 'IPAdapterInsightFaceLoader',
          'CLIPLoader', 'CLIPTextEncode', 'QwenLoader', 'TextEncodeQwenImageEdit',
          'ModelSamplingFlux', 'CheckpointLoaderSimple', 'LoraLoader', 'VAEDecode']:
    print(f'  {n}: {"FOUND" if n in data else "MISSING"}')

# 检查输出目录
print('\n=== 检查 yuzu sdxl qwen 模型 ===')
all_files = (list_models('CheckpointLoaderSimple','ckpt_name') or []) + \
            (list_models('UNETLoader','unet_name') or []) + \
            (loras)
for kw in ['yuzu', 'sdxl', 'illustrious', 'anima', 'qwen', 'dmd2', 'animagine', 'pony', 'flux', 'chroma']:
    matches = [f for f in all_files if kw in f.lower()]
    if matches:
        print(f'  {kw}: {matches}')
