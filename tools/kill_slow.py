"""杀掉慢任务"""
import urllib.request
BASE = 'http://127.0.0.1:8188'
req = urllib.request.Request(BASE + '/interrupt', data=b'{}',
                              headers={'Content-Type': 'application/json'},
                              method='POST')
try:
    r = urllib.request.urlopen(req, timeout=5)
    print(f'/interrupt: {r.status}')
except Exception as e:
    print(f'err: {e}')

import time; time.sleep(2)

# 顺便清掉 pending 的自己
req2 = urllib.request.Request(BASE + '/queue', data=b'{"clear": true}',
                               headers={'Content-Type': 'application/json'},
                               method='POST')
try:
    r2 = urllib.request.urlopen(req2, timeout=5)
    print(f'/queue clear: {r2.status} {r2.read()[:200]}')
except urllib.error.HTTPError as e:
    print(f'/queue clear err: {e.code} {e.read()[:200]}')
except Exception as e:
    print(f'/queue clear err: {e}')

# 看现在队列
r3 = urllib.request.urlopen(BASE + '/queue', timeout=5)
print(f'queue: {r3.read().decode()[:300]}')
