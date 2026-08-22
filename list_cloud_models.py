"""List cloud model files for key directories."""
import json
import os
import urllib.request
import base64
import sys

CRED = "XT11TL:bCu5w26jSI"
BASE = "https://wp08.unicorn.org.cn:11274"

def list_dir(folder):
    out = f"C:/Users/jwu40/Documents/trae_projects/Dakangtu/cloud_{folder.replace('/','_')}.json"
    if os.path.exists(out):
        with open(out, encoding='utf-8') as f:
            return json.load(f)
    req = urllib.request.Request(
        f"{BASE}/models/{folder}",
        headers={"Authorization": "Basic " + base64.b64encode(CRED.encode()).decode()},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.loads(r.read())
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return data

# Key directories we care about
folders = [
    "checkpoints",
    "diffusion_models",
    "unet_gguf",
    "clip_gguf",
    "text_encoders",
    "loras",
    "vae",
    "sam3",
    "ipadapter",
    "clip_vision",
    "controlnet",
]

for f in folders:
    try:
        files = list_dir(f)
        print(f"\n=== {f} ({len(files)} files) ===")
        # Filter for things relevant to our workflow
        keywords = ['anima', 'qwen', 'wan', 'flux', 'gguf', 'sam3', 'sam_3', 'vace', 'lora',
                    'illustrious', 'qwen_image', 'turbo', 'pose_studio', 'qie', 'qwenimage',
                    'relight', 'cn', 'control', 'ip-adapter', 'instantid', 'pulid']
        for x in files:
            xl = x.lower()
            if any(k in xl for k in keywords):
                print(f"  * {x}")
    except Exception as e:
        print(f"\n=== {f} ERROR ===\n  {e}")
