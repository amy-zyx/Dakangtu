# Amy POV Chapter 2: retained asset aliases and V11 entry compatibility.
image amy_autumn_bar = Transform("images/backgrounds/act3/amy_autumn_bar.png", size=(1920, 1080))
image amy_autumn_entrance = Transform("images/backgrounds/act3/amy_autumn_entrance.png", size=(1920, 1080))
image amy_autumn_counter = Transform("images/backgrounds/act3/amy_autumn_counter.png", size=(1920, 1080))
image amy_autumn_booth = Transform("images/backgrounds/act3/amy_autumn_booth.png", size=(1920, 1080))
image amy_autumn_street = Transform("images/backgrounds/act3/amy_autumn_street.png", size=(1920, 1080))
image amy_autumn_car = Transform("images/backgrounds/act3/amy_autumn_car.png", size=(1920, 1080))
image amy_autumn_ami = Transform("images/characters/ami/amy_autumn_sweater.png", ysize=900, fit="contain")
image amy_autumn_jack = Transform(amy_jack_with_cross("images/characters/jack/amy_autumn_jacket.png"), ysize=900, fit="contain")

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
    (149, 66), Transform(amy_jack_with_cross("images/characters/jack/amy_ch2_laugh_extended.png"), zoom=0.68),
)
image amy_ch2_jack curious = Composite(
    (900, 1080),
    (149, 66), Transform(amy_jack_with_cross("images/characters/jack/amy_ch2_curious_extended.png"), zoom=0.68),
)
image amy_ch2_jack thoughtful = Composite(
    (900, 1080),
    (149, 66), Transform(amy_jack_with_cross("images/characters/jack/amy_ch2_thoughtful_extended.png"), zoom=0.68),
)

label amy_act3:
    jump amy_v11_start

label amy_ch2_scene_1:
    jump amy_v11_date1
label amy_ch2_scene_2:
    jump amy_v11_date2
label amy_ch2_scene_3:
    jump amy_v11_date3
