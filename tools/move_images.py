# -*- coding: utf-8 -*-
# 将图片从子目录移动到 images/ 根目录
# Ren'Py 8 的图片查找不递归子目录

import os
import shutil

game_images = os.path.join(os.path.dirname(__file__), '..', 'game', 'images')
game_images = os.path.abspath(game_images)

print("移动图片到正确位置...")
print(f"源目录: {game_images}\n")

moves = [
    # (源路径, 目标文件名)
    ('bg/airport_terminal.png', 'airport_terminal.png'),
    ('bg/airport_arrival.png', 'airport_arrival.png'),
    ('bg/airport_cafe.png', 'airport_cafe.png'),
    ('bg/airport_window.png', 'airport_window.png'),
    ('bg/wellington_city.png', 'wellington_city.png'),

    ('characters/ami normal.png', 'ami normal.png'),
    ('characters/ami smile.png', 'ami smile.png'),
    ('characters/ami surprised.png', 'ami surprised.png'),
    ('characters/ami blush.png', 'ami blush.png'),
    ('characters/ami thinking.png', 'ami thinking.png'),
    ('characters/ami sad.png', 'ami sad.png'),

    ('characters/jack normal.png', 'jack normal.png'),
    ('characters/jack smile.png', 'jack smile.png'),
    ('characters/jack surprised.png', 'jack surprised.png'),
    ('characters/jack apologize.png', 'jack apologize.png'),
    ('characters/jack thinking.png', 'jack thinking.png'),
    ('characters/jack wave.png', 'jack wave.png'),

    ('cg/airport_meet.png', 'airport_meet.png'),
    ('cg/first_coffee.png', 'first_coffee.png'),
    ('cg/ending_act1.png', 'ending_act1.png'),
]

for src_rel, dst_name in moves:
    src = os.path.join(game_images, src_rel)
    dst = os.path.join(game_images, dst_name)

    if os.path.exists(src):
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(src, dst)
        print(f"  [OK] {src_rel} -> {dst_name}")
    else:
        print(f"  [SKIP] {src_rel} 不存在")

# 清理空的子目录
for subdir in ['bg', 'characters', 'cg']:
    subdir_path = os.path.join(game_images, subdir)
    if os.path.exists(subdir_path) and not os.listdir(subdir_path):
        os.rmdir(subdir_path)
        print(f"\n  [CLEANUP] 删除空目录: {subdir}/")

print("\n完成！")
