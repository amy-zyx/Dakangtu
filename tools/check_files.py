import os
d = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_v1'
if not os.path.isdir(d):
    print('NO_DIR')
else:
    files = sorted(os.listdir(d))
    if not files:
        print('EMPTY')
    for f in files:
        full = os.path.join(d, f)
        print(f'{f}\t{os.path.getsize(full)} bytes')
