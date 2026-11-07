# Engine regression and visual checks for the V11 chapter.
init python:
    build.classify("game/amy_ch2_tests.rpy", None)
    build.classify("game/amy_ch2_tests.rpyc", None)

screen amy_v11_portrait_check(style, amy_mood, jack_mood):
    modal True
    zorder 150
    $ background = {"date": "bar", "campus": "welcome", "creator": "rooftop", "beach": "beach", "boat": "boat"}[style]
    add Transform(amy_v11_backgrounds[background], size=(1920, 1080))
    add amy_v11_portrait("ami", amy_mood, style) xalign 0.05 yalign 1.0
    add amy_v11_portrait("jack", jack_mood, style) xalign 1.0 yalign 1.0

testsuite amy_ch2_v11:
    setup:
        $ renpy.test.amy_v11_backup = (list(persistent.amy_ch2_cards or []), list(persistent.amy_ch2_endings or []), persistent.amy_ch2_true_ending_completed)
        $ renpy.test.amy_v11_album_backup = list(renpy.amy_session_seen_cgs)
    before testcase:
        $ renpy.amy_session_cards = []
        $ renpy.amy_session_lottery_seen = False
        $ amy_ch2_sync_cards()
        $ persistent.amy_ch2_endings = []
        $ persistent.amy_ch2_true_ending_completed = False
    after testcase:
        if eval not renpy.get_screen("main_menu"):
            run MainMenu(confirm=False)
            skip until screen "main_menu"
    teardown:
        $ persistent.amy_ch2_cards, persistent.amy_ch2_endings, persistent.amy_ch2_true_ending_completed = renpy.test.amy_v11_backup
        $ renpy.amy_session_seen_cgs = renpy.test.amy_v11_album_backup
        $ renpy.save_persistent()
        exit

    testcase wechat_unlock:
        parameter mode = ["skip", "correct", "wrong"]
        parameter chapter = ["amy_act2", "amy_act3"]
        run Start(chapter)
        skip until screen "choice"
        if eval mode == "skip":
            click "跳过"
        else:
            click "输入解锁密码"
            skip until screen "input"
            keysym "K_1"
            keysym "K_0"
            keysym "K_2"
            if eval mode == "correct":
                keysym "K_8"
            else:
                keysym "K_9"
            keysym "K_RETURN"
            if eval mode == "wrong":
                assert "密码不正确。本章将跳过微信截图。"
        if eval chapter == "amy_act2":
            skip until "下了班，我开车从 City 出发。在路上，我一直在想等会儿要见的那个人。"
        else:
            skip until screen "amy_v11_drinks"
        assert eval amy_ch2_wechat_unlocked == (mode == "correct")
        assert eval amy_ch2_memory_available("poster")
        assert eval all(amy_ch2_memory_available(which) == (mode == "correct") for which in ("time", "space", "rules", "ending"))

    testcase order_0:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        assert eval f"心动 {amy_ch2_stats['love']}    理智 {amy_ch2_stats['wisdom']}    幸运 {amy_ch2_stats['luck']}" in renpy.get_widget("amy_v11_fusion", "amy_v11_totals_text").text
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        pause 1.3
        screenshot "fusion_relationship_totals.png"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase order_1:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase order_2:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase order_3:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase order_4:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase order_5:
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "让 Jack 选一杯 Surprise Me"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "两个人一起寻找机关"
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Ami 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_choice"
        click "先保护本金，再争取收益"
        skip until screen "amy_v11_choice"
        click "每次出现前先问对方愿不愿意"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "space" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        assert eval amy_ch2_stats == amy_v11_test_stats
        click "C 真结局：人间"
        skip until screen "amy_v11_fusion"
        click "继续"
        skip until screen "amy_ch2_fullscreen_poster"
        click "继续"
        if eval amy_ch2_memory_available("ending"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_continue_story"
        assert eval not persistent.amy_ch2_true_ending_completed
        click "继续故事"
        skip until "Act 3：雨落星河"
        assert eval persistent.amy_ch2_true_ending_completed
        assert eval len(persistent.amy_ch2_cards) == 3
        assert eval act3_love == 0

    testcase branches_time:
        parameter (a, b, c) = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
        run Start("amy_v11_time")
        skip until screen "amy_v11_choice"
        click expression (['陪她去吉他社试听', '先带她办完新生手续', '带她走滑板社发现的校园近路'][a])
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval persistent.amy_ch2_cards == ["time"]
        assert eval all(0 <= x <= 100 for x in amy_ch2_stats.values())
        assert eval len(amy_ch2_awarded_nodes) == 1

    testcase branches_space:
        parameter (a, b, c) = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
        run Start("amy_v11_space")
        if eval amy_ch2_memory_available("space"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click expression (['带 Ami 去挑一件巴黎的小礼物', '去左岸书店，各选一本书交换', '跟着街头音乐随机拐进一条小巷'][a])
        $ amy_v11_paris_expected_scene = ("paris_flowers_cg", "paris_books_cg", "paris_music_cg")[a]
        skip until eval amy_v11_scene == amy_v11_paris_expected_scene
        assert eval not amy_v11_actors
        skip until screen "amy_v11_choice"
        click expression (['先保护本金，再争取收益', '为未来的自由设立目标', '留一小部分资金尝试新机会'][b])
        skip until screen "amy_v11_choice"
        click expression (['每次出现前先问对方愿不愿意', '约定一个只属于两人的暗号', '把下一站交给彼此的共同记忆'][c])
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval persistent.amy_ch2_cards == ["space"]
        assert eval all(0 <= x <= 100 for x in amy_ch2_stats.values())
        assert eval len(amy_ch2_awarded_nodes) == 3

    testcase branches_rules:
        parameter (a, b, c) = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
        run Start("amy_v11_rules")
        skip until screen "amy_v11_choice"
        click expression (['建立可重复的物理测试', '先保护居民再试验', '用一次大胆的现场实验'][a])
        skip until screen "amy_v11_choice"
        click expression (['移走石头，邀请他探索世界', '和他一起推一次', '把石头改造成会滚动的音乐舞台'][b])
        skip until screen "amy_v11_choice"
        click expression (['平等权限，各自拥有独立项目', '共同建造一座可以自由进出的家', '让所有居民都能提出修改世界的建议'][c])
        if eval amy_ch2_memory_available("rules"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval persistent.amy_ch2_cards == ["rules"]
        assert eval all(0 <= x <= 100 for x in amy_ch2_stats.values())
        assert eval len(amy_ch2_awarded_nodes) == 3

    testcase date_choices:
        parameter (drink, book) = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        run Start("amy_v11_start")
        skip until screen "choice"
        click "跳过"
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click expression (['让 Jack 选一杯 Surprise Me', '试试 Gin：Aviation', '点熟悉的 Creamy Panna Cotta'][drink])
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click expression (['两个人一起寻找机关', '直接请工作人员打开', '自己试了半天没找到'][book])
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        $ opening = [(60, 50, 55), (63, 60, 50), (60, 60, 50)][drink]
        $ bookshelf_delta = [(10, 0, 0), (3, 10, 0), (0, 0, 0)][book]
        assert eval tuple(amy_ch2_stats[k] for k in ("love", "wisdom", "luck")) == tuple(a + b for a, b in zip(opening, bookshelf_delta))
        assert eval len(amy_ch2_awarded_nodes) == 2
        assert eval persistent.amy_ch2_cards == []

    testcase asset_and_frames:
        parameter (style, am, ja) = [('date', 'smile', 'laugh'), ('date', 'laugh', 'brow'), ('date', 'thoughtful', 'thoughtful'), ('date', 'blush', 'angry'), ('date', 'curious', 'curious'), ('campus', 'smile', 'smile'), ('campus', 'blush', 'laugh'), ('creator', 'smile', 'smile'), ('creator', 'curious', 'angry'), ('beach', 'smile', 'smile'), ('boat', 'smile', 'smile'), ('campus', 'laugh', 'laugh'), ('creator', 'thoughtful', 'smile'), ('creator', 'laugh', 'smile'), ('beach', 'thoughtful', 'smile'), ('boat', 'curious', 'smile'), ('boat', 'touched', 'smile')]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        assert eval amy_v11_art_ready()
        run Show("amy_v11_portrait_check", style=style, amy_mood=am, jack_mood=ja)
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot f"portrait_{style}_{am}_{ja}.png"
        run Hide("amy_v11_portrait_check")

    testcase visual_screens:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot "car_hub.png"
        run Show("amy_v11_drinks")
        screenshot "drinks.png"
        run Hide("amy_v11_drinks")
        $ renpy.amy_session_cards = ["time", "space", "rules"]
        $ amy_ch2_sync_cards()
        run Show("amy_v11_route_end", title="三条世界线")
        screenshot "cards.png"
        run Hide("amy_v11_route_end")
        run Show("amy_v11_continue_story")
        screenshot "true_continue.png"
        run Hide("amy_v11_continue_story")

    testcase cards_survive_new_play:
        run Start("amy_v11_time")
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "B 回主页面"
        skip until screen "main_menu"
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        assert eval persistent.amy_ch2_cards == ["time"]
        assert eval amy_ch2_completed == ["time"]
        assert "时间：如果我们十八岁就相遇【已收藏】"

    testcase full_memory:
        parameter name = ["time", "space", "rules", "ending"]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        if eval renpy.loadable("images/cg/amy_v11/wechat/" + name + ".png"):
            run Show("amy_ch2_memory", title="现实记忆", artwork="amy_ch2_memory_" + name, source_width=1000)
            $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
            screenshot f"memory_{name}.png"
            run Hide("amy_ch2_memory")

    testcase save_load_car_menu:
        run Start("amy_v11_date2")
        skip until screen "amy_v11_drinks"
        click "看完酒单，选择酒款"
        skip until screen "amy_v11_choice"
        click "试试 Gin：Aviation"
        skip until screen "amy_v11_drink_closeup"
        click "继续"
        skip until screen "amy_v11_choice"
        click "直接请工作人员打开"
        skip until screen "amy_v11_choice"
        assert eval amy_ch2_stats == {"love": 66, "wisdom": 70, "luck": 50}
        run FileSave("amy-v11-qa", confirm=False)
        $ amy_ch2_stats = {"love": 0, "wisdom": 0, "luck": 0}
        run FileLoad("amy-v11-qa", confirm=False)
        skip until screen "amy_v11_choice"
        assert eval amy_ch2_stats == {"love": 66, "wisdom": 70, "luck": 50}
        assert eval amy_v11_scene == "car"
        assert eval not amy_v11_actors
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")

    testcase stat_bounds_and_legacy_collection:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_stats = {"love": 98, "wisdom": 1, "luck": 50}
        $ amy_ch2_award_once("qa_cap", "love", 10, False)
        $ amy_ch2_award_once("qa_floor", "wisdom", -10, False)
        $ amy_ch2_award_once("qa_cap", "love", 10, False)
        assert eval amy_ch2_stats == {"love": 100, "wisdom": 0, "luck": 50}
        $ renpy.amy_session_cards = []
        $ persistent.amy_ch2_cards = ["time"]
        $ persistent.amy_ch2_endings = ["space"]
        $ amy_ch2_fragments = ["rules"]
        $ amy_ch2_sync_cards()
        assert eval persistent.amy_ch2_cards == []
        assert eval amy_ch2_completed == persistent.amy_ch2_endings

    testcase replay_from_settlement:
        run Start("amy_v11_time")
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "A 重新选择"
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "先带她办完新生手续"
        if eval amy_ch2_memory_available("time"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval amy_ch2_stats == {"love": 63, "wisdom": 55, "luck": 50}
        assert eval not amy_ch2_card_new
        assert eval persistent.amy_ch2_cards == ["time"]

    testcase relationship_threshold:
        parameter (expected_love, picks) = [(85, (0, 0, 0, 0, 1, 2, 2, 2, 2)), (86, (0, 0, 0, 0, 0, 2, 0, 2, 2)), (100, (0, 0, 0, 0, 0, 0, 1, 1, 1))]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ renpy.amy_session_cards = ["time", "space", "rules"]
        $ amy_ch2_sync_cards()
        $ amy_ch2_choices = {node: list(options)[pick] for (node, options), pick in zip(amy_v12_rewards.items(), picks)}
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats["love"] == expected_love
        assert eval amy_v12_true_ready() == (expected_love > 85)
        run Show("amy_v11_route_end", title="三条世界线")
        $ amy_v11_expected_totals = f"心动 {expected_love}    理智 {amy_ch2_stats['wisdom']}    幸运 {amy_ch2_stats['luck']}"
        assert eval amy_v11_expected_totals in renpy.get_widget("amy_v11_route_end", "amy_v11_totals_text").text
        if eval expected_love > 85:
            assert "C 真结局：人间"
            assert eval renpy.get_widget("amy_v11_route_end", "amy_v11_love_gate_hint") is None
        else:
            assert "C 真结局：尚未解锁"
            assert eval "心动达到 86，且高于另外两项，解锁人间" in renpy.get_widget("amy_v11_route_end", "amy_v11_love_gate_hint").text
            $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
            screenshot "cards_love_gate.png"
        run Hide("amy_v11_route_end")
        run Jump("amy_v11_hub")
        skip until screen "amy_v11_choice"
        if eval expected_love > 85:
            assert "隐藏结局「人间」"
        else:
            assert not "隐藏结局「人间」"
        $ renpy.amy_session_cards = ["time", "space"]
        $ amy_ch2_sync_cards()
        assert eval not amy_v12_true_ready()

    testcase ending_comparison_boundaries:
        parameter (scores, expected) = [((86, 86, 50), (False, False, False)), ((87, 82, 90), (False, False, True)), ((81, 82, 85), (False, True, True)), ((81, 82, 81), (False, True, False)), ((65, 60, 70), (False, False, True)), ((75, 75, 75), (False, False, True)), ((90, 80, 86), (True, False, False))]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ renpy.amy_session_cards = ["time", "space", "rules"]
        $ amy_ch2_sync_cards()
        $ amy_ch2_stats = dict(zip(("love", "wisdom", "luck"), scores))
        assert eval (amy_v12_true_ready(), amy_v12_friends_ready(), amy_v12_lottery_ready()) == expected

    testcase cg_album_replay:
        $ renpy.amy_session_seen_cgs = []
        click "CG 相册"
        assert not "03 相遇"
        click "关闭相册"
        run Start("amy_v11_finish_time")
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        click "CG 相册"
        skip until screen "amy_v11_album"
        assert eval renpy.amy_session_seen_cgs == [amy_v11_endings["time"][4]]
        assert not "17 下一站，世界"
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot "cg_album_partial.png"
        click "03 相遇"
        assert "返回相册"
        assert not "下载 CG"
        screenshot "cg_album_view.png"
        click "返回相册"
        click "关闭相册"
        click "B 回主页面"
        skip until screen "main_menu"
        click "CG 相册"
        assert "03 相遇"
        click "关闭相册"

    testcase alternate_endings:
        parameter (kind, picks, scores) = [("friends", (1, 1, 1, 1, 0, 0, 0, 0, 0), (91, 100, 50)), ("lottery", (0, 1, 2, 2, 2, 2, 2, 2, 0), (68, 65, 85))]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ renpy.amy_session_cards = ["time", "space", "rules"]
        $ amy_ch2_choices = {node: list(options)[pick] for (node, options), pick in zip(amy_v12_rewards.items(), picks)}
        run Jump("amy_v11_hub")
        skip until screen "amy_v11_choice"
        assert eval tuple(amy_ch2_stats[k] for k in ("love", "wisdom", "luck")) == scores
        assert "从约会重选"
        if eval kind == "friends":
            assert not "打开手套箱（彩蛋结局）"
            $ amy_ch2_selected_route = "time"
            run Jump("amy_v11_ending")
            skip until screen "amy_v11_route_end"
            click "C 一般结局：各自的世界"
            skip until screen "amy_v11_fusion"
            click "继续"
        else:
            assert not "一般结局：各自的世界"
            click "打开手套箱（彩蛋结局）"
        skip until screen "amy_v11_alternate_ending"
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot f"ending_{kind}.png"
        assert eval not amy_ch2_true_ending_seen
        assert not "返回车内"
        click "返回主菜单"
        skip until screen "main_menu"
        if eval kind == "lottery":
            assert eval renpy.amy_session_lottery_seen
            run Start("amy_v11_hub")
            skip until screen "amy_v11_choice"
            $ amy_ch2_choices = {node: list(options)[pick] for (node, options), pick in zip(amy_v12_rewards.items(), picks)}
            run Jump("amy_v11_hub")
            skip until screen "amy_v11_choice"
            assert eval amy_ch2_stats["luck"] == 85
            assert not "打开手套箱（彩蛋结局）"

    testcase direct_entry_guard:
        parameter entry = ["amy_v11_true", "amy_v11_fusion", "amy_v11_friends", "amy_v11_lottery"]
        $ renpy.amy_session_cards = ["time", "space", "rules"]
        $ amy_ch2_sync_cards()
        run Start(entry)
        skip until screen "amy_v11_choice"
        assert eval not amy_v12_true_ready()
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval amy_v11_scene == "car"

    testcase capped_score_replacement:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_choices = {'cocktail': '让 Jack 选一杯 Surprise Me', 'bookshelf': '两个人一起寻找机关', 'time_welcome': '陪她去吉他社试听', 'space_paris': '带 Ami 去挑一件巴黎的小礼物', 'space_market': '先保护本金，再争取收益', 'space_boundary': '每次出现前先问对方愿不愿意', 'rules_bridge': '建立可重复的物理测试', 'rules_stone': '和他一起推一次', 'rules_contract': '平等权限，各自拥有独立项目'}
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats["love"] == 100
        $ renpy.test.amy_score_before = dict(amy_ch2_stats)
        $ amy_v11_choose("cocktail", "wisdom", 10, "试试 Gin：Aviation")
        $ renpy.test.amy_score_swapped = dict(amy_ch2_stats)
        $ amy_v11_choose("cocktail", "wisdom", 10, "试试 Gin：Aviation")
        assert eval amy_ch2_stats == renpy.test.amy_score_swapped
        $ amy_v11_choose("cocktail", "luck", 5, "让 Jack 选一杯 Surprise Me")
        assert eval amy_ch2_stats == renpy.test.amy_score_before

    testcase legacy_choice_scoring:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_choices = {"cocktail": "gin", "bookshelf": "staff"}
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats == {"love": 66, "wisdom": 70, "luck": 50}
        $ amy_v11_choose("cocktail", "luck", 5, "让 Jack 选一杯 Surprise Me")
        assert eval amy_ch2_stats == {"love": 63, "wisdom": 60, "luck": 55}


    testcase session_cards_ignore_saved_collection:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_finish_world("time")
        run FileSave("amy-session-qa", confirm=False)
        $ renpy.amy_session_cards = []
        $ amy_ch2_sync_cards()
        run FileLoad("amy-session-qa", confirm=False)
        skip until screen "amy_v11_choice"
        assert eval persistent.amy_ch2_cards == []
        assert eval amy_ch2_completed == []
        assert eval amy_ch2_fragments == []

    testcase settlement_empty_slots_and_gain:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_v11_choose("time_welcome", "love", 5, "陪她去吉他社试听")
        pause 0.3
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot "choice_gain.png"
        assert eval amy_ch2_stats["love"] == 65
        assert eval renpy.get_screen("amy_v11_notice").scope["message"] == "心动 +5"
        $ amy_ch2_finish_world("time")
        $ amy_ch2_selected_route = "time"
        run Show("amy_v11_route_end")
        assert eval persistent.amy_ch2_cards == ["time"]
        assert "C 真结局：尚未解锁"
        assert eval renpy.get_widget("amy_v11_route_end", "amy_v11_love_gate_hint") is None
        assert eval "心动 65    理智 50    幸运 50" in renpy.get_widget("amy_v11_route_end", "amy_v11_totals_text").text
        screenshot "single_card.png"
        click "C 真结局：尚未解锁"
        pause 0.3
        assert eval renpy.get_screen("amy_v11_notice").scope["message"] == "集齐三个世界的记忆，并在选择中进一步靠近彼此。"
        run Hide("amy_v11_route_end")
        run Hide("amy_v11_notice")
        pause 0.6
        run Show("amy_v11_ending_hold", route="rules")
        screenshot "ending_clear_cg.png"
        run Hide("amy_v11_ending_hold")

    testcase creator_action_staging:
        run Start("amy_v11_rules")
        skip until eval _last_say_what == "[caption]"
        assert eval not renpy.showing("amy_v11_ami")
        assert eval not renpy.showing("amy_v11_jack")
        assert eval not renpy.get_screen("amy_v11_moment")
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa_v11"
        screenshot "creator_action.png"
        skip until screen "amy_v11_choice"
        assert eval renpy.showing("amy_v11_ami")
        assert eval renpy.showing("amy_v11_jack")

# Run these two suites in separate engine processes to verify a real relaunch.
testsuite amy_session_restart_seed:
    testcase seed:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_finish_world("time")
        $ amy_ch2_finish_world("space")
        $ amy_ch2_finish_world("rules")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_collect_cg(amy_v11_endings["time"][4])
        assert eval len(renpy.amy_session_seen_cgs) == 1
        $ persistent.amy_v11_seen_cgs = list(renpy.amy_session_seen_cgs)
        $ renpy.save_persistent()
        exit

testsuite amy_session_restart_verify:
    testcase cleared:
        assert eval renpy.amy_session_cards == []
        assert eval persistent.amy_ch2_cards == []
        assert eval renpy.amy_session_seen_cgs == []
        assert eval persistent.amy_v11_seen_cgs is None
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        assert not "时间：如果我们十八岁就相遇【已收藏】"
        assert eval amy_ch2_completed == []
        exit
