# 简单的 Ren'Py 脚本语法检查器
# 检查项目结构、引号配对、label/jump 对应等

import os
import re
import sys

# 设置 stdout 编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def check_file(filepath):
    """检查单个 .rpy 文件的基本语法问题"""
    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except UnicodeDecodeError:
        # 尝试其他编码
        with open(filepath, 'r', encoding='gbk') as f:
            content = f.read()
            lines = content.split('\n')

    # 1. 检查标签定义和跳转
    labels = set()
    jumps = []
    in_python_block = False

    for i, line in enumerate(lines, 1):
        # 跳过注释
        code_part = line.split('#')[0]

        # 跳过 Python init 块
        if re.match(r'\s*init\s+python\s*:', code_part):
            in_python_block = True
            continue
        if in_python_block:
            if re.match(r'^[a-zA-Z]', code_part) and not code_part.startswith(' '):
                in_python_block = False
            else:
                continue

        # 检查标签定义
        m = re.match(r'\s*label\s+(\w+)\s*:', code_part)
        if m:
            labels.add(m.group(1))

        # 检查跳转
        m = re.match(r'\s*jump\s+(\w+)', code_part)
        if m:
            jumps.append((i, m.group(1)))

    # 检查跳转目标是否存在
    for line_num, target in jumps:
        if target not in labels:
            errors.append(f"  [行{line_num}] 'jump {target}' 目标标签不存在")

    # 2. 检查中文引号
    for i, line in enumerate(lines, 1):
        if '"' in line:
            # 简单检查：未配对的双引号（粗略）
            if line.count('"') % 2 != 0:
                # 排除行内有 `\` 转义的情况
                warnings.append(f"  [行{i}] 可能有未闭合的引号")

    return errors, warnings


def main():
    game_dir = os.path.join(os.path.dirname(__file__), '..', 'game')

    print("=" * 60)
    print("Ren'Py 脚本语法检查")
    print("=" * 60)
    print(f"扫描目录: {os.path.abspath(game_dir)}\n")

    total_errors = 0
    total_warnings = 0

    for root, dirs, files in os.walk(game_dir):
        # 跳过 cache 和 saves 目录
        dirs[:] = [d for d in dirs if d not in ('cache', 'saves', 'tl', '__pycache__')]

        for file in files:
            if file.endswith('.rpy'):
                filepath = os.path.join(root, file)
                print(f"检查: {os.path.relpath(filepath, game_dir)}")
                errors, warnings = check_file(filepath)
                for err in errors:
                    print(f"  ❌ {err}")
                for warn in warnings:
                    print(f"  ⚠️  {warn}")
                total_errors += len(errors)
                total_warnings += len(warnings)
                if not errors and not warnings:
                    print(f"  ✅ OK")

    print("\n" + "=" * 60)
    if total_errors == 0:
        print(f"✅ 语法检查通过！({total_warnings} 个警告)")
    else:
        print(f"❌ 发现 {total_errors} 个错误，{total_warnings} 个警告")
    print("=" * 60)

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
