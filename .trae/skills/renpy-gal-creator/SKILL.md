---
name: "renpy-gal-creator"
description: "Helps create anime-style visual novels (gal games) with Ren'Py. Invoke when user asks to write Ren'Py scripts, add characters, create scenes, design choices, customize UI, or develop gal game content."
---

# Ren'Py Gal 游戏开发助手

本 skill 帮助创建动漫风格的 Galgame（视觉小说），基于 Ren'Py 引擎。

## 触发条件

当用户执行以下操作时调用此 skill：
- 要求编写或修改 Ren'Py 脚本（.rpy 文件）
- 添加新角色、场景、背景、立绘
- 创建对话分支、选项菜单、多结局
- 自定义 UI、GUI 样式、对话框
- 添加音乐、音效、转场效果
- 实现存档、变量、条件判断等游戏逻辑
- 询问 Ren'Py 语法或最佳实践

## 项目结构

```
game/
├── script.rpy          # 主脚本，游戏入口（label start:）
├── options.rpy         # 全局游戏配置（名称、版本、转场等）
├── gui.rpy             # GUI 样式配置（颜色、字体、尺寸等）
├── screens.rpy         # 自定义屏幕（菜单、对话框等）
├── tl/                 # 翻译文件目录
├── gui/                # GUI 图片资源
│   ├── button/
│   ├── bar/
│   ├── frame.png
│   ├── textbox.png
│   └── window_icon.png
├── images/             # 游戏图片资源（如未创建需新建）
│   ├── bg/             # 背景图 bg_xxx.png/jpg
│   ├── characters/     # 角色立绘（命名：角色_表情.png）
│   └── cg/             # 事件 CG 图
├── audio/              # 音频资源（如未创建需新建）
│   ├── music/          # BGM .ogg
│   ├── sound/          # 音效 .ogg
│   └── voice/          # 语音 .ogg
└── saves/              # 自动生成的存档目录
```

## 核心语法速查

### 1. 角色定义

```renpy
# 简单角色
define h = Character("花音", color="#ff99cc")

# 高级角色：带窗口样式、语音前缀等
define m = Character(
    "美月",
    color="#99ccff",
    what_color="#ffffff",
    window_background="gui/textbox.png",
    voice_tag="mizuki"
)

# 旁白（无名字）
define narrator = Character(None)
```

### 2. 图片定义

```renpy
# 背景图（无需显式定义，放在 images/ 下即可自动识别）
# 命名规则：bg room.png → scene bg room
# 命名规则：eileen happy.png → show eileen happy

# 显式定义（高级用法）
image bg school = "images/bg/school_day.jpg"
image bg school sunset = "images/bg/school_sunset.jpg"

# 角色立绘
image kaon happy = "images/characters/kaon_happy.png"
image kaon sad = "images/characters/kaon_sad.png"
image kaon blush:
    "images/characters/kaon_blush1.png"
    pause 0.2
    "images/characters/kaon_blush2.png"
    pause 0.2
    repeat
```

### 3. 场景与画面操作

```renpy
label start:
    # 切换背景（with 后接转场）
    scene bg school with dissolve

    # 显示立绘
    show kaon happy at left with dissolve

    # 隐藏立绘
    hide kaon with dissolve

    # 移动立绘
    show kaon happy at right with move

    # 显示 CG（全屏插画）
    scene cg first_date with Dissolve(1.0)
```

### 4. 对话与旁白

```renpy
# 角色对话
h "早上好，今天的天气真好呢！"
h "（他今天看起来好帅……）"  # 内心独白风格一
h "...{w=0.5}{nw}"  # 停顿 + 等待点击
m "你好，{color=#ff6666}花音同学{/color}。"  # 内联颜色

# 旁白
"那是一个樱花盛开的春天。"
"命运的齿轮，就此开始转动。"

# 自动排版标记
# {w}        等待玩家点击
# {w=1.0}    等待1秒后继续
# {nw}       显示后不要等待
# {fast}     瞬间显示剩余文字
# {p}        暂停，等同 {w}{nw}
# {p=1.0}    暂停1秒
# {cps=20}   临时改变文字速度
```

### 5. 选项菜单（分支核心）

```renpy
menu:
    "要和花音一起回家吗？"

    "当然一起走":
        h "太好了！那我们走吧~"
        $ flower_know_love += 1
        jump after_school_route1

    "今天还有事……":
        h "这样啊……那明天见。"
        jump after_school_route2

    "沉默不语":
        "我一时不知道该怎么回答。"
        jump after_school_route3

label after_school_route1:
    # ...剧情
```

### 6. 变量与条件判断

```renpy
# 初始化变量（游戏开始时）
default flower_know_love = 0
default mizuki_friendship = 0
default player_name = "同学"
default got_good_ending = False

# 修改变量
$ flower_know_love += 1
$ player_name = renpy.input("请输入你的名字：")

# 条件判断
if flower_know_love >= 5:
    h "其实……我一直很喜欢你！"
elif flower_know_love >= 3:
    h "和你在一起，我很开心。"
else:
    h "我们……算是朋友吧。"
```

### 7. 音乐与音效

```renpy
# 播放 BGM（循环）
play music "audio/music/school_daily.ogg" fadein 2.0

# 切换 BGM
play music "audio/music/romantic.ogg" fadeout 1.0 fadein 1.5

# 停止 BGM
stop music fadeout 2.0

# 播放音效（不循环）
play sound "audio/sound/school_bell.ogg"

# 队列音效（上一个播完再播）
queue sound "audio/sound/chime.ogg"

# 播放语音
m voice "mizuki_line001.ogg"
m "今天也要加油哦~"
```

### 8. 转场效果

```renpy
# 常用转场
with dissolve           # 0.5秒淡入淡出
with Dissolve(1.0)      # 1秒淡入淡出
with fade               # 全黑淡入淡出
with Fade(0.5, 0.0, 0.5)  # 自定义三阶段淡入淡出
with pixellate          # 像素化
with move               # 移动
with moveinleft         # 从左进入
with moveoutright       # 从右退出
with zoomin             # 放大进入
with shake              # 震动效果
with None               # 无转场
```

### 9. 屏幕与自定义 UI

```renpy
# 自定义 HUD 屏幕
screen affection_display:
    frame:
        xalign 0.98 yalign 0.02
        background None
        vbox:
            text "花音好感度：[flower_know_love]" color "#ff99cc" size 24
            text "美月友情：[mizuki_friendship]" color "#99ccff" size 24

# 在游戏中显示/隐藏
show screen affection_display
hide screen affection_display
```

### 10. 多结局结构模板

```renpy
label check_ending:
    if flower_know_love >= 8 and got_good_ending:
        jump ending_flower_true
    elif flower_know_love >= 5:
        jump ending_flower_good
    elif mizuki_friendship >= 6:
        jump ending_mizuki_friend
    else:
        jump ending_normal

label ending_flower_true:
    scene cg wedding with Dissolve(2.0)
    play music "audio/music/true_ending.ogg" fadein 2.0
    h "我会永远和你在一起。"
    "——TRUE END——"
    return
```

## 动漫风格 Galgame 开发最佳实践

### 角色设计
- 每个主要角色至少 4-5 种表情（普通/微笑/悲伤/害羞/惊讶/愤怒）
- 角色颜色需与性格匹配：粉色系=温柔、蓝色系=冷静、红色系=元气
- 使用 `color` 参数给角色名字上色，增强辨识度

### 剧情节奏
- 每 10-20 行对话插入一个选项或情绪转折
- 关键剧情前用转场/音乐/BGM 切换烘托气氛
- 内心独白使用括号或不同样式

### 画面构图
- 主要角色立绘位置：`at left` / `at right` / `at truecenter`
- 多人对话时注意立绘不重叠：`at left`, `at right`, `at center`
- 重要事件使用全屏 CG：`scene cg xxx`

### 音效氛围
- 每个场景配 BGM（日常/恋爱/紧张/悲伤等）
- 选项点击、开门、脚步声等使用 sound 效果
- 关键台词可配语音 voice

### GUI 动漫风建议
```renpy
# gui.rpy 中可修改：
define gui.accent_color = '#ffb6d9'    # 粉紫强调色
define gui.text_color = '#ffffff'
define gui.name_text_size = 48
define gui.text_size = 32
define gui.text_font = "SourceHanSansLite.ttf"
```

## 常见任务代码模板

### 角色介绍序章
```renpy
label prologue:
    scene black
    play music "audio/music/title.ogg" fadein 3.0
    with Pause(2.0)
    scene bg school_entrance with dissolve
    "春天，樱花飞舞的季节。"
    "我站在校门口，看着来来往往的学生。"
    show kaon normal at right with dissolve
    h "啊！你是新生吧？我叫花音，是你的同班同学哦！"
    return
```

### 好感度选项系统
```renpy
label lunch_choice:
    menu:
        "午饭要和谁一起吃？"

        "和花音一起":
            $ flower_know_love += 2
            jump lunch_with_kaon

        "和美月一起":
            $ mizuki_friendship += 2
            jump lunch_with_mizuki

        "一个人吃":
            jump lunch_alone
```

### 自定义主菜单修改
在 `screens.rpy` 中找到 `screen main_menu:`，修改背景：
```renpy
screen main_menu():
    tag menu
    style_prefix "main_menu"
    add "gui/main_menu_bg.png"  # 添加动漫风主菜单背景图
    # ...其他内容
```

## 调试与验证

- 修改脚本后按 `Shift+R` 在游戏中重载
- 按 `Shift+D` 打开开发者菜单
- 按 `Shift+O` 打开控制台（可输入 Python 表达式）
- 变量值可用 `[variable_name]` 在对话中查看

## 注意事项

1. 图片命名务必一致：`bg school.jpg` → `scene bg school`
2. 所有 .rpy 文件缩进必须使用 4 个空格
3. `default` 声明的变量可被存档保存；`define` 是常量
4. 音频推荐使用 OGG 格式（兼容性最佳）
5. 大项目建议拆分多个 .rpy 文件：`characters.rpy`、`chapter1.rpy`、`chapter2.rpy` 等
6. 修改 `gui.rpy` 后需在游戏中选择「重新生成 GUI」图片或手动生成

## 常用资源网站（可选）

- 背景/立绘：itch.io (搜索 renpy assets)
- 免费 BGM：Dova-Syndrome、魔王魂
- 音效：freesound.org
- 字体：思源黑体（Source Han Sans）、站酷快乐体
