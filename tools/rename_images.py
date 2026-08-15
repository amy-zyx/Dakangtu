# -*- coding: utf-8 -*-
# 重命名图片文件以匹配 Ren'Py 命名规范
# ami_normal.png → "ami normal.png"
# jack_normal.png → "jack normal.png"

import os
import shutil

game_images = os.path.join(os.path.dirname(__file__), '..', 'game', 'images')
game_images = os.path.abspath(game_images)

# 重命名规则
renames = [
    # 背景：airport_terminal.png → "airport terminal.png"
    ('bg', 'airport_terminal.png', 'airport terminal.png'),
    ('bg', 'airport_arrival.png', 'airport arrival.png'),
    ('bg', 'airport_cafe.png', 'airport cafe.png'),
    ('bg', 'airport_window.png', 'airport window.png'),
    ('bg', 'wellington_city.png', 'wellington city.png'),

    # 角色立绘：ami_normal.png → "ami normal.png"
    ('characters', 'ami_normal.png', 'ami normal.png'),
    ('characters', 'ami_smile.png', 'ami smile.png'),
    ('characters', 'ami_surprised.png', 'ami surprised.png'),
    ('characters', 'ami_blush.png', 'ami blush.png'),
    ('characters', 'ami_thinking.png', 'ami thinking.png'),
    ('characters', 'ami_sad.png', 'ami sad.png'),

    ('characters', 'jack_normal.png', 'jack normal.png'),
    ('characters', 'jack_smile.png', 'jack smile.png'),
    ('characters', 'jack_surprised.png', 'jack surprised.png'),
    ('characters', 'jack_apologize.png', 'jack apologize.png'),
    ('characters', 'jack_thinking.png', 'jack thinking.png'),
    ('characters', 'jack_wave.png', 'jack wave.png'),

    # CG
    ('cg', 'cg_airport_meet.png', 'airport meet.png'),
    ('cg', 'cg_first_coffee.png', 'first coffee.png'),
    ('cg', 'cg_ending_act1.png', 'ending act1.png'),
]

print("重命名图片文件...")
for subdir, old_name, new_name in renames:
    old_path = os.path.join(game_images, subdir, old_name)
    new_path = os.path.join(game_images, subdir, new_name)
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"  [OK] {subdir}/{old_name} → {new_name}")
    else:
        print(f"  [SKIP] {subdir}/{old_name} 不存在")

print()
print("完成！现在图片命名符合 Ren'Py 规范。")
