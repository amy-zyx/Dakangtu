"""流式管道传 DMD2 LoRA 到云端"""
import subprocess, os
KEY = r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\.ssh_keys\id_rsa'
SRC = r'C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\models\loras\DMD2\dmd2_sdxl_4step_lora_fp16.safetensors'
REMOTE_DIR = '/root/My_Comfy_AI/models/loras/DMD2/'
REMOTE_PATH = REMOTE_DIR + 'dmd2_sdxl_4step_lora_fp16.safetensors'
HOST = 'cpod-1ud2p6nylymq.podtcp.compshare.cn'
PORT = '28682'

# Step 1: 远端删干净
ssh_clean = ['ssh', '-i', KEY, '-p', PORT, '-o', 'StrictHostKeyChecking=no',
             f'root@{HOST}', f'rm -f {REMOTE_PATH} && echo CLEANED']
r = subprocess.run(ssh_clean, capture_output=True, text=True, timeout=30)
print('clean:', r.stdout.strip(), r.stderr.strip()[:200])

# Step 2: cat | ssh 管道
size = os.path.getsize(SRC)
print(f'uploading {size} bytes ({size/1024/1024:.1f} MB)...')

with open(SRC, 'rb') as f:
    ssh = subprocess.Popen(
        ['ssh', '-i', KEY, '-p', PORT, '-o', 'StrictHostKeyChecking=no',
         f'root@{HOST}', f'cat > {REMOTE_PATH}'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # 流式分块写
    sent = 0
    chunk = 1024 * 1024  # 1MB
    last_print = 0
    while True:
        buf = f.read(chunk)
        if not buf:
            break
        try:
            ssh.stdin.write(buf)
            ssh.stdin.flush()
        except BrokenPipeError:
            print('  ! broken pipe')
            break
        sent += len(buf)
        if sent - last_print >= 10 * 1024 * 1024:  # 每 10MB 报一次
            print(f'  ... {sent/1024/1024:.1f} MB / {size/1024/1024:.1f} MB')
            last_print = sent
    ssh.stdin.close()
    out, err = ssh.communicate(timeout=300)
    print(f'  total sent: {sent/1024/1024:.1f} MB')
    print(f'  exit: {ssh.returncode}')
    if err:
        print(f'  err: {err.decode()[:300]}')
    if out:
        print(f'  out: {out.decode()[:200]}')

# Step 3: 验证
ssh_verify = ['ssh', '-i', KEY, '-p', PORT, '-o', 'StrictHostKeyChecking=no',
              f'root@{HOST}', f'ls -la {REMOTE_DIR} && echo "---" && wc -c {REMOTE_PATH}']
r = subprocess.run(ssh_verify, capture_output=True, text=True, timeout=30)
print('verify:')
print(r.stdout)
if r.stderr:
    print('stderr:', r.stderr)
