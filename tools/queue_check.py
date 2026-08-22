import urllib.request, json
BASE = 'http://127.0.0.1:8188'
lines = []
try:
    r = urllib.request.urlopen(BASE + '/queue', timeout=5)
    q = json.loads(r.read())
    lines.append('=== /queue ===')
    lines.append('running: ' + str([p[1] for p in q.get('queue_running', [])]))
    lines.append('pending: ' + str([p[1] for p in q.get('queue_pending', [])]))
    lines.append('exec_info: ' + str(q.get('exec_info', {})))
except Exception as e:
    lines.append(f'/queue ERR: {e}')

pid = 'a1f56918-54d3-4918-b4b7-60a827cada6f'
try:
    r = urllib.request.urlopen(BASE + f'/history/{pid}', timeout=5)
    h = json.loads(r.read())
    lines.append(f'\n=== /history/{pid} ===')
    if h and pid in h:
        ent = h[pid]
        lines.append('status: ' + str(ent.get('status', {})))
        lines.append('outputs keys: ' + str(list(ent.get('outputs', {}).keys())))
    else:
        lines.append('not in history yet')
except Exception as e:
    lines.append(f'/history ERR: {e}')

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\queue_check.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('OK lines=', len(lines))
