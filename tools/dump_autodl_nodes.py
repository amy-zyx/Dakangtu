"""深挖 object_info 看看真实结构"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=30, context=ctx)
data = json.loads(r.read())

# 直接 dump CheckpointLoaderSimple 节点的全部内容
for node in ['CheckpointLoaderSimple', 'UNETLoader', 'LoraLoader']:
    print(f'\n========= {node} =========')
    if node not in data:
        print('NODE NOT IN OBJECT_INFO')
        continue
    info = data[node]
    # 列举所有 input 字段
    required = info['input'].get('required', {})
    for k, v in required.items():
        print(f'  required.{k} => {str(v)[:200]}')
    if 'optional' in info['input']:
        opt = info['input']['optional']
        for k, v in opt.items():
            print(f'  optional.{k} => {str(v)[:200]}')
