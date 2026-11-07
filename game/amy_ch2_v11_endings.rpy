# Alternate fictional endings for Amy Chapter 2.
define amy_v11_friends_cg = "images/cg/amy_v11/ending_friends.png"
define amy_v11_lottery_cg = "images/cg/amy_v11/ending_lottery.png"

screen amy_v11_alternate_ending(title):
    modal True
    use amy_v11_album_button
    vbox:
        xalign .5
        yalign .93
        spacing 16
        text title size 48 color "#ffe4ac" xalign .5 outlines [(2, "#07101dcc", 0, 2)]
        textbutton "返回主菜单" action MainMenu(confirm=False) xalign .5 text_size 34 text_color "#ffffff" text_outlines [(2, "#07101dcc", 0, 2)]

label amy_v11_friends:
    $ amy_ch2_sync_cards()
    $ amy_v12_recalculate()
    if not amy_v12_friends_ready():
        jump amy_v11_hub
    $ amy_v11_play_music("ending_friends")
    $ amy_v11_cue("fusion", .46)
    $ amy_v11_collect_cg("images/backgrounds/amy_v11/fusion_ticket_v2.png")
    call screen amy_v11_fusion("三份记忆，各自的世界")
    call amy_v11_stage("car")
    $ amy_v11_emote("jack", "thoughtful")
    jack "Ami，我想回北京。想了很久，今天终于能把这句话说出来。"
    $ amy_v11_emote("ami", "thoughtful")
    amy_v11_amy "嗯。我会留在奥克兰。这里有我想继续过下去的生活。"
    narrator "车里安静了一会儿。我以为我会急着说点什么，后来发现，我们都只是在等对方把这句话说完。"
    jack "那以后，我还能给你发消息吗？"
    $ amy_v11_emote("ami", "smile")
    amy_v11_amy "当然。你到北京的时候，记得跟我说一声。"
    jack "以朋友的身份？"
    amy_v11_amy "嗯。以后想起对方，也还是可以打个电话。"
    window hide
    scene expression Transform(amy_v11_friends_cg, size=(1920, 1080)) at amy_v11_slow_camera
    $ amy_v11_collect_cg(amy_v11_friends_cg)
    with dissolve
    pause .6
    narrator "后来，Jack 回到了北京，我留在奥克兰。各自忙起来以后，我们偶尔才联系一次。"
    $ amy_v11_cue("message", .36)
    amy_v11_jack_message "北京今天难得有这么好的天。你那边呢？"
    $ amy_v11_cue("send", .32)
    amy_v11_amy_message "天快黑了。海港的灯刚亮起来，下次拍给你看。"
    narrator "我把手机放回窗台。海港吹来一点风，我想，北京那边应该正是下午。"
    window hide
    call screen amy_v11_alternate_ending("一般结局：各自的世界")
    return

label amy_v11_lottery:
    $ amy_ch2_sync_cards()
    $ amy_v12_recalculate()
    if not amy_v12_lottery_ready():
        jump amy_v11_hub
    $ renpy.amy_session_lottery_seen = True
    $ renpy.block_rollback()
    call amy_v11_stage("car")
    $ amy_v11_cue("latch", .45)
    narrator "我打开手套箱找充电线，一张折起来的纸跟着掉到膝盖上。"
    amy_v11_amy "咦，我之前买的那张彩票。差点忘了还在这里。"
    jack "查一下？说不定连充电线都不用找了。"
    $ amy_v11_emote("ami", "curious")
    narrator "我在手机上对了第一遍。又把彩票递给他，让他从头对一次。"
    jack "等一下。最后一个号码也一样。"
    $ amy_v11_cue("card", .58)
    $ amy_v11_emote("ami", "laugh")
    amy_v11_amy "一千三百万新西兰元。Jack，是 13 million，我没看错吧？"
    amy_v11_amy "Jack，你再看一眼日期。我的手在抖。"
    $ amy_v11_emote("jack", "laugh")
    jack "看了。你刚才还说，想自己决定明天醒在哪座城市。"
    amy_v11_amy "我现在想先睡一觉。明天还是真的，我们就把地图摊开。"
    $ amy_v11_play_music("ending_lottery")
    window hide
    scene expression Transform(amy_v11_backgrounds["paris"], size=(1920, 1080))
    with dissolve
    pause .55
    scene expression Transform(amy_v11_backgrounds["newyork"], size=(1920, 1080))
    with dissolve
    pause .55
    scene expression Transform(amy_v11_backgrounds["beach"], size=(1920, 1080))
    with dissolve
    pause .55
    $ amy_v11_cue("fusion", .57)
    scene expression Transform(amy_v11_lottery_cg, size=(1920, 1080)) at amy_v11_slow_camera
    $ amy_v11_collect_cg(amy_v11_lottery_cg)
    with dissolve
    narrator "兑奖以后，我们把日常开销留够，余下的时间终于能自己安排。第一张机票买去了巴黎。后来，地图上的线越画越长。"
    narrator "我收好找零的纸币，Jack 把卡塞回钱包。登机广播一响，我们拖着箱子就跑，笑得差点忘了看登机口。"
    jack "下一站去哪？"
    amy_v11_amy "你先告诉我，明天想在哪个城市醒来。"
    window hide
    call screen amy_v11_alternate_ending("彩蛋  下一站，世界")
    return
