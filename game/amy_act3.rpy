# Amy POV 第二章。括号内为待补的真实内容。
image amy_autumn_bar = Transform("images/backgrounds/act3/amy_autumn_bar.png", size=(1920, 1080))
image amy_autumn_entrance = Transform("images/backgrounds/act3/amy_autumn_entrance.png", size=(1920, 1080))
image amy_autumn_counter = Transform("images/backgrounds/act3/amy_autumn_counter.png", size=(1920, 1080))
image amy_autumn_booth = Transform("images/backgrounds/act3/amy_autumn_booth.png", size=(1920, 1080))
image amy_autumn_street = Transform("images/backgrounds/act3/amy_autumn_street.png", size=(1920, 1080))
image amy_autumn_car = Transform("images/backgrounds/act3/amy_autumn_car.png", size=(1920, 1080))
image amy_autumn_ami = Transform("images/characters/ami/amy_autumn_sweater.png", ysize=900, fit="contain")
image amy_autumn_jack = Transform("images/characters/jack/amy_autumn_jacket.png", ysize=900, fit="contain")

image amy_autumn_invite_chat = Transform(Composite(
    (576, 1280),
    (0, 0), "amy_private/autumn_invite.jpg",
    (16, 148), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 223), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 373), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 523), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 701), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 851), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 926), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (16, 1076), Transform("amy_chat_avatar_jack", size=(61, 61)),
    (499, 298), Transform("amy_chat_avatar_ami", size=(61, 61)),
    (499, 448), Transform("amy_chat_avatar_ami", size=(61, 61)),
    (499, 598), Transform("amy_chat_avatar_ami", size=(61, 61)),
    (499, 776), Transform("amy_chat_avatar_ami", size=(61, 61)),
    (499, 1001), Transform("amy_chat_avatar_ami", size=(61, 61)),
), crop=(0, 133, 576, 755), ysize=960, fit="contain")

image amy_autumn_plan_chat = Transform(Composite(
    (623, 1280),
    (0, 0), "amy_private/autumn_plan.jpg",
    (17, 9), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 171), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 364), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 445), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 526), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 607), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 907), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (17, 1056), Transform("amy_chat_avatar_jack", size=(66, 66)),
    (540, 90), Transform("amy_chat_avatar_ami", size=(66, 66)),
    (540, 283), Transform("amy_chat_avatar_ami", size=(66, 66)),
    (540, 757), Transform("amy_chat_avatar_ami", size=(66, 66)),
    (540, 1206), Transform("amy_chat_avatar_ami", size=(66, 66)),
), ysize=960, fit="contain")

label amy_act3:
    scene black
    with fade
    centered "第二章\n今晚的月色好美"

    if renpy.loadable("amy_private/autumn_invite.jpg"):
        narrator "后来，他告诉我，他喝了我送他的那瓶兔子酒。"
        scene black
        show amy_autumn_invite_chat at truecenter
        with dissolve
        pause

    if renpy.loadable("amy_private/autumn_plan.jpg"):
        scene black
        show amy_autumn_plan_chat at truecenter
        with dissolve
        pause

    call amy_act3_bar
    call amy_act3_moon
    call amy_act3_car

    scene black
    with fade
    centered "待续"
    return

label amy_act3_bar:
    scene amy_autumn_entrance
    with dissolve
    narrator "那是这个月我们第一次一起出去喝酒。Jack 花了心思，找了一家入口藏在书柜后面的酒吧。"
    narrator "【待确认：我看到书柜入口时的反应。】"

    scene amy_autumn_bar
    with dissolve
    narrator "那天晚上，我们喝了很多酒。"

    scene amy_autumn_counter
    with dissolve
    narrator "我们聊了很多，最后聊到人生哲学。"
    narrator "【待补：最初聊的话题和酒吧里的真实对白。】"

    scene amy_autumn_booth
    show amy_autumn_ami at amy_ami_foreground
    show amy_autumn_jack at right
    with dissolve
    narrator "我一直在等他抱我一下，或者牵我的手。可他一直没有。"
    return

label amy_act3_moon:
    scene amy_autumn_street
    with dissolve
    narrator "从酒吧出来，我们走在奥克兰的街上。那晚的月亮又圆又大。"
    show amy_autumn_ami at amy_ami_foreground
    show amy_autumn_jack at right
    with dissolve
    ami "今晚的月色好美。"
    narrator "Jack 把手放到我背后，我们一起走到车边。"
    return

label amy_act3_car:
    scene amy_autumn_car
    with dissolve
    narrator "我们坐在车里，看着月光。那是我们的第一个吻。"
    narrator "【待补：初吻前后的原话和我当时的感受。】"
    return
