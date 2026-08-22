"""查 QwenLoader 和 TextEncodeQwenImageEdit 的输入规范"""
import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
r = urllib.request.urlopen(base + '/object_info', timeout=60, context=ctx)
data = json.loads(r.read())

for n in ['QwenLoader', 'TextEncodeQwenImageEdit', 'TextEncodeQwenImageEditPlus',
          'ModelMergeQwenImage', 'TorchCompileModelQwenImage',
          'NunchakuQwenImageDiTLoader', 'QwenImageDiffsynthControlnet']:
    print(f'\n========= {n} =========')
    info = data.get(n)
    if not info:
        print('NOT FOUND')
        continue
    print('  class_type:', info.get('class_type', n))
    print('  category:', info.get('category', ''))
    req = info['input'].get('required', {})
    opt = info['input'].get('optional', {})
    print('  --- required ---')
    for k, v in req.items():
        s = str(v)
        if len(s) > 300: s = s[:300] + '...'
        print(f'    {k}: {s}')
    if opt:
        print('  --- optional ---')
        for k, v in opt.items():
            s = str(v)
            if len(s) > 200: s = s[:200] + '...'
            print(f'    {k}: {s}')
    print('  output:', info.get('output', '?'))
