"""简化版：直接打印，不用 sleep 循环"""
import urllib.request, ssl, json
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
lines = []
for path in ['/system_stats', '/queue', '/object_info', '/history', '/prompt']:
    try:
        r = urllib.request.urlopen(base + path, timeout=6, context=ctx)
        body = r.read()[:100].decode('utf-8','ignore')
        lines.append(f'{path} | OK {r.status} | {body}')
    except urllib.error.HTTPError as e:
        body = e.read()[:100].decode('utf-8','ignore')
        lines.append(f'{path} | HTTP {e.code} | {body}')
    except Exception as e:
        lines.append(f'{path} | ERR | {e}')
out = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\probe2.txt'
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('wrote', out)
