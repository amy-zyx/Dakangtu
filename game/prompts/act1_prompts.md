# 大康兔 Act 1 图片生成 Prompt 集
# Dakangtu Act 1 - AI Image Generation Prompts
# 模型：Animagine XL v3.0（不是 v1.0）
# 风格：动漫风 SDXL
# 通用负面提示词：见 NEGATIVE_PROMPT

## ========================================
# Animagine XL v3.0 专用语法
## ========================================

# Animagine 用标签式（tag-based）语法，逗号分隔
# 必须以 rating: 开头控制内容等级
# 推荐使用 rating:questionable（允许暴露但不过分）

# 内容等级（按需选择）
RATING_SAFE = "rating:safe"
RATING_QUESTIONABLE = "rating:questionable"  # ⭐ 推荐
RATING_EXPLICIT = "rating:explicit"

# 角色一致性标签
# 阿米：160cm 中国女生，穿着暴露
AMI_TAGS = "1girl, chinese, petite, short_slim_figure, age_20, long_straight_black_hair, brown_eyes, alluring_face, revealing_outfit, crop_top, midriff, low_cut_shirt, short_skirt, high_heels, stylish_fashion, seductive"

# 杰克：175cm 中国男生，短发
JACK_TAGS = "1boy, chinese, average_build, age_22, short_black_hair, brown_eyes, handsome, friendly_smile, casual, t_shirt, jeans, sneakers"

# Animagine 专用负面提示词
NEGATIVE_PROMPT = "lowres, bad_anatomy, bad_hands, text, error, missing_fingers, extra_digit, fewer_digits, cropped, worst_quality, low_quality, jpeg_artifacts, signature, watermark, username, blurry, 3d, realistic, photorealistic, deformed, extra_limbs, mutated, poorly_drawn_hands, poorly_drawn_face, mutation, extra_fingers, bad_proportions, disfigured, malformed, missing_arms, missing_legs, fused_fingers, long_neck"

# 质量标签（必须加）
QUALITY = "masterpiece, best_quality, absurdres, highres, anime_style, detailed"

# 角色立绘尺寸
CHAR_SIZE = "768x1024, upper_body, portrait, looking_at_viewer, simple_background"

# 背景尺寸
BG_SIZE = "1280x720, wide_shot, scenery, no_humans"

# CG 全屏插画尺寸
CG_SIZE = "1280x720, two_characters, cinematic"


## ========================================
# 🏞️ 背景图 (Backgrounds) - 5 张
## ========================================

[airport_terminal.png]
# 用途：开场，杰克站在到达大厅
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {BG_SIZE},
airport, terminal, wellington_airport, arrival_hall, interior,
floor_to_ceiling_windows, gray_sky, overcast, airplanes_on_tarmac,
departure_board, waiting_seats, tiled_floor, automatic_walkway,
natural_daylight, atmosphere, perspective, scenic, depth_of_field"

[airport_arrival.png]
# 备用背景
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {BG_SIZE},
airport, arrival_gate, check_in_counters, morning_light,
tall_windows, interior, atmosphere, no_humans"

[airport_cafe.png]
# 用途：阿米和杰克喝咖啡
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {BG_SIZE},
airport_cafe, interior, floor_to_ceiling_windows,
wellington_harbor, wooden_tables, two_coffee_cups,
afternoon_sunlight, ocean_view, blue_sea, distant_mountains,
modern_design, warm_lighting, atmosphere, no_humans"

[airport_window.png]
# 用途：咖啡店窗边
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {BG_SIZE},
cafe_window_seat, side_window, sunlight_streaming,
light_rays, dust_particles, golden_hour,
wooden_chair, blurred_ocean_view, cozy_atmosphere,
no_humans, depth_of_field"

[wellington_city.png]
# 用途：第一幕结束
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {BG_SIZE},
wellington, cityscape, harbor_view, colorful_wooden_houses,
hillside, cable_car, sky_tower, blue_ocean,
green_hills, partly_cloudy, aerial_view,
new_zealand, atmosphere, masterpiece, no_humans"


## ========================================
# 👧 阿米立绘 (Ami) - 6 张
## ========================================
# 阿米：160cm 中国女生，穿着暴露

[ami normal.png]
# 用途：默认平静
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
neutral_expression, calm, soft_smile, light_makeup, white_background"

[ami smile.png]
# 用途：开心笑
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
happy, bright_smile, eyes_closed, joyful, warm_expression,
white_background"

[ami surprised.png]
# 用途：惊讶
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
surprised, wide_eyes, open_mouth, raised_eyebrows,
light_blush, white_background"

[ami blush.png]
# 用途：害羞脸红
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
shy, deep_blush, looking_down, embarrassed_smile,
hands_near_face, white_background"

[ami thinking.png]
# 用途：思考
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
thoughtful, looking_up, hand_on_chin, pondering,
white_background"

[ami sad.png]
# 用途：失落
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{AMI_TAGS},
sad, disappointed, downcast_eyes, small_frown,
looking_down, melancholy, white_background"


## ========================================
# 🧑 杰克立绘 (Jack) - 6 张
## ========================================
# 杰克：175cm 中国男生，短发

[jack normal.png]
# 用途：默认平静
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
calm, slight_smile, friendly, standing,
white_background"

[jack smile.png]
# 用途：惊喜笑
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
big_smile, bright_eyes, happy, laughing,
white_background"

[jack surprised.png]
# 用途：被调侃
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
surprised, wide_eyes, raised_eyebrows, awkward_smile,
white_background"

[jack apologize.png]
# 用途：道歉
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
apologetic, hand_rubbing_back_of_head, sheepish_smile,
sorry_gesture, white_background"

[jack thinking.png]
# 用途：思考
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
thoughtful, looking_up, hand_on_chin, pondering,
considering, white_background"

[jack wave.png]
# 用途：挥手告别
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CHAR_SIZE},
{JACK_TAGS},
waving, hand_raised, friendly_smile, goodbye,
white_background"


## ========================================
# 🎨 CG 事件图 (Cinematic Graphics) - 3 张
## ========================================

[airport_meet.png]
# 备用 CG：相遇瞬间
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CG_SIZE},
{AMI_TAGS}, {JACK_TAGS},
standing, airport_arrival_hall, first_meeting,
looking_at_each_other, scattered_luggage, surprised,
daylight, cinematic, key_visual, two_characters"

[first_coffee.png]
# CG：咖啡店对话
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CG_SIZE},
{AMI_TAGS}, {JACK_TAGS},
sitting, cafe_table, by_window, two_coffee_cups,
ocean_view, afternoon_light, warm_atmosphere,
intimate_conversation, romantic_mood, key_visual"

[ending_act1.png]
# 用途：第一幕结束 CG
tags = "{RATING_QUESTIONABLE}, {QUALITY}, {CG_SIZE},
{AMI_TAGS}, {JACK_TAGS},
{AMI_TAGS_subtype} waving from airport_shuttle_bus_window,
bus_driving_away, {JACK_TAGS_subtype} standing_on_platform,
sunset, golden_light, dramatic_silhouette,
emotional_farewell, wellington_city_background,
romantic_ending, lens_flare, bokeh, key_visual"


## ========================================
# 📋 角色设定摘要
## ========================================

# 阿米 (Ami)
# ─────────────────────────
# 性别：女
# 国籍：中国
# 身高：160cm
# 体型：娇小纤细
# 年龄：20岁
# 发型：黑色长直发
# 眼睛：棕色
# 性格：温柔、带点路痴、可爱
# 穿着：暴露（紧身上衣露脐、低胸、短裙、高跟鞋）

# 杰克 (Jack)
# ─────────────────────────
# 性别：男
# 国籍：中国
# 身高：175cm
# 体型：标准偏运动型
# 年龄：22岁
# 发型：黑色短发
# 眼睛：棕色
# 性格：阳光、礼貌、乐于助人
# 穿着：休闲（T恤、牛仔裤、运动鞋）


## ========================================
# ComfyUI Animagine XL 专用设置
## ========================================

# 模型路径
MODEL = "models/animagine-xl-v3.0/animagine-xl-v3.0.safetensors"

# 推荐参数
SAMPLER = "euler_ancestral"  # Animagine 官方推荐
SCHEDULER = "karras"
STEPS = 28
CFG = 7
RESOLUTION = {
    "character": "832x1216",   # 竖版，重采样到 768x1024
    "background": "1280x720",  # 横版
    "cg": "1280x720"           # 横版
}

# VAE（推荐用内置的）
VAE = "内置 (sdxl_vae.safetensors)"

# 下载命令（如果还没下载）：
# hf download Linaqruf/animagine-xl-v3.0 --local-dir ./models/animagine-xl-v3.0


## ========================================
# Animagine XL 使用要点
## ========================================

# 1. 必须以 rating: 开头
#    - rating:safe              → 干净，无任何暴露
#    - rating:questionable      → 允许一定暴露（推荐）✅
#    - rating:explicit          → 露点/sex 内容
#    - rating:nsfw              → 同 explicit

# 2. 用逗号分隔标签，不用自然语言句子
#    ❌ "A girl with long hair smiling"
#    ✅ "1girl, long_hair, smile"

# 3. 质量标签放最前
#    "masterpiece, best_quality, absurdres"

# 4. 标签顺序影响权重（前面的权重更高）
#    推荐顺序: rating → quality → 数量/性别 → 角色特征 → 动作/表情 → 背景 → 服装

# 5. 角色一致性技巧
#    - 用同一组 seed 偏移生成同一角色的不同表情
#    - 用 IP-Adapter 节点 + 第一张满意图作为 reference
#    - 用 Reference-only 节点（ComfyUI 内置）
#    - 固定角色描述标签（已封装在 AMI_TAGS / JACK_TAGS）

# 6. Animagine 暴露穿着的额外标签（如果默认生成不够暴露）：
#    "large_breasts, navel, bare_shoulders, thigh_gap, cleavage, no_bra, underboob"
