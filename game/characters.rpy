# 角色定义文件
# 阿米：女主角，从新加坡转机来新西兰的女生
# 杰克：男主角，来接人却迷路的本地大学生

# 阿米 - 温柔、有点路痴的亚洲女生
define am = Character("阿米",
    color="#ffb6c1",
    what_color="#ffffff"
)

# 杰克 - 阳光、礼貌的本地大学生
define jk = Character("杰克",
    color="#87ceeb",
    what_color="#ffffff"
)

# 旁白
define narrator = Character(None, what_color="#dddddd")

# 内心独白（用 narrator 但颜色不同）
# 在游戏中通过 "（xxx）" 实现内心独白
