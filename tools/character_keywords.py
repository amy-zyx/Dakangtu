# -*- coding: utf-8 -*-
"""
VNCCS 角色关键词配置 - 用 CharacterAssetSelector 节点
=====================================================

字段:
- face: 脸/眼睛/表情
- head: 头发/帽子
- top: 上衣
- bottom: 下装
- shoes: 鞋
- extra_negative_prompt: 额外负面
- new_costume_name: 新服装名

怎么用 (在 ComfyUI 浏览器):
1. 添加 CharacterAssetSelector (或 QWEN 版) 节点
2. 选 character: a (Ami) 或 j (Jack)
3. 在 face/head/top/bottom/shoes 5 个字段填下面的关键词
4. 连到 VNCCS_CharacterGenerator.character 输入
"""

# ============================================================
# Ami (character="a")
# ============================================================
AMI = {
    "character": "a",
    "costume": "N",  # Naked (基础体型)

    # 脸部特征 - 眼睛/表情/脸型
    "face": "20 years old chinese girl, soft feminine features, slim oval face, "
            "kind gentle expression, large expressive brown eyes, soft eyelashes, "
            "small nose, light pink lips, natural minimal makeup",

    # 头发/帽子
    "head": "very long straight black hair, smooth shiny hair, side parting, "
            "no bangs, hair reaching waist, dark black color",

    # 上衣
    "top": "simple white cotton t-shirt, crew neck, short sleeves, "
           "no print, no logo, no design, plain clean white, fitted casual style",

    # 下装
    "bottom": "light blue denim jeans, slim fit, mid-rise, classic 5-pocket style, "
              "ankle length, casual everyday wear",

    # 鞋子
    "shoes": "white sneakers, simple low-top canvas shoes, white rubber sole, "
             "casual sporty style",

    # 额外负面
    "extra_negative_prompt": "3d, realistic, photo, gradient, complex shading, "
                              "cheongsam, tangzhuang, hanfu, cleavage, crop top, midriff, "
                              "mature, old, dark skin, exaggerated proportions",
}


# ============================================================
# Jack (character="j")
# ============================================================
JACK = {
    "character": "j",
    "costume": "N",

    # 脸部特征
    "face": "22 years old chinese boy, bishounen handsome protagonist face, "
            "sharp jaw, narrow face, model-like face, kind gentle expression, "
            "large expressive brown eyes, soft eyelashes, "
            "slightly tanned light skin, clean-shaven, refined features",

    # 头发
    "head": "short black hair, side-swept bangs, neat styled hair, "
            "medium length on top, short on sides, modern casual hairstyle, dark black color",

    # 上衣
    "top": "black cotton t-shirt, crew neck, short sleeves, "
           "with 'fire woods' text in dark charcoal black printed on chest, "
           "slightly darker than shirt, fitted casual style, no other design",

    # 下装
    "bottom": "dark navy slim fit jeans, mid-rise, classic style, ankle length, "
              "casual everyday wear",

    # 鞋子
    "shoes": "white sneakers, simple low-top canvas shoes, white rubber sole, "
             "casual sporty style",

    # 额外负面
    "extra_negative_prompt": "3d, realistic, photo, gradient, complex shading, "
                              "suit, formal, business, school uniform, "
                              "mature, old, dark skin, exaggerated muscles, "
                              "fire wood (singular, must be plural)",
}


# ============================================================
# 表情关键词 (给 PoseStudio / EmotionGenerator)
# ============================================================
EMOTION_PROMPTS = {
    "smile":    "smiling gently, mouth corners up, warm friendly expression, eyes slightly squinted with smile",
    "surprise": "surprised expression, mouth slightly open, eyes wide, eyebrows raised, slight gasp",
    "blush":    "blushing expression, pink cheeks, embarrassed looking down, shy smile, hand near face",
    "thinking": "thinking pose, hand on chin, contemplative expression, eyes looking up and to the side, slight frown",
    "sad":      "sad expression, downcast eyes looking down, slight frown, soft melancholic look",
    "happy":    "happy cheerful expression, bright wide smile, eyes sparkling with joy, energetic",
    "worried":  "worried expression, slight frown, concerned eyes, eyebrows furrowed, looking at something off-screen",
}


# ============================================================
# 怎么用
# ============================================================
HOW_TO = """
═══════════════════════════════════════════════════
  VNCCS CharacterAssetSelector 节点 - 5 字段
═══════════════════════════════════════════════════

节点位置 (右键 → Add Node):
  VNCCS / CharacterAssetSelector
  或
  VNCCS / CharacterAssetSelectorQWEN  (推荐, 用 Qwen 模型)

字段:
  face   - 脸/眼睛/表情关键词
  head   - 头发/帽子关键词
  top    - 上衣关键词
  bottom - 下装关键词
  shoes  - 鞋关键词

═══════════════════════════════════════════════════
  步骤
═══════════════════════════════════════════════════

1. 在 ComfyUI 添加 CharacterAssetSelector (或 QWEN)
2. 选 character: a (Ami) 或 j (Jack)
3. 把下面 AMI / JACK 字典的 5 个字段填进去
4. 连到 VNCCS_CharacterGenerator.character 输入
5. Queue Prompt

═══════════════════════════════════════════════════
  完整 workflow 链
═══════════════════════════════════════════════════

[CharacterAssetSelector]    →  character (IMAGE)
                              ↓
[VNCCS_CharacterGenerator]  ←  poses (PoseStudio)
                              ←  prompt
                              ←  pipe (ControlCenter)
                              ↓
                            IMAGE  (角色立绘)

═══════════════════════════════════════════════════
"""


if __name__ == "__main__":
    import json
    print("═══════════════════════════════════════")
    print(" Ami (character='a') - 5 字段配置")
    print("═══════════════════════════════════════")
    print(json.dumps(AMI, ensure_ascii=False, indent=2))

    print("\n═══════════════════════════════════════")
    print(" Jack (character='j') - 5 字段配置")
    print("═══════════════════════════════════════")
    print(json.dumps(JACK, ensure_ascii=False, indent=2))

    print("\n═══════════════════════════════════════")
    print(" 表情 prompt 关键词 (给 PoseStudio)")
    print("═══════════════════════════════════════")
    print(json.dumps(EMOTION_PROMPTS, ensure_ascii=False, indent=2))

    print(HOW_TO)
