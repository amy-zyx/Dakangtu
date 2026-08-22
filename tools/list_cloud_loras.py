"""正确解析 LoraLoader 列表"""
import socket, ssl, json

def http_get(host, path, port=443, timeout=15):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f'GET {path} HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode())
    chunks = []
    while True:
        d = s.recv(65536)
        if not d: break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks)
    if b'\r\n\r\n' in raw:
        return raw.split(b'\r\n\r\n', 1)[1].decode('utf-8','ignore')
    return raw.decode('utf-8','ignore')

host = '8188-cpod-1ud2p6nylymq.pod.compshare.cn'
oi = json.loads(http_get(host, '/object_info'))

def get_options(node_name, param_name):
    p = oi.get(node_name, {}).get('input', {}).get('required', {}).get(param_name)
    if p is None: return []
    if isinstance(p, list) and len(p) > 0:
        first = p[0]
        if isinstance(first, list):
            return first
        return [first]
    return []

out = []
out.append('=== LoraLoader (SDXL/SD 链) ===')
for n in get_options('LoraLoader', 'lora_name'):
    out.append(f'  {n}')

out.append('\n=== LoraLoaderModelOnly ===')
for n in get_options('LoraLoaderModelOnly', 'lora_name'):
    out.append(f'  {n}')

out.append('\n=== CheckpointLoaderSimple ===')
for n in get_options('CheckpointLoaderSimple', 'ckpt_name'):
    out.append(f'  {n}')

out.append('\n=== UNETLoader ===')
for n in get_options('UNETLoader', 'unet_name'):
    out.append(f'  {n}')

out.append('\n=== CLIPLoader ===')
for n in get_options('CLIPLoader', 'clip_name'):
    out.append(f'  {n}')

out.append('\n=== VAELoader ===')
for n in get_options('VAELoader', 'vae_name'):
    out.append(f'  {n}')

# 找 Yuzu/Illustrious/Anima
out.append('\n=== 含 yuzu/illust/anima 关键词 ===')
for node in ['LoraLoader', 'LoraLoaderModelOnly']:
    for n in get_options(node, 'lora_name'):
        nl = n.lower()
        if 'yuzu' in nl or 'illust' in nl or 'anima' in nl or 'illustrious' in nl:
            out.append(f'  [{node}] {n}')

text = '\n'.join(out)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_loras2.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(text)
