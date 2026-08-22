"""探测 ComfyUI 是否识别新 LoRA + 触发 model 列表刷新"""
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

def http_post(host, path, port=443, timeout=15):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f'POST {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode())
    chunks = []
    while True:
        d = s.recv(65536)
        if not d: break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks).decode('utf-8', 'ignore')
    return raw[:400]

host = '8188-cpod-1ud2p6nylymq.pod.compshare.cn'

# 1. 尝试 /refresh (老 ComfyUI 端点)
print('=== POST /refresh ===')
print(http_post(host, '/refresh'))

# 2. 尝试 /models/refresh
print('\n=== POST /models/refresh ===')
print(http_post(host, '/models/refresh'))

# 3. 尝试 /api/models/refresh
print('\n=== POST /api/models/refresh ===')
print(http_post(host, '/api/models/refresh'))

# 4. 读 /object_info 看 LoraLoader 列表
oi = json.loads(http_get(host, '/object_info'))
ll = oi.get('LoraLoader', {}).get('input', {}).get('required', {}).get('lora_name')
opts = ll[0] if isinstance(ll, list) and isinstance(ll[0], list) else []
print('\n=== 当前 LoraLoader 选项 ===')
for o in opts:
    marker = ' <== YUZU' if 'Yuzu' in o else ''
    print(f'  {o}{marker}')
