# -*- coding: utf-8 -*-
"""
生成 Anima-Turbo v1.0 ComfyUI workflow
使用 ComfyUI 官方 API 格式 (prompt format)，保证 100% 正确连接
用法：
  1. python tools/build_workflow.py > workflow.json
  2. 把生成的 JSON 粘贴到 ComfyUI (Ctrl+V)
  3. 或者保存为 .json 后用 ComfyUI 加载
"""

import json


# Anima-Turbo v1.0 是 single-file checkpoint
# 不需要单独的 VAE/CLIP loader

def build_prompt(positive, negative, width=832, height=1216, seed=12345):
    """
    生成 ComfyUI 官方 prompt 格式（不是 workflow JSON，是 prompt 格式）
    格式：{node_id: {class_type, inputs}}
    这种格式是 ComfyUI 内部 API 用的，100% 正确
    """
    return {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": "anima-turbo-v1.0.safetensors"
            }
        },
        "2": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "clip": ["1", 1],  # from node 1, output 1 (CLIP)
                "text": positive
            }
        },
        "3": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "clip": ["1", 1],  # from node 1, output 1 (CLIP)
                "text": negative
            }
        },
        "4": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "5": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["1", 0],          # MODEL output
                "positive": ["2", 0],       # positive conditioning
                "negative": ["3", 0],       # negative conditioning
                "latent_image": ["4", 0],   # latent
                "seed": seed,
                "control_after_generate": "randomize",
                "steps": 10,
                "cfg": 1.0,                 # Anima-Turbo 必须低 CFG
                "sampler_name": "euler",
                "scheduler": "simple",
                "denoise": 1.0
            }
        },
        "6": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["5", 0],
                "vae": ["1", 2]             # VAE output
            }
        },
        "7": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["6", 0],
                "filename_prefix": "AnimaTurbo_Output"
            }
        }
    }


# Anima-Turbo 通用参数
COMMON = {
    "steps": 10,
    "cfg": 1.0,
    "sampler": "euler",
    "scheduler": "simple",
    "denoise": 1.0
}

NEGATIVE = "low quality, worst quality, score_1, score_2, score_3, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, 3d, realistic, deformed, extra limbs, mutated"

# 角色标签
AMI = "1girl, chinese, petite, short_slim_figure, age_20, long_straight_black_hair, brown_eyes, alluring_face, revealing_outfit, crop_top, midriff, low_cut_shirt, short_skirt, high_heels, stylish_fashion, seductive"
JACK = "1boy, chinese, average_build, age_22, short_black_hair, brown_eyes, handsome, friendly_smile, casual, t_shirt, jeans, sneakers"

# 20 张图的 prompt 预设
IMAGES = {
    # ===== 背景 (5) =====
    "airport_terminal.png": {
        "positive": f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport, terminal, wellington_airport, arrival_hall, interior, floor_to_ceiling_windows, gray_sky, overcast, airplanes_on_tarmac, departure_board, waiting_seats, tiled_floor, natural_daylight, perspective, depth_of_field",
        "width": 1280, "height": 720
    },
    "airport_arrival.png": {
        "positive": f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport, arrival_gate, check_in_counters, morning_light, tall_windows, interior",
        "width": 1280, "height": 720
    },
    "airport_cafe.png": {
        "positive": f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport_cafe, interior, floor_to_ceiling_windows, wellington_harbor, wooden_tables, two_coffee_cups, afternoon_sunlight, ocean_view, blue_sea, distant_mountains, modern_design, warm_lighting",
        "width": 1280, "height": 720
    },
    "airport_window.png": {
        "positive": f"masterpiece, best quality, score_7, safe, scenery, no_humans, cafe_window_seat, side_window, sunlight_streaming, light_rays, golden_hour, wooden_chair, blurred_ocean_view, cozy_atmosphere, depth_of_field",
        "width": 1280, "height": 720
    },
    "wellington_city.png": {
        "positive": f"masterpiece, best quality, score_7, safe, scenery, no_humans, wellington, cityscape, harbor_view, colorful_wooden_houses, hillside, cable_car, sky_tower, blue_ocean, green_hills, partly_cloudy, aerial_view, new_zealand",
        "width": 1280, "height": 720
    },

    # ===== 阿米立绘 (6) =====
    "ami normal.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, neutral_expression, calm, soft_smile, light_makeup, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "ami smile.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, happy, bright_smile, eyes_closed, joyful, warm_expression, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "ami surprised.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, surprised, wide_eyes, open_mouth, raised_eyebrows, light_blush, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "ami blush.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, shy, deep_blush, looking_down, embarrassed_smile, hands_near_face, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "ami thinking.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, thoughtful, looking_up, hand_on_chin, pondering, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "ami sad.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, sad, disappointed, downcast_eyes, small_frown, looking_down, melancholy, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },

    # ===== 杰克立绘 (6) =====
    "jack normal.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, calm, slight_smile, friendly, standing, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "jack smile.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, big_smile, bright_eyes, happy, laughing, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "jack surprised.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, surprised, wide_eyes, raised_eyebrows, awkward_smile, white_background, simple_background, looking_at_viewer, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "jack apologize.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, apologetic, hand_rubbing_back_of_head, sheepish_smile, sorry_gesture, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "jack thinking.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, thoughtful, looking_up, hand_on_chin, pondering, considering, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },
    "jack wave.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {JACK}, waving, hand_raised, friendly_smile, goodbye, white_background, simple_background, upper_body, portrait",
        "width": 832, "height": 1216
    },

    # ===== CG (3) =====
    "airport_meet.png": {
        "positive": f"masterpiece, best quality, score_7, safe, 2girls, 2boys, {AMI}, {JACK}, standing, airport_arrival_hall, first_meeting, looking_at_each_other, scattered_luggage, surprised, daylight, cinematic, key_visual",
        "width": 1280, "height": 720
    },
    "first_coffee.png": {
        "positive": f"masterpiece, best quality, score_7, safe, 2girls, 2boys, {AMI}, {JACK}, sitting, cafe_table, by_window, two_coffee_cups, ocean_view, afternoon_light, warm_atmosphere, intimate_conversation, romantic_mood, key_visual",
        "width": 1280, "height": 720
    },
    "ending_act1.png": {
        "positive": f"masterpiece, best quality, score_7, safe, {AMI}, {JACK}, waving, from_bus_window, bus_driving_away, standing_on_platform, sunset, golden_light, dramatic_silhouette, emotional_farewell, wellington_city_background, romantic_ending, lens_flare, bokeh, key_visual",
        "width": 1280, "height": 720
    },
}


def build_workflow_json(prompt):
    """
    把 prompt 格式转为 ComfyUI workflow (UI) 格式
    prompt: {node_id: {class_type, inputs}}
    return: workflow JSON 格式（带可视化信息）
    """
    # 节点位置布局
    positions = {
        "CheckpointLoaderSimple": [60, 200],
        "CLIPTextEncode": [440, 60],
        "EmptyLatentImage": [440, 480],
        "KSampler": [920, 200],
        "VAEDecode": [1280, 200],
        "SaveImage": [1560, 200],
        "CLIPTextEncode_2": [440, 320]  # negative prompt
    }

    nodes = []
    link_id = 1
    last_node_id = 0
    links = []

    for node_id, info in prompt.items():
        nid = int(node_id)
        class_type = info["class_type"]
        inputs = info["inputs"]

        # 确定节点位置
        if class_type == "CLIPTextEncode":
            # 判断是正向还是负向
            pos = positions[class_type] if "text" in inputs and "portrait" in str(inputs.get("text", "")) else positions["CLIPTextEncode_2"]
            if pos == positions["CLIPTextEncode_2"]:
                title = "Negative Prompt"
            else:
                title = "Positive Prompt"
        else:
            pos = positions.get(class_type, [60, 200])
            title = class_type

        # 构造 input 列表
        input_list = []
        for inp_name, inp_val in inputs.items():
            if isinstance(inp_val, list) and len(inp_val) == 2:
                # 来自其他节点的连接
                input_list.append({
                    "name": inp_name,
                    "type": "MODEL" if "model" in inp_name.lower() else "CLIP" if "clip" in inp_name else "CONDITIONING" if "positive" in inp_name or "negative" in inp_name else "LATENT" if "latent" in inp_name else "VAE" if "vae" in inp_name else "IMAGE",
                    "link": link_id
                })
                # 添加到 links
                src_node, src_slot = inp_val
                link_type = "MODEL" if "model" in inp_name.lower() else "CLIP" if "clip" in inp_name else "CONDITIONING" if "positive" in inp_name or "negative" in inp_name else "LATENT" if "latent" in inp_name else "VAE" if "vae" in inp_name else "IMAGE"
                links.append([link_id, src_node, src_slot, nid, list(inputs.keys()).index(inp_name), link_type])
                link_id += 1

        # 构造 output 列表（简化处理）
        if class_type == "CheckpointLoaderSimple":
            outputs = [
                {"name": "MODEL", "type": "MODEL", "links": [], "slot_index": 0},
                {"name": "CLIP", "type": "CLIP", "links": [], "slot_index": 1},
                {"name": "VAE", "type": "VAE", "links": [], "slot_index": 2}
            ]
        elif class_type == "CLIPTextEncode":
            outputs = [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [], "slot_index": 0}]
        elif class_type == "EmptyLatentImage":
            outputs = [{"name": "LATENT", "type": "LATENT", "links": [], "slot_index": 0}]
        elif class_type == "KSampler":
            outputs = [{"name": "LATENT", "type": "LATENT", "links": [], "slot_index": 0}]
        elif class_type == "VAEDecode":
            outputs = [{"name": "IMAGE", "type": "IMAGE", "links": [], "slot_index": 0}]
        else:
            outputs = []

        # widget values
        widget_values = []
        for k, v in inputs.items():
            if not (isinstance(v, list) and len(v) == 2):
                widget_values.append(v)

        node = {
            "id": nid,
            "type": class_type,
            "pos": pos,
            "size": [315, 100],
            "flags": {},
            "order": nid - 1,
            "mode": 0,
            "inputs": input_list,
            "outputs": outputs,
            "properties": {},
            "widgets_values": widget_values
        }
        if title != class_type:
            node["title"] = title
        nodes.append(node)
        last_node_id = max(last_node_id, nid)

    # 反向填充 link 引用（在 outputs.links 里）
    for link in links:
        link_id, src_node, src_slot, dst_node, dst_slot, _ = link
        for n in nodes:
            if n["id"] == src_node and src_slot < len(n["outputs"]):
                n["outputs"][src_slot]["links"].append(link_id)

    return {
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
                "description": "Auto-generated by build_workflow.py",
                "version": "3.0"
            }
        },
        "version": 0.4
    }


if __name__ == "__main__":
    # 第一个 prompt 作为模板
    first = next(iter(IMAGES.values()))
    prompt = build_prompt(
        positive=first["positive"],
        negative=NEGATIVE,
        width=first["width"],
        height=first["height"]
    )

    # 输出 prompt 格式（用于 ComfyUI API）
    print("# ===== PROMPT FORMAT (ComfyUI API) =====")
    print(json.dumps(prompt, indent=2, ensure_ascii=False))
    print()
    print("# ===== WORKFLOW FORMAT (UI 拖入) =====")
    workflow = build_workflow_json(prompt)
    print(json.dumps(workflow, indent=2, ensure_ascii=False))
    print()
    print(f"# ===== 全部 {len(IMAGES)} 张图 =====")
    for i, (filename, cfg) in enumerate(IMAGES.items(), 1):
        p = build_prompt(cfg["positive"], NEGATIVE, cfg["width"], cfg["height"], seed=12345+i)
        print(f"\n## {i}. {filename} ({cfg['width']}x{cfg['height']})")
        print(f"positive: {cfg['positive']}")
