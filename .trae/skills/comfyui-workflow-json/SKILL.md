---
name: "comfyui-workflow-json"
description: "Enforces the ComfyUI Workflow JSON UI format with proper nodes/links arrays. **MANDATORY**: invoke whenever creating or fixing any ComfyUI workflow JSON file. Prevents the recurring 'no connections / no links' bug where the API format gets written but ComfyUI shows a blank canvas with no wires."
---

# ComfyUI Workflow JSON — UI 格式规范

> 🚨 **本 skill 的存在原因**：作者反复把 ComfyUI workflow 写成 **API 格式**（顶层用节点 ID 当 key），导致拖进 ComfyUI 后画布上 **没有连线 / 没有链接**，节点之间是断开的。  
> **唯一正确的格式是 UI 格式**（顶层有 `nodes` 数组 + `links` 数组）。

## ⚡ 触发条件

每次要写/改 ComfyUI workflow JSON 时，**第一步**调用此 skill。无论：
- 新建 workflow
- 修复损坏的 workflow
- 把 API 格式转 UI 格式
- 给 workflow 加新节点

## 🎯 核心规则

**ComfyUI 拖入画布后看到连线 = JSON 顶层有 `nodes` + `links` 两个数组。**  
没有这两个数组 = API 格式，**会丢连线**。

---

## 完整 UI 格式模板

```json
{
  "last_node_id": <最大节点ID>,
  "last_link_id": <最大连线ID>,
  "nodes": [
    { "id": 1, "type": "...", "pos": [...], "size": [...],
      "inputs": [...], "outputs": [...], "properties": {...},
      "widgets_values": [...], "class_type": "..." },
    ...
  ],
  "links": [
    [<link_id>, <src_node>, <src_slot>, <dst_node>, <dst_slot>, "<type>"],
    ...
  ],
  "groups": [...],
  "config": {},
  "extra": { "workflow_info": { ... } },
  "version": 1
}
```

## 节点对象字段

| 字段 | 必需 | 说明 |
|---|---|---|
| `id` | ✅ | 唯一数字 ID |
| `type` | ✅ | 节点类型名（与 class_type 一致）|
| `pos` | ✅ | `[x, y]` 画布坐标 |
| `size` | ✅ | `[w, h]` 节点大小 |
| `inputs` | ✅ | 输入端口数组（无入站 = `[]`）|
| `outputs` | ✅ | 输出端口数组（无出站 = `[]`）|
| `properties` | ✅ | 至少含 `"Node name for S&R": "<class_type>"` |
| `widgets_values` | ✅ | 用户配置的参数值数组（按节点定义顺序）|
| `class_type` | ✅ | **解析器用**，与 type 一致 |

## inputs 数组每项

```json
{
  "name": "<端口名>",
  "type": "<端口类型>",
  "link": <link_id 或 null>,
  "slot_index": <输入槽位编号>
}
```

## outputs 数组每项

```json
{
  "name": "<端口名>",
  "type": "<端口类型>",
  "links": [<link_id>, <link_id>, ...]   // ⚠️ outputs 用复数 links 数组
}
```

## links 数组每项

```json
[<link_id>, <src_node_id>, <src_slot_index>, <dst_node_id>, <dst_slot_index>, "<type>"]
```

- `link_id` 唯一
- `src_slot` = 来源节点 outputs 数组中的下标
- `dst_slot` = 目标节点 inputs 数组中的下标（**注意 inputs 是 link 字段，不是 links 字段**）

---

## 完整示例（IndexTTS-2 7 节点）

```json
{
  "last_node_id": 7,
  "last_link_id": 6,
  "nodes": [
    {
      "id": 1,
      "type": "IndexTTS2ModelLoader",
      "pos": [-700, 0],
      "size": [320, 130],
      "inputs": [],
      "outputs": [
        { "name": "MODEL", "type": "MODEL", "links": [1] }
      ],
      "properties": { "Node name for S&R": "IndexTTS2ModelLoader" },
      "widgets_values": ["model.pt", "qwen", "codec", "cuda"],
      "class_type": "IndexTTS2ModelLoader"
    },
    {
      "id": 2,
      "type": "LoadAudio",
      "pos": [-700, 180],
      "size": [320, 100],
      "inputs": [],
      "outputs": [
        { "name": "AUDIO", "type": "AUDIO", "links": [2] }
      ],
      "properties": { "Node name for S&R": "LoadAudio" },
      "widgets_values": ["sample.wav"],
      "class_type": "LoadAudio"
    },
    {
      "id": 6,
      "type": "IndexTTS2Synthesize",
      "pos": [0, 200],
      "size": [400, 450],
      "inputs": [
        { "name": "model", "type": "MODEL", "link": 1, "slot_index": 0 },
        { "name": "text", "type": "TEXT", "link": 4, "slot_index": 1 },
        { "name": "ref_audio", "type": "AUDIO", "link": 2, "slot_index": 2 }
      ],
      "outputs": [
        { "name": "AUDIO", "type": "AUDIO", "links": [6] }
      ],
      "properties": { "Node name for S&R": "IndexTTS2Synthesize" },
      "widgets_values": [0.8, 0.8, 30, 1.0],
      "class_type": "IndexTTS2Synthesize"
    }
  ],
  "links": [
    [1, 1, 0, 6, 0, "MODEL"],
    [2, 2, 0, 6, 2, "AUDIO"],
    [4, 4, 0, 6, 1, "TEXT"],
    [6, 6, 0, 7, 0, "AUDIO"]
  ],
  "groups": [],
  "config": {},
  "extra": { "workflow_info": { "version": "1.0" } },
  "version": 1
}
```

---

## 🚨 常见错误（必须避免）

| 错误 | 症状 | 修复 |
|---|---|---|
| **写成 API 格式** | 顶层是 `"1": {...}` 节点 ID 当 key | 改用 `nodes: []` + `links: []` |
| **缺 `links` 数组** | 画布上没连线 | 加上顶层 `links` 数组 |
| **缺 `inputs` 字段** | 节点不显示输入端口 | 每个节点加 `"inputs": []` 或带 link 的数组 |
| **缺 `outputs` 字段** | 节点不显示输出端口 | 每个节点加 `"outputs": []` 或带 links 的数组 |
| **`class_type` 拼错** | "Node has no class_type" | 与 `type` 保持完全一致 |
| **link ID 不匹配** | 拖进去节点孤立 | 节点的 `link` 字段必须在 `links` 数组中存在 |
| **slot_index 错位** | 线连到错误输入槽 | 重新对照节点实际输入顺序 |

---

## 写 workflow 前的自检清单

1. ✅ 顶层是 `nodes: []`（数组，不是 dict）
2. ✅ 顶层有 `links: []` 数组
3. ✅ 每个 node 含 `inputs` 和 `outputs`（哪怕是空数组）
4. ✅ 每个 node 含 `class_type` 字段
5. ✅ `outputs.links` 数组里的 link ID 都在顶层 `links` 中存在
6. ✅ 每个 input 的 `link` 字段值都在顶层 `links` 中存在
7. ✅ `widgets_values` 顺序与节点实际定义匹配
8. ✅ `last_node_id` = 最大 node ID
9. ✅ `last_link_id` = 最大 link ID

---

## 🔄 把 API 格式转 UI 格式

```python
# tools/api_to_ui_workflow.py
import json, sys

def api_to_ui(api_wf: dict) -> dict:
    nodes = []
    links = []
    next_link_id = 1
    max_node_id = 0
    
    for node_id_str, node_data in api_wf.items():
        nid = int(node_id_str) if isinstance(node_id_str, str) and node_id_str.isdigit() else None
        if nid is None: continue
        max_node_id = max(max_node_id, nid)
        
        # 解析 inputs
        inputs = []
        outputs = []
        for input_name, input_data in node_data.get("inputs", {}).items():
            if isinstance(input_data, list) and len(input_data) >= 2:
                src_node, src_slot = input_data[0], input_data[1]
                if isinstance(src_node, str) and src_node.isdigit():
                    link_id = next_link_id
                    next_link_id += 1
                    links.append([link_id, int(src_node), src_slot, nid, len(inputs), input_data[2] if len(input_data) > 2 else "*"])
                    inputs.append({
                        "name": input_name,
                        "type": input_data[2] if len(input_data) > 2 else "*",
                        "link": link_id,
                        "slot_index": len(inputs)
                    })
            else:
                # 普通 widget
                inputs.append({
                    "name": input_name,
                    "type": "WIDGET",
                    "link": None,
                    "slot_index": len(inputs)
                })
        
        # outputs 通常为空（API 格式不存 outputs，从 schema 推）
        class_type = node_data.get("class_type", "")
        widgets = []
        for k, v in node_data.get("inputs", {}).items():
            if not (isinstance(v, list) and len(v) >= 2):
                widgets.append(v)
        
        nodes.append({
            "id": nid,
            "type": class_type,
            "pos": [0, 0],
            "size": [320, 100],
            "inputs": inputs,
            "outputs": outputs,
            "properties": {"Node name for S&R": class_type},
            "widgets_values": widgets,
            "class_type": class_type
        })
    
    return {
        "last_node_id": max_node_id,
        "last_link_id": next_link_id - 1,
        "nodes": nodes,
        "links": links,
        "groups": [],
        "config": {},
        "extra": {},
        "version": 1
    }

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f: api_wf = json.load(f)
    with open(dst, "w") as f: json.dump(api_to_ui(api_wf), f, indent=2)
    print(f"Converted {src} -> {dst}")
```

用法：
```powershell
python tools/api_to_ui_workflow.py old_workflow.json new_workflow.json
```

---

## 📁 已有的参考示例

项目内以下文件已确认是**正确的 UI 格式**，可作为新 workflow 的模板：

| 文件 | 节点数 | 用途 |
|---|---|---|
| `workflows/galgame_zimage_inpaint_v1.json` | 11 | z-image inpainting（最完整的参考）|
| `workflows/galgame_zimage_inpaint_auto_v1.json` | 15 | 含 GroundingDINO + SAM2 |
| `workflows/galgame_wan22_bg_lora_v1.json` | 7 | Wan 2.2 + LoRA |
| `workflows/galgame_anima_cover_img2img_v1.json` | 11 | Anima 封面 |
| `workflows/galgame_anima_cover_ipadapter_flux_v1.json` | 12 | Anima + IPAdapter |
| `workflows/galgame_index_tts2_v1.json` | 7 | IndexTTS-2 语音合成 |

**老 API 格式**（仍可加载但 JSON 编辑器看不到线）：
- `galgame_zimage_pixelart_v1.json`
- `galgame_sdxl_pixelart_v1.json`
- `galgame_zimage_pixelart_inpaint_v1.json`
- `galgame_bg_anima_*.json`（3 个）
- `galgame_bg_zimage_*.json`（2 个）
- `VNCCS_3.0_new_char_creator.json`

---

## 写新 workflow 的工作流

1. **复制一个参考文件**（如 `galgame_zimage_inpaint_v1.json`）
2. **改 nodes 数组里的节点**：
   - 改 `class_type` / `type`
   - 改 `widgets_values` 参数
   - 改 `pos` / `size` 调整布局
3. **改 links 数组**：
   - 每条新连线加一项 `[link_id, src, src_slot, dst, dst_slot, "type"]`
   - 同步更新源节点 `outputs.links` 和目标节点 `inputs.link`
4. **更新 `last_node_id` 和 `last_link_id`**
5. **保存 → 拖到 ComfyUI 验证连线**

---

## ComfyUI 内置节点 schema 速查

下面是常见内置节点的端口定义（写新 workflow 时参考）：

### `KSampler`
- inputs: model, positive, negative, latent_image, seed, steps, cfg, sampler_name, scheduler, denoise
- outputs: LATENT
- widgets_values: [seed, "fixed", steps, cfg, "euler", "simple", denoise]

### `UNETLoader`
- inputs: (none)
- outputs: MODEL
- widgets_values: ["model.safetensors", "default"]

### `CLIPLoader`
- inputs: (none)
- outputs: CLIP
- widgets_values: ["clip.safetensors", "qwen_image"]

### `CLIPTextEncode`
- inputs: clip
- outputs: CONDITIONING
- widgets_values: ["text prompt"]

### `VAELoader`
- inputs: (none)
- outputs: VAE
- widgets_values: ["ae.safetensors"]

### `EmptyLatentImage`
- inputs: (none)
- outputs: LATENT
- widgets_values: [1920, 1080, 1]

### `VAEDecode`
- inputs: samples, vae
- outputs: IMAGE
- widgets_values: []

### `VAEEncode`
- inputs: pixels, vae
- outputs: LATENT
- widgets_values: []

### `LoraLoader`
- inputs: model, clip
- outputs: MODEL, CLIP
- widgets_values: ["lora.safetensors", 0.85, 0.85]

### `SaveImage`
- inputs: images
- outputs: (none)
- widgets_values: ["filename_prefix"]

### `LoadImage`
- inputs: (none)
- outputs: IMAGE, MASK
- widgets_values: ["image.png"]

### `ImageToMask`
- inputs: image (with channel)
- outputs: MASK
- widgets_values: ["alpha"]

### `InvertMask`
- inputs: mask
- outputs: MASK
- widgets_values: []

### `MaskBlur`
- inputs: mask
- outputs: MASK
- widgets_values: [10, 10]

### `SetLatentNoiseMask`
- inputs: samples, mask
- outputs: LATENT
- widgets_values: []

### `LoadAudio`
- inputs: (none)
- outputs: AUDIO
- widgets_values: ["audio.wav"]

### `SaveAudio`
- inputs: audio
- outputs: (none)
- widgets_values: ["prefix", "wav", 24000]

---

## 💡 故障排查

| 症状 | 原因 | 解决 |
|---|---|---|
| 拖入后画布是空白 / 节点都孤立 | API 格式（缺 nodes/links 数组）| 按本 skill 转换 |
| "Node has no class_type" | 节点对象缺 `class_type` | 加上 `"class_type": "<type 字段值>"` |
| 连线画到错误位置 | `slot_index` 错位 | 对照节点真实输入顺序 |
| 拖入后报错节点未找到 | class_type 在用户 ComfyUI 里没装 | 改用本地已装节点的 class_type |
| 节点端口对不上 | widgets_values 顺序错 | 查 schema 调整 |

---

## 沉淀教训（来自本项目）

- **不要写成 API 格式**（顶层 `"1": {...}`）—— 拖进 ComfyUI 没连线
- **必须含 `nodes` + `links` 顶层数组** —— UI 格式唯一标志
- **每个 node 都需 `inputs` 和 `outputs`**（哪怕是空数组）
- **`class_type` 字段不可省略**（与 `type` 相同）
- **outputs 端口用 `links: []`（复数）**，**inputs 端口用 `link:`（单数）**
