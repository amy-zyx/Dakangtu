# -*- coding: utf-8 -*-
# 一键生成 1x1 透明 PNG 占位文件
# 重要规则（2026-08-15 踩坑总结）：
#   1. 所有图片必须放在 game/images/ 根目录，不要建子目录！
#   2. 图片名带空格时，必须在 .rpy 中显式声明：image xxx = "images/xxx.png"
#   3. 文件名和代码标签必须完全一致（包括空格、下划线、连字符）

import os
import struct
import zlib

def create_transparent_png(path):
    """生成一个 1x1 透明 PNG 文件"""
    # PNG 文件头
    png_signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk (图像头): 1x1 像素, 8位 RGBA
    ihdr_data = struct.pack('>IIBBBBB', 1, 1, 8, 6, 0, 0, 0)
    ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff
    ihdr_chunk = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)

    # IDAT chunk (图像数据): 1 个透明像素
    raw_data = b'\x00\x00\x00\x00\x00'  # filter byte + RGBA
    compressed = zlib.compress(raw_data)
    idat_crc = zlib.crc32(b'IDAT' + compressed) & 0xffffffff
    idat_chunk = struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)

    # IEND chunk (结束标记)
    iend_crc = zlib.crc32(b'IEND') & 0xffffffff
    iend_chunk = struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)

    # 写入文件
    with open(path, 'wb') as f:
        f.write(png_signature)
        f.write(ihdr_chunk)
        f.write(idat_chunk)
        f.write(iend_chunk)


def create_silent_ogg(path):
    """生成一个静音 OGG 占位文件（Ren'Py 会忽略无法播放的音频）"""
    with open(path, 'wb') as f:
        f.write(b'')


# 资源清单
# 注意：所有 PNG 都直接放在 game/images/ 根目录，不建子目录！
# 格式: (图片标签名, 文件名, 类型)
resources = [
    # 背景图
    ("bg airport_terminal", "airport_terminal.png", "png"),
    ("bg airport_arrival", "airport_arrival.png", "png"),
    ("bg airport_cafe", "airport_cafe.png", "png"),
    ("bg airport_window", "airport_window.png", "png"),
    ("bg wellington_city", "wellington_city.png", "png"),

    # 角色立绘 - 阿米（命名带空格，需要显式声明）
    ("ami normal", "ami normal.png", "png"),
    ("ami smile", "ami smile.png", "png"),
    ("ami surprised", "ami surprised.png", "png"),
    ("ami blush", "ami blush.png", "png"),
    ("ami thinking", "ami thinking.png", "png"),
    ("ami sad", "ami sad.png", "png"),

    # 角色立绘 - 杰克
    ("jack normal", "jack normal.png", "png"),
    ("jack smile", "jack smile.png", "png"),
    ("jack surprised", "jack surprised.png", "png"),
    ("jack apologize", "jack apologize.png", "png"),
    ("jack thinking", "jack thinking.png", "png"),
    ("jack wave", "jack wave.png", "png"),

    # CG 图
    ("cg airport_meet", "airport_meet.png", "png"),
    ("cg first_coffee", "first_coffee.png", "png"),
    ("cg ending_act1", "ending_act1.png", "png"),
]

# 音频资源（按类型分组）
audio_resources = {
    "music": [
        "bgm_airport.ogg",
        "bgm_daily.ogg",
        "bgm_romantic.ogg",
        "bgm_dramatic.ogg",
    ],
    "sound": [
        "sfx_airport_announce.ogg",
        "sfx_luggage_drop.ogg",
        "sfx_footsteps.ogg",
        "sfx_cup.ogg",
        "sfx_camera.ogg",
        "sfx_wind.ogg",
    ],
    "voice": [],
}


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)

    # 生成 PNG 图片（直接放 game/images/ 根目录）
    images_dir = os.path.join(project_root, "game", "images")
    os.makedirs(images_dir, exist_ok=True)

    print(f"图片输出目录: {images_dir}")
    print()

    for label, filename, _ in resources:
        full_path = os.path.join(images_dir, filename)
        create_transparent_png(full_path)
        print(f"  [PNG] {filename}  (label: '{label}')")

    # 生成 OGG 音频
    print()
    for subdir, files in audio_resources.items():
        audio_dir = os.path.join(project_root, "game", "audio", subdir)
        os.makedirs(audio_dir, exist_ok=True)
        for filename in files:
            full_path = os.path.join(audio_dir, filename)
            create_silent_ogg(full_path)
            print(f"  [OGG] audio/{subdir}/{filename}")

    # 生成 image 声明脚本（直接复制到 .rpy 文件顶部）
    print()
    print("=" * 60)
    print("建议在每个 .rpy 文件顶部加入以下 image 声明：")
    print("=" * 60)
    print()
    print("# ====== 图片显式声明（防 lint 报错） ======")
    for label, filename, _ in resources:
        print(f'image {label} = "images/{filename}"')

    print()
    print(f"完成！生成了 {len(resources)} 张图片和 {sum(len(f) for f in audio_resources.values())} 个音频。")


if __name__ == "__main__":
    main()
