# -*- coding: utf-8 -*-
"""
大康兔 Act 1 全套 20 张图批量生成器
通过 ComfyUI API 调用，每张图自动保存并下载到本地
"""
import json
import urllib.request
import urllib.error
import time
import os
import sys
import uuid

COMFYUI_URL = "http://127.0.0.1:8188"
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def api_request(endpoint, method="GET", data=None):
    url = f"{COMFYUI_URL}{endpoint}"
    if data is not None:
        data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method=method,
                                      headers={"Content-Type": "application/json"})
    else:
        req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode('utf-8')}"}
    except Exception as e:
        return {"error": str(e)}


def queue_prompt(prompt):
    payload = {"prompt": prompt, "client_id": str(uuid.uuid4())}
    result = api_request("/prompt", "POST", payload)
    if "error" in result:
        return None
    return result.get("prompt_id")


def wait_for_completion(prompt_id, timeout=300):
    start = time.time()
    while time.time() - start < timeout:
        history = api_request(f"/history/{prompt_id}")
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(1)
    return None


def download_image(filename, output_path):
    url = f"{COMFYUI_URL}/view?filename={filename}&subfolder=&type=output"
    with urllib.request.urlopen(url, timeout=30) as resp:
        with open(output_path, "wb") as f:
            f.write(resp.read())


# ===== 角色标签（v3 已验证：2D 卡通萝莉） =====
AMI = "1girl, asian, loli, petite, slim_body, small_chest, age_18, long_straight_hair, black_hair, very_long_hair, brown_eyes, cute_face, childlike_face, big_eyes, small_nose, flat_chest, casual, modern, denim_shorts, sneakers, cute_animal_print_t_shirt, 2d_anime_style, cartoon_style, cel_shading, anime_screenshot, beautiful_detailed_eyes"

JACK = "1boy, asian, average_build, age_22, short_black_hair, brown_eyes, handsome, friendly_smile, casual, t_shirt, jeans, sneakers, modern, young_man, student, 2d_anime_style, cartoon_style, cel_shading, anime_screenshot"

# ===== 通用参数 =====
COMMON_PARAMS = {
    "unet_name": "anima-turbo-v1.0.safetensors",
    "clip_name": "qwen_3_06b_base.safetensors",
    "vae_name": "qwen_image_vae.safetensors",
    "clip_type": "qwen_image",
    "steps": 8,
    "cfg": 1.0,
    "sampler": "euler",
    "scheduler": "simple",
    "denoise": 1.0,
}

NEGATIVE = "low quality, worst quality, score_1, score_2, score_3, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, 3d, realistic, photorealistic, deformed, extra limbs, mutated, ugly, large_breasts, mature, chinese_clothing, cheongsam, qipao, hanfu, high_heels, navel, midriff, crop_top, sexy, seductive, revealing, large_hips, plump"


def build_prompt(positive, width, height, seed):
    """构造 ComfyUI prompt"""
    return {
        "1": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": COMMON_PARAMS["unet_name"],
                "weight_dtype": "default"
            }
        },
        "2": {
            "class_type": "CLIPLoader",
            "inputs": {
                "clip_name": COMMON_PARAMS["clip_name"],
                "type": COMMON_PARAMS["clip_type"]
            }
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {"vae_name": COMMON_PARAMS["vae_name"]}
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": ["2", 0], "text": positive}
        },
        "5": {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": ["2", 0], "text": NEGATIVE}
        },
        "6": {
            "class_type": "EmptyLatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1}
        },
        "7": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["1", 0],
                "positive": ["4", 0],
                "negative": ["5", 0],
                "latent_image": ["6", 0],
                "seed": seed,
                "control_after_generate": "randomize",
                "steps": COMMON_PARAMS["steps"],
                "cfg": COMMON_PARAMS["cfg"],
                "sampler_name": COMMON_PARAMS["sampler"],
                "scheduler": COMMON_PARAMS["scheduler"],
                "denoise": COMMON_PARAMS["denoise"]
            }
        },
        "8": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["7", 0], "vae": ["3", 0]}
        },
        "9": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["8", 0],
                "filename_prefix": "Dakangtu_Act1"
            }
        }
    }


# ===== 20 张图清单 =====
IMAGES = [
    # 背景 (5)
    ("airport_terminal", "background", 1280, 720,
     f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport, terminal, wellington_airport, arrival_hall, interior, floor_to_ceiling_windows, gray_sky, overcast, airplanes_on_tarmac, departure_board, waiting_seats, tiled_floor, natural_daylight, perspective, depth_of_field"),
    ("airport_cafe", "background", 1280, 720,
     f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport_cafe, interior, floor_to_ceiling_windows, wellington_harbor, wooden_tables, two_coffee_cups, afternoon_sunlight, ocean_view, blue_sea, distant_mountains, modern_design, warm_lighting"),
    ("airport_window", "background", 1280, 720,
     f"masterpiece, best quality, score_7, safe, scenery, no_humans, cafe_window_seat, side_window, sunlight_streaming, light_rays, golden_hour, wooden_chair, blurred_ocean_view, cozy_atmosphere, depth_of_field"),
    ("wellington_city", "background", 1280, 720,
     f"masterpiece, best quality, score_7, safe, scenery, no_humans, wellington, cityscape, harbor_view, colorful_wooden_houses, hillside, cable_car, sky_tower, blue_ocean, green_hills, partly_cloudy, aerial_view, new_zealand"),
    ("airport_arrival", "background", 1280, 720,
     f"masterpiece, best quality, score_7, safe, scenery, no_humans, airport, arrival_gate, check_in_counters, morning_light, tall_windows, interior"),

    # 阿米立绘 (6)
    ("ami normal", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, neutral_expression, calm, soft_smile, light_makeup"),
    ("ami smile", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, happy, bright_smile, eyes_closed, joyful, warm_expression"),
    ("ami surprised", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, surprised, wide_eyes, open_mouth, raised_eyebrows, light_blush"),
    ("ami blush", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, shy, deep_blush, looking_down, embarrassed_smile, hands_near_face"),
    ("ami thinking", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, thoughtful, looking_up, hand_on_chin, pondering"),
    ("ami sad", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {AMI}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, sad, disappointed, downcast_eyes, small_frown, looking_down, melancholy"),

    # 杰克立绘 (6)
    ("jack normal", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, calm, slight_smile, friendly, standing"),
    ("jack smile", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, big_smile, bright_eyes, happy, laughing"),
    ("jack surprised", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, surprised, wide_eyes, raised_eyebrows, awkward_smile"),
    ("jack apologize", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, apologetic, hand_rubbing_back_of_head, sheepish_smile, sorry_gesture"),
    ("jack thinking", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, thoughtful, looking_up, hand_on_chin, pondering, considering"),
    ("jack wave", "character", 832, 1216,
     f"masterpiece, best quality, score_7, safe, {JACK}, upper_body, portrait, looking_at_viewer, face_focus, white_background, simple_background, waving, hand_raised, friendly_smile, goodbye"),

    # CG (3)
    ("airport_meet", "cg", 1280, 720,
     f"masterpiece, best quality, score_7, safe, {AMI}, {JACK}, standing, airport_arrival_hall, first_meeting, looking_at_each_other, scattered_luggage, surprised, daylight, cinematic, key_visual, two_characters"),
    ("first_coffee", "cg", 1280, 720,
     f"masterpiece, best quality, score_7, safe, {AMI}, {JACK}, sitting, cafe_table, by_window, two_coffee_cups, ocean_view, afternoon_light, warm_atmosphere, intimate_conversation, romantic_mood, key_visual"),
    ("ending_act1", "cg", 1280, 720,
     f"masterpiece, best quality, score_7, safe, {AMI}, {JACK}, waving, from_bus_window, bus_driving_away, standing_on_platform, sunset, golden_light, dramatic_silhouette, emotional_farewell, wellington_city_background, romantic_ending, lens_flare, bokeh, key_visual"),
]


def main():
    print("=" * 70)
    print(f"大康兔 Act 1 - 批量生成 {len(IMAGES)} 张图")
    print("=" * 70)

    # 测试连接
    sys_info = api_request("/system_stats")
    if "error" in sys_info:
        print(f"[ERR] ComfyUI 离线: {sys_info['error']}")
        return

    vram_free = sys_info['devices'][0]['vram_free'] / 1024**3
    print(f"\nComfyUI v{sys_info['system']['comfyui_version']}")
    print(f"VRAM: {vram_free:.1f}GB free")
    print(f"开始生成...\n")

    success = 0
    failed = 0
    start_time = time.time()

    for i, (name, category, w, h, positive) in enumerate(IMAGES, 1):
        print(f"[{i:2d}/{len(IMAGES)}] 生成 {name}.png ({w}x{h}) ...", end=" ", flush=True)

        seed = 1000 + i
        prompt = build_prompt(positive, w, h, seed)
        prompt_id = queue_prompt(prompt)

        if not prompt_id:
            print("FAIL (提交失败)")
            failed += 1
            continue

        history = wait_for_completion(prompt_id, timeout=120)
        if not history:
            print("FAIL (超时)")
            failed += 1
            continue

        # 找到生成的图片
        images = []
        for nid, output in history.get("outputs", {}).items():
            images.extend(output.get("images", []))

        if not images:
            print("FAIL (无图片)")
            failed += 1
            continue

        # 下载图片
        img = images[0]
        output_path = os.path.join(OUTPUT_DIR, f"{name}.png")
        try:
            download_image(img['filename'], output_path)
            size = os.path.getsize(output_path) / 1024
            print(f"OK ({size:.0f}KB)")
            success += 1
        except Exception as e:
            print(f"FAIL (下载: {e})")
            failed += 1

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print(f"[OK] 完成: {success} 成功, {failed} 失败, 耗时 {elapsed:.0f}s")
    print(f"图片保存在: {os.path.abspath(OUTPUT_DIR)}/")
    print("=" * 70)


if __name__ == "__main__":
    main()
