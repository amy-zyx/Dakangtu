"""Wait for prompt 47cb21b1-f073-43c7-ac7e-13197c7e40da to finish and report results."""
import json
import urllib.request
import time
import os

PROMPT_ID = "47cb21b1-f073-43c7-ac7e-13197c7e40da"
URL = f"http://127.0.0.1:8188/history/{PROMPT_ID}"
COMFY_SHARED = r"C:\Users\jwu40\AppData\Local\Comfy-Desktop\ComfyUI-Shared"

print(f"Waiting for prompt {PROMPT_ID}...")
last_state = None
for i in range(150):  # 12.5 min max
    try:
        h = json.loads(urllib.request.urlopen(URL, timeout=10).read())
        if PROMPT_ID in h:
            entry = h[PROMPT_ID]
            status = entry.get('status', {})
            s_str = status.get('status_str')
            done = status.get('completed')
            errs = status.get('messages', [])
            if s_str != last_state or done:
                last_state = s_str
                print(f"  [{i*5}s] state={s_str} completed={done}")
            if done:
                if s_str == 'error':
                    for m in errs:
                        if m[0] == 'execution_error':
                            print(f"  ERROR: {m[1].get('exception_message','')[:400]}")
                            print(f"  node: {m[1].get('node_id')} type: {m[1].get('node_type')}")
                # check outputs
                out_798 = entry.get('outputs', {}).get('798', {})
                print(f"  outputs(798): {list(out_798.keys()) if out_798 else 'none'}")
                # also check 797 (CharacterCreatorV2 produces the preview)
                out_797 = entry.get('outputs', {}).get('797', {})
                print(f"  outputs(797): {list(out_797.keys()) if out_797 else 'none'}")
                for k, v in out_798.items():
                    if isinstance(v, list) and v and isinstance(v[0], dict) and 'filename' in v[0]:
                        print(f"  798.{k} files:")
                        for img in v:
                            print(f"    {img}")
                for k, v in out_797.items():
                    if isinstance(v, list) and v and isinstance(v[0], dict) and 'filename' in v[0]:
                        print(f"  797.{k} files:")
                        for img in v:
                            print(f"    {img}")
                break
    except Exception as e:
        print(f"  [{i*5}s] waiting... ({e})")
    time.sleep(5)
else:
    print("TIMEOUT after 12.5 min")
