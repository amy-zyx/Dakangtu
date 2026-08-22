"""等待 a1f56918 完成并下载"""
import urllib.request, json, urllib.parse, time, os
BASE = 'http://127.0.0.1:8188'
OUT_DIR = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_v1'
os.makedirs(OUT_DIR, exist_ok=True)
pid = 'a1f56918-54d3-4918-b4b7-60a827cada6f'
log_path = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_wait.log'
log = open(log_path, 'w', encoding='utf-8')

for i in range(400):  # 最多 13 分钟
    time.sleep(2)
    try:
        r = urllib.request.urlopen(BASE + f'/history/{pid}', timeout=5)
        hist = json.loads(r.read())
    except Exception as e:
        log.write(f'[{i}] err: {e}\n'); log.flush(); continue
    if hist and pid in hist:
        outputs = hist[pid].get('outputs', {})
        log.write(f'[{i}] DONE! outputs keys: {list(outputs.keys())}\n')
        for node_out in outputs.values():
            for img in node_out.get('images', []):
                fn = img['filename']
                sub = img.get('subfolder', '')
                tp = img.get('type', 'output')
                url = f'{BASE}/view?filename={urllib.parse.quote(fn)}&subfolder={urllib.parse.quote(sub)}&type={tp}'
                local = os.path.join(OUT_DIR, fn)
                with urllib.request.urlopen(url, timeout=60) as rr:
                    with open(local, 'wb') as f:
                        f.write(rr.read())
                log.write(f'  [OK] {fn} -> {local} ({os.path.getsize(local)} bytes)\n')
                log.flush()
        log.write('SUCCESS\n')
        log.close()
        break
    if i % 15 == 0:
        try:
            qr = urllib.request.urlopen(BASE + '/queue', timeout=4)
            qd = json.loads(qr.read())
            log.write(f'[{i}] queue: running={[p[1][:8] for p in qd.get("queue_running",[])]} pending={[p[1][:8] for p in qd.get("queue_pending",[])]}\n')
            log.flush()
        except Exception:
            pass
else:
    log.write('TIMEOUT\n')
    log.close()
print('done')
