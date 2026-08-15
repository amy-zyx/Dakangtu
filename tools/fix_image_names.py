# -*- coding: utf-8 -*-
# 批量替换 act1.rpy 中的图片引用
# image_airport_xxx → bg airport_xxx
# image_jack_xxx    → jack_xxx
# image_ami_xxx     → ami_xxx
# image_cg_xxx      → cg xxx

import re
import os

filepath = os.path.join(os.path.dirname(__file__), '..', 'game', 'act1.rpy')
filepath = os.path.abspath(filepath)

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换规则
# 1. image_airport_xxx → bg airport_xxx
content = re.sub(r'\bimage_airport_(\w+)', r'bg airport_\1', content)
# 2. image_jack_xxx → jack_xxx
content = re.sub(r'\bimage_jack_(\w+)', r'jack \1', content)
# 3. image_ami_xxx → ami_xxx
content = re.sub(r'\bimage_ami_(\w+)', r'ami \1', content)
# 4. image_cg_xxx → cg xxx
content = re.sub(r'\bimage_cg_(\w+)', r'cg \1', content)
# 5. show image_xxx → show xxx
# 6. scene image_xxx → scene xxx

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"已修复: {filepath}")
print("替换规则：")
print("  scene image_airport_xxx  → scene bg airport_xxx")
print("  show image_jack_xxx      → show jack xxx")
print("  show image_ami_xxx       → show ami xxx")
print("  scene image_cg_xxx       → scene cg xxx")
