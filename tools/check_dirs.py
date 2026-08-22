"""检查多个输出目录"""
import os
dirs = [
    r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\cloud_panel_v1',
    r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_v1',
    r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\yuzu_v2',
]
for d in dirs:
    name = os.path.basename(d)
    print(f'\n=== {name} ===')
    if not os.path.isdir(d):
        print('  (dir not exist)')
        continue
    files = sorted(os.listdir(d))
    if not files:
        print('  EMPTY')
        continue
    for f in files:
        full = os.path.join(d, f)
        print(f'  {f}\t{os.path.getsize(full)//1024} KB')
