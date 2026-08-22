"""Convert ComfyUI GUI workflow JSON to API prompt format (VNCCS-aware)."""
import json
import sys
from pathlib import Path


# Map of node class -> primary JSON-config input name
JSON_CONFIG_INPUT = {
    "CharacterCreatorV2": "widget_data",
    "VNCCS_CharacterGenerator": "widget_data",
    "VNCCS_ClothesDesigner": "widget_data",
    "VNCCS_ClothesGenerator": "widget_data",
    "VNCCS_PoseStudio": "pose_data",
    "VNCCS_ControlCenter": "node_state",
    "VNCCS_MigrationAssistent": "node_state",
}

# Top-level required inputs that must NOT be inside the JSON blob.
TOP_LEVEL_BY_CLASS = {
    "VNCCS_ControlCenter": ["repo_id"],
}


def to_api_prompt(graph: dict) -> dict:
    """GUI workflow JSON -> {node_id: {class_type, inputs}} API dict."""
    nodes = graph.get("nodes", [])

    link_map = {}
    for link in graph.get("links", []):
        if not isinstance(link, list) or len(link) < 5:
            continue
        link_map[link[0]] = (link[1], link[2])

    prompt = {}
    for node in nodes:
        node_id = node.get("id")
        class_type = node.get("type") or node.get("class_type")
        if node_id is None or class_type is None:
            continue

        inputs = {}
        widget_values = list(node.get("widgets_values", []))
        widget_idx = 0

        for inp in node.get("inputs", []):
            name = inp.get("name")
            link = inp.get("link")
            if link is not None and link in link_map:
                from_id, from_idx = link_map[link]
                inputs[name] = [str(from_id), from_idx]
            else:
                if widget_idx < len(widget_values):
                    inputs[name] = widget_values[widget_idx]
                    widget_idx += 1

        for tl_name in TOP_LEVEL_BY_CLASS.get(class_type, []):
            if tl_name not in inputs and widget_idx < len(widget_values):
                inputs[tl_name] = widget_values[widget_idx]
                widget_idx += 1

        json_input = JSON_CONFIG_INPUT.get(class_type)
        remaining = [w for w in widget_values[widget_idx:] if w not in (None, "")]
        if json_input and remaining:
            if class_type == "CharacterCreatorV2":
                merged = {}
                for w in remaining:
                    if isinstance(w, str) and w.startswith("{"):
                        try:
                            obj = json.loads(w)
                            if isinstance(obj, dict):
                                merged.update(obj)
                                continue
                        except Exception:
                            pass
                    merged[f"_extra_{len(merged)}"] = w
                ci = merged.get("character_info")
                if isinstance(ci, dict) and "character" in merged:
                    if ci.get("name") and ci.get("name") != merged["character"]:
                        ci["name"] = merged["character"]
                        merged["character_info"] = ci
                inputs[json_input] = json.dumps(merged, ensure_ascii=False)
            else:
                extras = {}
                for w in remaining:
                    if isinstance(w, str) and w.startswith("{"):
                        try:
                            obj = json.loads(w)
                            if isinstance(obj, dict):
                                extras.update(obj)
                                continue
                        except Exception:
                            pass
                    extras[f"_extra_{len(extras)}"] = w
                inputs[json_input] = json.dumps(extras, ensure_ascii=False)

        prompt[str(node_id)] = {
            "class_type": class_type,
            "inputs": inputs,
        }
    return prompt


def submit(prompt_dict: dict, base_url: str, cred: str, extra_paths: list = None) -> dict:
    """Submit a prompt dict to ComfyUI /prompt API."""
    import urllib.request
    import urllib.error
    import base64

    url = base_url.rstrip("/") + "/prompt"
    body = json.dumps({"prompt": prompt_dict}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Basic " + base64.b64encode(cred.encode()).decode(),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "body": e.read().decode("utf-8", errors="replace")[:1500]}


def main():
    if len(sys.argv) < 2:
        print("usage: python workflow_to_api.py <input.json> [output.json]")
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    with open(src, encoding="utf-8") as f:
        graph = json.load(f)

    api_prompt = to_api_prompt(graph)
    out = {"prompt": api_prompt}
    s = json.dumps(out, ensure_ascii=False, indent=2)
    if dst:
        dst.write_text(s, encoding="utf-8")
        print(f"OK 写入 {dst} ({len(api_prompt)} nodes)")
    else:
        print(s)


if __name__ == "__main__":
    main()
