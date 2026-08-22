"""等待队列并下载 db728526 的输出"""
import urllib.request, ssl, json, urllib.parse, time, os
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
BASE = 'https://u1124262-787335b17f4f.bjb2.seetacloud.com:8443'
prompt_id = 'db728526-a6cb-4113-9ce4-f6afbcdcc754'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_rita_v1'
os.makedirs(OUT_DIR, exist_ok=True)

print('>>> 开始轮询...')
for i in range(180):  # 最多 6 分钟
    time.sleep(3)
    # 1. 查队列
    try:
        qr = urllib.request.urlopen(BASE + '/queue', timeout=8, context=ctx)
        qd = json.loads(qr.read())
        running = qd.get('queue_running', [])
        pending = qd.get('queue_pending', [])
        my_in_running = any(p[1] == prompt_id for p in running)
        my_in_pending = any(p[1] == prompt_id for p in pending)
    except Exception as e:
        print(f'  [{i}] queue err: {e}')
        continue
    # 2. 查历史
    try:
        hr = urllib.request.urlopen(BASE + f'/history/{prompt_id}', timeout=8, context=ctx)
        hist = json.loads(hr.read())
    except Exception as e:
        hist = {}
        print(f'  [{i}] history err: {e}')

    status = 'DONE' if (hist and prompt_id in hist) else ('RUNNING' if my_in_running else ('PENDING' if my_in_pending else '?'))
    print(f'  [{i:3d}] {i*3:3d}s | queue: running={len(running)} pending={len(pending)} | 我的: {status}')

    if hist and prompt_id in hist:
        entry = hist[prompt_id]
        print(f'\n>>> 完成！outputs:')
        outputs = entry.get('outputs', {})
        if not outputs:
            print('   无输出，检查 status:', entry.get('status', {}))
        for node_id, node_out in outputs.items():
            if 'images' in node_out:
                for img in node_out['images']:
                    fn = img['filename']
                    sub = img.get('subfolder', '')
                    tp = img.get('type', 'output')
                    url = f'{BASE}/view?filename={urllib.parse.quote(fn)}&subfolder={urllib.parse.quote(sub)}&type={tp}'
                    local = os.path.join(OUT_DIR, fn)
                    print(f'   下载 {fn} -> {local}')
                    with urllib.request.urlopen(url, timeout=60, context=ctx) as r:
                        with open(local, 'wb') as f:
                            f.write(r.read())
                    print(f'   OK {os.path.getsize(local)} bytes')
        break
else:
    print('!! 超时')
