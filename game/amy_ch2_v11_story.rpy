# V11 authored dialogue, generated from Amy's supplied manuscript. Source line numbers aid review.


label amy_v11_start:
    $ amy_ch2_migrate()
    show screen amy_v11_status
    $ amy_v11_play_music("chapter")
    centered "第二章  你眼中的宇宙"
    call amy_wechat_unlock
    jump amy_v11_date1

label amy_v11_date1:
    call amy_v11_stage("drive", "date", actors=True)
    show screen amy_v11_status
    # source:37
    narrator "那是我们第一次约好单独出去喝酒。"
    # source:38
    narrator "Jack 开着车，我坐在副驾驶。"
    # source:39
    narrator "他一路都在讲话。从一件荒唐的小事，讲到世界怎么运转。"
    # source:40
    narrator "奇怪的是，我一点也不想打断他。"
    # source:42
    $ amy_v11_emote("jack", "curious")
    jack "你不觉得很多人活得很奇怪吗？"
    # source:43
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "哪里奇怪？"
    # source:44
    $ amy_v11_emote("jack", "thoughtful")
    jack "一边抱怨这个世界，一边又特别努力地适应它。仿佛适应得够好，就算赢了。"
    # source:45
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你觉得应该怎样？"
    # source:46
    $ amy_v11_emote("jack", "curious")
    jack "至少得试着改变点什么吧。马克思不是说过么，哲学家们只是用不同方式解释世界，问题在于改变世界。"
    # source:47
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那今晚呢？你想先从哪件小事开始？"
    # source:48
    $ amy_v11_emote("jack", "laugh")
    jack "先从不接受一杯难喝的酒开始。"
    # source:49
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好。我们就从一杯喜欢的酒开始。"
    # source:51
    narrator "他讲这些话的时候，眼睛会突然亮起来。"
    # source:52
    narrator "我第一次发现，一个人的眼睛里，原来真的可以有星河和宇宙。"
    # source:53
    narrator "我不是被他的理论说服了。我只是喜欢看他认真讲述自己相信的事情。"
    # source:55
    $ amy_v11_emote("jack", "laugh")
    jack "你在笑什么？"
    # source:56
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你讲话像在给电影配旁白。"
    # adapted from source:57 (Jack’s confirmed wording: 神圣启示)
    $ amy_v11_emote("jack", "curious")
    jack "你觉得，有些巧合会不会是一种神圣启示？"
    # source:58
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "什么？"
    # source:59
    $ amy_v11_emote("jack", "thoughtful")
    jack "有些事发生得太刚好，会让人想知道，那是不是在提醒自己什么。"
    # source:60
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "我也说不准。有些事是走过了，回头才看出意义。"
    # source:61
    $ amy_v11_emote("jack", "laugh")
    jack "我想起西西弗斯。石头不会给他答案，他却还是要过自己的日子。"
    # source:62
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "然后呢？"
    # source:63
    $ amy_v11_emote("jack", "smile")
    jack "然后他还是会推。至于为什么推，也许可以由他自己决定。"
    # source:64
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我喜欢这个想法。就算没得选，也还有一点是属于自己的。"
    # source:65
    $ amy_v11_emote("jack", "thoughtful")
    jack "我一直觉得，这世界像一部早就写完的戏。"
    # source:66
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "谁写的？"
    # source:67
    $ amy_v11_emote("jack", "curious")
    jack "神吧。一个什么都知道、什么都能安排的家伙。"
    # source:68
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你呢？你是演员？"
    # source:69
    $ amy_v11_emote("jack", "thoughtful")
    jack "演员至少还能挑剧本。我连剧本都看过了。"
    # source:70
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "如果看见的那一页不如你所愿，一定也不好受吧。"
    # source:71
    $ amy_v11_emote("jack", "curious")
    jack "是啊。我就是不明白，他既然有那么大的本事，为什么偏偏给我写成这样。"
    # source:72
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有些事发生了，连问一句为什么，都不知道该找谁。"
    # source:73
    $ amy_v11_emote("jack", "laugh")
    jack "对。我想找他谈谈，问问这到底是什么水平。"
    # source:74
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "如果真能见到他，我陪你问。今晚先让我陪你找个停车位吧。"
    # source:76
    narrator "他笑了。我又忍不住看他。"
    # source:77
    narrator "我喜欢他笑起来的样子。更喜欢他认真看向我的那一瞬间。"
    # source:78
    narrator "那时我还不知道，这双眼睛后来会让我想象出多少个世界。"
    jump amy_v11_date2

label amy_v11_date2:
    $ amy_v11_play_music("chapter")
    call amy_v11_stage("bar", "date", actors=True)
    show screen amy_v11_status
    # source:87
    $ amy_v11_emote("jack", "curious")
    jack "喝什么？"
    # source:88
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "Cocktail。先看看菜单。"
    # source:89
    $ amy_v11_emote("jack", "smile")
    jack "别人喝酒一瓶啤酒就解决了。你到哪儿都得研究 Cocktail。"
    # source:90
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "酒都喝了，为什么不喝点有意思的？"
    # source:91
    $ amy_v11_emote("jack", "smile")
    jack "Fancy lady."
    # source:92
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "Thank you. 我接受这个评价。"
    # source:100
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "这个紫色的挺漂亮。这个北极星也不错。"
    # source:101
    $ amy_v11_emote("jack", "smile")
    jack "你看酒单的样子像在挑一个新宇宙。"
    # source:102
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "每一杯都有自己的性格嘛。"
    # source:103
    $ amy_v11_emote("jack", "curious")
    jack "Gin 呢？"
    # source:104
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "怎么了？"
    # source:105
    $ amy_v11_emote("jack", "smile")
    jack "Gin 会让人流眼泪。"
    # source:106
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "谁说的？"
    # source:107
    $ amy_v11_emote("jack", "smile")
    jack "我说的。"
    # source:108
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那就不算证据。"
    # source:109
    $ amy_v11_emote("jack", "smile")
    jack "有些事不需要证据，经历一次就知道了。"
    # source:110
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "我喝酒可从来不哭。倒想看看它有什么本事。"
    # source:111
    $ amy_v11_emote("jack", "laugh")
    jack "你这人真有意思。"
    call screen amy_v11_drinks
    menu (screen="amy_v11_choice"):
        "让 Jack 选一杯 Surprise Me":
            # source:116
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "今天你来选。Surprise me."
            # source:117
            $ amy_v11_emote("jack", "curious")
            jack "你确定把决定权交给我？"
            # source:118
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "只是把这一杯交给你。别的还得看表现。"
            # source:119
            $ amy_v11_emote("jack", "smile")
            jack "那我选“莫拉之美”。名字听着温柔，颜色却像藏了点危险。"
            # source:120
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "这是在形容酒，还是形容我？"
            # source:121
            $ amy_v11_emote("jack", "curious")
            jack "你觉得呢？"
            # source:122
            narrator "我明明知道他在故意留白，却喜欢看他把话说到一半的样子。"
            call screen amy_v11_drink_closeup(0, "莫拉之美")
            $ amy_v11_choose("cocktail", "luck", 5, "让 Jack 选一杯 Surprise Me")
        "试试 Gin：Aviation":
            # source:126
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "我要一杯 Aviation。Gin 做的，对吧？"
            # source:127
            $ amy_v11_emote("jack", "curious")
            jack "对。你是非要验证一下？"
            # source:128
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "理论可以听，结论我自己下。"
            # source:129
            $ amy_v11_emote("jack", "smile")
            jack "那今晚就做个实验。"
            # source:130
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "实验对象是我，观察员是你。"
            # source:131
            $ amy_v11_emote("jack", "curious")
            jack "如果真的哭了呢？"
            # source:132
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "那也不能证明是 Gin 的问题。"
            # source:133
            $ amy_v11_emote("jack", "laugh")
            jack "行，你已经开始写论文了。"
            # source:134
            narrator "我不喜欢别人替我规定感受。包括一杯酒会不会让我流泪。"
            call screen amy_v11_drink_closeup(3, "Aviation")
            $ amy_v11_choose("cocktail", "wisdom", 10, "试试 Gin：Aviation")
        "点熟悉的 Creamy Panna Cotta":
            # source:138
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "还是 Panna Cotta 吧。我喜欢 Creamy 的。"
            # source:139
            $ amy_v11_emote("jack", "curious")
            jack "这么多没试过的，偏偏选熟悉的？"
            # source:140
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "冒险也得有个自己喜欢的起点。"
            # source:141
            $ amy_v11_emote("jack", "smile")
            jack "听着像一种生活哲学。"
            # source:142
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "也可能只是我想喝奶油味。"
            # source:143
            $ amy_v11_emote("jack", "laugh")
            jack "这解释更可信。"
            # source:144
            narrator "有时候好运不是撞上未知，而是刚好知道自己喜欢什么。"
            call screen amy_v11_drink_closeup(2, "潘纳科塔")
            $ amy_v11_choose("cocktail", "wisdom", 10, "点熟悉的 Creamy Panna Cotta")
    jump amy_v11_date3

label amy_v11_date3:
    call amy_v11_stage("bar", "date", actors=True)
    show screen amy_v11_status
    # source:154
    $ amy_v11_emote("jack", "smile")
    jack "我给你讲个鬼故事。"
    # source:155
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好啊。"
    # source:156
    $ amy_v11_emote("jack", "smile")
    jack "一个人，半夜独自坐电梯。"
    # source:157
    $ amy_v11_emote("jack", "smile")
    jack "电梯到了某一层，门打开。外面站着两个人。"
    # source:158
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。"
    # source:159
    $ amy_v11_emote("jack", "smile")
    jack "那两个人朝里面看了一眼，谁也没进。"
    # source:160
    $ amy_v11_emote("jack", "smile")
    jack "“哎呀，好挤啊。我们等下一班吧。”"
    # source:162
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "……"
    # source:163
    $ amy_v11_emote("jack", "curious")
    jack "你想想，他们看见的到底是什么？"
    # source:164
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你这是用一个电梯，把唯物主义送走了。"
    # source:165
    $ amy_v11_emote("jack", "laugh")
    jack "你不是说要自己验证吗？要不要半夜去坐一趟？"
    # source:166
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不要。实验也要考虑成本。"
    # source:167
    $ amy_v11_emote("jack", "smile")
    jack "看来理性还是有边界的。"
    # source:168
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我主要是怕你一路上再讲十个。"
    # source:170
    narrator "我知道他在制造气氛。停顿、压低声音、再等我反应。"
    # source:171
    narrator "这种套路，我本来最不喜欢。"
    # source:172
    narrator "但看他认真演完一个并不高明的鬼故事，我竟然觉得特别可爱。"
    # source:173
    narrator "不是故事有多恐怖。是他讲完以后，那副等着看我反应的样子。"
    # source:175
    $ amy_v11_emote("jack", "laugh")
    jack "你怎么还笑？"
    # source:176
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我在想，电梯里到底有多少人。"
    # source:177
    $ amy_v11_emote("jack", "curious")
    jack "这就是问题所在。你以为自己看到的，就一定是全部吗？"
    # source:178
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "笛卡尔式怀疑？"
    # source:179
    $ amy_v11_emote("jack", "smile")
    jack "也许。人连自己的感官都未必能完全相信，却总爱把看到的当成真相。"
    # source:180
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那至少我现在能确定一件事。"
    # source:181
    $ amy_v11_emote("jack", "curious")
    jack "什么？"
    # source:182
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你讲鬼故事的时候，表情特别丰富。"
    # source:183
    $ amy_v11_emote("jack", "laugh")
    jack "这倒是真的。"
    jump amy_v11_date4

label amy_v11_date4:
    call amy_v11_stage("bookshelf", "date", actors=True)
    show screen amy_v11_status
    # source:190
    narrator "后来 Jack 带我去另一个地方。他说那里藏着一个秘密。"
    # source:191
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "所以你带我来……看书？"
    # source:192
    $ amy_v11_emote("jack", "curious")
    jack "你不觉得有意思吗？最好的入口，往往看起来不像入口。"
    # source:193
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你这是带我喝酒，还是带我解谜？"
    # source:194
    $ amy_v11_emote("jack", "curious")
    jack "有什么区别？都是为了发现隐藏的世界。"
    # source:195
    narrator "一整面书柜立在面前。我已经开始兴奋了。"
    menu (screen="amy_v11_choice"):
        "两个人一起寻找机关":
            # source:200
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "你找左边，我找右边。"
            # source:201
            $ amy_v11_emote("jack", "smile")
            jack "我们两个智商加起来超过三百。"
            # source:202
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "那总不能输给一个书柜。"
            # source:204
            $ amy_v11_emote("jack", "thoughtful")
            jack "看来世界还没准备好难倒我们。"
            # source:205
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "别得意，下一关可能更难。"
            $ amy_v11_choose("bookshelf", "love", 10, "两个人一起寻找机关")
        "直接请工作人员打开":
            # source:209
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "为什么不直接问工作人员？"
            # source:210
            $ amy_v11_emote("jack", "curious")
            jack "你就这么放弃解谜的快乐？"
            # source:211
            $ amy_v11_emote("ami", "thoughtful")
            amy_v11_amy "我只是选择更快进入下一关。"
            # source:213
            $ amy_v11_emote("jack", "laugh")
            jack "有道理。效率也是一种智慧。"
            # source:214
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "欢迎来到隐藏关卡。"
            $ amy_v11_choose("bookshelf", "wisdom", 10, "直接请工作人员打开")
        "自己试了半天没找到":
            # source:218
            $ amy_v11_emote("jack", "curious")
            jack "怎么样，发现机关了吗？"
            # source:219
            $ amy_v11_emote("ami", "thoughtful")
            amy_v11_amy "没有。看来我们还得承认世界有未知。"
            # source:220
            $ amy_v11_emote("jack", "smile")
            jack "三百多的智商，被一排书教育了。"
            # source:221
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "至少它很有实力。"
            $ amy_v11_choose("bookshelf", None, 10, "自己试了半天没找到")
    jump amy_v11_date5

label amy_v11_date5:
    $ amy_v11_cue("latch", 0.5)
    call amy_v11_stage("secret", "date", actors=True)
    show screen amy_v11_status
    # source:231
    narrator "门打开的一刻，我真的很开心。"
    # source:232
    narrator "我喜欢这种藏起来的地方。像普通生活突然露出一条秘密通道。"
    # source:233
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "太好了！居然真的藏在书柜后面。"
    # source:234
    $ amy_v11_emote("jack", "smile")
    jack "我就知道你会喜欢。"
    # source:235
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有一种解密成功的感觉。"
    # source:237
    narrator "我们坐下来。可他坐得离我有点远。"
    # source:238
    narrator "我忍不住想：为什么不坐近一点？是礼貌，还是试探？"
    # source:240
    $ amy_v11_emote("jack", "smile")
    jack "你今天穿得好保守啊。"
    # source:241
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "今天有点冷，我想穿得暖和些。"
    # source:242
    $ amy_v11_emote("jack", "smile")
    jack "第一次见你的时候，穿得特别性感，也特别漂亮。"
    # source:243
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "谢谢你还记得。四月的奥克兰，我还是舍不得放下这件毛衣。"
    # source:244
    $ amy_v11_emote("jack", "laugh")
    jack "没问题。"
    # source:245
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "原来你留意到了。"
    # source:246
    $ amy_v11_emote("jack", "smile")
    jack "观察力是美德。"
    # source:247
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "那也看看别的呀。比如我现在很喜欢这里。"
    jump amy_v11_date6

label amy_v11_date6:
    call amy_v11_stage("counter", "date", actors=True)
    show screen amy_v11_status
    # source:255
    $ amy_v11_emote("jack", "curious")
    jack "你看那边那个，像不像 Stoner？"
    # source:256
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你怎么见谁都能判断出来？"
    # source:257
    $ amy_v11_emote("jack", "smile")
    jack "看状态。人总会泄露一点自己的秘密。"
    # source:258
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你觉得 Bartender 呢？"
    # source:259
    $ amy_v11_emote("jack", "smile")
    jack "Bartender 肯定一直 high。"
    # source:260
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "这什么理论？"
    # source:261
    $ amy_v11_emote("jack", "smile")
    jack "经验主义。"
    # source:262
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我昨天还有个朋友说，她男朋友在日本当 Bartender。"
    # source:263
    $ amy_v11_emote("jack", "smile")
    jack "那你可以拿我的理论去问问。"
    # source:264
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我怕她觉得我朋友认识了个奇怪的哲学家。"
    # source:265
    $ amy_v11_emote("jack", "laugh")
    jack "那就说我是民间社会学家。"
    # source:267
    narrator "我们聊生活、工作，聊一些根本不需要结论的话题。"
    # source:268
    narrator "他喜欢把普通的事说得像一场荒诞喜剧。我就笑着拆他的台。"
    # source:269
    narrator "也许那天说过的大部分话，我后来都记不清了。"
    # source:270
    narrator "但我记得我们都很开心。"
    # source:272
    $ amy_v11_emote("jack", "blush")
    jack "你脸红了。"
    # source:273
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有一点晕。"
    # source:274
    $ amy_v11_emote("jack", "smile")
    jack "走，出去吹吹风。"
    # source:275
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好。"
    jump amy_v11_date7

label amy_v11_date7:
    $ amy_v11_cue("step", 0.44)
    call amy_v11_stage("street", "date", actors=True)
    show screen amy_v11_status
    # source:282
    narrator "四月的夜风有些冷。"
    # source:283
    narrator "我们沿着街道往下走。他轻轻把手扶在我衣服的背后。"
    # source:284
    narrator "那只手很克制，离得不远，也没有真正搂住我。"
    # source:285
    narrator "我那时想的是：为什么不再近一点？"
    # source:286
    narrator "后来我才猜想，那也许是他在试探我是否愿意被靠近。"
    # source:288
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你看，月亮。"
    # source:289
    $ amy_v11_emote("jack", "smile")
    jack "嗯。"
    # source:290
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "天空塔也看得见。"
    # source:291
    $ amy_v11_emote("jack", "smile")
    jack "今晚这城市倒挺像一部电影。"
    # source:292
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那这部电影叫什么？"
    # source:293
    $ amy_v11_emote("jack", "curious")
    jack "还没演完，怎么能先定名字？"
    # source:294
    narrator "我看着月亮，想起那句没有说出口的话。"
    # source:295
    narrator "今晚月色真美。"
    jump amy_v11_date8

label amy_v11_date8:
    $ amy_v11_cue("door", 0.48)
    call amy_v11_stage("car", "date", actors=True)
    show screen amy_v11_status
    # source:303
    $ amy_v11_emote("jack", "smile")
    jack "今天说了这么多，有些话你可以忘了。"
    # source:304
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你想让我记住什么？"
    # source:305
    $ amy_v11_emote("jack", "smile")
    jack "你的能力大于你的野心。"
    # source:306
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "什么意思？"
    # source:307
    $ amy_v11_emote("jack", "smile")
    jack "你有能力做到更多。但你对自己要求得还不够。You need to push yourself harder."
    # source:308
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你是觉得，我还可以再相信自己一点？"
    # source:309
    $ amy_v11_emote("jack", "smile")
    jack "我是在说，你不应该把自己活成一个缩水的版本。"
    # source:310
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "这句我会记住。"
    # source:312
    narrator "那天我们说过很多话。只有这句，我真的记了很久。"
    # source:313
    narrator "不是因为他替我决定了人生，而是因为他让我想起，自己还有很多可能。"
    # source:315
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那我也问你一个问题。"
    # source:316
    $ amy_v11_emote("jack", "smile")
    jack "说。"
    # source:317
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "假如你能改变一件事——时间、空间，或者世界的规则。"
    # source:318
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你会选哪一个？"
    # source:319
    $ amy_v11_emote("jack", "smile")
    jack "这三个可不是同一量级的问题。"
    # source:320
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "所以才有意思。"
    # source:321
    $ amy_v11_emote("jack", "curious")
    jack "改变时间，是改写因果；改变空间，是取消距离；改变规则……那就是决定什么叫可能。"
    # source:322
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "听起来你都想要。"
    # source:323
    $ amy_v11_emote("jack", "curious")
    jack "如果只能选一个，得看代价是什么。"
    # source:324
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "这次先不谈代价。你选。"
    jump amy_v11_hub

label amy_v11_time:
    $ amy_v11_play_music("time")
    $ amy_ch2_selected_route = "time"
    show screen amy_v11_status
    centered "平行宇宙  十八岁的我们\nJack 20 岁 / Ami 18 岁"
    call amy_v11_stage("welcome", "campus", actors=True)
    # source:368
    amy_ch2_jack_narrator "二十岁。中山大学。医学院。"
    # source:369
    amy_ch2_jack_narrator "原来时间真能倒着走。连我这块摔出缺口的板子都回来了。"
    # source:370
    amy_v11_member "社长！你那横幅又掉了！"
    # source:371
    $ amy_v11_emote("jack", "smile")
    jack "别急。伟大的组织，总是从经费不足开始的。"
    # source:373
    amy_ch2_jack_narrator "然后我看见了她。"
    # source:374
    amy_ch2_jack_narrator "明明是第一次见面，却像有人提前把这一幕塞进了我的记忆。"
    # source:375
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "学长，请问新生报到处往哪边走？"
    # source:376
    $ amy_v11_emote("jack", "curious")
    jack "……你叫什么？"
    # source:377
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "Ami。怎么了？"
    # source:378
    $ amy_v11_emote("jack", "curious")
    jack "没什么。就是觉得，我们应该认识。"
    # source:379
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "这算迎新活动的一部分吗？"
    # source:380
    $ amy_v11_emote("jack", "laugh")
    jack "如果算，学校得给我发最佳创意奖。"
    # source:381
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那奖品是什么？"
    # source:382
    $ amy_v11_emote("jack", "smile")
    jack "先把你送到报到处，免得第一天就迷路。"
    # source:383
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好啊。谢谢学长。"
    # source:384
    amy_ch2_jack_narrator "她笑了。我忽然想，那个写剧本的家伙，至少这一场没有写错。"
    call amy_v11_stage("guitar_club", "campus", actors=True)
    # source:388
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "无聊寂寞帮？这什么名字？"
    # source:389
    $ amy_v11_emote("jack", "smile")
    jack "滑板社。"
    # source:390
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我想听听这个名字是谁起的。"
    # source:391
    $ amy_v11_emote("jack", "smile")
    jack "我。"
    # source:392
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你是社长？"
    # source:393
    $ amy_v11_emote("jack", "smile")
    jack "创始人兼社长。招新、搬桌子、修板子，目前都归我管。"
    # source:394
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那为什么叫无聊寂寞帮？"
    # source:395
    $ amy_v11_emote("jack", "smile")
    jack "因为人类发明的大部分事情，都是为了对抗无聊。"
    # source:396
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "医学也是？"
    # source:397
    $ amy_v11_emote("jack", "smile")
    jack "医学是为了对抗死亡。滑板先负责对抗星期三下午。"
    # source:398
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "听起来组织目标还挺明确。"
    # source:399
    $ amy_v11_emote("jack", "thoughtful")
    jack "荒诞世界里，总得有点自己的仪式。西西弗斯推石头，我们推板子。"
    # source:400
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "他可没收社费。"
    # source:401
    $ amy_v11_emote("jack", "smile")
    jack "那是他的组织管理有问题。"
    # source:403
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我其实想加入吉他社。"
    # source:404
    $ amy_v11_emote("jack", "smile")
    jack "那边。树底下那个弹错了三次和弦的摊位。"
    # source:405
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你连这个都听出来了？"
    # source:406
    $ amy_v11_emote("jack", "smile")
    jack "没听出来。看见他们社长皱眉三次。"
    # source:407
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "所以你要继续招募你的帮众？"
    # source:408
    $ amy_v11_emote("jack", "smile")
    jack "今天先带你去看看。"
    # source:409
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你走得开吗？我可以等你忙完。"
    # source:410
    $ amy_v11_emote("jack", "smile")
    jack "无聊寂寞帮第一条帮规：遇到更有意思的事，允许临时改道。"
    menu (screen="amy_v11_choice"):
        "陪她去吉他社试听":
            # source:414
            $ amy_v11_emote("jack", "smile")
            jack "先去听你想听的。我的摊位不会长腿跑掉。"
            # source:415
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "万一有人来报名？"
            # source:416
            $ amy_v11_emote("jack", "smile")
            jack "那他先练习一下对抗寂寞。"
            $ amy_v11_choose("time_welcome", "love", 5, "陪她去吉他社试听")
        "先带她办完新生手续":
            # source:418
            $ amy_v11_emote("jack", "smile")
            jack "先拿学生卡、找宿舍，再去吉他社。否则今晚你得睡在我们的滑板摊位。"
            # source:419
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "原来社长还提供后勤服务。"
            $ amy_v11_choose("time_welcome", "wisdom", 5, "先带她办完新生手续")
        "带她走滑板社发现的校园近路":
            # source:421
            $ amy_v11_emote("jack", "smile")
            jack "我知道一条近路。不过你得相信我的方向感。"
            # source:422
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "你刚刚把报名横幅挂反了。"
            # source:423
            $ amy_v11_emote("jack", "thoughtful")
            jack "那叫从另一个角度理解世界。"
            $ amy_v11_choose("time_welcome", "luck", 5, "带她走滑板社发现的校园近路")
    call amy_v11_stage("guitar_club", "campus", actors=True)
    # source:428
    amy_v11_guitar_senior "要不要试一段？不用紧张。"
    # source:429
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我会一点，但好久没弹了。"
    # source:430
    $ amy_v11_emote("jack", "smile")
    jack "没关系。我们社第一次活动也有一半人不会站在板子上。"
    # source:431
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "包括社长吗？"
    # source:432
    $ amy_v11_emote("jack", "smile")
    jack "社长负责用行动证明，摔倒不是组织耻辱。"
    # source:434
    amy_ch2_jack_narrator "她拨弦的时候，周围的招新声忽然远了。"
    # source:435
    amy_ch2_jack_narrator "我想起一个很久以前的黄昏。可那时，我们明明还没有一起度过任何黄昏。"
    # source:436
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "怎么样？"
    # source:437
    $ amy_v11_emote("jack", "smile")
    $ amy_v11_cue("guitar", 0.54)
    jack "你刚才那段，再弹一遍。"
    # source:438
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "为什么？"
    # source:439
    $ amy_v11_emote("jack", "smile")
    jack "想记住。"
    # source:440
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那等你想听的时候，我再弹给你听。"
    call amy_v11_stage("classroom_cg", "campus", actors=False)
    amy_ch2_jack_narrator "后来我们选到了同一门课。她总坐窗边，我坐在她后面一排。"
    amy_ch2_jack_narrator "那支备用铅笔已经借出去好几次了。这回她又把笔在纸上划了两下，没出墨，我就把铅笔推到她桌角。"
    amy_v11_amy "谢谢。你怎么每次都多带一支？"
    jack "第一次是碰巧。后来是想，万一你还坐在我前面呢。"
    amy_v11_amy "那下次我也带一支。万一你的笔不出墨了呢。"
    amy_ch2_jack_narrator "她转回去记笔记。我看见铅笔在她指间转了一圈，才落到纸上。"
    call amy_v11_stage("skateyard", "campus", actors=True)
    # source:444
    amy_v11_member "社长！你说的那个动作，自己先做一个！"
    # source:445
    $ amy_v11_emote("jack", "smile")
    jack "可以。失败是实验数据，成功是附带奖励。"
    # source:447
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你们社团的教学方式挺特别。"
    # source:448
    $ amy_v11_emote("jack", "smile")
    jack "我们奉行实践出真知。"
    # source:449
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "马克思要是知道你用他的思想解释摔跤……"
    # source:450
    $ amy_v11_emote("jack", "thoughtful")
    jack "哲学家们解释世界，我们负责改变膝盖上的淤青。"
    # source:451
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "慢慢来呀，我还想看你下次滑呢。"
    # source:453
    $ amy_v11_emote("jack", "curious")
    $ amy_v11_cue("landing", 0.43)
    jack "看见没有？"
    # source:454
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "看见啦。刚才你落地站稳的那一下，我也跟着松了口气。"
    # source:455
    $ amy_v11_emote("jack", "smile")
    jack "不。是暂时与重力达成了停战协议。"
    # source:457
    amy_ch2_jack_narrator "后来她经常来。有时候带吉他，有时候带一本书。有时候什么都不做，只坐在树下看我们折腾。"
    # source:458
    amy_ch2_jack_narrator "她不必成为无聊寂寞帮的成员，也已经是这里的一部分。"
    call amy_v11_stage("rain_corridor", "campus", actors=True)
    # source:462
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "刚才看你一次次站起来，我就在想，你遇到想不明白的事，也会这样一直找答案吗？"
    # source:463
    $ amy_v11_emote("jack", "thoughtful")
    jack "会吧。有些事过去了，我还是会想知道，它为什么会那样发生。"
    # source:464
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你会想向谁问这个问题？"
    # source:465
    $ amy_v11_emote("jack", "thoughtful")
    jack "如果有一个神把所有人的剧本都写好了，那就向他讨。"
    # source:466
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你相信真的有神？"
    # source:467
    $ amy_v11_emote("jack", "thoughtful")
    jack "相信。我甚至觉得自己看过人生剧本的某些片段。"
    # source:468
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你会去祈祷吗？"
    # source:469
    $ amy_v11_emote("jack", "smile")
    jack "会。有时候从教堂出来，后来真的发生一些事情。你可以说是巧合。"
    # source:470
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你觉得不是？"
    # source:471
    $ amy_v11_emote("jack", "thoughtful")
    jack "我不知道。我也不敢说那就是神给我的启示。"
    # source:473
    $ amy_v11_emote("jack", "angry")
    jack "但我有时候很生气。如果他真的什么都能安排，为什么要把有些事写成那样？"
    # source:474
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "相信有个答案，却一直等不到它。换作我，也会觉得难过。"
    # source:475
    $ amy_v11_emote("jack", "angry")
    jack "对。甚至想问他，凭什么。"
    # source:476
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那如果他把我写进你的剧本呢？"
    # source:477
    $ amy_v11_emote("jack", "smile")
    jack "这一页，我想慢一点翻。"
    # source:478
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好啊。那就等雨再小一点。"
    # source:479
    $ amy_v11_emote("jack", "thoughtful")
    jack "有些事不用急着问缘由。能在这一页遇见你，就已经很好了。"
    call amy_v11_stage("rain_path", "campus", actors=True)
    # source:484
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你第一次见我，为什么说我们应该认识？"
    # source:485
    $ amy_v11_emote("jack", "smile")
    jack "因为太熟悉了。像我曾经在别的地方见过你。"
    # source:486
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "如果不是在这里呢？比如再晚十年，或者在另一个城市。"
    # source:487
    $ amy_v11_emote("jack", "smile")
    jack "那就在那里认识。"
    # source:488
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你怎么这么确定？"
    # source:489
    $ amy_v11_emote("jack", "thoughtful")
    jack "我不知道。但我觉得，我遇到你，肯定会追你。"
    # source:490
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "这句话你倒是一点不犹豫。"
    # source:491
    $ amy_v11_emote("jack", "smile")
    jack "有些事情，不需要先论证完毕才敢开始。"
    # source:494
    amy_ch2_jack_narrator "她在我身边走着。我忽然不想再提前知道下一页写了什么。"
    call amy_v11_stage("time_cg", "campus", actors=False)
    # source:499
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "Jack，你今天摔了几次？"
    # source:500
    $ amy_v11_emote("jack", "smile")
    jack "没数。"
    # source:501
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我数了。七次。"
    # source:502
    $ amy_v11_emote("jack", "smile")
    jack "西西弗斯推了那么多年石头，也没见他抱怨过。"
    # source:503
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你还能选择什么时候再试，也能在累的时候歇一会儿。"
    # source:504
    $ amy_v11_emote("jack", "smile")
    jack "所以我比他幸运。"
    # source:506
    $ amy_v11_emote("jack", "curious")
    jack "看见没有？"
    # source:507
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "看见啦！"
    # source:508
    $ amy_v11_emote("jack", "smile")
    jack "这是人类对荒诞的一次小小胜利。"
    # source:509
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "先把护膝戴好吧。"
    # source:511
    $ amy_v11_emote("jack", "curious")
    jack "这首歌叫什么？"
    # source:512
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不告诉你。"
    # source:513
    $ amy_v11_emote("jack", "curious")
    jack "自己写的？"
    # source:514
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。"
    # source:515
    $ amy_v11_emote("jack", "curious")
    jack "写给谁的？"
    # source:516
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "写给一个每次摔倒，都愿意再站起来的人。"
    # source:518
    $ amy_v11_emote("jack", "curious")
    jack "那我可以听完吗？"
    # source:519
    $ amy_v11_emote("ami", "blush")
    amy_v11_amy "当然。你坐在这儿，我就想弹给你听。"
    # source:520
    $ amy_v11_emote("jack", "curious")
    jack "所以，是写给我的？"
    # source:521
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "不告诉你。"
    # source:523
    amy_ch2_jack_narrator "我一直觉得，那个写剧本的神，对我有些不公平。"
    # source:524
    amy_ch2_jack_narrator "有些安排，我到现在也无法理解。"
    # source:525
    amy_ch2_jack_narrator "可至少在这个黄昏，我不想追问原因。"
    call amy_v11_memory("time")
    # source:1040
    amy_ch2_jack_narrator "如果真有一个神写好了剧本，我想问他很多事。"
    # source:1041
    amy_ch2_jack_narrator "但这一页，我不想改。"
    jump amy_v11_finish_time

label amy_v11_space:
    $ amy_v11_play_music("space")
    $ amy_ch2_selected_route = "space"
    show screen amy_v11_status
    centered "平行宇宙  一秒钟的距离"
    call amy_v11_stage("car", "date", actors=True)
    # source:540
    $ amy_v11_emote("jack", "curious")
    jack "这是哪儿？"
    # source:541
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你刚才选了空间。"
    # source:542
    $ amy_v11_emote("jack", "curious")
    jack "所以空间就这么轻易地投降了？"
    # source:543
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你不是一直说要去巴黎吗？"
    # source:544
    $ amy_v11_emote("jack", "smile")
    jack "我说过。但我没说要让整个宇宙替我订机票。"
    $ amy_v11_cue("portal", 0.43)
    call amy_v11_stage("paris", "date", actors=True)
    # source:549
    $ amy_v11_emote("jack", "smile")
    jack "巴黎。"
    # source:550
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我们说过的巴黎。"
    # source:551
    $ amy_v11_emote("jack", "smile")
    jack "是。我们说过。"
    call amy_v11_memory("space")
    # source:553
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "所以，第一站想去哪？"
    # source:554
    $ amy_v11_emote("jack", "smile")
    jack "先在这里站一分钟。"
    # source:555
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "为什么？"
    # source:556
    $ amy_v11_emote("jack", "smile")
    jack "我想确认它是真的。那些在聊天框里说过的地方，原来有一天真的能踩在脚下。"
    # source:557
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那我们慢慢走，找个地方吃早餐。今天还有很多时间。"
    # source:558
    $ amy_v11_emote("jack", "smile")
    jack "你知道吗，我甚至说过，死也要死在巴黎。"
    # source:559
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我更想跟你在巴黎好好过一天。你看，天才刚刚亮呢。"
    # source:560
    $ amy_v11_emote("jack", "laugh")
    jack "你总能把悲壮史诗改成生活指南。"
    # source:561
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我只是舍不得让你这么早谢幕。"
    # source:563
    $ amy_v11_emote("jack", "smile")
    jack "巴黎的好处，是允许人把生活过得像文学。"
    # source:564
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也允许人吃完可颂以后，把黄油弄到袖子上。"
    # source:565
    $ amy_v11_emote("jack", "smile")
    jack "那也是文学的一部分。只是评论家通常不写。"
    call amy_v11_stage("bookshop", "date", actors=True)
    # source:569
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你看，哲学书店。"
    # source:570
    $ amy_v11_emote("jack", "thoughtful")
    jack "萨特、波伏瓦、加缪……这地方适合吵一场关于自由的架。"
    # source:571
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我想先看你会挑哪一本，再听听它为什么让你停下来。"
    # source:572
    $ amy_v11_emote("jack", "curious")
    jack "加缪吧。人知道世界荒诞，还要不要热烈地活？"
    # source:573
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "我想，你愿意来巴黎，本身就算是一个回答。"
    # source:574
    $ amy_v11_emote("jack", "smile")
    jack "我只是觉得，一个人若连浪漫都要经过成本收益分析，那也太可怜。"
    # source:575
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我会做成本收益分析，但我还是会陪你来巴黎。两件事不冲突。"
    # source:576
    $ amy_v11_emote("jack", "smile")
    jack "听你这么说，我觉得理性和浪漫真的能坐在一张桌上。"
    # source:578
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "去吧。我知道你想试。"
    # source:579
    $ amy_v11_emote("jack", "curious")
    jack "那你呢？"
    # source:580
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我去那边看橱窗。十分钟后见。我们又不是非得每一秒都做同一件事。"
    # source:581
    $ amy_v11_emote("jack", "thoughtful")
    jack "说得好。自由的第一条：允许彼此有自己的十分钟。"
    menu (screen="amy_v11_choice"):
        "带 Ami 去挑一件巴黎的小礼物":
            # source:585
            $ amy_v11_emote("jack", "smile")
            jack "想送你一件东西，证明今天不是一场梦。"
            # source:586
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "那挑一件你真的喜欢的，不要挑最贵的。"
            # source:587
            $ amy_v11_emote("jack", "smile")
            jack "那你在这儿等我一下。"
            call amy_v11_stage("paris_flowers_cg", actors=False)
            narrator "他在街角的花摊前停下来，请店主包了一小束奶白和淡粉色的花。等我走近，他把花递到我面前。"
            jack "刚才经过的时候，你多看了它们一眼。"
            amy_v11_amy "你看见了呀。我还以为只有我自己知道。"
            jack "本来想问你喜欢哪一束。后来想，今天也可以让我猜一次。"
            amy_v11_amy "那你猜中了。等会儿找个能装水的杯子吧，我想让它们多开一会儿。"
            narrator "我低头闻了闻花。包花的纸被风吹得轻轻响，我就这样抱着它，跟他沿着河边慢慢走。"
            $ amy_v11_choose("space_paris", "love", 5, "带 Ami 去挑一件巴黎的小礼物")
        "去左岸书店，各选一本书交换":
            # source:589
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "交换以后不准解释为什么选。"
            # source:590
            $ amy_v11_emote("jack", "curious")
            jack "那不是很危险？"
            # source:591
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "留点悬念。人生又不是每一页都要剧透。"
            call amy_v11_stage("paris_books_cg", actors=False)
            narrator "我们各自走进一排书架。再碰头时，他拿着一本蓝布封面的游记，我挑了一本红封面的短篇集。"
            jack "数到三，一起换？"
            amy_v11_amy "好。翻到喜欢的那页，就夹张书签。等读完，我们再交换一次。"
            narrator "两本书在桌面上擦肩而过。他低头翻开第一页，我没有问他为什么挑这本。反正以后还有机会问。"
            $ amy_v11_choose("space_paris", "wisdom", 5, "去左岸书店，各选一本书交换")
        "跟着街头音乐随机拐进一条小巷":
            # source:593
            $ amy_v11_emote("jack", "curious")
            jack "你确定不知道目的地？"
            # source:594
            $ amy_v11_emote("ami", "thoughtful")
            amy_v11_amy "不知道才叫探险。"
            # source:595
            $ amy_v11_emote("jack", "smile")
            jack "好。今天把导航权交给命运。"
            call amy_v11_stage("paris_music_cg", actors=False)
            narrator "拐过第二个弯，我们才看见手风琴。乐手就坐在拱门底下，拉得很慢，像是不怕路过的人听不完。"
            amy_v11_amy "我们在这儿坐一会儿吧。"
            jack "等下一首？"
            amy_v11_amy "嗯。今天难得走错路，还走到了这么好的地方。"
            narrator "我闭着眼，用鞋尖跟着拍子。等最后一个音落下去，我们谁也没急着起身。"
            $ amy_v11_choose("space_paris", "luck", 5, "跟着街头音乐随机拐进一条小巷")
    call amy_v11_stage("seine", "date", actors=True)
    if amy_ch2_choices.get("space_paris") in ("带 Ami 去挑一件巴黎的小礼物", "带 Amy 去挑一件巴黎的小礼物"):
        narrator "傍晚坐到河边时，Jack 找来一个盛水的玻璃杯，把那束花放在我们中间。"
    elif amy_ch2_choices.get("space_paris") == "去左岸书店，各选一本书交换":
        jack "先说好，读得慢的人也可以约下一次见面。"
        amy_v11_amy "可以呀。书是借口，我想见你又不用等到最后一页。"
    elif amy_ch2_choices.get("space_paris") == "跟着街头音乐随机拐进一条小巷":
        narrator "到了河边，他还在哼巷子里那支曲子。哼错了一拍，我顺着他错的那一拍往下接。"
    # source:600
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "白天你说，巴黎适合把生活过得像文学。现在呢？"
    # source:601
    $ amy_v11_emote("jack", "smile")
    jack "现在我觉得，文学还是写得保守了。"
    # source:602
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "为什么？"
    # source:603
    $ amy_v11_emote("jack", "smile")
    jack "因为它没有写到你坐在我旁边。"
    # source:604
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "你又开始了。"
    # source:605
    $ amy_v11_emote("jack", "thoughtful")
    jack "我是认真的。有些话写出来很俗，活出来却不一样。"
    # source:606
    $ amy_v11_emote("ami", "smile")
    $ amy_v11_cue("glass", 0.55)
    amy_v11_amy "那就别解释了。碰杯。"
    # source:608
    $ amy_v11_emote("jack", "smile")
    jack "人生奇妙而漫长，充满了惊喜。"
    # source:610
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "下一站呢？"
    # source:611
    $ amy_v11_emote("jack", "smile")
    jack "你选。巴黎是我想来的地方，下一站应该去你想去的地方。"
    # source:612
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "纽约。华尔街。"
    $ amy_v11_cue("portal", 0.43)
    call amy_v11_stage("newyork", "date", actors=True)
    # source:616
    $ amy_v11_emote("jack", "smile")
    jack "从塞纳河到华尔街，一秒钟。资本主义终于发明了最有效率的交通工具。"
    # source:617
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "可惜不能把交易风险也瞬移走。"
    # source:618
    $ amy_v11_emote("jack", "thoughtful")
    jack "这里的人很奇妙。他们把世界折算成数字，再用数字重新决定世界。"
    # source:619
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "数字不是敌人。真正危险的是以为自己能控制一切。"
    # source:620
    $ amy_v11_emote("jack", "curious")
    jack "金融巨鳄们吞噬的是钱，还是别人的人生？"
    # source:621
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有时候是别人的钱，有时候是自己的时间。市场不会因为谁的故事感人就给谁让路。"
    # source:622
    $ amy_v11_emote("jack", "curious")
    jack "那你为什么还想进去？"
    # source:623
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "因为我想有选择权。"
    # source:624
    $ amy_v11_emote("jack", "curious")
    jack "什么样的选择权？"
    # source:625
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不必因为账单、债务或者未来的不确定性，被迫接受自己不想要的生活。我希望能靠自己的能力，解决财务上的困境。"
    # source:626
    $ amy_v11_emote("jack", "smile")
    jack "所以你要做一个独立的人。"
    # source:627
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我本来就是。投资只是让我有更大的空间去选择。"
    # source:628
    $ amy_v11_emote("jack", "curious")
    jack "包括选择和谁在一起？"
    # source:629
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "当然。未来我希望和一个人在一起，是因为我真的喜欢他，不是因为我需要他养我、救我，或者替我做决定。"
    # source:630
    $ amy_v11_emote("jack", "smile")
    jack "这话听起来有点像宣战。"
    # source:631
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "我只是想有一天，我说愿意跟你在一起的时候，你知道那是因为我喜欢你。"
    # source:632
    $ amy_v11_emote("jack", "curious")
    jack "那如果那个人想照顾你呢？"
    # source:633
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我会很开心，也会珍惜。但被爱和依赖，是两回事。"
    # source:635
    $ amy_v11_emote("jack", "smile")
    jack "我突然明白了。你不是想赢过所有人。你想把自己的人生从别人手里赎回来。"
    # source:636
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。我想把做决定的自由留给自己，也想留给和我一起生活的人。"
    call amy_v11_stage("market", "date", actors=True)
    # source:640
    $ amy_v11_emote("jack", "curious")
    jack "如果现在给你一百万，你会做什么？"
    # source:641
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "先问币种、期限、风险承受能力，以及这钱是不是可以承受亏损。"
    # source:642
    $ amy_v11_emote("jack", "smile")
    jack "我给你一个史诗级机会，你先给我发风险问卷。"
    # source:643
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "史诗级机会通常更需要风险问卷。"
    # source:644
    $ amy_v11_emote("jack", "curious")
    jack "那你不想当金融巨鳄？"
    # source:645
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我想拥有财富，但不想被财富吞掉。自由不是永远盯着行情。"
    # source:646
    $ amy_v11_emote("jack", "curious")
    jack "那等你财富自由了，第一件事做什么？"
    # source:647
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "可能是把电脑合上，去一个喜欢的地方。也可能是开一家真正属于自己的公司。"
    # source:648
    $ amy_v11_emote("jack", "smile")
    jack "这个答案有意思。赚钱不是终点，是为了把时间还给自己。"
    call amy_v11_moment("模拟市场 / 非真实交易", "这是一场关于选择与风险的模拟决策。")
    menu (screen="amy_v11_choice"):
        "先保护本金，再争取收益":
            # source:651
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "能长期留在市场里，比一次赢得漂亮重要。"
            # source:652
            $ amy_v11_emote("jack", "thoughtful")
            jack "有道理。我们留得住下一次选择的机会，才谈得上自由。"
            $ amy_v11_choose("space_market", "wisdom", 5, "先保护本金，再争取收益")
        "为未来的自由设立目标":
            # source:654
            $ amy_v11_emote("ami", "thoughtful")
            amy_v11_amy "我希望有一天，我们可以自由决定明天醒来在哪个城市。"
            # source:655
            $ amy_v11_emote("jack", "smile")
            jack "这个目标，我愿意参与。"
            $ amy_v11_choose("space_market", "love", 5, "为未来的自由设立目标")
        "留一小部分资金尝试新机会":
            # source:657
            $ amy_v11_emote("ami", "curious")
            amy_v11_amy "可以冒险，但要先知道最多能失去什么。"
            # source:658
            $ amy_v11_emote("jack", "smile")
            jack "终于允许一点冒险了。"
            $ amy_v11_choose("space_market", "luck", 5, "留一小部分资金尝试新机会")
    $ amy_v11_cue("portal", 0.43)
    call amy_v11_stage("silicon", "date", actors=True)
    # source:663
    $ amy_v11_emote("jack", "curious")
    jack "巴黎让人想写诗，纽约让人想赚钱。硅谷呢？"
    # source:664
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "让人想做产品。"
    # source:665
    $ amy_v11_emote("jack", "smile")
    jack "你也想创业。"
    # source:666
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "对。我喜欢把一个模糊的想法变成真正能运行的东西。"
    # source:667
    $ amy_v11_emote("jack", "smile")
    jack "我脑子里有太多想法。每个都觉得应该马上开始。"
    # source:668
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那就挑一个。先做最小的版本，找真实用户验证。"
    # source:669
    $ amy_v11_emote("jack", "curious")
    jack "你已经开始排项目计划了？"
    # source:670
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "还没。我只是想先弄清楚我们解决的是什么问题。"
    # source:671
    $ amy_v11_emote("jack", "curious")
    jack "如果做一个让远距离的人真正有陪伴感的产品呢？"
    # source:672
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "可以。但不能只写“连接世界”四个字。我们得想用户为什么需要它，怎么用，数据怎么保护。"
    # source:673
    $ amy_v11_emote("jack", "smile")
    jack "我负责想象边界，你负责把边界推开。"
    # source:674
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我也会有想法呀。我不是只负责实现你的愿景。"
    # source:675
    $ amy_v11_emote("jack", "curious")
    jack "好。那我们一起决定做什么。"
    call amy_v11_stage("demo", "date", actors=True)
    # source:680
    $ amy_v11_emote("jack", "angry")
    jack "怎么又报错？刚才明明能跑。我们不能把这种东西拿去给别人看。"
    # source:682
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我看一下日志。"
    # source:683
    $ amy_v11_emote("jack", "smile")
    jack "我们已经在这里耗了半天了。"
    # source:684
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我知道你急。我也希望它今天能跑起来。"
    # source:686
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "找到了。不是整个方案有问题，是接口返回的数据结构变了。给我十分钟。"
    # source:687
    $ amy_v11_emote("jack", "curious")
    jack "十分钟能解决？"
    # source:688
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "先让我试。解决不了，我们就做一个不依赖这个接口的演示版本。"
    # source:690
    $ amy_v11_emote("jack", "curious")
    jack "你怎么总能这么冷静？"
    # source:691
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我也会急。只是把问题拆成一小步，就知道接下来能做什么了。"
    # source:692
    $ amy_v11_emote("jack", "laugh")
    jack "这句话应该写在所有创业公司的墙上。"
    # source:693
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我学新东西很快，做事也快。但我们得给问题一点被解决的时间。"
    # source:694
    $ amy_v11_emote("jack", "smile")
    jack "好。你处理技术，我去把演示故事重新梳理一遍。"
    # source:695
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "一会儿我们一起过。你讲愿景，我讲它怎么真正落地。"
    # source:697
    $ amy_v11_emote("jack", "smile")
    jack "我刚才差点想把电脑从窗户扔出去。"
    # source:698
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "还好没扔。预算表里没这一项。"
    # source:699
    $ amy_v11_emote("jack", "smile")
    jack "如果我们真的一起开公司——"
    # source:700
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "嗯？"
    # source:701
    $ amy_v11_emote("jack", "thoughtful")
    jack "我可能需要你时不时提醒我，世界不必在今天之内被改变。"
    # source:702
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我会提醒你。但我也希望你一直保留那股想改变世界的劲。"
    $ amy_v11_cue("portal", 0.43)
    call amy_v11_stage("beach", "beach", actors=True)
    # source:707
    $ amy_v11_emote("jack", "thoughtful")
    jack "我们一天里去了巴黎、纽约、硅谷。这个世界突然小得像一张桌布。"
    # source:708
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "可有些事情还是不能快进。比如一个产品从想法到成熟，比如信任。"
    # source:709
    $ amy_v11_emote("jack", "curious")
    jack "还有爱？"
    # source:710
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "还有爱。"
    # source:711
    $ amy_v11_emote("jack", "curious")
    jack "如果随时能见面，人还会期待下一次见面吗？"
    # source:712
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "会吧。瞬移只能解决距离，不能替我们决定想不想靠近。"
    menu (screen="amy_v11_choice"):
        "每次出现前先问对方愿不愿意":
            # source:715
            $ amy_v11_emote("jack", "smile")
            jack "我想见你，但不会把你的时间当成我的权限。"
            # source:716
            $ amy_v11_emote("ami", "thoughtful")
            amy_v11_amy "这才是我想要的自由。"
            $ amy_v11_choose("space_boundary", "wisdom", 5, "每次出现前先问对方愿不愿意")
        "约定一个只属于两人的暗号":
            # source:718
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "月亮。"
            # source:719
            $ amy_v11_emote("jack", "smile")
            jack "你发月亮，我就知道你想我了。"
            $ amy_v11_choose("space_boundary", "love", 5, "约定一个只属于两人的暗号")
        "把下一站交给彼此的共同记忆":
            # source:721
            $ amy_v11_emote("ami", "smile")
            amy_v11_amy "那就去一个我们没有真的到过、却一起想象过的地方。"
            # source:722
            $ amy_v11_emote("jack", "smile")
            jack "这听起来比随机坐标更危险。因为它会让人舍不得离开。"
            $ amy_v11_choose("space_boundary", "luck", 5, "把下一站交给彼此的共同记忆")
    $ amy_v11_cue("portal", 0.43)
    call amy_v11_stage("water_town", "boat", actors=True)
    # source:728
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你还记得吗？"
    # source:729
    $ amy_v11_emote("jack", "curious")
    jack "什么？"
    # source:730
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有一次，我们牵着手，躺在一起。我说，想象一下，我们现在不在房间里。"
    call amy_v11_stage("hands", "date", actors=False)
    # source:732
    amy_v11_amy_memory "我们在一条小河上。坐着一只乌篷船。船慢慢往前走，抬头就是星星。"
    call amy_v11_stage("boat", "boat")
    # source:734
    $ amy_v11_emote("jack", "smile")
    jack "我记得。"
    # source:735
    $ amy_v11_emote("ami", "touched")
    amy_v11_amy "那时候我们哪里也没去。却好像真的到了这里。"
    # source:736
    $ amy_v11_emote("jack", "curious")
    jack "现在真的到了，反而不知道该说什么。"
    # source:737
    $ amy_v11_emote("ami", "touched")
    amy_v11_amy "那就不用说。"
    # source:739
    $ amy_v11_emote("jack", "curious")
    jack "巴黎有那么多灯，纽约有那么多数字。这里什么都没有。"
    # source:740
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "有水声。有星星。"
    # source:741
    $ amy_v11_emote("jack", "smile")
    jack "还有你。"
    # source:743
    $ amy_v11_emote("ami", "touched")
    amy_v11_amy "我们数星星吧。"
    # source:744
    $ amy_v11_emote("jack", "smile")
    jack "好。"
    call amy_v11_stage("rooms", "date", actors=False)
    # source:749
    amy_ch2_jack_narrator "巴黎、纽约、硅谷、海边，还有那条原本只存在于想象里的船。"
    # source:750
    amy_ch2_jack_narrator "原来最远的距离，不是地图上的公里数。"
    # source:752
    $ amy_v11_cue("send", 0.5)
    amy_v11_amy_message "月亮。"
    # source:753
    $ amy_v11_emote("jack", "laugh")
    $ amy_v11_cue("message", 0.52)
    jack "现在方便见面吗？"
    # source:754
    $ amy_v11_cue("send", 0.5)
    amy_v11_amy_message "方便。"
    call amy_v11_stage("boat", "boat", actors=True)
    # source:1050
    $ amy_v11_emote("ami", "touched")
    amy_v11_amy "我们数星星吧。"
    # source:1051
    $ amy_v11_emote("jack", "smile")
    jack "好。"
    jump amy_v11_finish_space

label amy_v11_rules:
    $ amy_v11_play_music("rules")
    $ amy_ch2_selected_route = "rules"
    show screen amy_v11_status
    centered "平行宇宙  造物者"
    call amy_v11_stage("unfinished", "creator", actors=True)
    # source:770
    amy_ch2_system "世界载入失败。正在等待造物者。"
    # source:771
    $ amy_v11_emote("jack", "curious")
    jack "谁把游戏做到一半就上线了？"
    # source:772
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "说不定是在等你。"
    # source:774
    $ amy_v11_emote("jack", "curious")
    jack "……管理员权限。连重写规则都行？"
    # source:775
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "看起来是。"
    # source:776
    $ amy_v11_emote("jack", "curious")
    jack "我一直想见见那个写剧本的家伙。想问他，明明有能力把一切安排得好一点，为什么非要让我走那些弯路。"
    # source:777
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "现在你坐到他的位置了。"
    # source:778
    $ amy_v11_emote("jack", "smile")
    jack "我先声明，我对这份工作没有敬畏之心。"
    # source:779
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我们先看看怎么用吧。这里有人住，动之前先想想他们会不会受影响。"
    # source:781
    amy_v11_child "我家呢？"
    # source:783
    $ amy_v11_emote("jack", "smile")
    jack "……我只是想把这里弄漂亮一点。"
    # source:784
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我知道你想把这里弄漂亮。可他还在找家，我们先看看能帮他做什么。"
    # source:785
    $ amy_v11_emote("jack", "curious")
    jack "神也是这么做的吗？"
    # source:786
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我不知道。但我们可以先把房子还给他。"
    $ amy_v11_cue("repair", 0.5)
    call amy_v11_moment("修复第一栋房屋", "Jack 负责建造，Ami 根据居民路径重排地块。房屋复原，孩子跑回门前。")
    # source:788
    $ amy_v11_emote("jack", "smile")
    jack "行。造物者第一课：别急着按 Delete。"
    call amy_v11_stage("bridge", "creator", actors=True)
    # source:792
    amy_ch2_system "世界的“真实”参数尚未定义。请管理员选择。"
    # source:793
    $ amy_v11_emote("jack", "smile")
    jack "这题笛卡尔会喜欢。"
    # source:794
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你又要怀疑世界是不是梦了？"
    # source:795
    $ amy_v11_emote("jack", "angry")
    jack "如果所有感官都可能骗我，我凭什么相信眼前这个城市？"
    # source:796
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "Jack，你看前面。桥要塌了，我们先帮桥上的人。"
    $ amy_v11_cue("impact", 0.54)
    with vpunch
    call amy_v11_moment("镜中桥没有承重", "居民踏上去，桥消失。Ami 及时用临时支架接住桥面。")
    # source:798
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你生成的是外观，不是结构。我们需要知道什么东西真的能承重。"
    # source:799
    $ amy_v11_emote("jack", "curious")
    jack "连造物者都得做测试？"
    # source:800
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。别人要从这座桥上走过去，我们一起确认它撑得住吧。"
    menu (screen="amy_v11_choice"):
        "建立可重复的物理测试":
            call amy_v11_moment("建立可重复的物理测试", "Ami 用数据面板测载荷，Jack 根据结果加固桥梁。")
            $ amy_v11_choose("rules_bridge", "wisdom", 5, "建立可重复的物理测试")
        "先保护居民再试验":
            call amy_v11_moment("先保护居民再试验", "Jack 将居民送至安全区，两人一起重建。")
            $ amy_v11_choose("rules_bridge", "love", 5, "先保护居民再试验")
        "用一次大胆的现场实验":
            call amy_v11_moment("用一次大胆的现场实验", "Jack 亲自踏上桥，Ami 用应急方块救场；两人相视而笑。")
            $ amy_v11_choose("rules_bridge", "luck", 5, "用一次大胆的现场实验")
    # source:806
    $ amy_v11_emote("jack", "smile")
    jack "我能怀疑一切，唯独怀疑的时候，我还在思考。"
    # source:807
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你慢慢想。我先把这边扶稳，等你一起修。"
    # source:808
    $ amy_v11_emote("jack", "laugh")
    jack "你把笛卡尔送进工程部了。"
    # source:809
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我只是觉得，哲学可以让我们问对问题，技术负责不让人掉下去。"
    # source:811
    $ amy_v11_emote("jack", "curious")
    jack "有时候我真的想知道，为什么偏偏是我。"
    # source:812
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你可以继续问。也可以先决定，这次你想怎样做。"
    call amy_v11_stage("two_cities", "creator", actors=True)
    # source:816
    amy_ch2_system "检测到社会冲突。是否开启“永远一致”规则？"
    # source:817
    $ amy_v11_emote("jack", "curious")
    jack "一键消除争吵？听起来像人类文明的重大升级。"
    # source:818
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你确定那不是把所有人都变成同一个人？"
    # source:820
    $ amy_v11_emote("jack", "curious")
    jack "没有冲突了。怎么反而像死了一样？"
    # source:821
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不同意见不总是故障。有时正是因为人不一样，才会有新的东西。"
    # source:822
    $ amy_v11_emote("jack", "smile")
    jack "黑格尔会说，矛盾推动变化。"
    # source:823
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那你要的是一个永远不犯错的世界，还是一个能成长的世界？"
    # source:825
    $ amy_v11_emote("jack", "curious")
    jack "我有无限建造权限，为什么还要开会？"
    # source:826
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "因为你能创造建筑，不能替他们决定什么值得保留。"
    # source:827
    $ amy_v11_emote("jack", "smile")
    jack "我真是给自己招了一群甲方。"
    # source:828
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "欢迎创业。"
    call amy_v11_moment("共同设计", "听取工坊师傅、学生和居民三方诉求；设计保留工坊历史、共享新学校空间的方案。")
    # source:831
    $ amy_v11_emote("jack", "thoughtful")
    jack "我原来以为，好的世界就是没有矛盾。"
    # source:832
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "也许好的世界，是矛盾出现以后，人们还能一起想办法。"
    # source:833
    $ amy_v11_emote("jack", "curious")
    jack "那神为什么不把这种办法提前写好？"
    # source:834
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也许没有一个答案能替所有人决定。"
    call amy_v11_stage("factory", "creator", actors=True)
    # source:839
    $ amy_v11_emote("jack", "curious")
    jack "这不荒谬吗？机器做得越来越多，人反而越来越累。"
    # source:840
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "因为产量和分配不是一回事。"
    # source:841
    $ amy_v11_emote("jack", "thoughtful")
    jack "哲学家们忙着解释世界，问题是改变它。那就动手。"
    # source:843
    amy_v11_worker "你替我们做完了所有事，那我们还能做什么？"
    # source:844
    $ amy_v11_emote("jack", "smile")
    jack "我本来是想解放你们。"
    # source:845
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你解决了劳动量，没有解决参与感和决定权。"
    # source:847
    $ amy_v11_emote("jack", "smile")
    jack "那就把权限交出去。"
    # source:848
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "不是把所有人扔进控制台就算赋权。先让他们能学会、能参与、能选择。"
    call amy_v11_stage("workshop", "creator")
    # source:850
    $ amy_v11_emote("jack", "thoughtful")
    jack "一个 AI 就能做过去一整队人的工作。以前我听到这话，只觉得世界又要把人挤出去。"
    # source:851
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也可能让一个人终于有机会做成以前做不成的东西。"
    # source:852
    $ amy_v11_emote("jack", "curious")
    jack "有两年，我每天都觉得自己在原地打转。做什么都不顺，像是有人故意把我的那几页剧本写得特别难看。"
    # source:853
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。"
    # source:854
    $ amy_v11_emote("jack", "curious")
    jack "我祈祷过，也问过为什么是我。后来开始自己做东西，做那个游戏。AI 帮我补上了以前根本凑不齐的人手。"
    jack "等它真的跑起来……我突然又认得自己了。"
    # source:855
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那种“这是我做出来的”的感觉？"
    # source:856
    $ amy_v11_emote("jack", "smile")
    jack "对。不是别人告诉我有价值，是我自己看见它活了。"
    # source:857
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "所以你不是要证明那两年没有发生。你是在重新创造之后的生活。"
    # source:858
    $ amy_v11_emote("jack", "smile")
    jack "我还没打算原谅那个编剧。"
    # source:859
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不用急着原谅。今天这个作品完成了，就先高兴一会儿。"
    # source:861
    $ amy_v11_emote("jack", "smile")
    jack "你这人……很擅长把宏大的问题变成今天能做完的事。"
    # source:862
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "先做出 MVP，再讨论宇宙的终极意义。"
    call amy_v11_stage("mountain", "creator", actors=True)
    # source:866
    $ amy_v11_emote("jack", "smile")
    jack "西西弗斯。"
    # source:867
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你最熟悉的那位。"
    # source:868
    $ amy_v11_emote("jack", "curious")
    jack "他至少知道自己的刑罚是什么。我有时候连自己为什么在推石头都不知道。"
    # source:870
    amy_v11_sisyphus "你是谁？"
    # source:871
    $ amy_v11_emote("jack", "smile")
    jack "一个能结束你惩罚的人。"
    # source:872
    amy_v11_sisyphus "那你先告诉我，结束之后是什么。"
    # source:873
    $ amy_v11_emote("jack", "thoughtful")
    jack "自由。休息。任何你想要的东西。"
    # source:874
    amy_v11_sisyphus "你知道我想要什么吗？"
    # source:876
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不如问他。"
    # source:877
    $ amy_v11_emote("jack", "curious")
    jack "我不明白。你明明受了这么久的苦，为什么不立刻离开？"
    # source:878
    amy_v11_sisyphus "因为我从来没有机会选择。你现在要替我选择第二次？"
    # source:880
    $ amy_v11_emote("jack", "curious")
    jack "我以前一直在问，为什么这块石头非得落在我头上。"
    # source:881
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你现在可以问另一句：如果石头还在，你想怎么面对它？"
    menu (screen="amy_v11_choice"):
        "移走石头，邀请他探索世界":
            call amy_v11_stage("mountain_rest", "creator")
            call amy_v11_moment("移走石头，邀请他探索世界", "西西弗斯先走到山外，选择是否回来。")
            $ amy_v11_choose("rules_stone", "wisdom", 5, "移走石头，邀请他探索世界")
        "和他一起推一次":
            call amy_v11_stage("mountain_team", "creator")
            call amy_v11_moment("和他一起推一次", "Jack、Ami 与西西弗斯并肩上山；Jack 体会共同承担并不等于替人决定。")
            $ amy_v11_choose("rules_stone", "love", 5, "和他一起推一次")
        "把石头改造成会滚动的音乐舞台":
            call amy_v11_stage("mountain_music", "creator")
            call amy_v11_moment("把石头改造成会滚动的音乐舞台", "山谷第一次传出笑声；西西弗斯决定是否继续。")
            $ amy_v11_choose("rules_stone", "luck", 5, "把石头改造成会滚动的音乐舞台")
    # source:887
    amy_v11_sisyphus "我今天想先坐一会儿。"
    # source:889
    $ amy_v11_emote("jack", "smile")
    jack "我以为造物者要给人一个答案。"
    # source:890
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "也许先给他选择答案的权利。"
    # source:891
    $ amy_v11_emote("jack", "laugh")
    jack "加缪说要想象西西弗斯是幸福的。以前我觉得这句话像在跟苦难开玩笑。"
    # source:892
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "也许不是说痛苦值得歌颂。只是说，人不一定要等世界变得合理，才允许自己活下去。"
    # source:893
    $ amy_v11_emote("jack", "curious")
    jack "那我也可以在没弄明白“为什么是我”之前，先把自己的游戏做好。"
    # source:894
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "当然可以。"
    call amy_v11_stage("theatre", "creator", actors=True)
    # source:899
    $ amy_v11_emote("jack", "thoughtful")
    jack "我说过吧。我好像见过自己的剧本。"
    # source:900
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你现在看到的，是它写下的版本。"
    # source:901
    $ amy_v11_emote("jack", "angry")
    jack "上面连我最讨厌的那两年都有。为什么？如果写剧本的神有能力改，为什么不改？Why did it happen to me?"
    with hpunch
    # source:903
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "Jack！"
    # source:905
    $ amy_v11_emote("jack", "smile")
    jack "我只想删掉那些东西。"
    # source:906
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我知道。但那些经历已经发生过。删掉这一页，可能连你后来做成的东西也一起没了。"
    # source:907
    $ amy_v11_emote("jack", "curious")
    jack "你是说我应该感谢那些事？"
    # source:908
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不是。我不会让你感谢伤害。只是现在，你可以决定下一幕怎么演。"
    # source:909
    $ amy_v11_emote("jack", "curious")
    jack "萨特那套？人要为自己的选择负责？"
    # source:910
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "责任不是惩罚。是你有能力作决定，也有权利不接受别人替你定义。"
    # source:912
    $ amy_v11_emote("jack", "curious")
    jack "如果他们都不按剧本来，戏不就乱了？"
    # source:913
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "会乱。但那才有机会出现你没写过的东西。"
    call amy_v11_moment("角色可拒绝自己的台词", "一个演员第一次没有念台词，而是走下舞台去看海。")
    # source:915
    $ amy_v11_emote("jack", "laugh")
    jack "管理员的失业危机开始了。"
    # source:916
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "恭喜，你创造出了第一个不听话的 NPC。"
    # source:917
    $ amy_v11_emote("jack", "smile")
    jack "不。是第一个真正能自己走路的人。"
    call amy_v11_stage("lab", "creator", actors=True)
    # source:921
    amy_ch2_system "是否将协作者设为平等造物者？"
    # source:922
    $ amy_v11_emote("jack", "smile")
    jack "我能直接把你设成永远陪着我的角色。"
    # source:923
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你可以试着按那个按钮。"
    # source:924
    $ amy_v11_emote("jack", "smile")
    jack "……你这话听起来像陷阱。"
    # source:925
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我只是想知道，你要的是一个不会离开的人，还是一个可以选择留下的人。"
    # source:927
    $ amy_v11_emote("jack", "curious")
    jack "要是自由意味着可能失去呢？"
    # source:928
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "那自由就真的有重量。"
    # source:929
    $ amy_v11_emote("jack", "thoughtful")
    jack "我费这么大力气创造世界，结果最重要的事还是不能保证。"
    # source:930
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "如果能保证，那可能就不是两个人之间的爱了。只是你写给自己的剧情。"
    # source:932
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "波伏娃谈过，真正的关系不能把另一个人变成自己的附属品。我也想创造东西，不只是站在这里被你保护。"
    # source:933
    $ amy_v11_emote("jack", "curious")
    jack "你想创造什么？"
    # source:934
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "一个实验室。让任何人都能学会使用这些工具，不必先得到神的许可。"
    # source:935
    $ amy_v11_emote("jack", "smile")
    jack "你还真是无论在哪个宇宙都要搞技术创业。"
    # source:936
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "你负责提出疯狂的想法，我负责让它们稳定上线。"
    # source:937
    $ amy_v11_emote("jack", "curious")
    jack "万一我着急呢？"
    # source:938
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "那就先把日志打开，我们一起看。着急的时候，有个人搭把手会好一点。"
    menu (screen="amy_v11_choice"):
        "平等权限，各自拥有独立项目":
            call amy_v11_moment("平等权限，各自拥有独立项目", "两人共享世界资源但保留个人创作空间。")
            $ amy_v11_choose("rules_contract", "wisdom", 5, "平等权限，各自拥有独立项目")
        "共同建造一座可以自由进出的家":
            call amy_v11_moment("共同建造一座可以自由进出的家", "家没有锁链，门从内外都能打开。")
            $ amy_v11_choose("rules_contract", "love", 5, "共同建造一座可以自由进出的家")
        "让所有居民都能提出修改世界的建议":
            call amy_v11_moment("让所有居民都能提出修改世界的建议", "世界开启公开提案广场。")
            $ amy_v11_choose("rules_contract", "luck", 5, "让所有居民都能提出修改世界的建议")
    # source:945
    $ amy_v11_emote("jack", "curious")
    jack "Ami，要不要跟我一起创造这个世界？"
    # source:946
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "好啊。我们给每一版留个备份，想试什么就放心去试。"
    # source:947
    $ amy_v11_emote("jack", "curious")
    jack "为什么？"
    # source:948
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "这样就算走错了一步，我们也还有地方可以回来。"
    amy_ch2_system "双人共创已启用。管理员 JACK / AMY。两人权限平等，可独立退出。"
    call amy_v11_stage("chapel", "creator", actors=True)
    # source:953
    $ amy_v11_emote("jack", "smile")
    jack "我以前真的去祈祷过。后来有些事发生了，我会忍不住想，它们是不是跟祈祷有关。"
    # source:954
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "你会觉得有人在听。"
    # source:955
    $ amy_v11_emote("jack", "curious")
    jack "有时会。有时又觉得，如果真的有人在听，为什么不早一点回答我。"
    # source:957
    $ amy_v11_emote("jack", "thoughtful")
    jack "我有时分不清，我是在等一个启示，还是只想知道，那些说不出口的话，有没有人听见。"
    # source:958
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "相信有人在听，却一直等不到回音，心里是会难过的。你可以慢慢说，我在听。"
    # source:959
    $ amy_v11_emote("jack", "curious")
    jack "那你呢？你怎么总能接受？"
    # source:960
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也不是每件事都不难过。我只是觉得，已经发生的事不会因为我反复追问就倒回去。能做的事，我会做；做不到的，"
    amy_v11_amy "我慢慢接受。"
    # source:961
    $ amy_v11_emote("jack", "curious")
    jack "你不想知道终极答案？"
    # source:962
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "想过。但我不想让找答案这件事，夺走我今天可以过的生活。"
    # source:964
    $ amy_v11_emote("jack", "curious")
    jack "……什么都没发生。"
    # source:965
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也许今天只是我们坐了一会儿。"
    # source:966
    $ amy_v11_emote("jack", "curious")
    jack "这也算剧情？"
    # source:967
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "算啊。能陪你安静坐一会儿，我就觉得这一页值得记住。"
    # source:969
    $ amy_v11_emote("jack", "thoughtful")
    jack "也许有些问题可以先留在这里。等我们走远一点，再回头想。"
    # source:970
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "那就出发吧。我们还有世界没建完。"
    $ amy_v11_cue("alert", 0.55)
    call amy_v11_stage("overload", "creator", actors=True)
    # source:974
    amy_ch2_system "检测到不可兼容的愿望。建议启用“统一幸福”协议：将所有居民的目标修改为相同。"
    amy_ch2_system "预览方案：旧桥及相连街巷不再列入通行路线。"
    # source:975
    $ amy_v11_emote("jack", "curious")
    jack "又来？我都造了一个世界，连幸福都不能一次性解决？"
    # source:976
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "因为他们是不同的人。"
    # source:977
    $ amy_v11_emote("jack", "thoughtful")
    jack "我想给他们一个没有痛苦的世界。"
    # source:978
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "我知道你想护着他们。可那座桥通往工坊，也通往他们的家。要不要先听听住在那里的人怎么说？"
    amy_v11_worker "远一点的路也能走。但每天收工，我都会从这座桥上回家。以前桥不稳，大家就轮流提着灯，照给过桥的人看。"
    $ amy_v11_emote("jack", "thoughtful")
    jack "那护栏呢？我们还有木料。你们想把它加在哪一边？"
    amy_v11_worker "靠水那边。那根旧木桩还在，我知道怎么绑牢。"
    # source:980
    $ amy_v11_emote("jack", "curious")
    jack "那我们到底创造了什么？"
    # source:981
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我们给他们留了木料，也留了把桥修成他们想要的样子的机会。"
    # source:982
    $ amy_v11_emote("jack", "curious")
    jack "可我还是会问，为什么偏偏是我。为什么那些年要发生。"
    # source:983
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "想问就问吧。找不到答案的时候，我们也可以先过好眼前这一小段。"
    $ amy_v11_cue("repair", 0.5)
    amy_ch2_system "已关闭“统一幸福”协议。通行路线由居民恢复。"
    call amy_v11_stage("bridge_repair_cg", "creator", actors=False)
    narrator "Jack 扶住靠水的那根立柱。我在面板上确认桥面能承重。工匠沿着木桩缠紧绳结，旁边有人举着灯，照着他手里的活。"
    amy_v11_worker "好了。我先过去。"
    narrator "他在桥中间停了一下，试着把手放上新扶栏。木头轻轻响了一声，稳稳地撑住了。提灯的人跟了上来，照亮后面人的脚下。"
    jack "我本来想把这座桥修得一点痕迹都没有。"
    amy_v11_amy "留着吧。以后路过，他们会记得这是自己修的。"
    # source:985
    $ amy_v11_emote("jack", "thoughtful")
    jack "这世界还真不怎么样。"
    # source:986
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "嗯。有些地方挺糟糕的。"
    # source:987
    $ amy_v11_emote("jack", "laugh")
    jack "你还笑？"
    # source:988
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "因为我们能一起把它慢慢做好。"
    # source:989
    $ amy_v11_emote("jack", "smile")
    jack "我想再做一个游戏。"
    # source:990
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "做啊。"
    # source:991
    $ amy_v11_emote("jack", "smile")
    jack "可能比这个还难。"
    # source:992
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "那就拆成几个版本。"
    # source:993
    $ amy_v11_emote("jack", "smile")
    jack "你还真是不怕我野心太大。"
    # source:994
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你的能力大于你的野心。Push yourself harder。不是你说的吗？"
    # source:996
    $ amy_v11_emote("jack", "smile")
    jack "你竟然拿我的话来教育我。"
    # source:997
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "偶尔借用一下。"
    call amy_v11_stage("rooftop", "creator", actors=True)
    # source:1001
    $ amy_v11_emote("jack", "curious")
    jack "我原以为有了神的权限，就能弄清楚为什么会发生那些事。"
    # source:1002
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "现在呢？"
    # source:1003
    $ amy_v11_emote("jack", "thoughtful")
    jack "还是不知道。"
    # source:1004
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "失望吗？"
    # source:1005
    $ amy_v11_emote("jack", "smile")
    jack "有一点。但我今天做成了一些东西。那种感觉……挺久没回来了。"
    # source:1006
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我看见了。"
    # source:1007
    $ amy_v11_emote("jack", "thoughtful")
    jack "我想，那个写剧本的家伙至少没想到，我会自己做个游戏来跟他较劲。"
    # source:1008
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也许他想到了。"
    # source:1009
    $ amy_v11_emote("jack", "smile")
    jack "那我就做得比他想的还好。"
    # source:1012
    $ amy_v11_emote("jack", "curious")
    jack "月亮谁点的？"
    # source:1013
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "没人点。它自己升起来了。"
    # source:1014
    $ amy_v11_emote("jack", "smile")
    jack "……这比我造的漂亮。"
    # source:1015
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我们在这里坐一会儿吧。桥上已经有人提灯了。"
    # source:1017
    $ amy_v11_emote("jack", "smile")
    jack "走吧。"
    # source:1018
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "去哪？"
    # source:1019
    $ amy_v11_emote("jack", "smile")
    jack "回人间。还有东西等着我们做。"
    amy_ch2_system "世界已交还给它的居民。共创权限保留，但不强制任何人留在世界中。"
    call amy_v11_memory("rules")
    # source:1061
    $ amy_v11_emote("jack", "curious")
    jack "以前我总问，为什么偏偏是我。"
    # source:1062
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "现在呢？"
    # source:1063
    $ amy_v11_emote("jack", "smile")
    jack "现在我至少做成了一件事。"
    # source:1064
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "而且是你自己做成的。"
    jump amy_v11_finish_rules

label amy_v11_finish_time:
    $ amy_v11_complete("time")
    hide screen amy_v11_status
    hide amy_v11_ami
    hide amy_v11_jack
    $ renpy.say(amy_ch2_system, ("获得" + amy_v11_endings["time"][1] + "「" + amy_v11_endings["time"][2] + "」" if amy_ch2_card_new else "卡牌已收藏"))
    $ amy_v11_ambience()
    if amy_ch2_card_new:
        $ amy_v11_cue("card", .55)
    $ amy_v11_play_music("ending_time")
    $ amy_v11_collect_cg(amy_v11_endings["time"][4])
    call screen amy_v11_ending_hold("time")
    jump amy_v11_ending

label amy_v11_finish_space:
    $ amy_v11_complete("space")
    hide screen amy_v11_status
    hide amy_v11_ami
    hide amy_v11_jack
    $ renpy.say(amy_ch2_system, ("获得" + amy_v11_endings["space"][1] + "「" + amy_v11_endings["space"][2] + "」" if amy_ch2_card_new else "卡牌已收藏"))
    $ amy_v11_ambience()
    if amy_ch2_card_new:
        $ amy_v11_cue("card", .55)
    $ amy_v11_play_music("space")
    $ amy_v11_collect_cg(amy_v11_endings["space"][4])
    call screen amy_v11_ending_hold("space")
    jump amy_v11_ending

label amy_v11_finish_rules:
    $ amy_v11_complete("rules")
    hide screen amy_v11_status
    hide amy_v11_ami
    hide amy_v11_jack
    $ renpy.say(amy_ch2_system, ("获得" + amy_v11_endings["rules"][1] + "「" + amy_v11_endings["rules"][2] + "」" if amy_ch2_card_new else "卡牌已收藏"))
    $ amy_v11_ambience()
    if amy_ch2_card_new:
        $ amy_v11_cue("card", .55)
    $ amy_v11_play_music("ending_rules")
    $ amy_v11_collect_cg(amy_v11_endings["rules"][4])
    call screen amy_v11_ending_hold("rules")
    jump amy_v11_ending

label amy_v11_true:
    $ amy_ch2_sync_cards()
    $ amy_v12_recalculate()
    if not amy_v12_true_ready():
        jump amy_v11_hub
    $ amy_v11_play_music("ending_true")
    hide screen amy_v11_status
    scene expression Transform(amy_v11_endings["time"][4], size=(1920, 1080))
    with dissolve
    pause 0.6
    scene expression Transform(amy_v11_endings["space"][4], size=(1920, 1080))
    with dissolve
    pause 0.6
    scene expression Transform(amy_v11_endings["rules"][4], size=(1920, 1080))
    with dissolve
    pause 0.6
    call amy_v11_stage("car", "date", actors=True)
    # source:1094
    amy_ch2_jack_narrator "我见过二十岁的自己，去过那些本来只能想象的地方。"
    # source:1095
    amy_ch2_jack_narrator "我甚至当过一次造物者。"
    # source:1096
    amy_ch2_jack_narrator "可回到这里，那个写剧本的神，还是没有告诉我为什么。"
    # source:1098
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "你在想什么？"
    # source:1099
    $ amy_v11_emote("jack", "smile")
    jack "好像做了一个很长的梦。"
    # source:1100
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "梦见什么？"
    # source:1101
    $ amy_v11_emote("jack", "thoughtful")
    jack "我们在广州相遇，去了巴黎，还造了一个世界。"
    # source:1102
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "听起来挺忙的。"
    # source:1103
    $ amy_v11_emote("jack", "laugh")
    jack "确实。连做梦都像在赶项目。"
    # source:1104
    $ amy_v11_emote("ami", "curious")
    amy_v11_amy "那现在呢？还想去哪里？"
    # source:1105
    $ amy_v11_emote("jack", "curious")
    jack "你呢？"
    # source:1106
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我觉得现在就挺好。"
    # source:1109
    $ amy_v11_emote("jack", "smile")
    jack "我以前总觉得，有些事非得有一个答案。"
    # source:1110
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "也许会有吧。只是不用今晚就知道。"
    # source:1111
    $ amy_v11_emote("jack", "smile")
    jack "你总能这么轻描淡写。"
    # source:1112
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "不是轻描淡写。只是我们已经在这里了。"
    $ amy_v11_actors = False
    hide amy_v11_ami
    hide amy_v11_jack
    with dissolve
    pause 1.0
    # source:1118
    $ amy_v11_emote("jack", "curious")
    jack "这次什么都没发生。"
    # source:1119
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "发生了啊。"
    # source:1120
    $ amy_v11_emote("jack", "curious")
    jack "什么？"
    # source:1121
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "我们还在一起。"
    centered "时间没有倒流，距离没有消失，世界也没有变得完美。"
    call amy_v11_memory("poster", restore=False)
    call amy_v11_memory("ending", restore=False)
    $ amy_v11_collect_cg("images/cg/amy_v11/ending_true_v2.png")
    call screen amy_v11_continue_story
    $ persistent.amy_ch2_true_ending_completed = True
    $ amy_ch2_true_ending_seen = True
    $ amy_ch2_sync_cards()
    $ renpy.save_persistent()
    $ amy_v11_clear()
    $ amy_v11_ambience()
    hide screen amy_v11_status
    scene black
    with dissolve
    centered "Jack 视角"
    jump act3
