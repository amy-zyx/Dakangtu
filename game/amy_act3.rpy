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


default amy_ch2_affection = 0
default amy_ch2_trust = 0
default amy_ch2_intellectualBond = 0
default amy_ch2_curiosity = 0
default amy_ch2_drinkChoice = None
default amy_ch2_worldChoice = None
default amy_ch2_bookshelfChoice = None
default amy_ch2_inspectedClues = []
default amy_ch2_doorOpened = False
default amy_ch2_chapter2Completed = False

image amy_ch2_tesla_sunset = Transform("images/cg/act3/amy_ch2_tesla_sunset.png", size=(1920, 1080))
image amy_ch2_bar_dim = Transform("images/backgrounds/act3/amy_autumn_bar.png", size=(1920, 1080), matrixcolor=BrightnessMatrix(-0.18))

screen amy_ch2_clues():
    default detail = "先观察一下吧。"
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1500
        padding (60, 45)
        vbox:
            spacing 28
            text "调查书柜" size 52 xalign 0.5
            text "这是游戏内虚构的机关。点选一处调查，再决定怎么做。" size 30
            for key, title, clue in [
                ("book", "旧书", "一本书的书脊比其他书干净，似乎经常被人碰触。"),
                ("clock", "挂钟", "挂钟停在 8:08。Jack：也许这只是没换电池。"),
                ("glass", "酒杯", "书柜旁有一只空酒杯，杯底压着一张写有星星符号的纸。")
            ]:
                textbutton (title + ("（已调查）" if key in amy_ch2_inspectedClues else "")):
                    action [AddToSet(amy_ch2_inspectedClues, key), SetScreenVariable("detail", clue)]
                    text_size 40
                    xfill True
                    yminimum 90
            text detail size 32
            textbutton "决定怎么做" action Return() text_size 40 xalign 0.5

# Shared 900 x 1080 portrait canvases keep expression changes anchored.
# Similar head scale, with Jack's crown about 130 pixels above Amy's.
# Extended Jack portraits continue below the viewport instead of ending at his waist.
# All Amy expressions use dedicated detailed portraits, reduced rather than enlarged.
image amy_ch2_ami smile = Composite(
    (900, 1080),
    (99, 181), Transform("images/characters/ami/amy_ch2_smile_hd.png", zoom=0.65),
)
image amy_ch2_ami tease = Composite(
    (900, 1080),
    (99, 181), Transform("images/characters/ami/amy_ch2_tease_hd.png", zoom=0.65),
)
image amy_ch2_ami thoughtful = Composite(
    (900, 1080),
    (144, 204), Transform("images/characters/ami/amy_ch2_thoughtful_hd.png", zoom=0.6),
)

image amy_ch2_jack laugh = Composite(
    (900, 1080),
    (149, 66), Transform("images/characters/jack/amy_ch2_laugh_extended.png", zoom=0.68),
)
image amy_ch2_jack curious = Composite(
    (900, 1080),
    (149, 66), Transform("images/characters/jack/amy_ch2_curious_extended.png", zoom=0.68),
)
image amy_ch2_jack thoughtful = Composite(
    (900, 1080),
    (149, 66), Transform("images/characters/jack/amy_ch2_thoughtful_extended.png", zoom=0.68),
)

label amy_act3:
    $ amy_ch2_migrate()
    show screen amy_ch2_status
    scene black
    with fade
    centered "第二章\n你眼中的宇宙"
    play music "audio/bgm/bgm_act2_1.ogg" fadein 2.0

label amy_ch2_scene_1:
    scene amy_ch2_tesla_sunset
    with dissolve
    narrator "那是我们第一次约好单独出去喝酒。"
    narrator "Jack 开着车，我坐在副驾驶。"
    narrator "夕阳透过车窗，落在他的侧脸上。"
    narrator "他一路都在说话。"
    narrator "说一些我记不清的话题，一件接着一件。"
    narrator "奇怪的是，我平时并不是一个喜欢听别人滔滔不绝的人。"
    narrator "可那天，我一点也不觉得吵。"
    jack "……所以我就觉得，这事儿特别离谱，你说是不是？"
    ami "嗯。"
    jack "你到底有没有在听？"
    ami "有啊。"
    jack "那我刚才说什么了？"
    ami "你说了一件特别离谱的事。"
    narrator "他笑起来真好看。"
    narrator "我以前从来不知道，一个人的眼睛里，真的可以有星河。"
    narrator "不是形容词。"
    narrator "是当他转过头看我的那一瞬间，我真的觉得，那里有一个宇宙。"
    narrator "深不见底，又闪闪发亮。"
    narrator "我想多看一会儿。"
    narrator "再多看一会儿。"
    jack "你老看我干什么？"
    ami "看你开车啊。"
    jack "我开车有什么好看的？"
    ami "你认真开车的样子比较好看。"
    jack "那我平时不好看？"
    ami "你话好多。"
    narrator "我没有告诉他。"
    narrator "其实我更喜欢他笑起来的样子。"
    narrator "那时候，我还不知道自己会有多喜欢这个人。"
    narrator "只觉得，如果这条路能再长一点，就好了。"
    jump amy_ch2_scene_2

label amy_ch2_scene_2:
    scene amy_autumn_bar
    with dissolve
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "喝什么？"
    ami "我看看 Cocktail Menu。"
    jack "你又喝 Cocktail？"
    ami "怎么啦？"
    jack "别人出去喝酒，拿瓶啤酒就完事儿了。你到哪里都要点 Cocktail。"
    ami "Cocktail 好喝呀。"
    show amy_ch2_jack laugh at right
    with dissolve
    jack "Fancy lady."
    ami "Thank you. I'll take that as a compliment."
    ami "这个我喜欢……这个也不错。哎，这个没喝过。"
    jack "你是来喝酒还是来做实验的？"
    ami "都可以啊。"
    jack "你不会想把菜单喝一遍吧？"
    ami "也不是不行。"
    narrator "我喜欢 Cocktail。"
    narrator "喜欢不同的颜色、味道，还有每杯酒背后的名字。"
    narrator "而 Jack 好像更喜欢看我选酒。"
    jack "有一种酒，你最好别喝。"
    show amy_ch2_ami thoughtful at amy_ami_foreground
    with dissolve
    ami "什么？"
    jack "Gin。"
    ami "为什么？"
    jack "Gin 会让人流眼泪。"
    ami "真的吗？"
    jack "真的。"
    ami "可是我喝酒不会哭。"
    jack "你确定？"
    ami "要不试试看？"
    show amy_ch2_jack laugh at right
    with dissolve
    jack "你还真是什么都想试啊。"
    ami "总得试过才知道。"
    narrator "他大概还不知道。"
    narrator "我对很多事情都是这样。"
    narrator "不太相信别人告诉我的答案。"
    narrator "我喜欢自己去寻找。"
    narrator "包括眼前这个人。"
    menu:
        "让 Jack Surprise Me":
            ami "这杯你帮我选。"
            jack "这么相信我？"
            ami "只是想看看，你有多了解我。"
            show amy_ch2_jack laugh at right
            with dissolve
            jack "那我可得认真一点。"
            narrator "有时候，把一点点选择权交给喜欢的人，也是一种试探。"
            $ amy_ch2_choices["cocktail"] = "surprise"
            $ amy_ch2_award_once("cocktail", "love", 10)
            $ renpy.force_autosave()
        "点 Gin，看看自己会不会流泪":
            ami "我想试试 Gin。"
            jack "不是说了会流泪吗？"
            ami "我喝酒不会哭。别人说的不算，我想自己试试。"
            jack "你还真是什么都想验证。"
            show amy_ch2_ami tease at amy_ami_foreground
            with dissolve
            ami "当然。"
            narrator "我喜欢亲自寻找答案。连眼泪这种事，也一样。"
            $ amy_ch2_choices["cocktail"] = "gin"
            $ amy_ch2_award_once("cocktail", "wisdom", 10)
            $ renpy.force_autosave()
        "点平常喜欢的 Cocktail":
            ami "我还是点我平常喜欢的那杯。"
            jack "不试试新的吗？"
            ami "今天已经有很多新鲜事了。熟悉的味道也可能带来惊喜。"
            jack "Fancy lady 还有自己的原则。"
            narrator "并不是每一种冒险，都需要从酒杯开始。"
            $ amy_ch2_choices["cocktail"] = "favorite"
            $ amy_ch2_award_once("cocktail", "luck", 10)
            $ renpy.force_autosave()
    jump amy_ch2_scene_3

label amy_ch2_scene_3:
    scene amy_ch2_bar_dim
    with dissolve
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "我给你讲个鬼故事。"
    ami "好啊。"
    jack "有一个人，半夜坐电梯。"
    ami "嗯。"
    jack "电梯到了一层，门打开了。门口站着两个人。"
    ami "然后呢？"
    jack "那两个人一直盯着电梯里面看，就是不进来。"
    ami "为什么？"
    jack "电梯里的人就问，你们进不进来啊？"
    pause 0.7
    jack "那两个人说——"
    jack "你怎么这么慢啊？"
    jack "可是……"
    jack "他们眼里的电梯，是空的。"
    pause 0.7
    ami "……就这？"
    jack "不恐怖吗？"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "好恐怖哦。"
    jack "你这表情一点都不恐怖。"
    ami "我已经吓死了。"
    show amy_ch2_jack curious at right
    with dissolve
    jack "你这人怎么这么难撩？"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "你在撩我吗？"
    show amy_ch2_jack curious at right
    with dissolve
    jack "没有啊，我在讲鬼故事。"
    narrator "我当然知道他在做什么。"
    narrator "那些老掉牙的小套路。"
    narrator "讲鬼故事，制造气氛，故意停顿，等着女生害怕。"
    narrator "我最讨厌套路了。"
    narrator "可是……"
    narrator "我喜欢看他用套路对付我的样子。"
    narrator "明明知道他下一句要说什么，我还是想听。"
    narrator "不是因为故事好听。"
    narrator "是因为讲故事的人是他。"
    ami "还有吗？"
    jack "你不是不怕吗？"
    ami "不怕就不能听了？"
    jack "你到底喜欢听鬼故事，还是喜欢听我讲话？"
    pause 0.7
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "你猜。"
    narrator "我想，他可能开始发现了。"
    narrator "我不是那种他讲一个鬼故事，就会尖叫着躲到他怀里的女生。"
    narrator "但我也不是完全不吃他这一套。"
    narrator "因为我已经开始期待，他下一次会怎样逗我笑。"
    jump amy_ch2_bookshelf
