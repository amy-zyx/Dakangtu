# A fixed catalogue of the CGs shown in Amy Chapter 2. Private chat images stay outside it.
define amy_v11_album_catalogue = (
    ("夕阳下的车", "images/cg/act3/amy_ch2_tesla_sunset.png"),
    ("教室的前后排", "images/cg/amy_v11/time_classroom.png"),
    ("相遇", "images/cg/amy_v11/ending_time.png"),
    ("巴黎的花束", "images/cg/amy_v11/paris_flowers.png"),
    ("左岸交换书", "images/cg/amy_v11/paris_book_exchange.png"),
    ("小巷的手风琴", "images/cg/amy_v11/paris_music_alley.png"),
    ("想象里的乌篷船", "images/cg/amy_v11/memory_hands.png"),
    ("陪伴", "images/cg/amy_v11/ending_space_stargazing.png"),
    ("走出山谷", "images/backgrounds/amy_v11/rules_mountain_rest.png"),
    ("一起推石头", "images/backgrounds/amy_v11/rules_mountain_team.png"),
    ("山谷的音乐舞台", "images/backgrounds/amy_v11/rules_mountain_music.png"),
    ("旧桥上的灯", "images/cg/amy_v11/creator_bridge_repair.png"),
    ("共创", "images/cg/amy_v11/ending_rules.png"),
    ("三份记忆", "images/backgrounds/amy_v11/fusion_ticket_v2.png"),
    ("人间", "images/cg/amy_v11/ending_true_v2.png"),
    ("各自的世界", "images/cg/amy_v11/ending_friends.png"),
    ("下一站，世界", "images/cg/amy_v11/ending_lottery.png"),
)

init python:
    renpy.amy_session_seen_cgs = []
    # Discard the former cross-launch collection when upgrading.
    persistent.amy_v11_seen_cgs = None

    def amy_v11_collect_cg(path):
        seen = renpy.amy_session_seen_cgs
        if path not in seen and any(path == cg for _, cg in amy_v11_album_catalogue) and renpy.loadable(path):
            renpy.amy_session_seen_cgs = seen + [path]


screen amy_v11_album_button():
    textbutton "CG 相册":
        action Show("amy_v11_album")
        align (.97, .94)
        padding (22, 12)
        background "#111d2edc"
        hover_background "#344763"
        text_size 30
        text_color "#ffe4ac"

screen amy_v11_album():
    modal True
    zorder 220
    default selected = None
    $ seen = renpy.amy_session_seen_cgs
    $ close_action = Hide("amy_v11_album") if selected is None else SetScreenVariable("selected", None)
    key "game_menu" action close_action
    add Solid("#0a1524")
    if selected is None:
        text "CG 相册" xpos 110 ypos 43 size 52 color "#ffe4ac"
        $ found = sum(path in seen for _, path in amy_v11_album_catalogue)
        text f"已收藏 {found} / {len(amy_v11_album_catalogue)}" xpos 365 ypos 61 size 29 color "#b9ccdb"
        textbutton "关闭相册" xpos 1650 ypos 46 action close_action text_size 30 text_color "#ffffff"
        grid 5 4:
            xalign .5
            ypos 138
            xspacing 24
            yspacing 18
            for index, (title, path) in enumerate(amy_v11_album_catalogue):
                if path in seen and renpy.loadable(path):
                    button:
                        xysize (310, 208)
                        padding (8, 8)
                        background "#283b50"
                        hover_background "#566781"
                        action SetScreenVariable("selected", (title, path))
                        vbox:
                            spacing 2
                            add Transform(path, xysize=(294, 162), fit="contain") xalign .5
                            text f"{index + 1:02d} {title}" xalign .5 size 24 color "#fff3da"
                else:
                    frame:
                        xysize (310, 208)
                        padding (10, 10)
                        background "#15253a"
                        text f"{index + 1:02d}  未解锁" align (.5, .5) size 24 color "#9badc0"
            for _ in range(20 - len(amy_v11_album_catalogue)):
                null width 310 height 208
    else:
        add Transform(selected[1], xysize=(1780, 920), fit="contain") align (.5, .39)
        text selected[0] xalign .5 yalign .97 size 32 color "#ffe4ac"
        textbutton "返回相册" align (.97, .97) action close_action text_size 30 text_color "#ffffff"
