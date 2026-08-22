# -*- coding: utf-8 -*-
"""生成 Ami 网球装 preview workflow 并尝试提交"""
import json
import uuid
import time
import urllib.request
import urllib.error

COMFYUI = "http://127.0.0.1:8188"
WF_SRC = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\VNCCS_3.0_new_char_creator.json"
WF_OUT = r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\ami_tennis_preview.json"

def main():
    print("=" * 60)
    print("生成 Ami 网球装 Preview Workflow")
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
        return
    
    print(f"[OK] 找到 CharacterCreatorV2 (id={v2_node['id']})")
    
    # 解析原 JSON
    cfg = json.loads(v2_node["widgets_values"][0])
    
    # 更新 Ami 网球装配置
    cfg["character"] = "a"
    cfg["character_info"] = {
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
    
    # 设置 preview 标志
    cfg["preview_valid"] = True
    cfg["preview_source"] = "gen"
    cfg["sprite_preview_index"] = 0
    cfg["sprite_preview_count"] = 1
    cfg["sprite_preview_request_id"] = int(time.time())
    cfg["sprite_preview_cache_bust"] = f"ami:{uuid.uuid4().int}"
    
    # 写回
    v2_node["widgets_values"][0] = json.dumps(cfg, ensure_ascii=False)
    
    print(f"[OK] CharacterCreatorV2 已更新")
    print(f"  character: {cfg['character']}")
    print(f"  name: {cfg['character_info']['name']}")
    print(f"  nsfw: {cfg['character_info']['nsfw']}")
    print(f"  preview_count: {cfg['sprite_preview_count']}")
    
    # 保存 workflow 文件
    with open(WF_OUT, "w", encoding="utf-8") as f:
        json.dump(wf, f, ensure_ascii=False, indent=2)
    print(f"[OK] 已保存: {WF_OUT}")
    
    # 尝试提交到 ComfyUI
    print(f"\n[...] 尝试提交到 {COMFYUI}/prompt ...")
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
        resp = urllib.request.urlopen(req, timeout=30).read()
        result = json.loads(resp)
        prompt_id = result.get("prompt_id")
        print(f"[OK] 提交成功! prompt_id: {prompt_id}")
        print("=" * 60)
        print("任务已提交，请在 ComfyUI 中查看进度")
        print("=" * 60)
        return prompt_id
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"[ERR] HTTP {e.code}")
        print(f"响应: {body[:500]}")
        print("\n" + "=" * 60)
        print("API 提交失败，请使用手动方式:")
        print(f"1. 打开 ComfyUI (http://127.0.0.1:8188)")
        print(f"2. 把下面文件拖到画布:")
        print(f"   {WF_OUT}")
        print(f"3. 点击 Queue Prompt 运行")
        print("=" * 60)
        return None
    except Exception as e:
        print(f"[ERR] {e}")
        return None

if __name__ == "__main__":
    main()
