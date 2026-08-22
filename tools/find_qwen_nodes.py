"""查 Qwen-Image 专用的 CLIP 加载节点"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

# 找所有可能与 qwen 相关的节点
qwen_related = [k for k in data.keys() if 'qwen' in k.lower() or 'image' in k.lower() and 'edit' in k.lower()]
print('=== 与 qwen 相关的节点 ===')
for k in qwen_related[:30]:
    print(' ', k)

# 找 CLIP 加载类节点
print('\n=== 所有 CLIPLoader 类节点 ===')
clip_loaders = [k for k in data.keys() if 'clip' in k.lower() and 'load' in k.lower()]
for k in clip_loaders:
    print(' ', k)

# 找 QwenImage 节点
print('\n=== QwenImage* / Qwen* 节点 ===')
qwen_nodes = [k for k in data.keys() if k.startswith('Qwen') or 'Qwen' in k]
for k in qwen_nodes:
    print(' ', k)
