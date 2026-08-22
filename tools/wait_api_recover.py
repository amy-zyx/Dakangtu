"""等待 API 恢复"""
import urllib.request, ssl, json, time
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
results = []
for k in range(10):
    time.sleep(5)
    for path in ['/system_stats', '/queue', '/object_info']:
        try:
            r = urllib.request.urlopen(base + path, timeout=8, context=ctx)
            results.append((k, path, r.status, r.read()[:120].decode('utf-8','ignore')))
        except Exception as e:
            results.append((k, path, 'ERR', str(e)[:80]))

# 写文件
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\probe_result.txt', 'w', encoding='utf-8') as f:
    for k, path, status, body in results:
        f.write(f'attempt {k} | {path} | {status} | {body}\n')
print('done, wrote probe_result.txt')
