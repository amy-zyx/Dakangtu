---
name: "comfyui-env"
description: "ComfyUI Desktop environment paths, API usage, and model download conventions for the Dakangtu project. Invoke when user asks to download models, install custom nodes, locate ComfyUI installation, submit workflows via API, or troubleshoot ComfyUI/Comfy Desktop issues."
---

# ComfyUI Desktop 环境速查（Dakangtu 项目专用）

> 🎯 **目的**：避免每次重复寻找 ComfyUI 安装位置、目录结构、API 端点、模型下载命令。

## 📁 关键路径（Windows，ComfyUI Desktop 安装）

```
ComfyUI 根目录 = C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\
```

⚠️ **注意有双层 `ComfyUI` 嵌套**（不是 typo！）：
- `Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\models\...`
- 外层是 Desktop 安装器目录，内层才是真正的 ComfyUI 仓库

### 子目录
| 用途 | 路径 |
|------|------|
| 模型 | `...\ComfyUI\models\` |
| 自定义节点 | `...\ComfyUI\custom_nodes\` |
| 输出图片 | `...\ComfyUI\output\` |
| 输入图片 | `...\ComfyUI\input\` |
| Workflow | `...\ComfyUI\workflows\` （部分安装） |
| Python 解释器 | `C:\Users\jwu40\AppData\Local\Python\pythoncore-3.14-64\python.exe` |
| Comfy Desktop | `C:\Users\jwu40\AppData\Local\Programs\Comfy Desktop\` |

### 模型分类子目录（models/ 下）
- `checkpoints/` (SDXL / SD1.5)
- `diffusion_models/` (Wan / Anima)
- `unet/`, `vae/`, `clip/`, `loras/`, `ipadapter/`
- `sams/`, `sam2/`, `sam3/` (SAM 系列)
- `text_encoders/`, `clip_vision/`

## 🌐 API 端点

```
Base URL = http://127.0.0.1:8188
```

| 端点 | 方法 | 用途 |
|------|------|------|
| `/system_stats` | GET | 连接测试、GPU/VRAM 查询 |
| `/object_info` | GET | 列出所有已安装节点 |
| `/prompt` | POST | 提交 workflow 任务 |
| `/history/{prompt_id}` | GET | 查询任务结果 |
| `/view?filename=...` | GET | 下载生成的图片 |
| `/upload/image` | POST | 上传参考图（multipart） |
| `/queue` | GET | 查看队列 |
| `/interrupt` | POST | 取消当前任务 |

## 📦 模型下载约定

### 工具
- `hf` CLI 已装（来自 `huggingface_hub`，用 `hf` 或 `huggingface-cli` 调用）
- Python：`C:\Users\jwu40\AppData\Local\Python\pythoncore-3.14-64\python.exe`

### ⚠️ 沙箱限制
沙箱**禁止**直接操作 `C:\Users\jwu40\AppData\Local\Comfy-Desktop\...` 路径。
**正确工作流**：
1. 先下载到项目目录的临时文件夹（如 `Dakangtu\models\<name>_dl\`）
2. 让用户手动复制到 ComfyUI 真实目录
3. 或者配置沙箱白名单（Settings → Permission → Custom Configuration）

### 下载命令模板

```powershell
# ✅ 正确：单文件下载（用完整仓库子路径作 filename）
hf download <repo_id> "<path/to/file.safetensors>" --local-dir <本地目标>

# ❌ 常见错误：只写文件名（找不到）
hf download <repo_id> <filename> --local-dir <dir>   # 报 "File not found"

# 多个文件
hf download <repo_id> "file1.safetensors" "file2.safetensors" --local-dir <dir>

# 下载整个仓库
hf download <repo_id> --local-dir <dir>
```

### 已知模型源

| 模型 | 仓库 | 文件路径 | 用途 |
|------|------|----------|------|
| Anima-Turbo v1.0 | `circlestone-labs/Anima` | `anima-turbo-v1.0.safetensors` | 主生成 |
| Qwen Image Edit 2511 | `Comfy-Org/Qwen-Image-Edit-2511` | `Qwen-Image-Edit-2511-GGUF-Q5` | VNCCS 默认 |
| SAM 3.1 multiplex | `Comfy-Org/sam3.1` | `checkpoints/sam3.1_multiplex_fp16.safetensors` | 分割（1.63GB） |
| Anima LLLite | - | `anima-lllite-any-test-like-v2.safetensors` | IP-Adapter 类 |
| SeedVR2 upscaler | - | `seedvr2_ema_3b-Q4_K_M.gguf` | 4x 放大 |

## 🛠️ 常用 Python 片段

### 路径常量（项目级）
```python
COMFYUI = r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI"
COMFYUI_API = "http://127.0.0.1:8188"
MODELS = rf"{COMFYUI}\models"
CUSTOM_NODES = rf"{COMFYUI}\custom_nodes"
INPUT = rf"{COMFYUI}\input"
OUTPUT = rf"{COMFYUI}\output"
```

### 提交 workflow（API 500 错误的应对）
VNCCS 3.0 的 `CharacterCreatorV2` 节点**通过 API 提交经常 500**。
**降级方案**：
1. 加载 workflow JSON
2. 找到 `CharacterCreatorV2` 节点，修改 `widgets_values[0]` 的 JSON（character / character_info / preview_* 字段）
3. 保存为新 JSON 文件（如 `ami_xxx_preview.json`）
4. 让用户在 ComfyUI 浏览器 Load 该 JSON + Queue Prompt

## 📝 工作流文件位置

项目工作流 JSON 在 `Dakangtu\workflows\`：
- `VNCCS_3.0_new_char_creator.json` — 角色创建（主）
- `ami_tennis_preview.json` — Ami 网球装 preview
- `ami_preview.json` — Ami preview
- `anima_turbo_*.json` — 基础 Anima 生成

## 🔍 节点查询技巧

```powershell
# 列出所有 VNCCS 节点
python -c "import json, urllib.request; data = json.loads(urllib.request.urlopen('http://127.0.0.1:8188/object_info', timeout=10).read()); print('\n'.join(sorted([k for k in data if 'nccs' in k.lower()])))"
```

## 💡 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| API 提交 500 | 复杂工作流（VNCCS）解析失败 | 改用手动 Load JSON |
| 模型"File not found in repository" | 仓库用子目录组织 | 用 `path/to/file.safetensors` 作为 filename |
| 沙箱拒绝访问 AppData | 沙箱白名单 | 下载到项目目录，再让用户复制 |
| ComfyUI 节点未出现 | 重启 ComfyUI | Manager → Restart |
| `comfyui-easy-sam3` 启动失败：`ModuleNotFoundError: No module named 'triton'` | Triton 无 Windows PyPI wheel | 已打补丁：`sam3/model/edt.py` 软导入 triton，缺失时用 OpenCV 走 CPU 路径。视频跟踪可用但慢，图像分割完全不受影响 |
| VNCCS 报 `Required node 'LoadSam3Model/easy sam3ModelLoader' is not available` | `comfyui-easy-sam3` 因 triton 缺失启动崩溃，没注册任何节点 | 同上：打补丁 + 重启 ComfyUI |
| `comfyui-kaola-indextts2` / `ComfyUI-IndexTTS2-main` / `comfyui-easy-indextts2` 报 `ImportError: cannot import name 'isin_mps_friendly'` / `OffloadedCache` 等 | 节点代码引用了 transformers 已移除的旧 API（transformers >= 4.40 / 5.x） | ⚠️ **三个 IndexTTS 包底层都用 vendored transformers 代码，逐一打补丁不可行**。<br>**推荐方案：直接 patch vendored 文件**：`python tools/patch_vendored_tts.py` 把所有 `transformers_generation_utils.py` 的 from-import 改为 try/except 并注入 fallback 函数（用 lazy torch import）。<br>**已弃用方案（会引起新问题）**：compat shim 会在 Python 启动时导入 torch，与 comfy-aimdo 的 CUDA allocator 初始化冲突，触发 `Allocator backend parsed at runtime != allocator backend parsed at load time, cudaMallocAsync != native` 错误。**如果之前装过 shim，务必先卸载**：`python tools/uninstall_compat_shim.py` |
| ComfyUI 启动报 `Neither pip nor uv are available for package management`（来自 ComfyUI-Manager） | venv 的 pip 被破坏（常见原因：`pip uninstall transformers` 副作用 / venv pip 装得不完整） | 恢复方法：<br>1. `python -m ensurepip --upgrade`（优先）<br>2. 若失败：`Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py \| python` 手动装 pip<br>3. `python -m pip install transformers` 重装 transformers（任意版本，shim 会处理兼容）<br>**注意：不要用 `pip uninstall transformers` 试探**，先确认 pip 自身能跑 |

### Triton 依赖说明

| 平台 | PyPI 有 triton 吗 |
|------|---|
| Linux | ✅ 有 |
| macOS | ⚠️ 部分（Apple Silicon） |
| **Windows** | **❌ 完全无**（官方不支持） |

**已打补丁的文件**：`C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\custom_nodes\comfyui-easy-sam3\sam3\model\edt.py`

补丁改动：
1. `import triton` → `try/except`，失败时 `triton=None, _HAS_TRITON=False`
2. triton 缺失时用 stub 类替代 `tl.constexpr`（让类型注解可解析）
3. `@triton.jit` → `@_jit_decorator`（triton 缺失时退化为恒等装饰器）
4. `edt_triton()` 函数：triton 缺失时用 OpenCV 走 CPU 路径

⚠️ 重启 ComfyUI 才会生效（custom_nodes 模块在启动时加载）。

**已打补丁的文件 2**：`custom_nodes\comfyui-kaola-indextts2\kaola_indextts\gpt\transformers_generation_utils.py`（⚠️ 已弃用）

补丁改动：
1. `from transformers.pytorch_utils import isin_mps_friendly` → `try/except ImportError` 软导入
2. 缺失时定义 fallback 函数，用 `torch.isin(elements, test_elements)` 替代

⚠️ 重启 ComfyUI 才会生效。

**为什么弃用 kaola**：该节点包携带的 vendored transformers 代码引用了大量旧 API，逐一打补丁不现实。Python 3.13 环境下无法降级 transformers（无预编译 wheel）。改用 `ComfyUI-IndexTTS2-main`（节点 `IndexTTS2Simple` / `IndexTTS2Advanced`）或 `comfyui-easy-indextts2`（节点 `easy indexTTSGenerate`）。
