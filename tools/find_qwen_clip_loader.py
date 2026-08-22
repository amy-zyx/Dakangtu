"""查 CLIPLoader 和 TripleCLIPLoader 接受什么 qwen 相关文件"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

for n in ['CLIPLoader', 'TripleCLIPLoader', 'QuadrupleCLIPLoader', 'CLIPLoaderGGUF', 'DualCLIPLoaderGGUF', 'TripleCLIPLoaderGGUF']:
    info = data.get(n)
    if not info: continue
    print(f'\n========= {n} =========')
    spec = info['input']['required']
    for k, v in spec.items():
        if isinstance(v, list) and v and isinstance(v[0], list):
            files = v[0]
            qwen_files = [f for f in files if 'qwen' in f.lower()]
            print(f'  required.{k}: 共 {len(files)} 个文件')
            print(f'    其中 Qwen 相关: {qwen_files[:10]}')
        else:
            print(f'  required.{k}: {str(v)[:150]}')
    if info['input'].get('optional'):
        for k, v in info['input']['optional'].items():
            print(f'  optional.{k}: {str(v)[:200]}')

# 找含 qwen vl / qwen image / qwen2.5 的所有文件
print('\n========= 所有含 qwen 的模型文件名 =========')
all_files = set()
for n, wkey in [('UNETLoader','unet_name'),('VAELoader','vae_name'),
                ('CLIPLoader','clip_name'),('DualCLIPLoader','clip_name1'),
                ('TripleCLIPLoader','clip_name1'),
                ('QuadrupleCLIPLoader','clip_name1')]:
    info = data.get(n)
    if not info: continue
    spec = info['input']['required'].get(wkey)
    if isinstance(spec, list) and spec and isinstance(spec[0], list):
        for f in spec[0]:
            all_files.add(f)
qwen_files = sorted(f for f in all_files if 'qwen' in f.lower())
for f in qwen_files:
    print(' ', f)
