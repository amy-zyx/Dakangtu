# -*- coding: utf-8 -*-
"""深度搜索 ComfyUI 目录"""
import os, subprocess

# ComfyUI Desktop 真实位置 - 用 PowerShell 找
ps_cmd = """
Get-ChildItem -Path "C:\\Users\\jwu40" -Recurse -Depth 5 -Filter "workflows" -ErrorAction SilentlyContinue | Select-Object FullName
Get-ChildItem -Path "C:\\Users\\jwu40" -Recurse -Depth 5 -Filter "VNCCS*" -ErrorAction SilentlyContinue | Select-Object FullName
"""
r = subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True, text=True, timeout=60)
print("STDOUT:", r.stdout)
if r.stderr:
    print("STDERR:", r.stderr[:500])
