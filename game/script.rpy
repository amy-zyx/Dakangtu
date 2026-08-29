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

    "希望你喜欢这个故事。"
    with Pause(2.0)

    # 跳转到第一幕
    jump act1

