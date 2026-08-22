# -*- coding: utf-8 -*-
"""直接提交 Ami 网球装 preview 到 ComfyUI"""
import json
import urllib.request
import urllib.error
import uuid
import time

COMFYUI = "http://127.0.0.1:8188"
WF_SRC = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\VNCCS_3.0_new_char_creator.json"

# Ami 网球装配置
AMI_TENNIS = {
    "character": "a",
    "character_info": {
        "sex": "female",
        "age": 20,
        "race": "chinese",
        "skin_color": "light skin, fair porcelain skin",
        "hair": "long straight black hair, very long hair, side parting",
        "eyes": "large brown eyes, expressive",
        "face": "round face shape, slightly chubby cheeks, soft feminine features, kind gentle expression, large expressive brown eyes, soft eyelashes, small nose, light pink lips",
        "body": "slim thick body type, curvy figure, well-endowed bust, large breasts, narrow waist, wide hips, feminine curves, 165cm, healthy voluptuous physique",
        "additional_details": "20 years old chinese girl, wearing tennis outfit, white tennis dress, short pleated tennis skirt, white sleeveless polo shirt, exposed cleavage, sporty fashion",
        "nsfw": True,
        "aesthetics": "masterpiece, best quality, score_7, anime, 2d flat illustration, visual novel style, simple flat color, cel shading",
        "negative_prompt": "bad quality, worst quality, low quality, score_1, score_2, score_3, blurry, jpeg artifacts, 3d, realistic, photorealistic, gradient, complex shading, mature, old, dark skin, exaggerated proportions, male, flat chest, skinny, thin body",
        "lora_prompt": "",
        "background_color": "Green",
        "name": "Ami_Tennis",
        "seed": 12345
    }
}


def submit_workflow():
    print("=" * 60)
    print("提交 Ami 网球装 Preview")
    print("=" * 60)
    
    # 加载 workflow
    with open(WF_SRC, "r", encoding="utf-8") as f:
        wf = json.load(f)
    
    # 找 CharacterCreatorV2 节点
    v2_node = None
    for node in wf["nodes"]:
        if node.get("type") == "CharacterCreatorV2":
            v2_node = node
            break
    
    if not v2_node:
        print("[ERR] 找不到 CharacterCreatorV2 节点")
        return None
    
    print(f"[OK] 找到 CharacterCreatorV2 (id={v2_node['id']})")
    
    # 解析原 JSON
    cfg = json.loads(v2_node["widgets_values"][0])
    
    # 更新 Ami 配置
    cfg["character"] = AMI_TENNIS["character"]
    cfg["character_info"] = AMI_TENNIS["character_info"]
    
    # 设置 preview 标志
    cfg["preview_valid"] = True
    cfg["preview_source"] = "gen"
    cfg["sprite_preview_index"] = 0
    cfg["sprite_preview_count"] = 1  # 只生成 1 张
    cfg["sprite_preview_request_id"] = int(time.time())
    cfg["sprite_preview_cache_bust"] = f"ami:{uuid.uuid4().int}"
    
    # 写回
    v2_node["widgets_values"][0] = json.dumps(cfg, ensure_ascii=False)
    
    print(f"[OK] 节点配置已更新")
    print(f"  character: {cfg['character']}")
    print(f"  name: {cfg['character_info']['name']}")
    print(f"  nsfw: {cfg['character_info']['nsfw']}")
    print(f"  preview_count: {cfg['sprite_preview_count']}")
    
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
    
    print(f"\n[...] 提交到 {COMFYUI}/prompt ...")
    try:
        resp = urllib.request.urlopen(req, timeout=30).read()
        result = json.loads(resp)
        prompt_id = result.get("prompt_id")
        print(f"[OK] 提交成功! prompt_id: {prompt_id}")
        return prompt_id
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"[ERR] HTTP {e.code}")
        print(f"响应: {body[:500]}")
        return None
    except Exception as e:
        print(f"[ERR] {e}")
        return None


if __name__ == "__main__":
    pid = submit_workflow()
    
    if pid:
        print("\n" + "=" * 60)
        print(f"✅ 任务已提交: {pid}")
        print("请在 ComfyUI 中查看进度")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ API 提交失败")
        print("请手动加载 workflow 文件:")
        print(f"  {WF_SRC.replace('.json', '_ami_preview.json')}")
        print("=" * 60)
        
        # 保存一个可以手动加载的版本
        with open(WF_SRC, "r", encoding="utf-8") as f:
            wf = json.load(f)
        for node in wf["nodes"]:
            if node.get("type") == "CharacterCreatorV2":
                cfg = json.loads(node["widgets_values"][0])
                cfg["character"] = AMI_TENNIS["character"]
                cfg["character_info"] = AMI_TENNIS["character_info"]
                cfg["preview_valid"] = True
                cfg["preview_source"] = "gen"
                cfg["sprite_preview_index"] = 0
                cfg["sprite_preview_count"] = 1
                cfg["sprite_preview_request_id"] = int(time.time())
                cfg["sprite_preview_cache_bust"] = f"ami:{uuid.uuid4().int}"
                node["widgets_values"][0] = json.dumps(cfg, ensure_ascii=False)
                break
        manual_path = WF_SRC.replace("VNCCS_3.0_new_char_creator.json", "ami_preview_manual.json")
        with open(manual_path, "w", encoding="utf-8") as f:
            json.dump(wf, f, ensure_ascii=False, indent=2)
        print(f"\n[OK] 手动版本已保存: {manual_path}")

        # 也保存 ami_preview.json (之前生成的那个)
        import shutil
        shutil.copy(manual_path, WF_OUT)
        print(f"[OK] 同时更新: {WF_OUT}")
