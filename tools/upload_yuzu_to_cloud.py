"""
上传 Yuzu LoRA 到 compshare (SSH key 方式)
需要先在远端 ~/.ssh/authorized_keys 加上本地公钥
"""
import subprocess, os, time

SSH_KEY = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\.ssh_keys\id_rsa'
LOCAL_LORA = r'C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\models\loras\Yuzu Soft[style]-Illus.safetensors'
REMOTE = 'root@cpod-1ud2p6nylymq.podtcp.compshare.cn'
PORT = '28682'

print(f'=== 1. 测试 SSH key 登录 ===')
test = subprocess.run(
    ['ssh', '-i', SSH_KEY, '-p', PORT, '-o', 'BatchMode=yes', '-o', 'StrictHostKeyChecking=no',
     f'{REMOTE}', 'echo LOGIN_OK && uname -a && ls -la /root/ 2>/dev/null | head -5'],
    capture_output=True, text=True, timeout=15
)
print('stdout:', test.stdout)
print('stderr:', test.stderr)
print('returncode:', test.returncode)

if test.returncode != 0:
    print('\n!! SSH key 还没生效，请你先跑上面那条贴公钥的命令')
    raise SystemExit(1)

print('\n=== 2. 找远端 ComfyUI models 路径 ===')
find = subprocess.run(
    ['ssh', '-i', SSH_KEY, '-p', PORT, '-o', 'BatchMode=yes',
     f'{REMOTE}', "find / -name 'loras' -type d 2>/dev/null | grep -i comfy | head -5"],
    capture_output=True, text=True, timeout=30
)
print('loras dirs:', find.stdout)

print('\n=== 3. 上传 Yuzu LoRA (scp) ===')
# 先 mkdir，再 scp
mk = subprocess.run(
    ['ssh', '-i', SSH_KEY, '-p', PORT, '-o', 'BatchMode=yes',
     f'{REMOTE}', "mkdir -p ~/ComfyUI/models/loras/ && echo MKDIR_OK"],
    capture_output=True, text=True, timeout=10
)
print('mkdir:', mk.stdout, mk.stderr)

size_mb = os.path.getsize(LOCAL_LORA) / 1024 / 1024
print(f'  本地文件: {size_mb:.1f} MB')
t0 = time.time()
scp = subprocess.run(
    ['scp', '-i', SSH_KEY, '-P', PORT, '-o', 'BatchMode=yes',
     LOCAL_LORA, f'{REMOTE}:~/ComfyUI/models/loras/'],
    capture_output=True, text=True, timeout=300
)
print(f'  scp 用时: {time.time()-t0:.1f}s')
print('  stdout:', scp.stdout)
print('  stderr:', scp.stderr)
print('  returncode:', scp.returncode)

if scp.returncode == 0:
    print('\n=== 4. 验证上传 ===')
    chk = subprocess.run(
        ['ssh', '-i', SSH_KEY, '-p', PORT, '-o', 'BatchMode=yes',
         f'{REMOTE}', "ls -la ~/ComfyUI/models/loras/ | grep -i yuzu"],
        capture_output=True, text=True, timeout=10
    )
    print('  远端 yuzu 文件:')
    print(chk.stdout)
else:
    print('\n!! 上传失败')
