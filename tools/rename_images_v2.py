# -*- coding: utf-8 -*-
# 重命名图片文件 - 最终正确版本
# 规则：
#   scene bg airport_terminal  → 查找 bg/airport_terminal.png
#   show ami normal           → 查找 characters/ami normal.png
#   scene cg ending_act1      → 查找 cg/ending_act1.png

import os
import shutil

game_images = os.path.join(os.path.dirname(__file__), '..', 'game', 'images')
game_images = os.path.abspath(game_images)

# 目标命名（最终正确版本）
final_names = {
    'bg': [
        'airport_terminal.png',
        'airport_arrival.png',
        'airport_cafe.png',
        'airport_window.png',
        'wellington_city.png',
    ],
    'characters': [
        'ami normal.png',
        'ami smile.png',
        'ami surprised.png',
        'ami blush.png',
        'ami thinking.png',
        'ami sad.png',
        'jack normal.png',
        'jack smile.png',
        'jack surprised.png',
        'jack apologize.png',
        'jack thinking.png',
        'jack wave.png',
    ],
    'cg': [
        'airport_meet.png',
        'first_coffee.png',
        'ending_act1.png',
    ],
}

print("重命名图片文件...")
for subdir, files in final_names.items():
    subdir_path = os.path.join(game_images, subdir)
    if not os.path.exists(subdir_path):
        print(f"  [SKIP] {subdir}/ 目录不存在")
        continue

    # 获取当前所有文件
    current_files = os.listdir(subdir_path)
    print(f"\n{subdir}/ 目录当前文件: {current_files}")

    # 智能匹配：包含目标文件名的关键字就重命名
    for target in files:
        target_path = os.path.join(subdir_path, target)
        if os.path.exists(target_path):
            print(f"  [OK] 已有: {target}")
            continue

        # 找最接近的源文件
        base = os.path.splitext(target)[0]  # 去掉 .png
        # 移除下划线和空格都尝试
        candidates = [
            base.replace('_', '_'),  # 已经是下划线
            base.replace('_', ' '),  # 空格版本
        ]

        found = False
        for src_name in current_files:
            src_base = os.path.splitext(src_name)[0]
            # 检查源文件名是否包含目标关键字
            keywords = base.split('_')
            if all(kw.lower() in src_base.lower() for kw in keywords):
                src_path = os.path.join(subdir_path, src_name)
                shutil.move(src_path, target_path)
                print(f"  [RENAME] {src_name} -> {target}")
                found = True
                break

        if not found:
            print(f"  [WARN] 未找到源文件: {target}")

print()
print("完成！")
