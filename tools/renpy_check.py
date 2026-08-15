# 使用 Ren'Py 自身的解析器来检查脚本
# 这会模拟 Ren'Py 实际加载游戏时的行为

import os
import sys
import subprocess

def main():
    sdk_dir = r"C:\Users\jwu40\Downloads\renpy-8.5.3-sdk"
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 使用 Ren'Py 的 check_script 命令
    # 这个命令在 Ren'Py 8 中可用
    renpy_exe = os.path.join(sdk_dir, "renpy.exe")

    print("=" * 60)
    print("Ren'Py 脚本解析检查")
    print("=" * 60)
    print(f"SDK: {sdk_dir}")
    print(f"项目: {project_dir}")
    print()

    # 尝试不同的 Ren'Py 命令
    commands = [
        [renpy_exe, project_dir, "check_scripts"],
        [renpy_exe, project_dir, "lint"],
        [renpy_exe, project_dir, "compile"],
    ]

    for cmd in commands:
        print(f"尝试: {' '.join(cmd)}")
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                encoding='utf-8',
                errors='replace'
            )
            print(f"退出码: {result.returncode}")
            if result.stdout:
                print(f"输出: {result.stdout[:1000]}")
            if result.stderr:
                print(f"错误: {result.stderr[:1000]}")
        except subprocess.TimeoutExpired:
            print("超时")
        except Exception as e:
            print(f"异常: {e}")
        print()


if __name__ == "__main__":
    main()
