# Runtime regression tests for Chapter 2 v4.
init python:
    build.classify("game/amy_ch2_tests.rpy", None)
    build.classify("game/amy_ch2_tests.rpyc", None)

screen amy_ch2_portrait_check(amy_art, jack_art, background="amy_autumn_bar"):
    modal True
    zorder 150
    add Transform(background, size=(1920, 1080))
    add amy_art xalign 0.05 yalign 1.0
    add jack_art xalign 1.0 yalign 1.0

testsuite amy_ch2_v4:
    setup:
        $ renpy.test.amy_ch2_saved_cards = list(persistent.amy_ch2_cards or [])
    before testcase:
        $ persistent.amy_ch2_cards = []
    after testcase:
        run MainMenu(confirm=False)
        skip until screen "main_menu"
    teardown:
        $ persistent.amy_ch2_cards = renpy.test.amy_ch2_saved_cards
        $ renpy.save_persistent()
        exit

    testcase order_0:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase order_1:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase order_2:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase order_3:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase order_4:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase order_5:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "空间：一秒到任何地方"
        skip until screen "choice"
        click "每次见面都先问对方愿不愿意"
        if eval renpy.loadable("amy_private/ch2_memory_space.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_space"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "space" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "time" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")
        assert eval len(amy_ch2_fragments) == 3
        $ amy_ch2_test_stats = dict(amy_ch2_stats)
        click "时间：如果我们十八岁就相遇【卡牌已获得】"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_time"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval amy_ch2_stats == amy_ch2_test_stats
        assert eval len(amy_ch2_fragments) == 3
        click "合成三张卡牌，进入真结局"
        skip until screen "amy_ch2_fusion"
        click "继续"
        skip until screen "choice"
        click "留在这里"
        if eval renpy.loadable("amy_private/ch2_memory_poster.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_poster"
            click "继续"
        if eval renpy.loadable("amy_private/ch2_memory_ending.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_ending"
            click "继续"
        skip until "Act 3：雨落星河"
        assert eval act3_love == 0
        assert eval not renpy.get_screen("amy_ch2_status")
        assert eval amy_ch2_true_ending_seen
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")

    testcase choices_0_0:
        run Start("amy_act3")
        skip until screen "choice"
        click "让 Jack Surprise Me"
        skip until screen "choice"
        click "和 Jack 一起找到机关"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 70, 'wisdom': 50, 'luck': 50}

    testcase choices_0_1:
        run Start("amy_act3")
        skip until screen "choice"
        click "让 Jack Surprise Me"
        skip until screen "choice"
        click "请工作人员帮忙打开"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 60, 'wisdom': 60, 'luck': 50}

    testcase choices_0_2:
        run Start("amy_act3")
        skip until screen "choice"
        click "让 Jack Surprise Me"
        skip until screen "choice"
        click "尝试寻找，却没找到"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 60, 'wisdom': 50, 'luck': 50}

    testcase choices_1_0:
        run Start("amy_act3")
        skip until screen "choice"
        click "点 Gin，看看自己会不会流泪"
        skip until screen "choice"
        click "和 Jack 一起找到机关"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 60, 'wisdom': 60, 'luck': 50}

    testcase choices_1_1:
        run Start("amy_act3")
        skip until screen "choice"
        click "点 Gin，看看自己会不会流泪"
        skip until screen "choice"
        click "请工作人员帮忙打开"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 50, 'wisdom': 70, 'luck': 50}

    testcase choices_1_2:
        run Start("amy_act3")
        skip until screen "choice"
        click "点 Gin，看看自己会不会流泪"
        skip until screen "choice"
        click "尝试寻找，却没找到"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 50, 'wisdom': 60, 'luck': 50}

    testcase choices_2_0:
        run Start("amy_act3")
        skip until screen "choice"
        click "点平常喜欢的 Cocktail"
        skip until screen "choice"
        click "和 Jack 一起找到机关"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 60, 'wisdom': 50, 'luck': 60}

    testcase choices_2_1:
        run Start("amy_act3")
        skip until screen "choice"
        click "点平常喜欢的 Cocktail"
        skip until screen "choice"
        click "请工作人员帮忙打开"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 50, 'wisdom': 60, 'luck': 60}

    testcase choices_2_2:
        run Start("amy_act3")
        skip until screen "choice"
        click "点平常喜欢的 Cocktail"
        skip until screen "choice"
        click "尝试寻找，却没找到"
        skip until screen "choice"
        assert eval amy_ch2_doorOpened
        assert eval amy_ch2_stats == {'love': 50, 'wisdom': 50, 'luck': 60}

    testcase rules_options_0:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "想象都能成真"
        skip until screen "choice"
        click "让石头永远停在山顶"
        skip until screen "choice"
        click "相爱的人永不分开"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")

    testcase rules_options_1:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "谎言会被揭穿"
        skip until screen "choice"
        click "让他自己决定推不推"
        skip until screen "choice"
        click "相爱的人不能说谎"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")

    testcase rules_options_2:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "规则：创造一个新世界"
        skip until screen "choice"
        click "可以修改记忆"
        skip until screen "choice"
        click "给他一个伙伴一起推"
        skip until screen "choice"
        click "任何人都可以自由选择爱"
        if eval renpy.loadable("amy_private/ch2_memory_rules.png"):
            skip until screen "amy_ch2_memory"
            assert eval renpy.get_screen("amy_ch2_memory").scope["artwork"] == "amy_ch2_memory_rules"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval not renpy.showing("cg act3 kiss")
        click "再来一次"
        skip until screen "choice"
        assert eval "rules" in amy_ch2_fragments
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        assert eval not renpy.showing("cg act3 kiss")

    testcase reward_bounds:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        $ amy_ch2_award_once("test_limit", "love", 1000, False)
        assert eval amy_ch2_stats["love"] == 100
        $ amy_ch2_award_once("test_limit", "love", 1000, False)
        assert eval amy_ch2_stats["love"] == 100
        $ amy_ch2_award_once("test_floor", "love", -1000, False)
        assert eval amy_ch2_stats["love"] == 0

    testcase car_menu_legacy_overlay:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        run Show("amy_ch2_world_stage", place="悬浮方块世界")
        assert screen "amy_ch2_world_stage"
        $ amy_ch2_completed = ["time", "space", "rules"]
        $ amy_ch2_fragments = ["time", "space", "rules"]
        run Jump("amy_ch2_route_hub")
        skip until screen "choice"
        assert eval renpy.showing("amy_autumn_car")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="screens")
        assert eval not renpy.get_screen("amy_ch2_world_stage", layer="master")
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa"
        screenshot "car_menu.png"

    testcase portrait_frames:
        parameter (amy_expression, jack_expression, frame_name) = [
            ("smile", "curious", "smile"),
            ("tease", "laugh", "laugh"),
            ("thoughtful", "thoughtful", "thoughtful")
        ]
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        run Show("amy_ch2_portrait_check", amy_art="amy_ch2_ami " + amy_expression, jack_art="amy_ch2_jack " + jack_expression)
        assert screen "amy_ch2_portrait_check"
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa"
        screenshot f"portrait_{frame_name}.png"
        run Hide("amy_ch2_portrait_check")

    testcase full_memory_images:
        parameter (memory_name, image_width) = [
            ("time", 857), ("space", 850), ("rules", 691), ("ending", 1536), ("poster", 1152)
        ]
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        if eval renpy.loadable("amy_private/ch2_memory_" + memory_name + ".png"):
            run Show("amy_ch2_memory", title="回忆", artwork="amy_ch2_memory_" + memory_name, source_width=image_width)
            assert screen "amy_ch2_memory"
            $ _test.screenshot_directory = ".codex-remote-attachments/_qa"
            screenshot f"memory_full_{memory_name}.png"
            run Hide("amy_ch2_memory")

    testcase cards_survive_new_playthrough:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        click "主动约 Amy 逛校园"
        if eval renpy.loadable("amy_private/ch2_memory_time.png"):
            skip until screen "amy_ch2_memory"
            click "继续"
        skip until screen "amy_ch2_route_end"
        assert eval persistent.amy_ch2_cards == ["time"]
        click "返回主菜单"
        skip until screen "main_menu"
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        assert eval persistent.amy_ch2_cards == ["time"]
        assert eval amy_ch2_completed == ["time"]
        assert "时间：如果我们十八岁就相遇【卡牌已获得】"
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa"
        run Show("amy_ch2_route_end", title="获得时间卡牌")
        screenshot "cards_time.png"
        run Hide("amy_ch2_route_end")

    testcase school_uniforms:
        run Start("amy_ch2_route_hub")
        skip until screen "choice"
        click "时间：如果我们十八岁就相遇"
        skip until screen "choice"
        assert eval renpy.showing("amy_ch2_school_ami")
        assert eval renpy.showing("amy_ch2_school_jack")
        assert eval not renpy.showing("amy_ch2_ami")
        assert eval not renpy.showing("amy_ch2_jack")
        run Show("amy_ch2_portrait_check", amy_art="amy_ch2_school_ami", jack_art="amy_ch2_school_jack", background="images/backgrounds/amy_ch2/amy_time_welcome.png")
        $ _test.screenshot_directory = ".codex-remote-attachments/_qa"
        screenshot "portrait_school.png"
        run Hide("amy_ch2_portrait_check")
