# -*- coding: utf-8 -*-
"""
生成 Ami preview 的 VNCCS workflow 文件
- API 提交一直 500 错误，所以直接生成一个可手动 load 的 workflow JSON
"""
import json
import time
import uuid

WF_SRC = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\VNCCS_3.0_new_char_creator.json"
WF_OUT = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_preview.json"

# Ami 角色配置（与 character_keywords.py 对齐）
AMI_CONFIG = {
    "character": "a",
    "character_info": {
        "sex": "female",
        "age": 20,
        "race": "chinese",
        "skin_color": "light skin, fair porcelain skin",
        "hair": "long straight black hair, very long hair, side parting",
        "eyes": "large brown eyes, expressive",
        "face": "soft features, gentle expression, slim oval face",
        "body": "slim, 165cm",
        "additional_details": "20 years old chinese girl, petite",
        "nsfw": False,
        "aesthetics": "masterpiece, best quality, score_7, anime, 2d flat illustration, visual novel style, simple flat color, cel shading",
        "negative_prompt": "bad quality, worst quality, low quality, score_1, score_2, score_3, blurry, jpeg artifacts, 3d, realistic, photorealistic, gradient, complex shading, mature, dark skin, exaggerated proportions",
        "lora_prompt": "",
        "background_color": "Green",
        "name": "Ami",
        "seed": 12345,
    }
}

# Preview 触发参数
PREVIEW_FLAGS = {
    "preview_valid": True,
    "preview_source": "gen",
    "sprite_preview_index": 0,
    "sprite_preview_count": 1,  # 只生成 1 张 preview
    "sprite_preview_request_id": int(time.time()),
    "sprite_preview_cache_bust": f"ami:{uuid.uuid4().int}",
}


def build_ami_preview_workflow():
    with open(WF_SRC, "r", encoding="utf-8") as f:
        wf = json.load(f)

    # 找 CharacterCreatorV2 节点
    v2 = None
    for n in wf["nodes"]:
        if n.get("type") == "CharacterCreatorV2":
            v2 = n
            break
    if not v2:
        raise RuntimeError("CharacterCreatorV2 节点未找到")

    # 解析原 JSON
    cfg = json.loads(v2["widgets_values"][0])

    # 写入 Ami 配置
    cfg["character"] = AMI_CONFIG["character"]
    cfg["character_info"] = AMI_CONFIG["character_info"]
    cfg.update(PREVIEW_FLAGS)

    # 同步写到 widgets_values[0]
    v2["widgets_values"][0] = json.dumps(cfg, ensure_ascii=False)

    # 保存
    with open(WF_OUT, "w", encoding="utf-8") as f:
        json.dump(wf, f, ensure_ascii=False, indent=2)

    print(f"[OK] 已生成: {WF_OUT}")
    print(f"  character  = {cfg['character']}")
    print(f"  name       = {cfg['character_info']['name']}")
    print(f"  preview_valid    = {cfg['preview_valid']}")
    print(f"  preview_count    = {cfg['sprite_preview_count']}")
    print(f"  cache_bust = {cfg['sprite_preview_cache_bust']}")


if __name__ == "__main__":
    build_ami_preview_workflow()
