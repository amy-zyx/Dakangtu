"""
Cloud ComfyUI Batch Runner
==========================

Submits a workflow to the cloud ComfyUI instance, monitors progress,
and downloads the generated images to a local folder.

Usage:
    python tools/cloud_batch.py <workflow.json> [--count 4] [--outdir outputs/cloud]

The workflow JSON must be in the ComfyUI GUI format (nodes/widgets_values
format). It will be converted to API format automatically.
"""
import argparse
import base64
import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

CRED = "XT11TL:bCu5w26jSI"
BASE = "https://wp08.unicorn.org.cn:11274"

# Add tools dir to path so we can import workflow_to_api
TOOLS = Path(__file__).parent
sys.path.insert(0, str(TOOLS))
from workflow_to_api import to_api_prompt


def http_post_json(path: str, body: dict) -> dict:
    url = BASE + path
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Basic " + base64.b64encode(CRED.encode()).decode(),
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def http_get_json(path: str) -> dict:
    url = BASE + path
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Basic " + base64.b64encode(CRED.encode()).decode(),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def download_view(filename: str, out_path: Path, subfolder: str = "", type_: str = "output") -> bool:
    url = f"{BASE}/view?filename={urllib.parse.quote(filename)}&type={type_}"
    if subfolder:
        url += f"&subfolder={urllib.parse.quote(subfolder)}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": "Basic " + base64.b64encode(CRED.encode()).decode()},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        out_path.write_bytes(r.read())
    return True


def wait_for_completion(prompt_id: str, timeout_s: int = 600) -> dict:
    print(f"  等待 {prompt_id} 完成...")
    deadline = time.time() + timeout_s
    last_msg = ""
    while time.time() < deadline:
        try:
            h = http_get_json(f"/history/{prompt_id}")
            entry = h.get(prompt_id)
            if entry:
                st = entry.get("status", {})
                msg = f"  state={st.get('status_str', '?')} done={st.get('completed', False)}"
                if msg != last_msg:
                    print(msg)
                    last_msg = msg
                if st.get("completed"):
                    return entry
        except Exception as e:
            print(f"  poll error: {e}")
        time.sleep(3)
    raise TimeoutError(f"Prompt {prompt_id} not completed in {timeout_s}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workflow", help="GUI-format workflow JSON")
    ap.add_argument("--outdir", default="outputs/cloud", help="Local output dir")
    ap.add_argument("--timeout", type=int, default=900, help="Wait timeout (s)")
    ap.add_argument("--client-id", default="cloud-batch-client")
    args = ap.parse_args()

    with open(args.workflow, encoding="utf-8") as f:
        graph = json.load(f)
    prompt = to_api_prompt(graph)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"Submitting {args.workflow} ({len(prompt)} nodes) → {BASE}")
    submit_body = {
        "prompt": prompt,
        "client_id": args.client_id,
    }
    res = http_post_json("/prompt", submit_body)
    if "error" in res:
        print("ERROR:", json.dumps(res, indent=2, ensure_ascii=False)[:1500])
        sys.exit(1)
    prompt_id = res["prompt_id"]
    print(f"  prompt_id: {prompt_id}, queue #{res.get('number')}")

    entry = wait_for_completion(prompt_id, timeout_s=args.timeout)

    # Collect all output images
    downloaded = []
    for node_id, node_out in entry.get("outputs", {}).items():
        for k, v in node_out.items():
            if isinstance(v, list):
                for img in v:
                    if isinstance(img, dict) and "filename" in img:
                        fn = img["filename"]
                        sub = img.get("subfolder", "")
                        t = img.get("type", "output")
                        try:
                            local = outdir / fn
                            download_view(fn, local, sub, t)
                            print(f"  ↓ {local}")
                            downloaded.append(local)
                        except Exception as e:
                            print(f"  ! skip {fn}: {e}")

    if not downloaded:
        # Check error messages
        st = entry.get("status", {})
        for m in st.get("messages", []):
            if m[0] == "execution_error":
                print("EXECUTION ERROR:", json.dumps(m[1], indent=2, ensure_ascii=False)[:1500])
        sys.exit(1)
    print(f"Done. {len(downloaded)} files in {outdir}")


if __name__ == "__main__":
    main()
