# ComfyUI Workflow 使用指南 (Anima-Turbo + IPAdapter)

## 📦 文件清单

| 文件 | 类型 | 用途 |
|------|------|------|
| `workflows/anima_turbo_workflow.json` | Workflow (UI) | 基础生成（无 IP-Adapter） |
| `workflows/anima_turbo_prompt.json` | Prompt (API) | 基础生成的 prompt 格式 |
| `workflows/anima_turbo_ipadapter_workflow.json` | **Workflow (UI) ⭐** | **带 IP-Adapter 推荐使用** |
| `workflows/anima_turbo_ipadapter_prompt.json` | Prompt (API) | IP-Adapter 的 prompt 格式 |
| `workflows/anima_turbo_prompts.json` | 文本 | 20 张图的 prompt 预设 |

---

## 🎯 双阶段工作流程（保证角色一致性）

### 阶段 1：先生成参考图（一次）

**目标**：用基础 workflow 生成 `ami_reference.png` 和 `jack_reference.png`

步骤：
1. 把 `anima_turbo_workflow.json` 拖到 ComfyUI 画布
2. 修改 Positive Prompt 为：
   ```
   masterpiece, best quality, score_7, safe,
   1girl, chinese, petite, short_slim_figure, age_20,
   long_straight_black_hair, brown_eyes, alluring_face,
   revealing_outfit, crop_top, midriff, low_cut_shirt,
   short_skirt, high_heels, stylish_fashion, seductive,
   neutral_expression, calm, gentle_smile,
   portrait, looking_at_viewer, upper_body, face_focus, white_background
   ```
3. Latent 尺寸：`832x1216`
4. 一直点 **Queue Prompt** 多次，直到生成满意的脸
5. 右键生成的图片 → **Save Image**，命名 `ami_reference.png`
6. 同样流程生成 `jack_reference.png`
7. **把两张图上传到 ComfyUI 服务器**（`ComfyUI/input/` 目录或用 Upload 按钮）

### 阶段 2：批量生成 20 张图

1. 把 `anima_turbo_ipadapter_workflow.json` 拖到 ComfyUI 画布
2. **LoadImage 节点**（节点 6）选择 `ami_reference.png`
3. 修改 **Positive Prompt 节点**（节点 3）的 text
4. 修改 **Latent 尺寸**
5. 点击 **Queue Prompt** 生成

---

## 📐 节点连接说明

```
[1] CheckpointLoaderSimple (anima-turbo-v1.0)
     ├─ MODEL(0) → [2] IPAdapterUnifiedLoader.model
     ├─ CLIP(1)  → [3] PositivePrompt.clip
     ├─ CLIP(1)  → [4] NegativePrompt.clip
     └─ VAE(2)   → [9] VAEDecode.vae

[2] IPAdapterUnifiedLoader (preset: PLUS high strength)
     ├─ model(0)     → [7] IPAdapter.model
     └─ ipadapter(1) → [7] IPAdapter.ipadapter

[3] Positive Prompt → [8] KSampler.positive
[4] Negative Prompt → [8] KSampler.negative
[5] EmptyLatentImage → [8] KSampler.latent_image

[6] LoadImage (ami_reference.png) → [7] IPAdapter.image

[7] IPAdapter (weight=0.8, weight_type=linear)
     └─ MODEL(0) → [8] KSampler.model

[8] KSampler (steps=10, cfg=1.0, euler, simple)
     └─ LATENT(0) → [9] VAEDecode.samples

[9] VAEDecode → [10] SaveImage
```

---

## ⚙️ IP-Adapter 关键参数

| 参数 | 值 | 说明 |
|------|-----|------|
| **preset** | `PLUS (high strength)` | 高强度，最适合动漫人物 |
| **weight** | `0.8` | 参考图影响强度。太高会抄袭参考图，太低没效果。0.7-0.9 是好区间 |
| **weight_type** | `linear` | 线性过渡。也可以试 `ease in-out` |
| **start_at** | `0.0` | 0% 时开始应用 |
| **end_at** | `0.8` | 80% 时停止。保留最后 20% 让文字 prompt 主导细节 |
| **combine_embeds** | `average` | 单图时用 average |
| **embeds_scaling** | `V only` | 推荐 SDXL/Anima 用这个 |

---

## 🎨 不同图类型的 Prompt 修改建议

### 角色立绘（阿米）
```
参考图：ami_reference.png
weight: 0.8-0.9
prompt: 在角色标签后加表情/动作
```

### 角色立绘（杰克）
```
参考图：把 LoadImage 改成 jack_reference.png
weight: 0.8-0.9
prompt: 用 JACK_TAGS 替换 AMI_TAGS
```

### 背景图（不需要 IP-Adapter）
```
不用 IP-Adapter 时：
- 把 IPAdapter 节点 bypass（右键 → Mode → Bypass）
- 或把 weight 改成 0
```

### 双角色 CG（需要更复杂）
用 **IPAdapter Combine** 节点同时输入两张参考图
（已超出基础 workflow 范围，需要额外配置）

---

## 🚀 20 张图生成顺序建议

| 批次 | 图片 | 类型 | 参考图 | Latent |
|------|------|------|--------|--------|
| 1 | ami_reference.png | 参考图 | 无 | 832x1216 |
| 2 | jack_reference.png | 参考图 | 无 | 832x1216 |
| 3 | ami normal/smile/surprised/blush/thinking/sad | 阿米 6 张 | ami | 832x1216 |
| 4 | jack normal/smile/surprised/apologize/thinking/wave | 杰克 6 张 | jack | 832x1216 |
| 5 | airport_terminal, airport_arrival, airport_cafe, airport_window, wellington_city | 背景 5 张 | 无（bypass IPAdapter）| 1280x720 |
| 6 | airport_meet, first_coffee, ending_act1 | CG 3 张 | ami+jack | 1280x720 |

---

## ⚠️ 重要注意事项

### 安装 IPAdapter Plus 节点
如果你 ComfyUI 里没有 IPAdapter 节点：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus
# 重启 ComfyUI
```

### 下载 IP-Adapter 模型
```bash
# PLUS 模型（推荐 SDXL/Anima）
hf download h94/IP-Adapter --local-dir ./models/ipadapter
# 或者
wget https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors
# 放到 ComfyUI/models/ipadapter/ 目录

# 下载 CLIP Vision 编码器
wget https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/image_encoder/model.safetensors
# 放到 ComfyUI/models/clip_vision/ 目录
```

### Anima-Turbo 的 IP-Adapter 兼容性
⚠️ **注意**：Anima-Turbo 用的是 Qwen 文本编码器，不是 CLIP。可能和 SDXL 训练的 IP-Adapter 不完全兼容。
如果效果差，可以考虑：
- 降低 weight 到 0.5
- 改用 Animagine XL v3.0（用 CLIP 编码器）
- 或试 LCM/Anima 的专用 IP-Adapter

---

## 🔧 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| "IPAdapter model not found" | 模型文件位置/命名错 | 按上面"下载 IP-Adapter 模型"步骤来 |
| 生成的图跟参考图差别太大 | weight 太低 | 调到 0.9-1.0 |
| 生成的图完全抄袭参考图 | weight 太高 + end_at=1.0 | weight 改 0.7，end_at 改 0.6 |
| 角色变形 | Anima-Turbo 不完全兼容 IP-Adapter | 改用 Animagine XL v3.0 |
| Latent 红色错误 | 尺寸不是 8 的倍数 | 用 832/1216、1280/720 等 8 倍数 |
| 连接线红色 | 节点未安装 | ComfyUI Manager 装 IPAdapter Plus |

---

## 📚 相关链接

- [ComfyUI_IPAdapter_plus GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- [IPAdapter 模型下载 (Hugging Face)](https://huggingface.co/h94/IP-Adapter)
- [Anima-Turbo 模型](https://huggingface.co/circlestone-labs/Anima)
- [ComfyUI 官方文档](https://docs.comfy.org/)
