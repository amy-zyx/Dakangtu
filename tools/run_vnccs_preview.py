# -*- coding: utf-8 -*-
"""真提交 VNCCS preview workflow - 不撒谎"""
import json, urllib.request, copy, os, uuid

COMFYUI = "http://127.0.0.1:8188"
WF = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\VNCCS_3.0_new_char_creator.json"

# Ami 关键词
AMI_KEYWORDS = {
    "character": "a",
    "character_info": {
        "sex": "female",
        "age": 20,
        "race": "chinese",
        "skin_color": "light skin, fair porcelain skin",
        "hair": "long straight black hair, very long hair, side parting",
        "eyes": "large brown eyes, expressive",
        "face": "soft features, gentle expression",
        "body": "slim, 165cm",
        "additional_details": "20 years old chinese girl",
        "nsfw": False,
        "aesthetics": "masterpiece, best quality, score_7, anime, 2d flat illustration, visual novel style",
        "negative_prompt": "bad quality, worst quality, low quality, score_1, score_2, score_3, blurry, jpeg artifacts, 3d, realistic",
        "lora_prompt": "",
        "background_color": "Green",
        "name": "Ami",
        "seed": 12345,
    }
}

# Jack 关键词
JACK_KEYWORDS = {
    "character": "j",
    "character_info": {
        "sex": "male",
        "age": 22,
        "race": "chinese",
        "skin_color": "light skin, slightly tanned",
        "hair": "short black hair, side-swept bangs",
        "eyes": "large brown eyes, expressive",
        "face": "bishounen, sharp jaw, narrow face, model-like face",
        "body": "athletic build, 175cm, slim muscular",
        "additional_details": "22 years old chinese boy, handsome, refined",
        "nsfw": False,
        "aesthetics": "masterpiece, best quality, score_7, anime, 2d flat illustration, visual novel style",
        "negative_prompt": "bad quality, worst quality, low quality, score_1, score_2, score_3, blurry, jpeg artifacts, 3d, realistic",
        "lora_prompt": "",
        "background_color": "Green",
        "name": "Jack",
        "seed": 54321,
    }
}

def submit(char_data, label):
    """真提交一个 preview 任务"""
    print(f"\n=== 提交 {label} preview ===")
    with open(WF, "r", encoding="utf-8") as f:
        wf = json.load(f)

    # 找 CharacterCreatorV2 节点 (id=797)
    v2_node = None
    for node in wf["nodes"]:
        if node.get("type") == "CharacterCreatorV2":
            v2_node = node
            break

    if not v2_node:
        print("ERR: 找不到 CharacterCreatorV2 节点")
        return None

    # widget_values[0] 是 JSON 配置, 改 character + character_info
    old_wv = v2_node["widgets_values"][0]
    try:
        config = json.loads(old_wv)
    except:
        config = {}

    config["character"] = char_data["character"]
    config["character_info"] = char_data["character_info"]
    # 让 preview 模式可工作
    config["preview_valid"] = True
    config["preview_source"] = "gen"
    config["sprite_preview_index"] = 0
    config["sprite_preview_count"] = 1
    config["sprite_preview_request_id"] = 1
    config["sprite_preview_cache_bust"] = f"{char_data['character']}:{uuid.uuid4().int}"

    v2_node["widgets_values"][0] = json.dumps(config, ensure_ascii=False)
    print(f"  V2 config updated: character={config['character']}, name={config['character_info']['name']}")

    # 提交到 ComfyUI
    payload = {
        "prompt": wf,
        "client_id": str(uuid.uuid4()),
    }
    req = urllib.request.Request(
        f"{COMFYUI}/prompt",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        resp = json.loads(urllib.request.urlopen(req, timeout=30).read())
        pid = resp.get("prompt_id")
        print(f"  ✅ 提交成功! prompt_id: {pid}")
        return pid
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"  HTTP {e.code} body: {body[:2000]}")
        return None
    except Exception as e:
        print(f"  ❌ ERR: {e}")
        return None

# 提交两个
ami_pid = submit(AMI_KEYWORDS, "Ami (a)")
jack_pid = submit(JACK_KEYWORDS, "Jack (j)")

print(f"\n=== 结果 ===")
print(f"Ami:  {ami_pid}")
print(f"Jack: {jack_pid}")
