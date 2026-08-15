# 一键生成 1x1 透明 PNG 占位文件的脚本
# 用于占位缺失的图片和音频资源

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
    """生成一个静音 OGG 占位文件（使用最小化的 OGG 格式）"""
    # 这里我们使用 Python 创建一个空文件
    # Ren'Py 会忽略无法播放的音频
    with open(path, 'wb') as f:
        f.write(b'')


# 资源清单
# 格式: (相对路径, 类型)
resources = [
    # 背景图
    ("game/images/bg/airport_terminal.png", "png"),
    ("game/images/bg/airport_arrival.png", "png"),
    ("game/images/bg/airport_cafe.png", "png"),
    ("game/images/bg/airport_window.png", "png"),
    ("game/images/bg/wellington_city.png", "png"),

    # 角色立绘 - 阿米
    ("game/images/characters/ami_normal.png", "png"),
    ("game/images/characters/ami_smile.png", "png"),
    ("game/images/characters/ami_surprised.png", "png"),
    ("game/images/characters/ami_blush.png", "png"),
    ("game/images/characters/ami_thinking.png", "png"),
    ("game/images/characters/ami_sad.png", "png"),

    # 角色立绘 - 杰克
    ("game/images/characters/jack_normal.png", "png"),
    ("game/images/characters/jack_smile.png", "png"),
    ("game/images/characters/jack_surprised.png", "png"),
    ("game/images/characters/jack_apologize.png", "png"),
    ("game/images/characters/jack_thinking.png", "png"),
    ("game/images/characters/jack_wave.png", "png"),

    # CG 图
    ("game/images/cg/cg_airport_meet.png", "png"),
    ("game/images/cg/cg_first_coffee.png", "png"),
    ("game/images/cg/cg_ending_act1.png", "png"),

    # 音频 - BGM
    ("game/audio/music/bgm_airport.ogg", "ogg"),
    ("game/audio/music/bgm_daily.ogg", "ogg"),
    ("game/audio/music/bgm_romantic.ogg", "ogg"),
    ("game/audio/music/bgm_dramatic.ogg", "ogg"),

    # 音频 - 音效
    ("game/audio/sound/sfx_airport_announce.ogg", "ogg"),
    ("game/audio/sound/sfx_luggage_drop.ogg", "ogg"),
    ("game/audio/sound/sfx_footsteps.ogg", "ogg"),
    ("game/audio/sound/sfx_cup.ogg", "ogg"),
    ("game/audio/sound/sfx_camera.ogg", "ogg"),
    ("game/audio/sound/sfx_wind.ogg", "ogg"),
]


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)

    for rel_path, file_type in resources:
        full_path = os.path.join(project_root, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        if file_type == "png":
            create_transparent_png(full_path)
            print(f"[PNG] Created: {rel_path}")
        elif file_type == "ogg":
            create_silent_ogg(full_path)
            print(f"[OGG] Created: {rel_path}")

    print(f"\nDone! Generated {len(resources)} placeholder files.")


if __name__ == "__main__":
    main()
