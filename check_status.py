import json, urllib.request
h = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/history/47cb21b1-f073-43c7-ac7e-13197c7e40da', timeout=10).read())
k = '47cb21b1-f073-43c7-ac7e-13197c7e40da'
e = h.get(k, {})
st = e.get('status', {})
print('state:', st.get('status_str'), 'done:', st.get('completed'))
print('---outputs(797)---')
print(json.dumps(e.get('outputs', {}).get('797', {}), indent=2)[:600])
print('---outputs(798)---')
print(json.dumps(e.get('outputs', {}).get('798', {}), indent=2)[:600])
print('---last error---')
for m in st.get('messages', []):
    if m[0] == 'execution_error':
        print(json.dumps(m[1], indent=2)[:600])
        break
