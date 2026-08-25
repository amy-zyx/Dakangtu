# ============================================================
# 大康图 - Act 1：落日和明天
# Dakangtu - Act 1: Sunset and Tomorrow
# ============================================================
# 剧本来源: plots/act1_script.md
# 背景:     game/images/backgrounds/  (3 张 1920x1080 2D anime galgame)
# 立绘:     game/images/characters/rita/  (暂用 Rita 角色图作为 LX 立绘)
# 角色定义: characters.rpy  (lx 已在该文件定义)
# ============================================================

# ============ 背景图声明 (1920x1080 全屏) ============
# 主体场景
image bg restaurant_interior  = "images/backgrounds/zimage_anime_bg_scene2_private_dining_room_00001_.png"
image bg dining_table_window  = "images/backgrounds/zimage_anime_bg_scene3_dining_table_window_00001_.png"
image bg bus_stop             = "images/backgrounds/zimage_anime_v5_bg_scene4_bus_stop_00001_.png"

# 兼容别名 (让旧 scene bg xxx 仍能工作 / 方便后续替换图)
image bg private_dining_room  = "images/backgrounds/zimage_anime_bg_scene2_private_dining_room_00001_.png"
image bg dining_table         = "images/backgrounds/zimage_anime_bg_scene3_dining_table_window_00001_.png"
image bg street_corner        = "images/backgrounds/zimage_anime_v5_bg_scene4_bus_stop_00001_.png"

# ============ LX 立绘声明 ============
# 注: 暂用 Rita 角色图作为 LX 立绘占位 (因 LX 角色立绘尚未生成)
# 立绘选择依据剧本描述: 姜黄色大衣 → preview_coat_yellow.png 最贴合
# 注意: image attribute 名不能用 Python 关键字, 故用 default_view 替代 default
image lx default_view = "images/characters/rita/preview_coat_yellow.png"   # 默认: 姜黄大衣版
image lx normal     = "images/characters/rita/face_neutral-emote_0001.png"
image lx smile      = "images/characters/rita/face_content-smile_0001.png"
image lx sweet_smile = "images/characters/rita/face_sweet-smile_0001.png"
image lx shy        = "images/characters/rita/face_shy-smile_0001.png"
image lx surprised  = "images/characters/rita/face_surprised_0001.png"
image lx radiant    = "images/characters/rita/face_radiant-smile_0001.png"
image lx laugh      = "images/characters/rita/face_laughing_0001.png"
image lx glance     = "images/characters/rita/face_glare-of-judgment_0001.png"

# 兼容别名
image lx coat_yellow = "images/characters/rita/preview_coat_yellow.png"

# ============================================================
# Act 1: 落日和明天
# ============================================================
label act1:

    # 标记剧情进度
    $ act1_complete = False
    $ current_location = "restaurant"
    $ current_time = "night"

    # ----------------- 标题 -----------------
    scene black
    with Pause(1.0)

    "Act 1：落日和明天"
    with Pause(2.0)

    # ============================================================
    # Scene 1: 推开 (包间远景)
    # ============================================================
    scene bg restaurant_interior
    with fade

    # 旁白：开场诗 (一字不改)
    "东风夜放花千树，更吹落、星如雨。"
    "宝马雕车香满路。凤箫声动，玉壶光转，一夜鱼龙舞。"
    "蛾儿雪柳黄金缕，笑语盈盈暗香去。"
    "众里寻他千百度，蓦然回首，那人却在，灯火阑珊处。"
    with Pause(1.5)

    "人的记忆是古怪的，很多感情最终只凝结成几个字，一幅画。"
    with Pause(1.0)

    "我推开门走了进去。"
    with Pause(0.5)

    # 旁白：环境描述
    "天贵食府应该是这条街最高档的餐厅了。气派的大门，走入后一个小桥流水的布置。"
    "空气里有淡淡的茉莉香，混着葱油和糖醋的气息。"
    "我按着手机里那条短信找过去，推开了包间的门。"
    with Pause(1.0)

    # 旁白：发现 LX
    "我在那一桌子喧闹里一眼扫过去，然后目光被她吸引了。"

    "是 LX。"
    "但我差点没认出她来。"
    "3年。整整3年。"
    with Pause(0.5)

    "高中毕业那个暑假我去了南方的大学，毕业后没有听到过她的音讯。"
    "我们本来就是不怎么说话的同学，高中三年都没怎么讲过话，"
    "唯一的交集就是在一个教室里上课。"
    "毕业那年我们没有说过再见，没有留过电话，连QQ号都没加过。"
    with Pause(0.5)

    # 旁白：LX 远景视觉锚点
    "可她现在就坐在那里，夺走了我的目光。"
    "窗外是程庄路的车，尾灯拉成一条条红色的丝线；"
    "她坐在那片红色光晕的边上，脸被窗外那道光勾了一道暖边。"
    "她正侧着头跟旁边的人说话，嘴角弯着，笑得很淡很从容。"
    with Pause(1.0)

    "她没有戴眼镜。"
    "我站在原地，盯着她看了好几秒才确认。"
    "高三那年她鼻梁上永远架着一副圆框眼镜，金色的细边。没有留意过她的眼睛。"
    "此刻她坐在那里，鼻梁上干干净净的，什么都没架。"
    "眼睛显得比以前大了整整一圈，深褐色的瞳仁里映着浅浅的光。"
    with Pause(1.0)

    "我大概没见过她不戴眼镜的样子。"
    "LX 剪短了头发，戴着一个红色的发卡，穿了件姜黄色的大衣，里面是米白色的 V 领毛衣。"
    "姜黄，像深秋里银杏叶还没落尽时那种颜色，带着一点暖调。"
    "大衣的线条垂下来，把她的身形拉得很修长。"
    "她偶尔动一下，大衣的下摆随着动作轻轻晃。"
    with Pause(1.0)

    # ============================================================
    # Scene 2: 相认 (餐桌近景)
    # ============================================================
    scene bg dining_table_window
    with dissolve

    # 显示 LX 立绘 (右侧)
    show lx sweet_smile at right zorder 2
    with dissolve

    "我走近落座。她大概只是随意地扫了一眼门口，看看是谁来晚了。"
    "她的目光从我脸上滑过去，又滑回来，停住了。"
    "然后她笑了。"
    "嘴角轻轻往上弯，眼睛弯成两道很浅的月牙。"
    "那枚红色的发卡在她偏头的时候滑了一下，碰到耳朵上方的发丝，又停住。"
    with Pause(1.0)

    "「LX？」"
    "我先开口了。我记得她的名字，她学习很好，我印象里是年级第4。"
    "虽然我们不怎么说话但是她的名字我是知道的，"
    "她也马上回复了我，显然几年时间我还没有被淡忘成某甲。"
    with Pause(0.5)

    show lx smile at right zorder 2
    with dissolve

    "我走到她的对面坐下，听着一群同学聊天。"
    "我平时都是聊天的主力，一个社牛，今天我倒是比较沉默，"
    "只是时不时的偷偷看看这位熟悉又陌生的美女。"
    "之后的同学聚会很模糊，就那几个人说那几个熟悉的话题。"
    "推杯换盏，时间过得很快。"
    with Pause(1.0)

    # ============================================================
    # Scene 3: 暧昧 (餐桌近景, 同图)
    # ============================================================
    "散场的时候我特意多留了一会儿，想要找个机会和她搭讪。"
    "我这个人是没有任何技巧的，就是寒暄说她出落得好漂亮，有一双白白的大长腿。"
    "这话听起来有点轻佻，实则我是词穷而已。"
    "她听到这个话大概也是吃了一惊，但是没有特意的回避我。"
    "我还是找机会把她送到了楼下。"
    with Pause(1.0)

    show lx shy at right zorder 2
    with dissolve

    "她站在餐桌边上，暖黄灯光落在她脸上。"
    "风把大衣下摆吹动了一下，红色发卡滑了一下，碰到耳朵上方的发丝。"
    with Pause(1.0)

    "她看着我。我看着她。我们站在那几秒钟里，谁都没说话。"
    "身边有人来来去去，打车的声音、告别的声音、初冬的风声混在一起，"
    "可那几秒钟里我什么都听不见。"
    with Pause(1.0)

    # 内心独白 cue (D 项 - 增强代入感)
    "（我想……算了，就这样吧。）"
    with Pause(0.5)

    # 暧昧对话 (核心)
    "我脑子一热，话就冲出口了。"
    "「你……腿真长，还白。」"
    with Pause(1.0)

    "话一出口我就想抽自己。这是什么鬼夸奖，轻佻得像在调戏。"
    "我尴尬地站着，不敢看她的眼睛。"
    with Pause(0.5)

    "但她没躲。她反而轻轻笑了一下，眼尾微微弯起来，"
    "声音轻轻的，带着点说不清的意味。"

    show lx smile at right zorder 2
    with dissolve

    # 保留核心暧昧台词
    lx "……那你多看几眼。"
    with Pause(1.0)

    "我愣住了。风从程庄路那边吹过来，她额前的碎发被吹乱了，"
    "她伸手去拢，那枚红色发卡在灯光下滑了一下。"
    "我想接话，但舌头像打了结，什么都说不出来。"
    with Pause(1.0)

    "她笑了一下，把围巾裹紧，朝我摆了摆手。"

    show lx sweet_smile at right zorder 2
    with dissolve

    lx "那我走了。"
    "「嗯。路上小心。」"
    with Pause(1.0)

    # ============================================================
    # Scene 4: 离去 (公交站)
    # ============================================================
    scene bg bus_stop
    with fade

    # LX 离场
    hide lx
    with dissolve

    with Pause(0.5)

    "然后她钻进车里，车门关上。"
    with Pause(0.8)

    # 视觉锚点：车尾灯红线
    "车尾灯在深蓝色夜色里拉成一条红线，慢慢弯过街角，消失了。"
    with Pause(1.0)

    "我站在路边，北京十月的风吹得我耳朵发冷。"
    with Pause(0.8)

    "「有缘就会再见面的」"
    with Pause(0.5)

    # 视觉锚点：路灯雨丝 + 远处公交车
    "路灯把雨丝照成斜线。远处一辆公交车慢慢驶来。"
    with Pause(1.0)

    "我小声念了一句，然后转身，朝着公交的方向慢慢走去。"
    "初冬下起了小雨。"
    with Pause(2.0)

    # ============================================================
    # 结束
    # ============================================================
    scene black
    with dissolve

    centered "{size=+10}—— 落日和明天 ——{/size}"
    with Pause(2.0)

    "[[END OF ACT 1]]"
    with Pause(1.5)

    $ act1_complete = True
    $ current_location = "bus_stop"
    return
