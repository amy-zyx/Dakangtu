"""短超时 + 并行探测"""
import socket, concurrent.futures
hosts = [
    '8188-cpod-1ud2p6nylymq.pod.compshare.cn',
    'cpod-1ud2p6nylymq.pod.compshare.cn',
    'cpod-1ud2p6nylymq.podtcp.compshare.cn',
]
ports = [443, 80, 8188, 8189, 22, 28682, 7860, 8000]

def probe(hp):
    h, p = hp
    try:
        s = socket.create_connection((h, p), timeout=1.5)
        s.close()
        return f'  {h}:{p} : OPEN'
    except socket.timeout:
        return f'  {h}:{p} : TIMEOUT'
    except Exception as e:
        return f'  {h}:{p} : {type(e).__name__}'

jobs = [(h, p) for h in hosts for p in ports]
out = []
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
    for r in ex.map(probe, jobs):
        out.append(r)

with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\recheck_new.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('DONE', len(out))
