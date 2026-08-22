"""杀掉卡死的 VNCCS_PoseStudio 任务，释放 GPU"""
import urllib.request, json
BASE = 'http://127.0.0.1:8188'
lines = []

# 1. /interrupt 杀掉 running 任务
try:
    req = urllib.request.Request(BASE + '/interrupt', data=b'{}', headers={'Content-Type': 'application/json'}, method='POST')
    r = urllib.request.urlopen(req, timeout=5)
    lines.append(f'POST /interrupt: {r.status} {r.read().decode()[:200]}')
except Exception as e:
    lines.append(f'POST /interrupt ERR: {e}')

import time
time.sleep(3)

# 2. 看队列
try:
    r = urllib.request.urlopen(BASE + '/queue', timeout=5)
    q = json.loads(r.read())
    lines.append(f'\n=== /queue after interrupt ===')
    lines.append(f'  running: {[p[1] for p in q.get("queue_running",[])]}')
    lines.append(f'  pending: {[p[1] for p in q.get("queue_pending",[])]}')
except Exception as e:
    lines.append(f'/queue ERR: {e}')

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\interrupt_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('OK')
