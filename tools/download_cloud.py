"""下载云端 panel v1 图像"""
import socket, ssl, json, os, time
def http_get(host, path, port=443, timeout=15, binary=False):
    s = socket.create_connection((host, port), timeout=timeout)
    if port == 443:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f'GET {path} HTTP/1.0\r\nHost: {host}\r\nUser-Agent: dl/1.0\r\nConnection: close\r\n\r\n'
    s.sendall(req.encode())
    chunks = []
    while True:
        d = s.recv(65536)
        if not d:
            break
        chunks.append(d)
    s.close()
    raw = b''.join(chunks)
    if b'\r\n\r\n' in raw:
        head, body = raw.split(b'\r\n\r\n', 1)
    else:
        return raw
    return body

host = '8188-cpod-1ud2p6nylymq.pod.compshare.cn'
out_dir = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_panel_v1'
os.makedirs(out_dir, exist_ok=True)

# history
h = json.loads(http_get(host, '/history'))
log = []
for pid, ent in h.items():
    status = ent.get('status', {})
    if isinstance(status, dict) and status.get('status_str') == 'success':
        for node_id, node_out in (ent.get('outputs') or {}).items():
            for img in node_out.get('images', []):
                fn = img.get('filename', '')
                sub = img.get('subfolder', '')
                ft = img.get('type', 'output')
                params = f"filename={fn}&subfolder={sub}&type={ft}"
                view_path = f'/view?{params}'
                data = http_get(host, view_path, timeout=30, binary=True)
                if isinstance(data, bytes) and len(data) > 1000:
                    out_fn = os.path.join(out_dir, f'{pid[:8]}_{fn}')
                    with open(out_fn, 'wb') as f:
                        f.write(data)
                    log.append(f'  SAVED {out_fn} ({len(data)} bytes)')
                else:
                    log.append(f'  ERR {pid} {fn}: got {len(data) if isinstance(data,bytes) else "?"} bytes')

text = '\n'.join(log)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\dl_log.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(text)
