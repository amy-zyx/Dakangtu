# -*- coding: utf-8 -*-
"""
通过 ComfyUI API 测试 Anima-Turbo 基础工作流
"""
import json
import urllib.request
import urllib.error
import time
import os
import sys

COMFYUI_URL = "http://127.0.0.1:8188"


def api_request(endpoint, method="GET", data=None):
    """调用 ComfyUI API"""
    url = f"{COMFYUI_URL}{endpoint}"
    if data is not None:
        data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method=method,
                                      headers={"Content-Type": "application/json"})
    else:
        req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode('utf-8')}"}
    except Exception as e:
        return {"error": str(e)}


def upload_image(filepath):
    """上传图片到 ComfyUI input 目录"""
    import mimetypes
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    filename = os.path.basename(filepath)

    with open(filepath, "rb") as f:
        file_data = f.read()

    body = (
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"image\"; filename=\"{filename}\"\r\n"
        f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        f"{COMFYUI_URL}/upload/image",
        data=body,
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def queue_prompt(prompt):
    """提交 prompt 到队列"""
    # 生成 client_id
    import uuid
    payload = {"prompt": prompt, "client_id": str(uuid.uuid4())}
    return api_request("/prompt", "POST", payload)


def get_history(prompt_id):
    """查询任务历史"""
    return api_request(f"/history/{prompt_id}")


def get_image(filename, subfolder="", folder_type="output"):
    """获取生成的图片"""
    params = f"filename={filename}&subfolder={subfolder}&type={folder_type}"
    return api_request(f"/view?{params}")


def wait_for_completion(prompt_id, timeout=300):
    """等待任务完成"""
    start = time.time()
    while time.time() - start < timeout:
        history = get_history(prompt_id)
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(2)
        print(f"  等待中... ({int(time.time() - start)}s)")
    return None


# ===== 测试 1：Anima-Turbo 基础工作流（用 UNETLoader） =====
basic_prompt = {
    "1": {
        "class_type": "UNETLoader",
        "inputs": {
            "unet_name": "anima-turbo-v1.0.safetensors",
            "weight_dtype": "default"
        }
    },
    "2": {
        "class_type": "CLIPLoader",
        "inputs": {
            "clip_name": "qwen_3_06b_base.safetensors",
            "type": "qwen_image"
        }
    },
    "3": {
        "class_type": "VAELoader",
        "inputs": {
            "vae_name": "qwen_image_vae.safetensors"
        }
    },
    "4": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": ["2", 0],
            "text": "masterpiece, best quality, score_7, safe, 1girl, asian, loli, petite, slim_body, small_chest, age_18, long_straight_hair, black_hair, very_long_hair, brown_eyes, cute_face, childlike_face, big_eyes, small_nose, full_body, looking_at_viewer, white_background, simple_background, neutral_expression, calm, soft_smile, flat_chest, cute_animal_print_t_shirt, denim_shorts, sneakers, casual, modern, 2d_anime_style, cartoon_style, cel_shading, anime_screenshot, beautiful_detailed_eyes"
        }
    },
    "5": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": ["2", 0],
            "text": "low quality, worst quality, score_1, score_2, bad anatomy, bad hands, missing fingers, extra digit, cropped, jpeg artifacts, signature, watermark, blurry, 3d, realistic, photorealistic, deformed, extra limbs, ugly, large_breasts, mature, chinese_clothing, cheongsam, qipao, hanfu, high_heels, navel, midriff, crop_top, sexy, seductive, revealing"
        }
    },
    "6": {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 832, "height": 1216, "batch_size": 1}
    },
    "7": {
        "class_type": "KSampler",
        "inputs": {
            "model": ["1", 0],
            "positive": ["4", 0],
            "negative": ["5", 0],
            "latent_image": ["6", 0],
            "seed": 42,
            "control_after_generate": "randomize",
            "steps": 8,
            "cfg": 1.0,
            "sampler_name": "euler",
            "scheduler": "simple",
            "denoise": 1.0
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": ["7", 0],
            "vae": ["3", 0]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "images": ["8", 0],
            "filename_prefix": "Dakangtu_Test"
        }
    }
}


if __name__ == "__main__":
    print("=" * 60)
    print("ComfyUI 连接测试 + 基础出图测试")
    print("=" * 60)

    # 1. 测试连接
    print("\n[1] 测试 ComfyUI 连接...")
    sys_info = api_request("/system_stats")
    if "error" in sys_info:
        print(f"  [ERR] 连接失败: {sys_info['error']}")
        sys.exit(1)
    print(f"  [OK] ComfyUI v{sys_info['system']['comfyui_version']}")
    print(f"  GPU: {sys_info['devices'][0]['name']}")
    print(f"  VRAM: {sys_info['devices'][0]['vram_free'] / 1024**3:.1f}GB free")

    # 2. 提交测试 prompt
    print("\n[2] 提交测试任务 (生成 1 张阿米立绘)...")
    result = queue_prompt(basic_prompt)
    if "error" in result:
        print(f"  [ERR] {result['error']}")
        sys.exit(1)

    prompt_id = result.get("prompt_id")
    if not prompt_id:
        print(f"  [ERR] 没有返回 prompt_id: {result}")
        sys.exit(1)

    print(f"  [OK] prompt_id: {prompt_id}")

    # 3. 等待完成
    print("\n[3] 等待生成完成 (预计 5-30 秒)...")
    history = wait_for_completion(prompt_id, timeout=120)
    if not history:
        print("  [ERR] 超时")
        sys.exit(1)

    # 4. 获取结果
    print("\n[4] 任务完成！")
    if "outputs" in history:
        for nid, output in history["outputs"].items():
            if "images" in output:
                for img in output["images"]:
                    print(f"  生成图片: {img['filename']}")
                    print(f"  子目录: {img.get('subfolder', '')}")
                    print(f"  完整路径: {COMFYUI_URL}/view?filename={img['filename']}&subfolder={img.get('subfolder', '')}&type=output")

    print("\n" + "=" * 60)
    print("[OK] 测试通过！")
    print("=" * 60)
