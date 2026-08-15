# 第一幕：惠灵顿机场的相遇
# Act 1: Meeting at Wellington Airport

# ====== 图片显式声明 ======
# 这些声明确保 lint 工具能识别所有用到的图片
# 实际图片文件位于 game/images/ 目录

# 背景图
image bg airport_terminal = "images/airport_terminal.png"
image bg airport_arrival = "images/airport_arrival.png"
image bg airport_cafe = "images/airport_cafe.png"
image bg airport_window = "images/airport_window.png"
image bg wellington_city = "images/wellington_city.png"

# 角色立绘 - 阿米
image ami normal = "images/ami normal.png"
image ami smile = "images/ami smile.png"
image ami surprised = "images/ami surprised.png"
image ami blush = "images/ami blush.png"
image ami thinking = "images/ami thinking.png"
image ami sad = "images/ami sad.png"

# 角色立绘 - 杰克
image jack normal = "images/jack normal.png"
image jack smile = "images/jack smile.png"
image jack surprised = "images/jack surprised.png"
image jack apologize = "images/jack apologize.png"
image jack thinking = "images/jack thinking.png"
image jack wave = "images/jack wave.png"

# CG 图
image cg airport_meet = "images/airport_meet.png"
image cg first_coffee = "images/first_coffee.png"
image cg ending_act1 = "images/ending_act1.png"

label act1_meeting:
    # 标记剧情进度
    $ act1_complete = True
    $ current_location = "wellington_airport"
    $ current_time = "afternoon"

    # ========== 场景1：黑屏开场 + 标题 ==========
    scene black
    with Pause(1.0)

    # 显示游戏标题
    "——《大康兔》——"
    "Act 1：惠灵顿机场的相遇"
    with Pause(2.0)

    # ========== 场景2：杰克视角的机场到达大厅 ==========
    # 背景：惠灵顿机场到达大厅
    # image: 机场到达大厅全景，落地窗外是阴天的惠灵顿
    scene bg airport_terminal
    with fade

    # 播放机场环境音
    play music "audio/music/bgm_airport.ogg" fadein 2.0

    # 旁白描述环境
    "惠灵顿国际机场，到达大厅。"
    "窗外是新西兰典型的灰色天空，海风从远处的库克海峡吹来。"
    "下午三点，我站在接机口的电子屏前，反复确认着航班信息。"

    # 显示杰克立绘
    # image: 杰克-普通表情，金发碧眼的本地大学生
    show jack normal at left
    with dissolve

    "我是杰克。维多利亚大学的学生，今天来机场是来接一个老朋友。"
    "（航班应该快到了吧……我看着手里的接机牌，上面写着歪歪扭扭的中文。）"
    "（希望他能看到……）"

    play sound "audio/sound/sfx_airport_announce.ogg"
    "广播里传来空乘的声音：'从新加坡经停奥克兰的航班SQ298已抵达……'"
    with Pause(1.5)

    # ========== 场景3：阿米出场 ==========
    play sound "audio/sound/sfx_footsteps.ogg"

    # 阿米推着行李车出现
    # image: 阿米-困惑表情，东亚面孔，疲惫但可爱
    show ami surprised at right
    with moveinright

    "我抬起头，看见一个亚洲面孔的女孩从出口走来。"
    "她推着一辆堆满行李的小车，正费力地张望着四周。"
    "一只手还举着手机，似乎在查地图。"

    "她看了我一眼，又看了看我手里的接机牌，眉头轻轻皱起。"

    # 阿米说话
    am "Excuse me..."

    "（声音有点轻，像是怕打扰到别人。）"

    am "...那个，请问这里到市中心怎么走？"

    # ========== 场景4：第一次选择 ==========
    # 杰克的内心独白
    "（等等，她是在问路吗？）"
    "（可是我的接机牌写的是中文名字啊……）"
    "（算了，反正航班也快到了，先帮帮她吧。）"

    menu:
        "怎么帮她？"

        "热情地告诉她路线":
            $ ami_love += 2
            jk "当然可以！你要去哪里？我可以告诉你怎么坐车。"
            show ami smile at right
            with dissolve
            am "真的？太感谢了！我是第一次来惠灵顿……"
            jump act1_help_route

        "问她是不是也在等人":
            $ ami_love += 1
            jk "你好！你是……也在等人吗？"
            show ami thinking at right
            with dissolve
            am "啊？我、我在找路……"
            jump act1_help_route

        "直接带她去机场咨询台":
            $ jack_love += 1
            jk "我带你去那边的咨询台吧，他们有详细地图。"
            show ami normal at right
            with dissolve
            am "好、好的！谢谢你！"
            jump act1_help_luggage


    # ========== 分支A：帮她问路 / 寒暄后 ==========
    label act1_help_route:
        "我正要回答，一个行李箱从行李车上滑了下来。"
        play sound "audio/sound/sfx_luggage_drop.ogg"

        show ami surprised at right
        with hpunch

        am "啊——！"

        "她的行李箱砸在地上，里面的东西散落了出来。"

        menu:
            "怎么办？"

            "立刻蹲下来帮她捡":
                $ ami_love += 3
                $ helped_with_luggage = True
                jk "别担心，我帮你！"
                jump act1_pick_luggage

            "先稳住她，再慢慢捡":
                $ ami_love += 1
                jk "没伤到吧？我来帮你。"
                jump act1_pick_luggage

    # ========== 分支B：直接带她去咨询台 ==========
    label act1_help_luggage:
        "我们刚要转身，她的行李箱滑了一下。"
        play sound "audio/sound/sfx_luggage_drop.ogg"
        show ami surprised at right
        with hpunch

        am "啊——！我的行李……！"

        menu:
            "怎么办？"

            "立刻蹲下来帮她捡":
                $ ami_love += 3
                $ helped_with_luggage = True
                jk "别担心，我帮你捡！"
                jump act1_pick_luggage

            "先稳住她，再慢慢捡":
                $ ami_love += 1
                jk "没伤到吧？慢慢来。"

    # ========== 共同剧情：捡行李 ==========
    label act1_pick_luggage:
        "我蹲下身，开始帮她捡散落的物品。"
        "一盒新加坡的肉骨茶调料、一本英文小说、一件毛衣……"

        show ami blush at right
        with dissolve

        am "真、真的很抱歉！给你添麻烦了……"

        jk "没关系，反正我也在等人。"
        jk "你是从哪里飞来的？"

        am "新加坡……转机过来的。"
        am "我是来惠灵顿读书的，Victoria University。"

        jk "（等等，Victoria University？）"

        "我愣了一下，然后笑了出来。"

        jk "哈哈，这么巧？我也是 Victoria University 的！"
        jk "我叫杰克，大三。"

        am "真、真的吗？！"

        show ami smile at right
        with dissolve

        am "我叫阿米，Ami。研究生新生。"
        am "请多关照！"

        $ met_at_airport = True
        $ player_name = "杰克"

    # ========== 场景5：咖啡馆 ==========
    # 我们已经互相认识了，但我的朋友还没来
    jk "对了，你刚下飞机一定累了吧？"
    jk "要不要先去机场的咖啡店坐一下？"
    jk "我朋友还要一会儿才到，我可以陪你等。"

    show ami thinking at right
    with dissolve

    am "这样……不会打扰你吗？"

    jk "完全不会！我也是自己一个人。"

    am "那……那好吧。谢谢你，杰克。"

    # 切换背景：机场咖啡店
    # image: 机场咖啡店，落地窗，海景
    scene bg airport_cafe
    show ami smile at right
    with fade

    play music "audio/music/bgm_daily.ogg" fadein 1.5

    "我们坐在窗边，两杯咖啡冒着热气。"
    "窗外，云层渐渐散开，阳光洒在海面上。"

    play sound "audio/sound/sfx_cup.ogg"
    am "（吹了吹咖啡）……"
    am "杰克，我可以问你一件事吗？"

    jk "当然。"

    show ami thinking at right
    with dissolve

    am "你……为什么一开始会注意到我？"
    am "我是说，这里有那么多人。"

    "（为什么呢？我想了想。）"

    menu:
        "为什么注意到她？"

        "因为她的行李快倒了":
            $ ami_love += 1
            jk "说真的，因为我看到你的行李快倒了。"
            jk "总不能看着它砸到你脚上吧？"
            show ami blush at right
            with dissolve
            am "原、原来是这样……"
            am "（脸有点红）"

        "因为她看起来是亚洲人":
            $ jack_love += 1
            jk "可能因为……看到亚洲面孔比较亲切？"
            jk "我也认识一些亚裔朋友。"
            show ami normal at right
            with dissolve
            am "这样啊……"

        "因为她的眼神很特别":
            $ ami_love += 2
            jk "嗯……可能是因为你的眼神？"
            jk "看起来有点迷茫，又有点坚定。"
            jk "有点像……嗯，我也说不清。"
            show ami blush at right
            with dissolve
            am "（低下头）你、你真会说话……"

    $ shared_coffee = True

    # ========== 场景6：命运的巧合 ==========
    "我们聊了聊各自的家乡、喜欢的音乐、还有对新西兰的期待。"

    show ami smile at right
    with dissolve

    am "说起来，我来之前查了很多惠灵顿的资料。"
    am "都说这里风很大，是真的吗？"

    jk "哈哈，是真的。'Windy Wellington'可不是白叫的。"
    jk "你今天运气不错，风不算大。"

    am "那我以后一定要买一件很厚的外套……"

    # 杰克突然想到什么
    jk "对了！"
    jk "你是研究生新生的话，应该需要人带你去校园吧？"
    jk "如果你不介意，我可以……"

    # 杰克的手机突然响了
    play sound "audio/sound/sfx_camera.ogg"  # 模拟手机铃声

    "我的手机响了。屏幕上显示：'Mike'。"

    jk "啊，我的朋友到了！抱歉，我要去接他一下。"

    show ami sad at right
    with dissolve

    am "嗯，没关系……"

    jk "你在这里等我一下？我马上回来！"
    jk "然后我送你到机场大巴站。"

    am "好、好的。"

    "（我匆匆跑向出口，心里想着：希望她还在那里。）"

    # ========== 场景7：尾声 ==========
    # 5分钟后，杰克带着朋友回来
    scene bg airport_window
    with fade

    "我带着朋友 Mike 回到咖啡店。"
    "阿米还在窗边坐着，阳光打在她的侧脸上。"

    show ami smile at right
    with dissolve

    am "杰克！这边！"

    "我向 Mike 介绍：'这是阿米，Victoria University 的研究生新生。'"

    "Mike 坏笑了一下：'哦？刚才还说要我快点过来，原来是急着见人呢。'"

    show ami blush at right
    with dissolve

    am "（脸红）你、你别乱说……"

    jk "Mike！你够了。"

    # ========== 场景8：第一幕结束 ==========
    scene bg wellington_city
    with dissolve

    "我们一起送阿米去了机场大巴站。"
    "临别时，她从包里拿出一盒肉骨茶调料。"

    show ami smile at right
    with dissolve

    am "这个……送给你。"
    am "谢谢你今天帮我。"
    am "如果……如果以后有机会的话，我请你吃饭。"

    jk "那我们互相留个联系方式吧。"

    am "嗯！"

    "我看着她走上大巴，车门关闭，缓缓驶出站台。"
    "她透过车窗向我挥了挥手。"

    play music "audio/music/bgm_romantic.ogg" fadein 2.0

    "（大康兔的第一次相遇，就这样结束了。）"
    "（但不知道为什么，我觉得……）"
    "（这不是最后一次见面。）"

    # 显示第一幕结束画面
    # image: 第一幕结束CG
    scene cg ending_act1
    with Dissolve(2.0)

    "——Act 1：完——"
    with Pause(3.0)

    # 自动存档
    $ renpy.save("act1_end", extra_info="第一幕结束")

    # 返回主菜单或继续第二幕
    return


# 第一幕结束后的入口
label after_act1:
    "你已经完成了第一幕。"
    "是否继续第二幕？"
    return
