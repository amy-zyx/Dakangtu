# Chapter 2 v4 continuation. Fantasy dialogue follows the supplied design.
define amy_ch2_jack_narrator = Character(None, what_color="#cccccc")
define amy_ch2_system = Character("系统", color="#b7d9ff")
default amy_ch2_stats = {"love": 50, "wisdom": 50, "luck": 50}
default amy_ch2_awarded_nodes = []
default amy_ch2_choices = {}
default amy_ch2_completed = []
default amy_ch2_fragments = []
default amy_ch2_true_ending_seen = False
default amy_ch2_schema = 0
default amy_ch2_selected_route = None
default amy_ch2_rule_visual = ""
default persistent.amy_ch2_cards = []
default amy_ch2_card_new = False

define amy_ch2_backgrounds = {
    "大学迎新摊位": "images/backgrounds/amy_ch2/amy_time_welcome.png",
    "大学林荫道": "images/backgrounds/amy_ch2/amy_time_path.png",
    "黄昏长椅": "images/backgrounds/amy_ch2/amy_time_bench.png",
    "巴黎街道": "images/backgrounds/amy_ch2/amy_space_paris.png",
    "塞纳河与埃菲尔铁塔": "images/backgrounds/amy_ch2/amy_space_seine.png",
    "纽约华尔街": "images/backgrounds/amy_ch2/amy_space_newyork.png",
    "硅谷科技园": "images/backgrounds/amy_ch2/amy_space_siliconvalley.png",
    "夏威夷海边": "images/backgrounds/amy_ch2/amy_space_hawaii.png",
    "悬浮方块世界": "images/backgrounds/amy_ch2/amy_rules_floating.png",
}

image amy_ch2_split_rooms = Composite(
    (1920, 1080),
    (0, 0), Transform(Transform("images/backgrounds/amy_ch2/amy_space_amy_room.png", size=(1920, 1080)), crop=(480, 0, 960, 1080)),
    (960, 0), Transform(Transform("images/backgrounds/amy_ch2/amy_space_jack_room.png", size=(1920, 1080)), crop=(480, 0, 960, 1080)),
    (957, 0), Solid("#182239", xysize=(6, 1080)),
)

image amy_ch2_school_ami = Composite(
    (900, 1080),
    (32, 195), Transform("images/characters/ami/amy_time_school_ami_ponytail.png", zoom=0.95),
)
image amy_ch2_school_jack = Composite(
    (900, 1080),
    (89, 66), Transform("images/characters/jack/amy_time_school_jack.png", zoom=0.82),
)

init python:
    def amy_ch2_award_once(node, stat, delta, notify=True):
        if node in store.amy_ch2_awarded_nodes:
            return
        store.amy_ch2_awarded_nodes = store.amy_ch2_awarded_nodes + [node]
        if stat:
            stats = dict(store.amy_ch2_stats)
            stats[stat] = max(0, min(100, stats[stat] + delta))
            store.amy_ch2_stats = stats
            if notify:
                title = {"love": "心动", "wisdom": "理智", "luck": "幸运"}[stat]
                renpy.notify(title + " +" + str(delta))
        elif notify:
            renpy.notify("属性未变")

    def amy_ch2_sync_cards():
        routes = ("time", "space", "rules")
        cards = [r for r in routes if r in (persistent.amy_ch2_cards or []) or r in store.amy_ch2_completed or r in store.amy_ch2_fragments]
        persistent.amy_ch2_cards = list(cards)
        store.amy_ch2_completed = list(cards)
        store.amy_ch2_fragments = list(cards)

    def amy_ch2_migrate():
        amy_ch2_sync_cards()
        if store.amy_ch2_schema:
            return
        # Convert saved choices from the earlier Chapter 2 draft once.
        drink = {"classic": "favorite"}.get(store.amy_ch2_drinkChoice, store.amy_ch2_drinkChoice)
        book = {"solve": "together", "ask": "staff", "fail": "failed"}.get(store.amy_ch2_bookshelfChoice)
        if drink in ("surprise", "gin", "favorite"):
            store.amy_ch2_choices["cocktail"] = drink
            amy_ch2_award_once("cocktail", {"surprise": "love", "gin": "wisdom", "favorite": "luck"}[drink], 10, False)
        if book:
            store.amy_ch2_choices["bookshelf"] = book
            amy_ch2_award_once("bookshelf", {"together": "love", "staff": "wisdom", "failed": None}[book], 10, False)
        store.amy_ch2_schema = 4

    def amy_ch2_finish_world(route):
        amy_ch2_sync_cards()
        is_new = route not in persistent.amy_ch2_cards
        if is_new:
            persistent.amy_ch2_cards = list(persistent.amy_ch2_cards) + [route]
        amy_ch2_sync_cards()
        renpy.save_persistent()
        return is_new

screen amy_ch2_status():
    if not main_menu:
        frame:
            xalign 0.5
            ypos 12
            background "#101723cc"
            padding (20, 12)
            vbox:
                spacing 8
                text "心动 [amy_ch2_stats['love']]   理智 [amy_ch2_stats['wisdom']]   幸运 [amy_ch2_stats['luck']]" size 28 color ("#ffe4ac" if max(amy_ch2_stats.values()) >= 70 else "#ffffff")
                hbox:
                    spacing 14
                    xalign 0.5
                    for route, mark in [("time", "时"), ("space", "空"), ("rules", "创")]:
                        frame:
                            xsize 36
                            ysize 48
                            background ("#edcf90" if route in persistent.amy_ch2_cards else "#39475d")
                            text mark size 24 align (0.5, 0.5) color "#102030"


screen amy_ch2_card_row():
    hbox:
        spacing 32
        xalign 0.5
        for route, title, mark in [("time", "时间卡牌", "时"), ("space", "空间卡牌", "空"), ("rules", "共创卡牌", "创")]:
            frame:
                xsize 250
                ysize 300
                padding (22, 24)
                background ("#405e85" if route in persistent.amy_ch2_cards else "#263140")
                vbox:
                    xalign 0.5
                    spacing 24
                    frame:
                        xalign 0.5
                        xsize 94
                        ysize 130
                        background ("#edcf90" if route in persistent.amy_ch2_cards else "#4c5663")
                        text mark size 68 align (0.5, 0.5) color "#152235"
                    text title xalign 0.5 size 36 color "#ffffff"
                    text ("已获得" if route in persistent.amy_ch2_cards else "待收集") xalign 0.5 size 26 color "#e2d8c2"

screen amy_ch2_route_end(title):
    modal True
    zorder 100
    add Solid("#08101be8")
    vbox:
        align (0.5, 0.5)
        spacing 28
        text title size 52 xalign 0.5 color "#ffe4ac"
        use amy_ch2_card_row
        text "本次旅程结束，已获得的卡牌会保留。" size 30 xalign 0.5 color "#ffffff"
        if len(persistent.amy_ch2_cards) == 3:
            textbutton "合成三张卡牌，进入真结局" action Return("ending") xalign 0.5 text_size 38
        textbutton "再来一次" action Return("again") xalign 0.5 text_size 38
        textbutton "返回主菜单" action Return("menu") xalign 0.5 text_size 34

screen amy_ch2_fusion():
    modal True
    zorder 100
    add Solid("#08101bf5")
    vbox:
        align (0.5, 0.5)
        spacing 38
        text "三张卡牌，合成同一个答案" size 48 xalign 0.5 color "#ffe4ac"
        use amy_ch2_card_row
        text "人间" size 72 xalign 0.5 color "#ffe4ac"
        textbutton "继续" action Return() xalign 0.5 text_size 40

screen amy_ch2_world_stage(place):
    zorder -1
    $ background = amy_ch2_backgrounds.get(place)
    if place == "悬浮方块世界":
        if amy_ch2_rule_visual in ("西西弗斯山坡", "石头停在山顶", "自主选择推石", "并肩推石"):
            $ background = "images/backgrounds/amy_ch2/amy_rules_sisyphus.png"
        elif amy_ch2_rule_visual == "月亮已点亮":
            $ background = "images/backgrounds/amy_ch2/amy_rules_moon.png"
    if place == "各自的房间":
        add "amy_ch2_split_rooms"
    elif background and renpy.loadable(background):
        add Transform(background, size=(1920, 1080))
    else:
        add Solid("#182239")
        text ("背景占位   " + place) xalign 0.5 ypos 72 size 34 color "#d0dcf1"
    if amy_ch2_rule_visual:
        frame:
            xalign 0.5
            yalign 0.45
            xsize 680
            padding (35, 35)
            background "#293e60ee"
            vbox:
                spacing 18
                text amy_ch2_rule_visual size 38 xalign 0.5
                if amy_ch2_rule_visual == "想象的城堡":
                    hbox:
                        spacing 16
                        xalign 0.5
                        for height in (130, 190, 130):
                            add Solid("#b5c9eb", xysize=(90, height)) yalign 1.0
                elif amy_ch2_rule_visual == "月亮已点亮":
                    text "●" size 150 color "#ffeac2" xalign 0.5

label amy_ch2_bookshelf:

    scene amy_autumn_entrance
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    narrator "后来 Jack 带我去另一个地方。他说那里有个秘密。"
    ami "所以你带我来……看书？"
    jack "你再看看。"
    narrator "墙上是一排书柜，乍看之下没什么特别。可我知道，这里藏着什么。"
    menu:
        "和 Jack 一起找到机关":
            ami "你看左边，我看右边。"
            jack "我们两个智商加起来超过三百。"
            ami "那就别输给一个书柜。"
            narrator "我们沿着书脊仔细寻找。我发现一本略微突出的旧书，Jack 伸手试着拉动。"
            narrator "咔哒。书柜缓缓打开。"
            jack "我们还真找到了！"
            show amy_ch2_ami tease at amy_ami_foreground
            with dissolve
            ami "合作愉快。"
            narrator "我喜欢和他一起找到秘密的感觉。"
            $ amy_ch2_choices["bookshelf"] = "together"
            $ amy_ch2_award_once("bookshelf", "love", 10)
            $ renpy.force_autosave()
        "请工作人员帮忙打开":
            ami "既然是酒吧的入口，问工作人员不是更快吗？"
            jack "这么直接？"
            ami "有效率也很浪漫啊。"
            narrator "工作人员微笑着走来，操作书柜机关。书柜缓缓打开。"
            ami "哇，真的藏在后面！"
            narrator "原来有些秘密，不需要自己解开，也一样让人开心。"
            $ amy_ch2_choices["bookshelf"] = "staff"
            $ amy_ch2_award_once("bookshelf", "wisdom", 10)
            $ renpy.force_autosave()
        "尝试寻找，却没找到":
            jack "你找到了吗？"
            ami "还没有。我们是不是漏看了什么？"
            jack "三百多的智商，败给了一个书柜。"
            show amy_ch2_ami tease at amy_ami_foreground
            with dissolve
            ami "至少这个书柜很有实力。"
            narrator "我们笑起来，工作人员见状过来帮忙打开书柜。"
            ami "好吧，今天它赢了。"
            narrator "找不到答案也没关系。和他一起找的过程，本身就很好玩。"
            $ amy_ch2_choices["bookshelf"] = "failed"
            $ amy_ch2_award_once("bookshelf", None, 0)
            $ renpy.force_autosave()

    $ amy_ch2_doorOpened = True
    jump amy_ch2_secret_bar

label amy_ch2_secret_bar:
    scene amy_autumn_booth
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    narrator "我真的很喜欢这种地方。"
    narrator "一个看起来平平无奇的书柜，后面竟然藏着另一个世界。"
    ami "哇，好神奇！"
    show amy_ch2_jack laugh at right
    with dissolve
    jack "喜欢吗？"
    ami "喜欢。像在解谜。"
    narrator "可是……他为什么坐得离我那么远？"
    narrator "是太绅士了，还是根本没打算靠近？"
    jack "你今天穿得好保守啊。"
    ami "啊？"
    jack "第一次见你的时候，穿得特别性感，特别漂亮。"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "有没有一种可能……今天很冷？"
    jack "哈哈哈。"
    ami "四月了诶，奥克兰都快入冬了。我穿毛衣很合理吧？"
    show amy_ch2_jack laugh at right
    with dissolve
    jack "合理，合理。"
    narrator "我又看见他笑了。真讨厌，笑起来还挺好看。"
    jump amy_ch2_bar_chat

label amy_ch2_bar_chat:
    scene amy_autumn_counter
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "你看那边那个人，像不像 Stoner？"
    ami "你怎么见谁都觉得人家是 Stoner？"
    jack "你看他那个状态。"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "那你觉得谁不是？"
    jack "Bartender 肯定一直都是 high 的。"
    ami "你这什么理论啊。"
    jack "职业观察。"
    ami "我昨天还有个朋友跟我说，她男朋友在日本做 Bartender。"
    jack "真的？"
    ami "嗯。所以我现在看 Bartender，都要想一下你这个理论。"
    narrator "我们聊工作、聊生活、聊那些没有什么意义、却很好笑的事。"
    narrator "我已经不记得大部分内容。只记得那天我们都很开心。"
    jack "你脸红了。"
    ami "有一点晕。"
    jack "出去走走？"
    ami "好。"
    jump amy_ch2_street_walk

label amy_ch2_street_walk:
    scene amy_autumn_street
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    narrator "街上的风有点冷。"
    narrator "他的手很轻，保持着一个不远不近的距离。"
    narrator "我那时只是在想：为什么不干脆搂住我呢？"
    narrator "后来我才明白，也许那是他在试探，我会不会拒绝他的靠近。"
    ami "你看，月亮。"
    jack "嗯。"
    narrator "还有远处的天空塔。"
    narrator "今晚月色真美。"
    jump amy_ch2_car_question

label amy_ch2_car_question:
    scene amy_autumn_car
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "今晚说了那么多，你可以忘记别的。"
    jack "但有一句，你要记住。"
    ami "哪一句？"
    jack "你的能力大于你的野心。"
    jack "你要 Push Yourself Harder。"
    pause 0.7
    narrator "这句话，我记住了。"
    narrator "也许以后，我真的会更努力一点。不是为了证明给谁看，而是为了不辜负自己。"
    ami "那我也问你一个问题。"
    jack "问。"
    ami "如果你有一种能力，只能先选一个……"
    ami "改变时间，穿越空间，或者重写世界的规则。"
    ami "你会选哪个？"
    show amy_ch2_jack laugh at right
    with dissolve
    jack "你这问题越来越大了。"
    ami "认真选。"
    jump amy_ch2_route_hub

label amy_ch2_route_hub:
    $ amy_ch2_migrate()
    show screen amy_ch2_status
    $ amy_ch2_rule_visual = ""
    scene amy_autumn_car
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    with dissolve
    pause 0.8
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack thoughtful at right
    with dissolve
    $ amy_ch2_time_caption = "时间：如果我们十八岁就相遇" + ("【卡牌已获得】" if "time" in amy_ch2_completed else "")
    $ amy_ch2_space_caption = "空间：一秒到任何地方" + ("【卡牌已获得】" if "space" in amy_ch2_completed else "")
    $ amy_ch2_rules_caption = "规则：创造一个新世界" + ("【卡牌已获得】" if "rules" in amy_ch2_completed else "")
    menu:
        "[amy_ch2_time_caption]":
            $ amy_ch2_selected_route = "time"
        "[amy_ch2_space_caption]":
            $ amy_ch2_selected_route = "space"
        "[amy_ch2_rules_caption]":
            $ amy_ch2_selected_route = "rules"
        "合成三张卡牌，进入真结局" if len(amy_ch2_fragments) == 3:
            jump amy_ch2_card_fusion
    $ renpy.force_autosave()
    jack "那就这个吧。"
    ami "你确定？"
    jack "确定。"
    narrator "我望着他的眼睛。里面像藏着时间、空间，还有一个只属于我们的宇宙。"
    scene expression Solid("#ffffff")
    with dissolve
    if amy_ch2_selected_route == "time":
        jump amy_ch2_time
    elif amy_ch2_selected_route == "space":
        jump amy_ch2_space
    jump amy_ch2_rules

label amy_ch2_kiss(travel=False):
    scene amy_autumn_car
    with dissolve
    pause 0.8
    return

label amy_ch2_time:
    scene
    with dissolve
    show screen amy_ch2_world_stage("大学迎新摊位") onlayer master zorder -1
    show amy_ch2_school_ami at amy_ami_foreground
    show amy_ch2_school_jack at right
    with dissolve
    amy_ch2_jack_narrator "十八岁？我怎么回到学校了？"
    narrator "医学系的，帮忙接一下新生！"
    ami "你好，请问新生报到往哪边走？"
    jack "……Amy？"
    ami "你认识我？"
    jack "我……好像在哪见过你。"
    show amy_ch2_school_ami at amy_ami_foreground
    with dissolve
    ami "这么老套的搭讪？"
    jack "不是，我是真的觉得见过。"
    amy_ch2_jack_narrator "她明明是第一次出现，却像一段我已经认识很久的记忆。"
    ami "那这位学长，能带个路吗？"
    jack "当然。跟我走。"
    show screen amy_ch2_world_stage("大学林荫道") onlayer master zorder -1
    with dissolve
    ami "你学医啊？"
    jack "嗯。你呢？"
    ami "刚来。很多地方都不熟。"
    jack "以后有问题可以找我。"
    ami "你确定？我问题可多了。"
    show amy_ch2_school_jack at right
    with dissolve
    jack "那我得 Push Myself Harder。"
    menu:
        "主动约 Amy 逛校园":
            jack "晚上带你去看看校园？"
            ami "好啊，学长。"
            $ amy_ch2_choices["time"] = "主动约 Amy 逛校园"
            $ amy_ch2_award_once("world_time", "love", 5)
            $ renpy.force_autosave()
        "帮 Amy 安排报到路线":
            jack "先把报到办完，剩下的慢慢逛。"
            ami "你还挺靠谱。"
            $ amy_ch2_choices["time"] = "帮 Amy 安排报到路线"
            $ amy_ch2_award_once("world_time", "wisdom", 5)
            $ renpy.force_autosave()
        "随机选一条小路":
            jack "走这边，碰碰运气。"
            ami "万一迷路呢？"
            jack "那就一起迷路。"
            $ amy_ch2_choices["time"] = "随机选一条小路"
            $ amy_ch2_award_once("world_time", "luck", 5)
            $ renpy.force_autosave()
    show screen amy_ch2_world_stage("黄昏长椅") onlayer master zorder -1
    with dissolve
    amy_ch2_jack_narrator "有些人不必提前认识十年，也会在第一眼觉得熟悉。"
    ami "学长，明天还能见到你吗？"
    jack "能。"
    $ amy_ch2_card_new = amy_ch2_finish_world("time")
    $ renpy.notify("获得时间卡牌" if amy_ch2_card_new else "已持有时间卡牌")
    $ renpy.force_autosave()
    call amy_ch2_show_memory("time")
    jump amy_ch2_route_complete

label amy_ch2_space:
    scene
    with dissolve
    show screen amy_ch2_world_stage("巴黎街道") onlayer master zorder -1
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "巴黎？真的来了？"
    ami "你不是一直想来吗？"
    jack "我小时候就想来看看。"
    ami "Fashion capital。还有你喜欢的滑板。"
    jack "这也太快了。"
    show screen amy_ch2_world_stage("塞纳河与埃菲尔铁塔") onlayer master zorder -1
    with dissolve
    ami "香槟？"
    jack "Fancy lady。"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "你就会说这个。"
    jack "下一站？"
    ami "华尔街。"
    show screen amy_ch2_world_stage("纽约华尔街") onlayer master zorder -1
    with dissolve
    jack "我们这算是环球闪现？"
    ami "你不是想看世界吗？"
    show screen amy_ch2_world_stage("硅谷科技园") onlayer master zorder -1
    with dissolve
    jack "这里是硅谷？"
    ami "独角兽们的地盘。"
    show screen amy_ch2_world_stage("夏威夷海边") onlayer master zorder -1
    with dissolve
    jack "我觉得这能力有点危险。"
    ami "为什么？"
    jack "只要想，就能立刻出现在任何地方。"
    ami "包括我身边？"
    jack "包括你身边。"
    pause 0.7
    menu:
        "每次见面都先问对方愿不愿意":
            jack "我想见你，但我会先问你。"
            ami "那我会很期待你的消息。"
            $ amy_ch2_choices["space"] = "每次见面都先问对方愿不愿意"
            $ amy_ch2_award_once("world_space", "wisdom", 5)
            $ renpy.force_autosave()
        "给彼此一个专属暗号":
            jack "说暗号，我就出现。"
            ami "那暗号是……月亮。"
            $ amy_ch2_choices["space"] = "给彼此一个专属暗号"
            $ amy_ch2_award_once("world_space", "love", 5)
            $ renpy.force_autosave()
        "随机传送到下一处惊喜":
            jack "再赌一次下一站？"
            ami "只要别把我丢在海里。"
            $ amy_ch2_choices["space"] = "随机传送到下一处惊喜"
            $ amy_ch2_award_once("world_space", "luck", 5)
            $ renpy.force_autosave()
    show screen amy_ch2_world_stage("各自的房间") onlayer master zorder -1
    with dissolve
    amy_ch2_jack_narrator "距离消失以后，真正重要的，好像不是我能不能一秒见到她。"
    amy_ch2_jack_narrator "而是她愿不愿意在那一秒见我。"
    $ amy_ch2_card_new = amy_ch2_finish_world("space")
    $ renpy.notify("获得空间卡牌" if amy_ch2_card_new else "已持有空间卡牌")
    $ renpy.force_autosave()
    call amy_ch2_show_memory("space")
    jump amy_ch2_route_complete

label amy_ch2_rules:
    scene
    with dissolve
    show screen amy_ch2_world_stage("悬浮方块世界") onlayer master zorder -1
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    jack "这又是哪？"
    ami "好像进入了一个方块游戏。"
    $ amy_ch2_rule_visual = "创造者 Jack   管理员权限已授予"
    jack "我有管理员权限？"
    ami "恭喜，你现在是上帝了。"
    jack "那我试试。"
    $ amy_ch2_rule_visual = "创造控制台"
    menu:
        "想象都能成真":
            $ amy_ch2_rule_visual = "想象的城堡"
            ami "如果你想象的和现实一模一样，你怎么确定现在不是梦？"
            jack "……有点意思。"
            $ amy_ch2_choices["rules_1"] = "想象都能成真"
            $ amy_ch2_award_once("world_rules_1", "luck", 5)
            $ renpy.force_autosave()
        "谎言会被揭穿":
            $ amy_ch2_rule_visual = "真实模式"
            ami "那你怎么确定自己知道的都是真相？"
            jack "至少我知道我在思考。"
            $ amy_ch2_choices["rules_1"] = "谎言会被揭穿"
            $ amy_ch2_award_once("world_rules_1", "wisdom", 5)
            $ renpy.force_autosave()
        "可以修改记忆":
            $ amy_ch2_rule_visual = "记忆编辑器"
            ami "如果你改掉我所有记忆，我还是原来的我吗？"
            jack "那我不想随便按这个按钮。"
            $ amy_ch2_choices["rules_1"] = "可以修改记忆"
            $ amy_ch2_award_once("world_rules_1", "love", 5)
            $ renpy.force_autosave()
    ami "你能改变画面，但不一定能改变什么才算真实。"
    $ amy_ch2_rule_visual = "西西弗斯山坡"
    ami "西西弗斯。现在你能改规则，你要怎么帮他？"
    menu:
        "让石头永远停在山顶":
            $ amy_ch2_rule_visual = "石头停在山顶"
            jack "这下结束了。"
            ami "那他明天想做什么？"
            $ amy_ch2_choices["rules_2"] = "让石头永远停在山顶"
            $ amy_ch2_award_once("world_rules_2", "wisdom", 5)
            $ renpy.force_autosave()
        "让他自己决定推不推":
            $ amy_ch2_rule_visual = "自主选择推石"
            jack "他怎么又推？"
            ami "因为这次是他自己选的。"
            $ amy_ch2_choices["rules_2"] = "让他自己决定推不推"
            $ amy_ch2_award_once("world_rules_2", "luck", 5)
            $ renpy.force_autosave()
        "给他一个伙伴一起推":
            $ amy_ch2_rule_visual = "并肩推石"
            jack "问题还在。"
            ami "但至少有人陪他笑了。"
            $ amy_ch2_choices["rules_2"] = "给他一个伙伴一起推"
            $ amy_ch2_award_once("world_rules_2", "love", 5)
            $ renpy.force_autosave()
    $ amy_ch2_rule_visual = "未点亮的月亮"
    amy_ch2_system "请选择关于爱情的最终规则。"
    menu:
        "相爱的人永不分开":
            $ amy_ch2_rule_visual = "发光锁链"
            ami "如果有一天有人不想继续呢？"
            jack "……永远在一起，不等于永远想在一起。"
            $ amy_ch2_choices["rules_3"] = "相爱的人永不分开"
            $ amy_ch2_award_once("world_rules_3", "love", 5)
            $ renpy.force_autosave()
        "相爱的人不能说谎":
            $ amy_ch2_rule_visual = "真实模式"
            ami "那你不能再拿鬼故事套路我了。"
            jack "我什么时候套路你？"
            amy_ch2_system "检测到可疑陈述。"
            $ amy_ch2_choices["rules_3"] = "相爱的人不能说谎"
            $ amy_ch2_award_once("world_rules_3", "wisdom", 5)
            $ renpy.force_autosave()
        "任何人都可以自由选择爱":
            $ amy_ch2_rule_visual = "锁链消失"
            jack "那跟现实有什么区别？"
            ami "至少这里我们承认，爱不能靠程序设定。"
            $ amy_ch2_choices["rules_3"] = "任何人都可以自由选择爱"
            $ amy_ch2_award_once("world_rules_3", "luck", 5)
            $ renpy.force_autosave()
    amy_ch2_system "管理员可以改变世界，却不能替别人决定是否爱你。"
    jack "那我这权限还有什么用？"
    ami "至少可以给我造一轮月亮。"
    $ amy_ch2_rule_visual = "月亮已点亮"
    ami "真好看。"
    jack "然后呢？"
    ami "回家吧。"
    $ amy_ch2_card_new = amy_ch2_finish_world("rules")
    $ renpy.notify("获得共创卡牌" if amy_ch2_card_new else "已持有共创卡牌")
    $ renpy.force_autosave()
    call amy_ch2_show_memory("rules")
    jump amy_ch2_route_complete

label amy_ch2_true_ending:
    scene amy_autumn_car
    with dissolve
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    show amy_ch2_ami smile at amy_ami_foreground
    show amy_ch2_jack curious at right
    with dissolve
    amy_ch2_jack_narrator "我去过十八岁，去过巴黎，也创造过一个世界。"
    amy_ch2_jack_narrator "可每个世界，都有不能替别人决定的事。"
    ami "你在想什么？"
    jack "我好像做了很长的梦。"
    ami "梦见什么？"
    jack "时间、空间……还有一轮我自己造出来的月亮。"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "那你现在想去哪？"
    menu:
        "留在这里":
            pass
    jack "哪里也不去。"
    ami "为什么？"
    jack "因为现在就很好。"
    scene amy_autumn_car
    with dissolve
    jack "……这次怎么什么都没发生？"
    show amy_ch2_ami tease at amy_ami_foreground
    with dissolve
    ami "为什么一定要发生什么？"
    ami "这样就很好啊。"
    narrator "我们不需要改变时间，不需要逃去另一个地方，也不需要创造完美的规则。"
    narrator "我们只需要在真实的世界里，诚实、自由地选择自己的人生。"
    centered "真结局   人间"
    centered "世界没有改变。但我们选择了如何生活。"
    call amy_ch2_show_memory("poster")
    call amy_ch2_show_memory("ending")
    $ amy_ch2_true_ending_seen = True
    $ amy_ch2_chapter2Completed = True
    $ renpy.force_autosave()
    hide screen amy_ch2_status
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    jump act3

label amy_ch2_scene_4:
    jump amy_ch2_bookshelf
label amy_ch2_scene_5:
    jump amy_ch2_bookshelf
label amy_ch2_scene_6:
    jump amy_ch2_bookshelf
label amy_ch2_bookshelf_draft:
    jump amy_ch2_bookshelf
label amy_ch2_epilogue:
    jump amy_ch2_route_hub
label amy_ch2_tbc:
    jump amy_ch2_bookshelf


label amy_ch2_route_complete:
    $ amy_ch2_sync_cards()
    scene amy_autumn_car
    $ renpy.hide_screen("amy_ch2_world_stage", layer="master")
    $ renpy.hide_screen("amy_ch2_world_stage", layer="screens")
    with dissolve
    $ amy_ch2_card_title = {"time": "时间", "space": "空间", "rules": "共创"}[amy_ch2_selected_route] + "卡牌"
    $ renpy.force_autosave()
    call screen amy_ch2_route_end(("获得" if amy_ch2_card_new else "已持有") + amy_ch2_card_title)
    if _return == "again":
        jump amy_ch2_route_hub
    elif _return == "ending":
        jump amy_ch2_card_fusion
    hide screen amy_ch2_status
    return

label amy_ch2_card_fusion:
    $ amy_ch2_sync_cards()
    if len(persistent.amy_ch2_cards) < 3:
        jump amy_ch2_route_hub
    scene amy_autumn_car
    with dissolve
    call screen amy_ch2_fusion
    jump amy_ch2_true_ending
