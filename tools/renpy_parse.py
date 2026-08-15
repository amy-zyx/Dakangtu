# -*- coding: utf-8 -*-
# 通过 Ren'Py 自带的 python 解释器加载并解析脚本
# 调用方法：
# "C:\Users\jwu40\Downloads\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" tools/renpy_parse.py

import sys
import os

# 切换到项目目录
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(project_dir)

# 添加 Ren'Py SDK 路径
sdk_dir = r"C:\Users\jwu40\Downloads\renpy-8.5.3-sdk"
sys.path.insert(0, sdk_dir)

try:
    # 直接导入 renpy 内部的 ast 模块
    from renpy.ast import parse
    from renpy.lexer import lex

    print("=" * 60)
    print("Ren'Py 脚本解析检查")
    print("=" * 60)

    game_dir = os.path.join(project_dir, "game")
    rpy_files = []

    for root, dirs, files in os.walk(game_dir):
        dirs[:] = [d for d in dirs if d not in ('cache', 'saves', 'tl', '__pycache__')]
        for file in files:
            if file.endswith('.rpy') and not file.endswith('.rpy.bak'):
                rpy_files.append(os.path.join(root, file))

    print(f"找到 {len(rpy_files)} 个 .rpy 文件")
    print()

    all_ok = True
    for filepath in rpy_files:
        rel_path = os.path.relpath(filepath, project_dir)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read()

            # 词法分析
            tokens = lex(source)
            # 语法分析
            ast = parse(tokens)

            print(f"[OK] {rel_path}")
        except Exception as e:
            print(f"[FAIL] {rel_path}")
            print(f"       {type(e).__name__}: {e}")
            all_ok = False

    print()
    print("=" * 60)
    if all_ok:
        print("[OK] 所有脚本解析成功！")
    else:
        print("[FAIL] 部分脚本有错误，请修复后重试")
    print("=" * 60)

    sys.exit(0 if all_ok else 1)

except ImportError as e:
    print(f"无法导入 renpy 模块: {e}")
    print("请使用 Ren'Py 自带的 Python 解释器运行此脚本：")
    print(f'  "{sdk_dir}\\lib\\py3-windows-x86_64\\python.exe" tools/renpy_parse.py')
    sys.exit(1)
