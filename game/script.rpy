# 《大康兔》主脚本
# Dakangtu - Main Script

# ====== 角色定义 ======
# 详细定义见 characters.rpy
# 阿米 = am
# 杰克 = jk
# 旁白 = narrator

# ====== 包含其他脚本文件 ======
# 这些文件会在游戏启动时被自动加载
# characters.rpy - 角色定义
# variables.rpy - 变量定义
# act1.rpy - 第一幕剧情

# ====== 游戏入口 ======
label start:
    # 显示游戏开场画面
    scene black
    with Pause(1.0)

    "——《大康兔》——"
    "一个发生在惠灵顿的爱情故事"
    with Pause(2.0)

    # 跳转到第一幕
    jump act1_meeting


# ====== 调试用：快速跳转到第一幕 ======
label debug_act1:
    jump act1_meeting

# ====== 调试用：跳转到第一幕末尾 ======
label debug_act1_end:
    $ ami_love = 5
    $ jack_love = 3
    $ met_at_airport = True
    $ helped_with_luggage = True
    $ shared_coffee = True
    jump act1_pick_luggage
