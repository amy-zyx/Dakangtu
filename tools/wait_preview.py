import json, urllib.request, time
# Wait for the queued prompt to finish
for i in range(120):
    try:
        hist = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/history/9e311187-c2c3-4189-8ea3-623ab72749b2', timeout=10).read())
        if '9e311187-c2c3-4189-8ea3-623ab72749b2' in hist:
            entry = hist['9e311187-c2c3-4189-8ea3-623ab72749b2']
            status = entry.get('status', {})
            print(f"[{i*5}s] status: {status.get('completed', False)}, executing: {status.get('executing', False)}")
            if status.get('completed'):
                # Output node is 798 (VNCCS_CharacterGenerator)
                out = entry.get('outputs', {}).get('798', {})
                for k, v in out.items():
                    if isinstance(v, list) and v and 'filename' in v[0]:
                        print(f"  {k}:")
                        for img in v:
                            print(f"    {img}")
                break
    except Exception as e:
        print(f"[{i*5}s] waiting... ({e})")
    time.sleep(5)
