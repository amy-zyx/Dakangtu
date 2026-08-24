"""
预下 DWPose 需要的两个 onnx/torchscript 模型
下到 comfyui_controlnet_aux/ckpts/{repo}/file，ComfyUI 检测到本地存在就不会再调 hf_hub_download
"""
import os
os.environ["HF_HUB_DISABLE_XET"] = "1"   # 绕开 xet/CAS（关键！）

from huggingface_hub import hf_hub_download
from pathlib import Path

ckpts = Path(r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\comfyui_controlnet_aux\ckpts")
ckpts.mkdir(parents=True, exist_ok=True)

# 1) yolox_l.onnx (来自 hr16/yolox-onnx)
print("[1/2] downloading yolox_l.onnx...")
try:
    p1 = hf_hub_download(
        repo_id="hr16/yolox-onnx",
        filename="yolox_l.onnx",
        local_dir=ckpts / "hr16" / "yolox-onnx",
    )
    print(f"   OK: {p1}  ({Path(p1).stat().st_size//1024//1024} MB)")
except Exception as e:
    print(f"   FAIL: {e}")

# 2) dw-ll_ucoco_384_bs5.torchscript.pt (来自 hr16/DWPose-TorchScript-BatchSize5)
print("[2/2] downloading dw-ll_ucoco_384_bs5.torchscript.pt...")
try:
    p2 = hf_hub_download(
        repo_id="hr16/DWPose-TorchScript-BatchSize5",
        filename="dw-ll_ucoco_384_bs5.torchscript.pt",
        local_dir=ckpts / "hr16" / "DWPose-TorchScript-BatchSize5",
    )
    print(f"   OK: {p2}  ({Path(p2).stat().st_size//1024//1024} MB)")
except Exception as e:
    print(f"   FAIL: {e}")

# 列出已下载
print("\n=== ckpts 目录 ===")
for f in sorted(ckpts.rglob("*.onnx")) + sorted(ckpts.rglob("*.torchscript.pt")):
    print(f"  {f}  ({f.stat().st_size//1024//1024} MB)")
