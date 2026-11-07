# Amy POV 第一章，对应原版 Act 2。
init python:
    build.classify("game/amy_private/**", None)

image amy_chat_avatar_jack = Composite(
    (570, 570),
    (0, 0), Solid("#354660", xysize=(570, 570)),
    (0, 0), Transform("images/characters/jack/jack_black_tshirt.png", crop=(225, 55, 570, 570)),
)
image amy_chat_avatar_ami = Composite(
    (265, 265),
    (0, 0), Solid("#385952", xysize=(265, 265)),
    (0, 0), Transform("images/characters/ami/ami_smile.png", crop=(185, 48, 265, 265)),
)

image amy_dinner_chat = Transform(Composite(
    (725, 1280),
    (0, 0), "amy_private/dinner.png",
    (19, 84), Transform("amy_chat_avatar_jack", size=(80, 80)),
    (19, 215), Transform("amy_chat_avatar_jack", size=(80, 80)),
    (19, 788), Transform("amy_chat_avatar_jack", size=(80, 80)),
    (628, 309), Transform("amy_chat_avatar_ami", size=(80, 80)),
    (628, 404), Transform("amy_chat_avatar_ami", size=(80, 80)),
    (628, 882), Transform("amy_chat_avatar_ami", size=(80, 80)),
    (628, 976), Transform("amy_chat_avatar_ami", size=(80, 80)),
    (628, 1150), Transform("amy_chat_avatar_ami", size=(80, 80)),
), ysize=960, fit="contain")
image amy_after_dinner_chat = Transform(Composite(
    (576, 1030),
    (0, 0), "amy_private/after_dinner.png",
    (14, 76), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 151), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 255), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 532), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 608), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 682), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (14, 757), Transform("amy_chat_avatar_jack", size=(65, 65)),
    (498, 393), Transform("amy_chat_avatar_ami", size=(65, 65)),
    (498, 895), Transform("amy_chat_avatar_ami", size=(65, 65)),
), ysize=960, fit="contain")

image amy_restaurant_interior = Transform("images/backgrounds/act2/amy_restaurant_interior.jpg", size=(1920, 1080))
image amy_driving_sunset = Transform("images/backgrounds/act2/amy_driving_sunset.jpg", size=(1920, 1080))
image amy_jack_black_tshirt = Transform(amy_jack_with_cross("images/characters/jack/jack_black_tshirt.png"), ysize=940, fit="contain")
image amy_jack_black_tshirt thoughtful = Transform(amy_jack_with_cross("images/characters/jack/jack_black_tshirt_thoughtful.png"), ysize=940, fit="contain")
# Frame the full-body Ami artwork at the same portrait scale as Jack.
image amy_ami smile = Transform("images/characters/ami/ami_smile.png", crop=(90, 0, 470, 680), zoom=1.4)
image amy_ami surprised = Transform("images/characters/ami/ami_surprised.png", crop=(90, 0, 470, 680), zoom=1.4)
image amy_ami soft_smile = Transform("images/characters/ami/ami_soft_smile.png", crop=(90, 0, 470, 680), zoom=1.4)

transform amy_ami_foreground:
    xalign 0.05
    yalign 1.0

transform amy_jack_lean:
    xalign 1.0
    yalign 1.0
    ease 0.35 xalign 0.94

label amy_act2:
    scene black
    play music "audio/bgm/bgm_act2_1.ogg" loop fadein 2.0
    with fade

    centered "第一章\n穿越时空的见面"
    call amy_wechat_unlock
    centered "{size=+10}一见如故旧，丝麟酌流霞。{/size}"

    scene amy_driving_sunset
    with dissolve

    narrator "下了班，我开车从 City 出发。在路上，我一直在想等会儿要见的那个人。"

    narrator "我们十三年前就认识了。可这么多年，他一直是我微信里的一个陌生朋友。"

    narrator "他的朋友圈总是很有意思。大概十年前吧，他还给我发过一个很好玩的表情，可怕吗，他问我。"

    narrator "三年前的一个深夜，他发现我居然还没删他，一时兴起就给我打了个语音电话。"

    narrator "没想到，我们一聊就聊了很久。接下来几天，又像什么都没发生过。"

    narrator "又过了半年，同样的剧情又一次毫无预兆的发生， 他给我发信息说他说他失败了- 我只是感觉孤独而已。 恍然若梦。"

    narrator "我们聊了很久很久。我不知道他记住了多少，但他跟我说过的话，我基本都记得。他是个有趣且戏剧化的人。我愿意听他讲话，不着边际的有趣。"

    narrator "这次见面本来不在我的计划里。可我也说不上为什么，有点期待见到他。"

    narrator "心跳有点快。夕阳照在脸上，有点发烫。"

    narrator "就快到了吧？我可不想迟到。"

    narrator "从skywiki论坛上看见他发的贴子加上他到现在已经十多年了。"

    narrator "这十多年里，我换了三份工作，搬了好几次家。可我一次也没见过他。"

    narrator "我转头望向车窗外，一时说不清自己在等什么。"

    narrator "隔着餐厅的玻璃，烛光轻轻晃着，映出一片片彩色的光斑。"

    narrator "一家典型的新西兰意大利餐厅。就是我们之前选的那家。"

    narrator "他说要请我吃饭。我没想到，他真的会请我吃饭。"

    narrator "我从来没想过，我真的会见到他。"

    if amy_ch2_wechat_unlocked and renpy.loadable("amy_private/dinner.png"):
        scene black
        show amy_dinner_chat at truecenter
        with dissolve
        pause

    $ amy_v11_ambience("bar")
    scene amy_restaurant_interior
    with dissolve

    narrator "我在桌边坐下，环顾四周。这才想起来，上一次和朋友来这家餐厅，我们坐的也是这张桌子。"

    narrator "这一次，我在等一个从来没见过，却觉得很熟悉的人。"

    narrator "那天公司庆祝 Saint Patrick’s Day，我穿了那条深绿色的裙子。领口有点低，趁 Jack 还没来，我特意往上拉了拉。毕竟都是中国人嘛。"

    $ amy_v11_cue("step", .34)
    narrator "忽然有个男生从门口走进来，穿着黑色 T 恤和牛仔裤。我一眼就认出了他。"
    show amy_jack_black_tshirt at right
    with dissolve

    narrator "我站起来，挥手， Hi 这里！。"
    show amy_ami smile at amy_ami_foreground
    with dissolve
    ami "你好。"
    narrator "我想给他一个热情的拥抱，结果跟他握了个手。好官方哦。"

    narrator "他和照片上看起来差别不大。他盯着我，眼睛很亮。"
    jack "终于见到了。"
    ami "是啊，终于见到了。"
    jack "其实我早就到了，我一直在外面。"

    narrator "坐下来以后，我点了一杯鸡尾酒。我喜欢鸡尾酒。"

    narrator "为了这顿饭，我还特地带了一瓶我最喜欢的兔子白葡萄酒，想送给 Jack。我知道他爱喝酒，也希望他喜欢我挑的这一瓶。"

    narrator "我看着坐在对面的人。他也仔细地看着我，目光很坚定的样子。"

    narrator "他开始跟我讲事业上的事。我突然打断他。"
    show amy_ami surprised
    show amy_jack_black_tshirt thoughtful
    with dissolve
    ami "你还记得我们是怎么认识的吗？"
    jack "哦哦，我记得。那时候是 homestay 介绍的一个女生朋友，她说 Ami 也在惠灵顿。"

    narrator "我微笑着看他。听到这里，我就知道他完全不记得了。我还是等他把故事讲完。"
    show amy_ami soft_smile
    with dissolve
    ami "你确定是这样子的吗？"
    jack "我确定。"

    narrator "我也不知道他是临时编出了这么一段故事，还是他脑海里真有这么一个人。可我们俩是怎么认识的，我记得很清楚。并不是他说的这样"

    narrator "听着他一直说话我有那么一瞬间在想，要是我们当时就见了面，现在的人生会不会有一点不一样？"

    narrator "如果我们在 2013 年就见了面，现在至少会是很好的朋友吧。"

    narrator "Jack 开始讲他在上海的故事。"
    show amy_jack_black_tshirt at amy_jack_lean

    narrator "我把手撑在桌上，仔细听他讲。他讲得很有热情，整个人都透着一股劲儿。人讲到自己热爱的事，身上确实会发光。"

    narrator "说话的时候，他一直看着我的脸，我往下拉了一下裙子，他眼睛没从我脸上移开过。我想，他应该是个很绅士的人。至少表面上"

    narrator "Jack用词很有意思，常常会用一个我没想到的词，挺有戏剧感的。有那么一瞬间，我觉得他好像是从武侠世界里走出来的人。这个念头一闪就过去了。"

    narrator "我隐约的感觉到他很聪明，有很多很deep东西。我已经很久没跟这么聪明的人聊天了。心里是欢喜的。"

    narrator "我们点的披萨上来了，接着是意大利面。我就喜欢吃 creamy 的意大利面。"

    narrator "奶油热量很高，酒的热量也很高。可开心最重要嘛，我觉得今天很开心。"

    narrator "Jack滔滔不绝，我一直听。我想，这个男生的 MBTI 应该跟我很搭吧。我不太爱讲话"
    show amy_ami surprised
    show amy_jack_black_tshirt thoughtful
    with dissolve
    ami "你测过 MBTI 吗？"
    jack "没测过。我不信那个。"
    narrator "我在心里猜，他应该是 ENTP。"

    narrator "吃完饭，我还在想，聊这么开心，他会不会请我再喝一杯？可他好像赶着回去，很快就出了餐厅。"

    $ amy_v11_ambience("street")
    $ amy_v11_cue("step", .37)
    scene bg_street_evening
    show amy_ami soft_smile at amy_ami_foreground
    show amy_jack_black_tshirt at right
    with dissolve

    narrator "我的车就停在餐厅旁边。我们并肩走在那条不太宽的马路上。太阳还没落山，天还有一点亮。时间明明还很早"

    narrator "我把酒递给他。他好像没想到我会带礼物，看起来挺开心的。"

    narrator "他送我到车边。我问他车停在哪儿，他说就在后面。"
    jack "想走一下，还是直接回家？"

    narrator "其实我还想跟他再聊一会儿。可他看起来有点匆忙，我也不知道他是不是还有下一场。"
    ami "那我先回去吧。谢谢你今天请我吃饭。很开心听你讲你的故事，希望你接下来一切都好。"
    jack "也祝你一切顺利。"

    hide amy_ami
    hide amy_jack_black_tshirt
    with dissolve
    $ amy_v11_ambience()
    $ amy_v11_cue("door", .38)
    narrator "我上了车，往北岸开。"

    narrator "我还会再见到他吗？"
    narrator "不知道。但至少下次见面，他就不再是个陌生人了。"

    if amy_ch2_wechat_unlocked and renpy.loadable("amy_private/after_dinner.png"):
        scene black
        show amy_after_dinner_chat at truecenter
        with dissolve
        pause

    stop music fadeout 2.0
    scene black
    with fade
    centered "{size=+10}一见如故旧，丝麟酌流霞。{/size}"
    centered "待续"
    return
