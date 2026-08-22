import json, urllib.request, urllib.error

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_tennis_preview_api.json', encoding='utf-8') as f:
    body = json.load(f)

req = urllib.request.Request(
    'http://127.0.0.1:8188/prompt',
    data=json.dumps(body).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
)
try:
    r = urllib.request.urlopen(req, timeout=30)
    print('STATUS:', r.status)
    print(r.read().decode('utf-8')[:1000])
except urllib.error.HTTPError as e:
    print('HTTP ERROR:', e.code)
    print(e.read().decode('utf-8')[:2000])
