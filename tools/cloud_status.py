"""HTTP/1.0 socket 短连接"""
import socket, ssl, json, time

def http_get(host, path, port=443, timeout=8):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f'GET {path} HTTP/1.0\r\nHost: {host}\r\nUser-Agent: probe/1.0\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode())
    chunks = []
    while True:
        d = s.recv(8192)
        if not d:
            break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks).decode('utf-8', 'ignore')
    body = raw.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in raw else raw
    return body

host = '8188-cpod-1ud2p6nylymq.pod.compshare.cn'

# /system_stats
stats = json.loads(http_get(host, '/system_stats'))
out = []
out.append('=== /system_stats ===')
out.append(f"  comfyui: {stats['system'].get('comfyui_version')}")
out.append(f"  python : {stats['system'].get('python_version')}")
out.append(f"  ram_total/free: {stats['system'].get('ram_total',0)/1024**3:.1f} / {stats['system'].get('ram_free',0)/1024**3:.1f} GB")
for d in stats.get('devices', []):
    out.append(f"  GPU {d.get('name','?')}: vram_total {d.get('vram_total',0)/1024**3:.1f}GB free {d.get('vram_free',0)/1024**3:.1f}GB")

# /queue
q = json.loads(http_get(host, '/queue'))
out.append('\n=== /queue ===')
out.append(f"  running: {len(q.get('queue_running',[]))}")
for item in q.get('queue_running', []):
    pid = item[1] if len(item) > 1 else '?'
    out.append(f'    {pid}')
out.append(f"  pending: {len(q.get('queue_pending',[]))}")

# /history
h = json.loads(http_get(host, '/history'))
out.append('\n=== /history ===')
out.append(f"  entries: {len(h)}")
for pid, ent in h.items():
    status = ent.get('status', '?')
    imgs = sum(len(v.get('images',[])) for v in (ent.get('outputs') or {}).values())
    out.append(f'  {pid} status={status} imgs={imgs}')

text = '\n'.join(out)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_status.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(text)
