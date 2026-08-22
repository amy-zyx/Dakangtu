"""探测 compshare - 极速版，每个 socket 加超时"""
import socket, urllib.request, ssl
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
host = 'cpod-1ud2p6nylymq.podtcp.compshare.cn'
out = []
out.append(f'HOST = {host}')

# DNS（最短超时）
socket.setdefaulttimeout(2)
try:
    ip = socket.gethostbyname(host)
    out.append(f'DNS OK: {ip}')
except Exception as e:
    out.append(f'DNS ERR: {e}')

# 端口快速扫描
open_ports = []
for port in [22, 28682, 8188, 7860, 8000, 8443, 9000, 6006, 8888, 5000, 5173]:
    try:
        s = socket.create_connection((host, port), timeout=1.5)
        open_ports.append(port)
        s.close()
    except Exception:
        pass
out.append(f'OPEN TCP: {open_ports}')

# 对开放端口做 HTTP
for port in open_ports:
    for proto in ['http', 'https']:
        try:
            r = urllib.request.urlopen(f'{proto}://{host}:{port}/', timeout=2, context=ctx)
            body = r.read(180).decode('utf-8', 'ignore').replace('\n', ' ').replace('\r', ' ')
            out.append(f'  {proto}://{host}:{port}  -> {r.status} | {body[:140]}')
            break  # http 通了就不试 https
        except urllib.error.HTTPError as e:
            out.append(f'  {proto}://{host}:{port}  -> HTTP {e.code}')
        except Exception:
            pass

text = '\n'.join(out)
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\probe2.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('OK lines=', len(out))
print('---')
print(text)
