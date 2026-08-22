"""列出 compshare 8188 所有可用的 CLIP 文件"""
import urllib.request, json, ssl
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
BASE = 'https://8188-cpod-1ud2p6nylymq.pod.compshare.cn'
r = urllib.request.urlopen(BASE + '/object_info', timeout=30, context=ctx)
data = json.loads(r.read())

def list_models(node, key):
    spec = data.get(node, {}).get('input', {}).get('required', {}).get(key)
    if isinstance(spec, list) and spec and isinstance(spec[0], list):
        return spec[0]
    return None

print('=== CLIPLoader.clip_name 全部 ===')
for m in list_models('CLIPLoader', 'clip_name') or []:
    print(' ', m)
print('\n=== CLIPLoader.type ===')
for t in (data.get('CLIPLoader', {}).get('input', {}).get('required', {}).get('type') or [[]])[0]:
    print(' ', t)
print('\n=== UNETLoader 全部 ===')
for m in list_models('UNETLoader', 'unet_name') or []:
    print(' ', m)
print('\n=== TextEncodeQwenImageEdit 节点 inputs ===')
print(json.dumps(data.get('TextEncodeQwenImageEdit', {}).get('input', {}), indent=2)[:500])
