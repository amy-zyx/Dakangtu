# -*- coding: utf-8 -*-
"""
将 ComfyUI prompt 格式 转为 workflow (UI) 格式
prompt 格式: {node_id: {class_type, inputs}}  -> 用于 API
workflow 格式: {nodes: [...], links: [...]}  -> 用于 UI 拖入
"""
import json
import sys

# 节点位置布局
LAYOUTS = {
    "CheckpointLoaderSimple": ([60, 200], [315, 98]),
    "CLIPTextEncode": ([440, 60], [420, 220]),
    "CLIPTextEncode_2": ([440, 320], [420, 120]),  # negative
    "EmptyLatentImage": ([440, 480], [315, 106]),
    "KSampler": ([920, 200], [315, 222]),
    "VAEDecode": ([1280, 200], [210, 46]),
    "SaveImage": ([1560, 200], [315, 100]),
    "PreviewImage": ([1560, 340], [315, 100]),
    "ImageResize": ([1280, 320], [210, 86]),
}

# 每个节点类的输出定义 (name, type)
OUTPUT_DEFS = {
    "CheckpointLoaderSimple": [
        ("MODEL", "MODEL"),
        ("CLIP", "CLIP"),
        ("VAE", "VAE"),
    ],
    "CLIPTextEncode": [("CONDITIONING", "CONDITIONING")],
    "EmptyLatentImage": [("LATENT", "LATENT")],
    "KSampler": [("LATENT", "LATENT")],
    "VAEDecode": [("IMAGE", "IMAGE")],
    "SaveImage": [],
    "PreviewImage": [],
    "ImageResize": [("IMAGE", "IMAGE")],
}

# 根据输入名推断输入类型
def infer_input_type(class_type, input_name):
    if input_name == "model":
        return "MODEL"
    if input_name == "clip":
        return "CLIP"
    if input_name in ("positive", "negative"):
        return "CONDITIONING"
    if input_name == "latent_image" or input_name == "samples":
        return "LATENT"
    if input_name == "vae":
        return "VAE"
    if input_name in ("images", "image"):
        return "IMAGE"
    return "*"


def convert_prompt_to_workflow(prompt):
    """
    prompt: {node_id_str: {class_type, inputs}}
    return: workflow dict
    """
    nodes = []
    links = []
    link_id = 1
    last_node_id = 0

    # 第一遍：创建所有节点
    for nid_str, info in prompt.items():
        nid = int(nid_str)
        class_type = info["class_type"]
        inputs = info["inputs"]

        # 选择位置（CLIPTextEncode 第二个用 _2 位置）
        if class_type == "CLIPTextEncode":
            # 启发式：如果 text 包含 "low quality"，认为是 negative
            text = inputs.get("text", "").lower()
            if "low quality" in text or "worst quality" in text:
                pos, size = LAYOUTS["CLIPTextEncode_2"]
                title = "Negative Prompt"
            else:
                pos, size = LAYOUTS["CLIPTextEncode"]
                title = "Positive Prompt"
        else:
            pos, size = LAYOUTS.get(class_type, ([60, 200], [315, 100]))
            title = class_type

        # 构造 inputs (UI 格式)
        ui_inputs = []
        input_order = []
        widget_values = []
        for inp_name, inp_val in inputs.items():
            input_order.append(inp_name)
            if isinstance(inp_val, list) and len(inp_val) == 2:
                # 来自其他节点的连接
                inp_type = infer_input_type(class_type, inp_name)
                ui_inputs.append({
                    "name": inp_name,
                    "type": inp_type,
                    "link": None,  # 稍后填充
                    "slot_index": len(ui_inputs)
                })
            else:
                # widget value
                ui_inputs.append({
                    "name": inp_name,
                    "type": "WIDGET",
                    "link": None,
                    "widget": True
                })
                widget_values.append(inp_val)

        # 构造 outputs
        ui_outputs = []
        for out_name, out_type in OUTPUT_DEFS.get(class_type, []):
            ui_outputs.append({
                "name": out_name,
                "type": out_type,
                "links": [],
                "slot_index": len(ui_outputs)
            })

        node = {
            "id": nid,
            "type": class_type,
            "pos": list(pos),
            "size": list(size),
            "flags": {},
            "order": nid - 1,
            "mode": 0,
            "inputs": ui_inputs,
            "outputs": ui_outputs,
            "properties": {},
            "widgets_values": widget_values
        }
        if title != class_type:
            node["title"] = title

        nodes.append(node)
        last_node_id = max(last_node_id, nid)

    # 第二遍：创建 link 并填充引用
    # 先构建 node_id -> node 映射
    node_map = {n["id"]: n for n in nodes}

    for nid_str, info in prompt.items():
        nid = int(nid_str)
        node = node_map[nid]
        class_type = info["class_type"]
        inputs = info["inputs"]

        for inp_name, inp_val in inputs.items():
            if isinstance(inp_val, list) and len(inp_val) == 2:
                src_node_id, src_slot = inp_val
                inp_type = infer_input_type(class_type, inp_name)

                # 找到对应的 input（按 name 匹配）
                target_input = None
                for inp in node["inputs"]:
                    if inp["name"] == inp_name:
                        target_input = inp
                        break

                if target_input is None:
                    print(f"  WARN: 节点 {nid} 没有 input {inp_name}")
                    continue

                # 填充 link id
                target_input["link"] = link_id

                # 添加到全局 links
                actual_inp_idx = node["inputs"].index(target_input)
                links.append([link_id, src_node_id, src_slot, nid, actual_inp_idx, inp_type])

                # 填充 src node 的 outputs.links
                if src_node_id in node_map:
                    src_node = node_map[src_node_id]
                    if src_slot < len(src_node["outputs"]):
                        src_node["outputs"][src_slot]["links"].append(link_id)

                link_id += 1

    workflow = {
        "last_node_id": last_node_id,
        "last_link_id": link_id - 1,
        "nodes": nodes,
        "links": links,
        "groups": [
            {
                "title": "Anima-Turbo v1.0 Pipeline",
                "bounding": [40, 40, 1880, 580],
                "color": "#3f789e"
            }
        ],
        "config": {},
        "extra": {
            "ds": {"scale": 1.0, "offset": [0, 0]},
            "info": {
                "name": "Anima-Turbo v1.0",
                "author": "Dakangtu",
                "description": "Auto-generated by convert_prompt.py",
                "version": "4.0"
            }
        },
        "version": 0.4
    }
    return workflow


if __name__ == "__main__":
    # 读取 prompt 格式
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            prompt = json.load(f)
    else:
        with open("workflows/anima_turbo_workflow.json", encoding="utf-8") as f:
            prompt = json.load(f)

    # 转换为 workflow 格式
    workflow = convert_prompt_to_workflow(prompt)

    # 输出
    out_file = "workflows/anima_turbo_workflow_v2.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)

    print(f"转换完成: {out_file}")
    print(f"  节点数: {len(workflow['nodes'])}")
    print(f"  连接数: {len(workflow['links'])}")
    print(f"  last_node_id: {workflow['last_node_id']}")
    print(f"  last_link_id: {workflow['last_link_id']}")
