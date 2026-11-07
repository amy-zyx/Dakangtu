# V11 user interface and shared presentation. Story text lives in amy_ch2_v11_story.rpy.
image amy_v11_ami = "images/characters/ami/amy_ch2_smile_hd.png"
image amy_v11_jack = amy_jack_with_cross("images/characters/jack/amy_ch2_curious_extended.png")

define amy_v11_amy = Character("Amy", color="#a8d9c5")
define amy_v11_member = Character("社员", color="#d7d4ff")
define amy_v11_guitar_senior = Character("吉他社学姐", color="#d7d4ff")
define amy_v11_child = Character("小孩", color="#f5d9ad")
define amy_v11_worker = Character("工人", color="#cfdae5")
define amy_v11_sisyphus = Character("西西弗斯", color="#d6c1a0")

define amy_v11_amy_message = Character("Amy  消息", color="#a8d9c5")
define amy_v11_jack_message = Character("Jack  消息", color="#b7d9ff")
define amy_v11_amy_memory = Character("Amy  回忆", color="#a8d9c5")

default amy_v11_style = "date"
default amy_v11_scene = "car"
default amy_v11_moods = {}
default amy_v11_actors = True
default amy_v11_last_ending = None
default amy_v11_drink = None
default amy_v11_last_choice = None
default amy_v11_cocktail_seen = False

define amy_v11_backgrounds = {
    "classroom_cg": "images/cg/amy_v11/time_classroom.png",
    "paris_flowers_cg": "images/cg/amy_v11/paris_flowers.png",
    "paris_books_cg": "images/cg/amy_v11/paris_book_exchange.png",
    "paris_music_cg": "images/cg/amy_v11/paris_music_alley.png",
    "bridge_repair_cg": "images/cg/amy_v11/creator_bridge_repair.png",
    "hands": "images/cg/amy_v11/memory_hands.png",
    "time_cg": "images/cg/amy_v11/ending_time.png",
    "drive": "images/cg/act3/amy_ch2_tesla_sunset.png",
    "bar": "images/backgrounds/act3/amy_autumn_bar.png",
    "bookshelf": "images/backgrounds/act3/amy_autumn_entrance.png",
    "secret": "images/backgrounds/act3/amy_autumn_booth.png",
    "counter": "images/backgrounds/act3/amy_autumn_counter.png",
    "street": "images/backgrounds/act3/amy_autumn_street.png",
    "car": "images/backgrounds/act3/amy_autumn_car.png",
    "welcome": "images/backgrounds/amy_ch2/amy_time_welcome.png",
    "guitar_club": "images/backgrounds/amy_v11/time_guitar_club.png",
    "skateyard": "images/backgrounds/amy_v11/time_skateyard.png",
    "rain_corridor": "images/backgrounds/amy_v11/time_rain_corridor.png",
    "rain_path": "images/backgrounds/amy_v11/time_rain_path.png",
    "campus_sunset": "images/backgrounds/amy_ch2/amy_time_bench.png",
    "paris": "images/backgrounds/amy_v11/space_paris_morning.png",
    "bookshop": "images/backgrounds/amy_v11/space_bookshop.png",
    "seine": "images/backgrounds/amy_v11/space_seine_night.png",
    "newyork": "images/backgrounds/amy_ch2/amy_space_newyork.png",
    "market": "images/backgrounds/amy_v11/space_market_cafe.png",
    "silicon": "images/backgrounds/amy_ch2/amy_space_siliconvalley.png",
    "demo": "images/backgrounds/amy_v11/space_cowork_demo.png",
    "beach": "images/backgrounds/amy_v11/space_hawaii_dusk.png",
    "water_town": "images/backgrounds/amy_v11/space_water_town.png",
    "boat": "images/backgrounds/amy_v11/space_boat_inside.png",
    "unfinished": "images/backgrounds/amy_v11/rules_unfinished.png",
    "bridge": "images/backgrounds/amy_v11/rules_mirror_bridge.png",
    "two_cities": "images/backgrounds/amy_v11/rules_two_cities.png",
    "factory": "images/backgrounds/amy_v11/rules_factory.png",
    "workshop": "images/backgrounds/amy_v11/rules_workshop.png",
    "mountain": "images/backgrounds/amy_v11/rules_mountain.png",
    "mountain_rest": "images/backgrounds/amy_v11/rules_mountain_rest.png",
    "mountain_team": "images/backgrounds/amy_v11/rules_mountain_team.png",
    "mountain_music": "images/backgrounds/amy_v11/rules_mountain_music.png",
    "theatre": "images/backgrounds/amy_v11/rules_theatre.png",
    "lab": "images/backgrounds/amy_v11/rules_shared_lab.png",
    "chapel": "images/backgrounds/amy_v11/rules_chapel.png",
    "overload": "images/backgrounds/amy_v11/rules_overload.png",
    "rooftop": "images/backgrounds/amy_v11/rules_rooftop.png",
    "rooms": "amy_ch2_split_rooms",
}

define amy_v11_endings = {
    "time": ("ENDING 1  相遇", "时间卡牌", "相遇", "不论在哪一个年纪遇见你，我想我都会喜欢你。", "images/cg/amy_v11/ending_time.png"),
    "space": ("ENDING 2  陪伴", "空间卡牌", "陪伴", "世界那么大，能一起抵达的地方，不止地图上那些。", "images/cg/amy_v11/ending_space_stargazing.png"),
    "rules": ("ENDING 3  共创", "共创卡牌", "创造", "我们无法替世界写好答案，却可以一起创造下一页。", "images/cg/amy_v11/ending_rules.png"),
}

init python:
    build.classify(".codex-remote-attachments/**", None)
    def amy_v11_clear():
        for layer in ("master", "screens"):
            renpy.hide_screen("amy_ch2_world_stage", layer=layer)
        for name in ("amy_ch2_status", "amy_v11_action", "amy_v11_drinks"):
            renpy.hide_screen(name)

    def amy_v11_portrait(who, mood, style):
        # Source-specific framing aligns faces while all bodies extend below the viewport.
        if style == "campus":
            if who == "jack":
                key = "campus_jack_laugh" if mood == "laugh" else "campus_jack"
            else:
                key = {"laugh": "campus_ami_laugh", "blush": "campus_ami_shy",
                       "thoughtful": "campus_ami_shy"}.get(mood, "campus_ami")
            scale, x, y = (0.82, 89, 66) if who == "jack" else (0.95, 32, 195)
            path = "images/characters/amy_v11/" + key + ".png"
        elif style == "creator":
            if who == "jack":
                key = "creator_jack_angry" if mood == "angry" else "creator_jack"
            else:
                key = {"curious": "creator_ami_curious", "thoughtful": "creator_ami_thoughtful",
                       "laugh": "creator_ami_laugh"}.get(mood, "creator_ami")
            scale, x, y = (0.9, 54, 62) if who == "jack" else (0.95, 32, 195)
            path = "images/characters/amy_v11/" + key + ".png"
        elif style in ("beach", "boat"):
            key = style + "_" + who
            if who == "ami" and (style, mood) in (("beach", "thoughtful"), ("boat", "curious"), ("boat", "touched")):
                key += "_" + mood
            path = "images/characters/amy_v11/" + key + ".png"
            scale, x, y = (0.74, 120, 65) if who == "jack" else (0.76, 113, 170)
        elif who == "jack":
            variants = {
                "laugh": ("images/characters/jack/amy_ch2_laugh_extended.png", 66),
                "brow": ("images/characters/amy_v11/date_jack_brow.png", 66),
                "angry": ("images/characters/amy_v11/date_jack_angry.png", 46),
                "thoughtful": ("images/characters/jack/amy_ch2_thoughtful_extended.png", 66),
            }
            path, y = variants.get(mood, ("images/characters/jack/amy_ch2_curious_extended.png", 66))
            scale, x = 0.68, 149
        else:
            variants = {
                "laugh": ("images/characters/ami/amy_ch2_tease_hd.png", 0.65, 99, 181),
                "thoughtful": ("images/characters/ami/amy_ch2_thoughtful_hd.png", 0.6, 144, 204),
                "blush": ("images/characters/amy_v11/date_ami_blush.png", 0.95, 32, 172),
                "curious": ("images/characters/amy_v11/date_ami_curious.png", 0.9, 54, 201),
            }
            path, scale, x, y = variants.get(mood, ("images/characters/ami/amy_ch2_smile_hd.png", 0.65, 99, 181))
        portrait = amy_jack_with_cross(path) if who == "jack" else path
        return Composite((900, 1080), (x, y), Transform(portrait, zoom=scale))

    def amy_v11_emote(who, mood):
        if not store.amy_v11_actors:
            return
        if store.amy_v11_moods.get(who) == mood:
            return
        store.amy_v11_moods = dict(store.amy_v11_moods, **{who: mood})
        style = store.amy_v11_style
        if style == "vacation":  # Saves made before the beach and boat wardrobes split.
            style = "beach" if store.amy_v11_scene == "beach" else "boat"
        positions = [amy_ami_foreground if who == "ami" else right]
        if mood in ("laugh", "blush", "touched"):
            positions.append(amy_v11_expression_motion(mood))
        renpy.show("amy_v11_" + who, what=amy_v11_portrait(who, mood, style), at_list=positions)

    def amy_v11_choose(node, stat, amount, choice):
        before = dict(store.amy_ch2_stats)
        if choice not in amy_v12_rewards.get(node, {}):
            raise ValueError("Unknown Amy relationship choice: " + node + "/" + choice)
        store.amy_ch2_choices = dict(store.amy_ch2_choices, **{node: choice})
        store.amy_v11_last_choice = choice
        if node not in store.amy_ch2_awarded_nodes:
            store.amy_ch2_awarded_nodes = store.amy_ch2_awarded_nodes + [node]
        amy_v12_recalculate()
        changes = []
        for key, title in (("love", "心动"), ("wisdom", "理智"), ("luck", "幸运")):
            delta = store.amy_ch2_stats[key] - before[key]
            if delta:
                changes.append(title + (" +" if delta > 0 else " ") + str(delta))
        if changes:
            renpy.show_screen("amy_v11_notice", message=" / ".join(changes))
            renpy.restart_interaction()
        renpy.force_autosave()

    def amy_v11_complete(route):
        amy_v12_recalculate()
        store.amy_ch2_selected_route = route
        store.amy_v11_last_ending = route
        store.amy_ch2_card_new = amy_ch2_finish_world(route)
        renpy.force_autosave()

    def amy_v11_art_ready():
        from renpy.store import amy_v11_backgrounds, amy_v11_endings
        files = [p for p in amy_v11_backgrounds.values() if p.startswith("images/")]
        files += [row[4] for row in amy_v11_endings.values()]
        files += ["images/backgrounds/amy_v11/cocktails.png", "images/backgrounds/amy_v11/fusion_ticket_v2.png",
                  "images/cg/amy_v11/ending_true_v2.png",
                  amy_v11_friends_cg, amy_v11_lottery_cg]
        files += ["images/characters/amy_v11/" + key + ".png" for key in (
            "campus_jack", "campus_jack_laugh", "campus_ami", "campus_ami_shy",
            "date_jack_brow", "date_jack_angry", "date_ami_blush", "date_ami_curious",
            "creator_jack", "creator_jack_angry", "creator_ami", "creator_ami_curious",
            "beach_jack", "beach_ami", "boat_jack", "boat_ami",
            "campus_ami_laugh", "creator_ami_laugh", "creator_ami_thoughtful",
            "beach_ami_thoughtful", "boat_ami_curious", "boat_ami_touched")]
        files += [amy_v11_cue_path(cue) for cue in amy_v11_custom_cues + tuple(amy_v11_reused_cues)]
        files += ["images/characters/jack/amy_ch2_" + key + "_extended.png" for key in ("curious", "laugh", "thoughtful")]
        files += ["images/characters/ami/amy_ch2_" + key + "_hd.png" for key in ("smile", "tease", "thoughtful")]
        return all(renpy.loadable(path) for path in files)

transform amy_v11_card_reveal(delay=0.0):
    alpha 0.0
    yoffset 28
    pause delay
    ease 0.4 alpha 1.0 yoffset 0

# Hidden attributes remain available to narrative logic.
screen amy_v11_notice(message):
    zorder 200
    style_prefix "notify"
    frame at notify_appear:
        text "[message!q]"
    timer 3.25 action Hide("amy_v11_notice")

screen amy_v11_status():
    null

screen amy_v11_card_row(animated=False):
    hbox:
        spacing 40
        xalign 0.5
        for index, route in enumerate(("time", "space", "rules")):
            frame:
                xsize 280
                ysize 330
                padding (12, 12)
                background ("#d5b778dd" if route in persistent.amy_ch2_cards else "#8aa4bf38")
                if animated:
                    at amy_v11_card_reveal(index * 0.25)
                if route in persistent.amy_ch2_cards:
                    vbox:
                        spacing 18
                        add Transform(amy_v11_endings[route][4], xysize=(256, 144), fit="contain")
                        text amy_v11_endings[route][1] size 32 color "#132033" xalign 0.5
                        text amy_v11_endings[route][2] size 28 color "#132033" xalign 0.5
                else:
                    frame:
                        xfill True
                        yfill True
                        background "#0a1624aa"
                        text "未获得" size 26 color "#adc1d080" align (0.5, 0.5)

screen amy_v11_ending_hold(route):
    modal True
    add Transform(amy_v11_endings[route][4], size=(1920, 1080)) at amy_v11_slow_camera
    use amy_v11_album_button
    vbox:
        xalign 0.5
        yalign 0.94
        spacing 18
        text amy_v11_endings[route][0] size 48 color "#ffe4ac" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        text amy_v11_endings[route][3] size 32 color "#ffffff" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        textbutton "继续" action Return() xalign 0.5 text_size 34 text_color "#ffffff" text_outlines [(2, "#07101dcc", 0, 2)]

screen amy_v11_relationship_totals():
    text f"心动 {amy_ch2_stats['love']}    理智 {amy_ch2_stats['wisdom']}    幸运 {amy_ch2_stats['luck']}":
        id "amy_v11_totals_text"
        xalign 0.5
        size 34
        color "#ffe4ac"
        outlines [(2, "#07101dcc", 0, 2)]

screen amy_v11_route_end(title=None):
    modal True
    zorder 110
    $ all_cards = amy_v12_has_all_cards()
    add Transform(amy_v11_endings[amy_ch2_selected_route or "time"][4], size=(1920, 1080))
    add Solid("#09132170")
    use amy_v11_album_button
    vbox:
        align (0.5, 0.5)
        spacing 26
        text (title or amy_v11_endings[amy_ch2_selected_route][0]) size 46 color "#ffe4ac" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        use amy_v11_card_row
        use amy_v11_relationship_totals
        textbutton "A 重新选择" action Return("hub") xalign 0.5 text_size 36 text_color "#ffffff" text_outlines [(2, "#07101dcc", 0, 2)]
        textbutton "B 回主页面" action Return("menu") xalign 0.5 text_size 36 text_color "#ffffff" text_outlines [(2, "#07101dcc", 0, 2)]
        if amy_v12_true_ready():
            textbutton "C 真结局：人间" action Return("true") xalign 0.5 text_size 36 text_color "#ffe4ac" text_outlines [(2, "#07101dcc", 0, 2)]
        elif amy_v12_friends_ready():
            textbutton "C 一般结局：各自的世界" action Return("friends") xalign 0.5 text_size 36 text_color "#ffe4ac" text_outlines [(2, "#07101dcc", 0, 2)]
        elif all_cards:
            textbutton "C 真结局：尚未解锁" action Show("amy_v11_notice", message="回到车内重选约会或世界路线，试试不同的选项。") xalign 0.5 text_size 36 text_color "#c3cbd5" text_outlines [(2, "#07101dcc", 0, 2)]
            text f"心动达到 {amy_v12_true_love_min}，且高于另外两项，解锁人间" id "amy_v11_love_gate_hint" size 30 color "#ffe4ac" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
            text f"理智达到 {amy_v12_friends_wisdom_min}，且高于心动，解锁各自的世界" size 28 color "#ffe4ac" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        else:
            textbutton "C 真结局：尚未解锁" action Show("amy_v11_notice", message="集齐三个世界的记忆，并在选择中进一步靠近彼此。") xalign 0.5 text_size 36 text_color "#c3cbd5" text_outlines [(2, "#07101dcc", 0, 2)]

screen amy_v11_fusion(title="三份记忆，通往人间"):
    modal True
    default ready = False
    add Transform("images/backgrounds/amy_v11/fusion_ticket_v2.png", size=(1920, 1080))
    add Solid("#07121b99")
    vbox:
        align (0.5, 0.5)
        spacing 35
        text title size 54 xalign 0.5 color "#ffe4ac"
        use amy_v11_card_row(animated=True)
        use amy_v11_relationship_totals
        text "相遇  陪伴  创造" size 38 xalign 0.5 color "#ffffff"
        if ready:
            textbutton "继续" action Return() xalign 0.5 text_size 42 text_color "#f5f0e8" text_hover_color "#ffe4ac"
    timer 1.2 action SetScreenVariable("ready", True)

screen amy_v11_continue_story():
    modal True
    add Transform("images/cg/amy_v11/ending_true_v2.png", size=(1920, 1080)) at amy_v11_slow_camera
    use amy_v11_album_button
    vbox:
        xalign 0.5
        yalign 0.94
        spacing 20
        text "TRUE ENDING 4  人间" size 48 color "#ffe4ac" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        text "但故事还没有结束。" size 32 color "#ffffff" xalign 0.5 outlines [(2, "#07101dcc", 0, 2)]
        textbutton "继续故事" action Return() xalign 0.5 text_size 36 text_color "#ffffff" text_outlines [(2, "#07101dcc", 0, 2)]

# Non-choice actions use the normal VN dialogue flow, with a brief full-scene shot.
label amy_v11_moment(title, caption):
    $ amy_v11_action_moods = dict(amy_v11_moods)
    window hide
    hide amy_v11_ami
    hide amy_v11_jack
    with dissolve
    pause 0.5
    narrator "[caption]"
    if amy_v11_actors:
        $ amy_v11_moods = {}
        $ amy_v11_emote("ami", amy_v11_action_moods.get("ami", "smile"))
        $ amy_v11_emote("jack", amy_v11_action_moods.get("jack", "smile"))
        with dissolve
    return

screen amy_v11_drinks():
    modal True
    zorder 120
    add Solid("#081422f2")
    vbox:
        align (0.5, 0.42)
        spacing 32
        text "今晚的酒单" size 50 xalign 0.5 color "#ffe4ac"
        hbox:
            spacing 30
            for index, name, subtitle, note in [(0, "莫拉之美", "Mora Beauty", "紫莓 / 黑莓 / 柑橘"), (1, "北极星", "Polar Star", "柚子 / 薄荷 / 气泡"), (2, "潘纳科塔", "Panna Cotta", "香草 / 奶油 / 莓果"), (3, "航空", "Aviation", "Gin / 柠檬 / 紫罗兰")]:
                frame:
                    xsize 330
                    ysize 480
                    padding (20, 20)
                    background "#1b2e48"
                    vbox:
                        spacing 18
                        add Transform("images/backgrounds/amy_v11/cocktails.png", crop=((index % 2) * 639, (index // 2) * 615, 639, 615), xysize=(290, 280), fit="contain") xalign 0.5
                        text name size 32 color "#ffe4ac" xalign 0.5
                        text subtitle size 25 color "#ffffff" xalign 0.5
                        text note size 24 color "#c5d6e5" xalign 0.5
    textbutton "看完酒单，选择酒款" action Return() xalign 0.5 yalign 0.85 text_size 36 text_color "#ffffff" text_hover_color "#ffe4ac"

screen amy_v11_choice(items):
    modal True
    vbox:
        align (0.5, 0.37)
        spacing 22
        for item in items:
            button:
                xsize 1230
                padding (32, 20)
                background "#0b1c35eb"
                hover_background "#34536df5"
                action item.action
                text item.caption size 34 color "#ffffff" hover_color "#ffe4ac" xalign 0.5 textalign 0.5

screen amy_v11_drink_closeup(index, name):
    modal True
    add Solid("#07121bd9")
    vbox:
        align (0.5, 0.5)
        spacing 20
        add Transform("images/backgrounds/amy_v11/cocktails.png", crop=((index % 2) * 639, (index // 2) * 615, 639, 615), xysize=(500, 680), fit="contain") xalign 0.5
        text name size 44 color "#ffe4ac" xalign 0.5
        textbutton "继续" action Return() xalign 0.5 text_size 38 text_color "#f5f0e8" text_hover_color "#ffe4ac"

# Old saved UI names delegate to the current presentation.
screen amy_ch2_status():
    use amy_v11_status
screen amy_ch2_card_row():
    use amy_v11_card_row
screen amy_ch2_route_end(title):
    use amy_v11_route_end(title)
screen amy_ch2_fusion():
    use amy_v11_fusion
screen amy_ch2_world_stage(place):
    add Transform(amy_v11_backgrounds.get(place, "images/backgrounds/act3/amy_autumn_car.png"), size=(1920, 1080))

label amy_v11_stage(background, style="date", actors=True):
    $ amy_v11_clear()
    $ amy_v11_actors = actors and background not in ("drive", "hands", "time_cg", "rooms")
    $ amy_v11_scene = background
    $ amy_v11_style = style
    $ amy_v11_moods = {}
    $ amy_v11_ambience(background)
    if background.endswith("_cg") or background in ("drive", "rain_path", "beach", "boat", "rooftop"):
        scene expression Transform(amy_v11_backgrounds[background], size=(1920, 1080)) at amy_v11_slow_camera
    else:
        scene expression Transform(amy_v11_backgrounds[background], size=(1920, 1080))
    if background == "rain_path":
        show amy_v11_rain at amy_v11_rain_fall
    $ amy_v11_collect_cg(amy_v11_backgrounds[background])
    with dissolve
    if amy_v11_actors:
        $ amy_v11_emote("ami", "smile")
        $ amy_v11_emote("jack", "smile")
        with dissolve
    return

label amy_v11_memory(which, restore=True):
    if which == "poster" or renpy.loadable("amy_private/ch2_memory_" + which + ".png"):
        $ amy_v11_ambience()
        scene black
        with dissolve
        if which == "poster":
            call screen amy_ch2_fullscreen_poster
        else:
            call screen amy_ch2_memory("现实记忆", "amy_ch2_memory_" + which, 1000)
        if restore:
            call amy_v11_stage(amy_v11_scene, amy_v11_style, amy_v11_actors)
    return

label amy_v11_hub:
    $ amy_v11_play_music("chapter")
    $ amy_ch2_migrate()
    $ amy_v12_recalculate()
    show screen amy_v11_status
    call amy_v11_stage("car", actors=False)
    pause 0.5
    $ amy_v11_time_caption = "时间：如果我们十八岁就相遇" + ("【已收藏】" if "time" in persistent.amy_ch2_cards else "")
    $ amy_v11_space_caption = "空间：一秒到任何地方" + ("【已收藏】" if "space" in persistent.amy_ch2_cards else "")
    $ amy_v11_rules_caption = "规则：创造一个新世界" + ("【已收藏】" if "rules" in persistent.amy_ch2_cards else "")
    menu (screen="amy_v11_choice"):
        "[amy_v11_time_caption]":
            $ amy_ch2_selected_route = "time"
        "[amy_v11_space_caption]":
            $ amy_ch2_selected_route = "space"
        "[amy_v11_rules_caption]":
            $ amy_ch2_selected_route = "rules"
        "隐藏结局「人间」" if amy_v12_true_ready():
            jump amy_v11_fusion
        "一般结局：各自的世界" if amy_v12_friends_ready():
            jump amy_v11_friends
        "打开手套箱（彩蛋结局）" if amy_v12_lottery_ready():
            jump amy_v11_lottery
        "从约会重选" if amy_v12_has_all_cards():
            jump amy_v11_date2
    call amy_v11_stage("car")
    jack "那就这个吧。"
    amy_v11_amy "你确定？"
    jack "确定。"
    narrator "我望着他的眼睛。里面像藏着时间、空间，还有一个只属于我们的宇宙。"
    $ amy_v11_cue("portal")
    scene expression Solid("#d5e2ef")
    with amy_v11_portal_dissolve
    jump expression "amy_v11_" + amy_ch2_selected_route

label amy_v11_ending:
    $ amy_v11_ambience()
    $ amy_ch2_sync_cards()
    $ amy_v11_last_ending = amy_ch2_selected_route
    call screen amy_v11_route_end
    if _return == "hub":
        jump amy_v11_hub
    elif _return == "replay":
        jump expression "amy_v11_" + amy_ch2_selected_route
    elif _return == "date":
        jump amy_v11_date2
    elif _return == "true":
        jump amy_v11_fusion
    elif _return == "friends":
        jump amy_v11_friends
    hide screen amy_v11_status
    return

label amy_v11_fusion:
    $ amy_ch2_sync_cards()
    $ amy_v12_recalculate()
    if not amy_v12_true_ready():
        jump amy_v11_hub
    $ amy_v11_cue("fusion", .6)
    $ amy_v11_collect_cg("images/backgrounds/amy_v11/fusion_ticket_v2.png")
    call screen amy_v11_fusion
    jump amy_v11_true
