"""扫描 AutoDL ComfyUI 完整模型清单（修正版）"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

def list_models(node_key, widget_name):
    if node_key not in data:
        return []
    spec = data[node_key]['input']['required'].get(widget_name)
    if spec is None:
        return []
    # 真实结构：spec 是 [列表, {...元数据}]，列表里是文件名
    if isinstance(spec, list) and len(spec) >= 1 and isinstance(spec[0], list):
        return spec[0]
    return []

for label, node, key in [
    ('Checkpoints', 'CheckpointLoaderSimple', 'ckpt_name'),
    ('UNET', 'UNETLoader', 'unet_name'),
    ('VAE', 'VAELoader', 'vae_name'),
    ('CLIP_name1', 'DualCLIPLoader', 'clip_name1'),
    ('CLIP_name2', 'DualCLIPLoader', 'clip_name2'),
    ('ControlNet', 'ControlNetLoader', 'control_net_name'),
]:
    items = list_models(node, key)
    print(f'\n===== {label} ({len(items)}) =====')
    for m in items:
        print(' ', m)

lora_items = list_models('LoraLoader', 'lora_name')
print(f'\n===== LoRA ({len(lora_items)}) =====')
for m in lora_items:
    print(' ', m)

# 找一下含目标关键词的模型
print('\n===== 项目所需模型匹配检查 =====')
targets = {
    'Anima-Turbo': ['anima', 'turbo'],
    'Qwen-Image-Edit': ['qwen', 'image-edit'],
    'GGUF Q5': ['q5', 'gguf'],
    'SAM': ['sam'],
    'IP-Adapter': ['ip-adapter', 'ipadapter'],
    'InstantID': ['instantid'],
    'Chroma': ['chroma'],
    'FLUX': ['flux'],
    'Anima': ['anima'],
}
all_models = (list_models('CheckpointLoaderSimple', 'ckpt_name')
              + list_models('UNETLoader', 'unet_name')
              + lora_items)
for name, keys in targets.items():
    matches = [m for m in all_models if any(k in m.lower() for k in keys)]
    if matches:
        print(f'  [OK]   {name}: {matches}')
    else:
        print(f'  [缺]  {name}: 未找到')
