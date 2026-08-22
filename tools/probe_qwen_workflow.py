"""查清 Qwen-Image-Edit 2511 工作流所需的所有具体节点名"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

def list_models(node_key, widget_name):
    if node_key not in data:
        return None
    spec = data[node_key]['input']['required'].get(widget_name)
    if spec is None:
        return None
    if isinstance(spec, list) and len(spec) >= 1 and isinstance(spec[0], list):
        return spec[0]
    return []

# VAE 名字
vae = list_models('VAELoader', 'vae_name')
print('=== VAE (Qwen 优先) ===')
for v in vae or []:
    if 'qwen' in v.lower() or 'ae' in v.lower():
        print(' ', v)

# CLIP name1 / name2
clip1 = list_models('DualCLIPLoader', 'clip_name1') or []
clip2 = list_models('DualCLIPLoader', 'clip_name2') or []
print('\n=== DualCLIPLoader.clip_name1 (Qwen 优先) ===')
for v in clip1:
    if 'qwen' in v.lower() or 'vl' in v.lower():
        print(' ', v)
print('\n=== DualCLIPLoader.clip_name2 (Qwen 优先) ===')
for v in clip2:
    if 'qwen' in v.lower() or 'vl' in v.lower():
        print(' ', v)

# KSampler 的 sampler / scheduler 可选项
print('\n=== KSampler 可用 sampler ===')
ks = data.get('KSampler', {}).get('input', {}).get('required', {})
sampler_opt = ks.get('sampler_name', [None])[0]
sched_opt = ks.get('scheduler', [None])[0]
if isinstance(sampler_opt, list):
    print('  sampler:', sampler_opt)
if isinstance(sched_opt, list):
    print('  scheduler:', sched_opt)

# ModelSamplingFlux 节点存在性
print('\n=== 关键节点存在性检查 ===')
for n in ['ModelSamplingFlux', 'CFGNorm', 'EmptyLatentImage', 'EmptySD3LatentImage', 'CLIPTextEncode', 'SaveImage', 'VAEDecode', 'LoraLoader', 'LoadImage']:
    print(f'  {n}: {"FOUND" if n in data else "MISSING"}')

# UNETLoader 权重类型
print('\n=== UNETLoader.weight_dtype 可选项 ===')
unet_info = data.get('UNETLoader', {}).get('input', {}).get('required', {}).get('weight_dtype')
if unet_info:
    print('  ', unet_info[0] if isinstance(unet_info, list) else unet_info)
