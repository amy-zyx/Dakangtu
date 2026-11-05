# Engine regression and visual checks for the V11 chapter.
init python:
    build.classify("game/amy_ch2_tests.rpy", None)
    build.classify("game/amy_ch2_tests.rpyc", None)

screen amy_v11_portrait_check(style, amy_mood, jack_mood):
    modal True
    zorder 150
    add Transform(amy_v11_backgrounds["bar" if style == "date" else "welcome" if style == "campus" else "rooftop" if style == "creator" else "beach"], size=(1920, 1080))
    add amy_v11_portrait("ami", amy_mood, style) xalign 0.05 yalign 1.0
    add amy_v11_portrait("jack", jack_mood, style) xalign 1.0 yalign 1.0

testsuite amy_ch2_v11:
    setup:
        $ renpy.test.amy_v11_backup = (list(persistent.amy_ch2_cards or []), list(persistent.amy_ch2_endings or []), persistent.amy_ch2_true_ending_completed)
    before testcase:
        $ persistent.amy_ch2_cards = []
        $ persistent.amy_ch2_endings = []
        $ persistent.amy_ch2_true_ending_completed = False
    after testcase:
        run MainMenu(confirm=False)
        skip until screen "main_menu"
    teardown:
        $ persistent.amy_ch2_cards, persistent.amy_ch2_endings, persistent.amy_ch2_true_ending_completed = renpy.test.amy_v11_backup
        $ renpy.save_persistent()
        exit

    testcase order_0:
        run Start("amy_v11_start")
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
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "规则：创造一个新世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "建立可重复的物理测试"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "移走石头，邀请他探索世界"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click "平等权限，各自拥有独立项目"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "rules" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "空间：一秒到任何地方"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click "带 Amy 去挑一件巴黎的小礼物"
        skip until screen "amy_v11_moment"
        click "继续"
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
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        skip until screen "amy_v11_choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回 Tesla，选择另一个世界"
        skip until screen "amy_v11_choice"
        assert eval amy_v11_scene == "car"
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval len(persistent.amy_ch2_cards) == 3
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【已收藏】"
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        click "解锁隐藏结局「人间」"
        skip until screen "amy_v11_fusion"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
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
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
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
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_choice"
        click expression (['带 Amy 去挑一件巴黎的小礼物', '去左岸书店，各选一本书交换', '跟着街头音乐随机拐进一条小巷'][a])
        skip until screen "amy_v11_moment"
        click "继续"
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
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click expression (['建立可重复的物理测试', '先保护居民再试验', '用一次大胆的现场实验'][a])
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click expression (['移走石头，邀请他探索世界', '和他一起推一次', '把石头改造成会滚动的音乐舞台'][b])
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_choice"
        click expression (['平等权限，各自拥有独立项目', '共同建造一座可以自由进出的家', '让所有居民都能提出修改世界的建议'][c])
        skip until screen "amy_v11_moment"
        click "继续"
        skip until screen "amy_v11_moment"
        click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
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
        assert eval sum(amy_ch2_stats.values()) == 160 + (3 if drink != 0 else 0) + ([10, 13, 0][book])
        assert eval len(amy_ch2_awarded_nodes) == 2
        assert eval persistent.amy_ch2_cards == []

    testcase asset_and_frames:
        parameter (style, am, ja) = [('date', 'smile', 'laugh'), ('date', 'laugh', 'brow'), ('date', 'thoughtful', 'thoughtful'), ('date', 'blush', 'angry'), ('date', 'curious', 'curious'), ('campus', 'smile', 'smile'), ('campus', 'blush', 'laugh'), ('creator', 'smile', 'smile'), ('creator', 'curious', 'angry'), ('vacation', 'smile', 'smile')]
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
        $ persistent.amy_ch2_cards = ["time", "space", "rules"]
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
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval "time" in persistent.amy_ch2_cards
        assert eval persistent.amy_ch2_cards == persistent.amy_ch2_endings
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval not renpy.showing("cg act3 kiss")
        click "返回主菜单"
        skip until screen "main_menu"
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        assert eval persistent.amy_ch2_cards == ["time"]
        assert eval amy_ch2_completed == ["time"]
        assert "时间：如果我们十八岁就相遇【已收藏】"

    testcase full_memory:
        parameter name = ["time", "space", "rules", "poster", "ending"]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        if eval renpy.loadable("amy_private/ch2_memory_" + name + ".png"):
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
        assert eval amy_ch2_stats == {"love": 56, "wisdom": 70, "luck": 50}
        run FileSave("amy-v11-qa", confirm=False)
        $ amy_ch2_stats = {"love": 0, "wisdom": 0, "luck": 0}
        run FileLoad("amy-v11-qa", confirm=False)
        skip until screen "amy_v11_choice"
        assert eval amy_ch2_stats == {"love": 56, "wisdom": 70, "luck": 50}
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
        $ persistent.amy_ch2_cards = ["time"]
        $ persistent.amy_ch2_endings = ["space"]
        $ amy_ch2_fragments = ["rules"]
        $ amy_ch2_sync_cards()
        assert eval persistent.amy_ch2_cards == ["time", "space", "rules"]
        assert eval amy_ch2_completed == persistent.amy_ch2_endings

    testcase replay_from_settlement:
        run Start("amy_v11_time")
        skip until screen "amy_v11_choice"
        click "陪她去吉他社试听"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        $ amy_v11_test_stats = dict(amy_ch2_stats)
        click "再体验一次本结局"
        skip until screen "amy_v11_choice"
        click "先带她办完新生手续"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_v11_ending_hold"
        click "继续"
        skip until screen "amy_v11_route_end"
        assert eval amy_ch2_stats == {"love": 53, "wisdom": 55, "luck": 50}
        assert eval not amy_ch2_card_new
        assert eval persistent.amy_ch2_cards == ["time"]

    testcase relationship_threshold:
        parameter (expected_love, choices) = [(100, {'cocktail': '让 Jack 选一杯 Surprise Me', 'bookshelf': '两个人一起寻找机关', 'time_welcome': '陪她去吉他社试听', 'space_paris': '带 Amy 去挑一件巴黎的小礼物', 'space_market': '先保护本金，再争取收益', 'space_boundary': '每次出现前先问对方愿不愿意', 'rules_bridge': '建立可重复的物理测试', 'rules_stone': '和他一起推一次', 'rules_contract': '平等权限，各自拥有独立项目'}), (91, {'cocktail': '让 Jack 选一杯 Surprise Me', 'bookshelf': '两个人一起寻找机关', 'time_welcome': '陪她去吉他社试听', 'space_paris': '去左岸书店，各选一本书交换', 'space_market': '先保护本金，再争取收益', 'space_boundary': '把下一站交给彼此的共同记忆', 'rules_bridge': '用一次大胆的现场实验', 'rules_stone': '移走石头，邀请他探索世界', 'rules_contract': '让所有居民都能提出修改世界的建议'}), (90, {'cocktail': '让 Jack 选一杯 Surprise Me', 'bookshelf': '两个人一起寻找机关', 'time_welcome': '陪她去吉他社试听', 'space_paris': '去左岸书店，各选一本书交换', 'space_market': '留一小部分资金尝试新机会', 'space_boundary': '把下一站交给彼此的共同记忆', 'rules_bridge': '用一次大胆的现场实验', 'rules_stone': '移走石头，邀请他探索世界', 'rules_contract': '让所有居民都能提出修改世界的建议'})]
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ persistent.amy_ch2_cards = ["time", "space", "rules"]
        $ amy_ch2_choices = dict(choices)
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats["love"] == expected_love
        assert eval amy_v12_true_ready() == (expected_love > 90)
        run Jump("amy_v11_hub")
        skip until screen "amy_v11_choice"
        if eval expected_love > 90:
            assert "隐藏结局「人间」"
        else:
            assert not "隐藏结局「人间」"
        $ persistent.amy_ch2_cards = ["time", "space"]
        assert eval not amy_v12_true_ready()

    testcase direct_entry_guard:
        parameter entry = ["amy_v11_true", "amy_v11_fusion"]
        $ persistent.amy_ch2_cards = ["time", "space", "rules"]
        run Start(entry)
        skip until screen "amy_v11_choice"
        assert eval not amy_v12_true_ready()
        assert eval not persistent.amy_ch2_true_ending_completed
        assert eval amy_v11_scene == "car"

    testcase capped_score_replacement:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_choices = {'cocktail': '让 Jack 选一杯 Surprise Me', 'bookshelf': '两个人一起寻找机关', 'time_welcome': '陪她去吉他社试听', 'space_paris': '带 Amy 去挑一件巴黎的小礼物', 'space_market': '先保护本金，再争取收益', 'space_boundary': '每次出现前先问对方愿不愿意', 'rules_bridge': '建立可重复的物理测试', 'rules_stone': '和他一起推一次', 'rules_contract': '平等权限，各自拥有独立项目'}
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats["love"] == 100
        $ renpy.test.amy_score_before = dict(amy_ch2_stats)
        $ amy_v11_choose("cocktail", "wisdom", 10, "试试 Gin：Aviation")
        $ renpy.test.amy_score_swapped = dict(amy_ch2_stats)
        $ amy_v11_choose("cocktail", "wisdom", 10, "试试 Gin：Aviation")
        assert eval amy_ch2_stats == renpy.test.amy_score_swapped
        $ amy_v11_choose("cocktail", "love", 10, "让 Jack 选一杯 Surprise Me")
        assert eval amy_ch2_stats == renpy.test.amy_score_before

    testcase legacy_choice_scoring:
        run Start("amy_v11_hub")
        skip until screen "amy_v11_choice"
        $ amy_ch2_choices = {"cocktail": "gin", "bookshelf": "staff"}
        $ amy_v12_recalculate()
        assert eval amy_ch2_stats == {"love": 56, "wisdom": 70, "luck": 50}
        $ amy_v11_choose("cocktail", "love", 10, "让 Jack 选一杯 Surprise Me")
        assert eval amy_ch2_stats == {"love": 63, "wisdom": 60, "luck": 50}
