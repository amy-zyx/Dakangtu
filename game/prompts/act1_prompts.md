# 大康兔 Act 1 图片生成 Prompt 集
# Dakangtu Act 1 - AI Image Generation Prompts
# 用途：ComfyUI + 任意动漫风格 SDXL 模型（如 Animagine XL / Kohaku XL / CounterfeitXL）
# 风格统一：anime visual novel style, soft lighting, pastel color palette
# 通用负面提示词：见 NEGATIVE_PROMPT

## ========================================
# 全局通用设定
## ========================================

# 主风格关键词（加到所有 prompt 开头）
STYLE_PREFIX = "anime visual novel style, soft cinematic lighting, pastel color palette, high quality, detailed, masterpiece, best quality, 2d game art"

# 角色一致性关键词
AMY_CHAR_TAGS = "1girl, asian girl, long straight black hair, brown eyes, gentle expression, slim build, age 22, school student outfit, beige cardigan, white shirt, denim skirt"
JACK_CHAR_TAGS = "1boy, european young man, short messy blonde hair, blue eyes, athletic build, age 23, casual outfit, navy hoodie, khaki pants"

# 全局负面提示词（避免生成错误内容）
NEGATIVE_PROMPT = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, 3d, realistic, photorealistic, deformed face, extra limbs, mutated hands, poorly drawn hands, poorly drawn face, mutation, extra fingers, bad proportions, disfigured, malformed limbs, missing arms, missing legs, fused fingers, too many fingers, long neck"

# 角色立绘尺寸（Ren'Py 中显示为半身像）
CHAR_SIZE = "768x1024, upper body portrait, looking at viewer, simple pastel background"

# 背景尺寸
BG_SIZE = "1280x720, wide shot, no humans or small figures in background, scenic view"

# CG 全屏插画尺寸
CG_SIZE = "1280x720, two characters full body or half body, cinematic composition"


## ========================================
# 🏞️ 背景图 (Backgrounds) - 5 张
## ========================================

[airport_terminal.png]
# 用途：开场，杰克站在到达大厅
prompt = "{STYLE_PREFIX}, {BG_SIZE}, {NEGATIVE_PROMPT}

# 描述：惠灵顿国际机场到达大厅，下午，灰色阴天，落地窗外是停机坪，候机区座椅，电子航班显示屏，玻璃幕墙，自动步道，现代简约设计，旅客剪影（远景小人物），自然光从落地窗洒入
positive = "wellington international airport interior, arrival hall, modern terminal, floor-to-ceiling glass windows, gray overcast sky outside, parked airplanes on tarmac, departure board with flight information, rows of empty waiting seats, tiled floor, automatic walkway, natural daylight from windows, no main characters, atmospheric perspective, anime background art, 16:9 aspect ratio, scenic wallpaper style, no humans in foreground, depth of field"

[airport_arrival.png]
# 备用背景（剧情中暂未使用）
prompt = "airport arrival gate, animated character standing in foreground, no main character in focus, airport interior with check-in counters, morning light streaming through tall windows"


[airport_cafe.png]
# 用途：阿米和杰克喝咖啡的场景
prompt = "{STYLE_PREFIX}, {BG_SIZE}, {NEGATIVE_PROMPT}

# 描述：机场内咖啡店，落地窗，海景（远处可见惠灵顿港湾），木质桌椅，两杯咖啡，温暖午后光线
positive = "airport cafe interior, floor-to-ceiling windows overlooking wellington harbor, wooden tables and chairs, two coffee cups on table, warm afternoon sunlight, ocean view outside, blue sea, distant mountains, casual modern cafe design, soft warm lighting, no people, anime background art, 16:9 scenic view, atmospheric"

[airport_window.png]
# 用途：杰克带 Mike 回来，咖啡店窗边
prompt = "{STYLE_PREFIX}, {BG_SIZE}, {NEGATIVE_PROMPT}

# 描述：咖啡店窗边座位特写，阳光从侧窗打进来，温暖氛围
positive = "cafe window seat, side window view, warm sunlight streaming in, light rays, dust particles in light, soft golden hour lighting, wooden chair, blurred ocean view outside window, cozy atmosphere, no people, anime background art, depth of field, 16:9 composition"

[wellington_city.png]
# 用途：第一幕结束，阿米坐大巴离开
prompt = "{STYLE_PREFIX}, {BG_SIZE}, {NEGATIVE_PROMPT}

# 描述：惠灵顿城市景观，港口，山丘，缆车，天空塔，彩色房子，新西兰风情
positive = "wellington cityscape, harbor view, colorful wooden houses on hillside, wellington cable car, sky tower in distance, blue ocean, rolling green hills, partly cloudy sky, scenic aerial view, new zealand aesthetic, anime background art, 16:9 wide shot, masterpiece, no people"


## ========================================
# 👧 阿米立绘 (Ami) - 6 张
## ========================================

[ami normal.png]
# 用途：默认表情，平静
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, neutral calm expression, gentle eyes, soft smile, beige cardigan over white blouse, standing pose, white background"

[ami smile.png]
# 用途：开心、感谢时的笑
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, happy bright smile, eyes slightly closed with joy, warm expression, beige cardigan over white blouse, standing pose, white background"

[ami surprised.png]
# 用途：行李掉落时的惊讶、问路时的表情
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, surprised expression, wide eyes, slightly open mouth, raised eyebrows, light blush on cheeks, beige cardigan over white blouse, white background"

[ami blush.png]
# 用途：害羞、脸红
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, shy blushing, deep pink blush on cheeks, looking down slightly, gentle embarrassed smile, hands near face, beige cardigan over white blouse, white background"

[ami thinking.png]
# 用途：思考、犹豫
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, thoughtful expression, looking up slightly, hand on chin, soft pondering look, beige cardigan over white blouse, white background"

[ami sad.png]
# 用途：杰克说要去接 Mike 时的失落
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS}, sad disappointed expression, slightly downcast eyes, small frown, looking down, melancholy mood, beige cardigan over white blouse, white background"


## ========================================
# 🧑 杰克立绘 (Jack) - 6 张
## ========================================

[jack normal.png]
# 用途：默认表情，平静
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, friendly calm expression, slight smile, blue eyes looking forward, navy hoodie with khaki pants, standing pose, white background"

[jack smile.png]
# 用途：发现是校友时的惊喜笑
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, big warm smile, bright happy eyes, friendly expression, laughing slightly, navy hoodie with khaki pants, white background"

[jack surprised.png]
# 用途：被 Mike 调侃
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, surprised expression, wide eyes, slightly raised eyebrows, awkward smile, navy hoodie with khaki pants, white background"

[jack apologize.png]
# 用途：要去接 Mike 时向阿米道歉
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, apologetic expression, slight bow pose, hand rubbing back of head, sheepish smile, sorry gesture, navy hoodie with khaki pants, white background"

[jack thinking.png]
# 用途：被问为什么注意到她
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, thoughtful expression, looking up, hand on chin, pondering look, considering words, navy hoodie with khaki pants, white background"

[jack wave.png]
# 用途：告别时挥手
prompt = "{STYLE_PREFIX}, {CHAR_SIZE}, {NEGATIVE_PROMPT}
positive = "{JACK_CHAR_TAGS}, waving hand goodbye, friendly smile, palm raised, parting gesture, navy hoodie with khaki pants, white background"


## ========================================
# 🎨 CG 事件图 (Cinematic Graphics) - 3 张
## ========================================

[airport_meet.png]
# 备用 CG：相遇瞬间
prompt = "{STYLE_PREFIX}, {CG_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS} and {JACK_CHAR_TAGS}, standing in airport arrival hall, first meeting scene, looking at each other, scattered luggage on floor, surprised expressions, soft daylight, cinematic composition, anime key visual"

[first_coffee.png]
# CG：咖啡店对话
prompt = "{STYLE_PREFIX}, {CG_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS} and {JACK_CHAR_TAGS}, sitting at cafe table by window, two coffee cups, ocean view outside, afternoon light, warm atmosphere, intimate conversation moment, anime key visual, romantic mood"

[ending_act1.png]
# 用途：第一幕结束 CG，阿米坐大巴挥手告别
prompt = "{STYLE_PREFIX}, {CG_SIZE}, {NEGATIVE_PROMPT}
positive = "{AMY_CHAR_TAGS} waving from airport shuttle bus window, bus driving away, {JACK_CHAR_TAGS} standing on platform watching, sunset golden light, dramatic silhouette composition, emotional farewell scene, wellington city background, anime key visual, romantic ending aesthetic, lens flare, bokeh"


## ========================================
# ComfyUI 建议设置
## ========================================

# 推荐模型（任选其一）：
# - Linaqruf/animagine-xl-v3.0  （最推荐，动漫专门）
# - KBlueLeaf/kohaku-xl-v7
# - gsdf/CounterfeitXL-V2.5

# 推荐采样器：Euler a / DPM++ 2M Karras
# 推荐步数：28-35
# 推荐 CFG：7-8
# 推荐分辨率：
#   - 角色立绘：832x1216（竖版）→ 重采样到 768x1024
#   - 背景：1280x720（横版）
#   - CG：1280x720（横版）

# 角色一致性建议：
#   1. 用同一组 seed 生成同一角色的所有表情（修改 seed 偏移）
#   2. 在 prompt 中固定角色描述关键词（已包含在 AMY_CHAR_TAGS / JACK_CHAR_TAGS）
#   3. 使用 IP-Adapter 或 Reference-only 节点保持角色脸型一致
