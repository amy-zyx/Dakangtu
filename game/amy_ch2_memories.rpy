# Flattened screenshots with cartoon avatars for distribution.
image amy_ch2_memory_ending = "images/cg/amy_v11/wechat/ending.png"
image amy_ch2_memory_space = "images/cg/amy_v11/wechat/space.png"
image amy_ch2_memory_time = "images/cg/amy_v11/wechat/time.png"
image amy_ch2_memory_rules = "images/cg/amy_v11/wechat/rules.png"

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
            and renpy.loadable("images/cg/amy_v11/wechat/" + which + ".png")
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
