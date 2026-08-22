"""快速检查 AutoDL / compshare 状态"""
import urllib.request, ssl, json
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
out = []

# AutoDL
out.append('=== AutoDL (8443) ===')
for ep in ['/system_stats', '/queue', '/prompt', '/object_info', '/history']:
    try:
        r = urllib.request.urlopen(f'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443{ep}', timeout=4, context=ctx)
        out.append(f'  {ep}: {r.status}')
    except urllib.error.HTTPError as e:
        out.append(f'  {ep}: HTTP {e.code}')
    except Exception as e:
        out.append(f'  {ep}: ERR {str(e)[:60]}')

# compshare
out.append('\n=== compshare (28682 HTTP) ===')
for proto in ['http', 'https']:
    try:
        r = urllib.request.urlopen(f'{proto}://cpod-1ud2p6nylymq.podtcp.compshare.cn:28682/', timeout=4, context=ctx)
        out.append(f'  {proto}://...:28682/: {r.status} | {r.read(80).decode("utf-8","ignore")}')
    except urllib.error.HTTPError as e:
        out.append(f'  {proto}://...:28682/: HTTP {e.code}')
    except Exception as e:
        out.append(f'  {proto}://...:28682/: ERR {str(e)[:60]}')

# 探测 8188/7860
import socket
out.append('\n=== compshare 其他端口扫描 ===')
host = 'cpod-1ud2p6nylymq.podtcp.compshare.cn'
for p in [8188, 7860, 8000, 9000, 22, 6006]:
    s = socket.create_connection((host, p), timeout=2)
    s.close()
    out.append(f'  {p}: OPEN')

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_recheck.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('OK')
