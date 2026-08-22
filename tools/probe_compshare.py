"""探测 compshare 新实例"""
import urllib.request, ssl, socket
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
host = 'cpod-1ud2p6nylymq.podtcp.compshare.cn'
results = []

# DNS
try:
    ip = socket.gethostbyname(host)
    results.append(f'DNS: {ip}')
except Exception as e:
    results.append(f'DNS ERR: {e}')

# TCP
for port in [22, 28682, 8188, 7860, 8000, 8443, 9000, 6006, 8888, 22, 5000, 5173]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, port))
        results.append(f'  {port:5d} : OPEN')
        s.close()
    except Exception:
        pass

# HTTP
for port in [8188, 7860, 8000, 8443, 9000, 6006, 8888, 5000, 5173]:
    for proto in ['http', 'https']:
        try:
            r = urllib.request.urlopen(f'{proto}://{host}:{port}/', timeout=4, context=ctx)
            body = r.read(200).decode('utf-8', 'ignore').replace('\n', ' ')
            results.append(f'  {proto}://{host}:{port}  -> {r.status} | {body[:150]}')
        except urllib.error.HTTPError as e:
            results.append(f'  {proto}://{host}:{port}  -> HTTP {e.code}')
        except Exception:
            pass

out = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\compshare_probe.txt'
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))
print('wrote', out, 'lines:', len(results))
