"""查云端历史看 db728526 prompt 的状态"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'

# 当前队列
qr = urllib.request.urlopen(base + '/queue', timeout=10, context=ctx)
print('=== /queue ===')
print(qr.read().decode('utf-8'))

# 该 prompt 的历史
prompt_id = 'db728526-a6cb-4113-9ce4-f6afbcdcc754'
hr = urllib.request.urlopen(base + f'/history/{prompt_id}', timeout=10, context=ctx)
body = hr.read().decode('utf-8')
print(f'\n=== /history/{prompt_id} (length {len(body)}) ===')
# 只显示前 2000 字符
print(body[:2000])
