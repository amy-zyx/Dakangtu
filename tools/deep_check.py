"""深度查队列和历史"""
import urllib.request, json
BASE = 'http://127.0.0.1:8188'
lines = []
try:
    r = urllib.request.urlopen(BASE + '/queue', timeout=5)
    q = json.loads(r.read())
    lines.append('=== /queue (raw) ===')
    lines.append(json.dumps(q, indent=2)[:1500])
except Exception as e:
    lines.append(f'/queue ERR: {e}')

# 查 /history 看 dea1a9c1
try:
    r = urllib.request.urlopen(BASE + '/history', timeout=5)
    h = json.loads(r.read())
    lines.append(f'\n=== /history 总条数: {len(h)} ===')
    for pid in list(h.keys())[-3:]:
        ent = h[pid]
        lines.append(f'  {pid[:8]}: status={ent.get("status",{})} out={list(ent.get("outputs",{}).keys())}')
except Exception as e:
    lines.append(f'/history ERR: {e}')

# 查 /system_stats
try:
    r = urllib.request.urlopen(BASE + '/system_stats', timeout=5)
    s = json.loads(r.read())
    devs = s.get('devices', [])
    lines.append(f'\n=== /system_stats devices: {len(devs)} ===')
    for d in devs:
        lines.append(f'  name={d.get("name")} mem_total={d.get("memory_total")} mem_free={d.get("memory_free")} type={d.get("type")}')
except Exception as e:
    lines.append(f'/system_stats ERR: {e}')

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\deep_check.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('OK')
