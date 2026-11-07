# Local-only Chapter 2 memory screenshots. Raw images are excluded from builds.
image amy_ch2_memory_ending = Transform(Composite(
    (1536, 1465),
    (0, 0), "amy_private/ch2_memory_ending.png",
    (44, 730), Transform("amy_chat_avatar_jack", size=(160, 160)),
    (44, 1006), Transform("amy_chat_avatar_jack", size=(160, 160)),
    (1333, 200), Transform("amy_chat_avatar_ami", size=(164, 164)),
    (1333, 1282), Transform("amy_chat_avatar_ami", size=(164, 164)),
))

image amy_ch2_memory_space = Transform(Composite(
    (850, 1536),
    (0, 0), "amy_private/ch2_memory_space.png",
    (24, 12), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 124), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 234), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 677), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 1074), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 1294), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (24, 1407), Transform("amy_chat_avatar_jack", size=(90, 90)),
    (738, 344), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 455), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 565), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 788), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 898), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 1185), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (738, 1514), Transform("amy_chat_avatar_ami", size=(90, 90)),
    (329, 1000), Solid("#d0d0d0", xysize=(126, 38)),
), crop=(0, 0, 850, 1536))

image amy_ch2_memory_time = Transform(Composite(
    (857, 1536),
    (0, 0), "amy_private/ch2_memory_time.png",
    (24, 130), Transform("amy_chat_avatar_jack", size=(91, 91)),
    (24, 414), Transform("amy_chat_avatar_jack", size=(91, 91)),
    (24, 526), Transform("amy_chat_avatar_jack", size=(91, 91)),
    (24, 1422), Transform("amy_chat_avatar_jack", size=(91, 91)),
    (744, 18), Transform("amy_chat_avatar_ami", size=(91, 91)),
    (744, 637), Transform("amy_chat_avatar_ami", size=(91, 91)),
    (744, 1091), Transform("amy_chat_avatar_ami", size=(91, 91)),
    (744, 1203), Transform("amy_chat_avatar_ami", size=(91, 91)),
    (230, 1351), Solid("#d0d0d0", xysize=(128, 34)),
))

image amy_ch2_memory_rules = Transform(Composite(
    (691, 1536),
    (0, 0), "amy_private/ch2_memory_rules.png",
    (18, 181), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 363), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 452), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 722), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 845), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 936), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (18, 1343), Transform("amy_chat_avatar_jack", size=(75, 75)),
    (599, 272), Transform("amy_chat_avatar_ami", size=(75, 75)),
    (599, 541), Transform("amy_chat_avatar_ami", size=(75, 75)),
    (599, 631), Transform("amy_chat_avatar_ami", size=(75, 75)),
    (599, 994), Transform("amy_chat_avatar_ami", size=(75, 75)),
    (599, 1200), Transform("amy_chat_avatar_ami", size=(75, 75)),
    (117, 1112), Solid("#d0d0d0", xysize=(105, 30)),
    (339, 1291), Solid("#d0d0d0", xysize=(105, 30)),
), crop=(0, 160, 691, 1243))

image amy_ch2_memory_poster = "images/cg/amy_v11/reality_memory_poster.png"

default amy_ch2_wechat_unlocked = False

label amy_wechat_unlock:
    $ amy_ch2_wechat_unlocked = False
    menu:
        "输入你的四位数生日，解锁特殊截图。"

        "输入解锁密码":
            $ amy_ch2_wechat_unlocked = renpy.input("请输入四位数生日（月日），输入完按 Enter。", allow="0123456789", length=4, mask="*") == "1028"
            if not amy_ch2_wechat_unlocked:
                centered "密码不正确。本章将跳过微信截图。"

        "跳过":
            pass
    return

init python:
    def amy_ch2_memory_available(which):
        return which == "poster" or (
            amy_ch2_wechat_unlocked
            and renpy.loadable("amy_private/ch2_memory_" + which + ".png")
        )

screen amy_ch2_fullscreen_poster():
    modal True
    zorder 110
    add Transform("amy_ch2_memory_poster", xysize=(config.screen_width, config.screen_height), fit="cover", blur=28.0) align (0.5, 0.5)
    add Solid("#070d1966")
    add Transform("amy_ch2_memory_poster", ysize=config.screen_height, fit="contain") align (0.5, 0.5)
    textbutton "继续":
        align (0.96, 0.94)
        text_size 38
        text_outlines [(2, "#070d19", 0, 1)]
        action Return()
    key "game_menu" action Return()
    key "K_RETURN" action Return()

screen amy_ch2_memory(title, artwork, source_width, whole=False):
    modal True
    zorder 110
    add Solid("#070d19f5")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 1030
        padding (28, 20)
        background "#172236"
        vbox:
            spacing 14
            xalign 0.5
            text title size 38 xalign 0.5 color "#ffffff"
            fixed:
                xsize 1080
                ysize 850
                add Transform(artwork, xysize=(1080, 850), fit="contain") align (0.5, 0.5)
            textbutton "继续":
                xalign 0.5
                text_size 38
                action Return()
    key "game_menu" action Return()
    key "K_RETURN" action Return()

label amy_ch2_show_memory(which):
    if amy_ch2_memory_available(which):
        scene black
        with dissolve
        if which == "space":
            call screen amy_ch2_memory("空间  想和你一起去的地方", "amy_ch2_memory_space", 850)
        elif which == "time":
            call screen amy_ch2_memory("时间  无论何时遇见", "amy_ch2_memory_time", 857)
        elif which == "rules":
            call screen amy_ch2_memory("共创  和你一起冒险", "amy_ch2_memory_rules", 691)
        elif which == "poster":
            call screen amy_ch2_fullscreen_poster
        else:
            call screen amy_ch2_memory("我会一直陪着你", "amy_ch2_memory_ending", 1536)
    return
