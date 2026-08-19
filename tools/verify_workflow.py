# -*- coding: utf-8 -*-
"""验证 workflow JSON 的连接正确性"""
import json
import sys

def verify(workflow_file):
    with open(workflow_file, encoding="utf-8") as f:
        data = json.load(f)

    print("=" * 60)
    print(f"文件: {workflow_file}")
    print("=" * 60)

    nodes = {int(n["id"]): n for n in data["nodes"]}
    links = data["links"]

    print(f"\n[1] 节点列表 (共 {len(nodes)} 个):")
    for nid, n in sorted(nodes.items()):
        inp_names = [i["name"] for i in n["inputs"]]
        out_names = [o["name"] for o in n["outputs"]]
        title = n.get("title", n["type"])
        print(f"  节点 {nid:>2} [{title}]: in={inp_names}  out={out_names}")

    print(f"\n[2] 连接列表 (共 {len(links)} 条):")
    for link in links:
        link_id, src, src_slot, dst, dst_slot, link_type = link
        src = int(src)
        dst = int(dst)
        src_node = nodes.get(src, {})
        dst_node = nodes.get(dst, {})
        src_out_name = src_node.get("outputs", [{}])[src_slot].get("name", "?") if src_node and src_slot < len(src_node.get("outputs", [])) else "?"
        dst_in_name = dst_node.get("inputs", [{}])[dst_slot].get("name", "?") if dst_node and dst_slot < len(dst_node.get("inputs", [])) else "?"
        print(f"  link {link_id}: 节点 {src}.{src_out_name}({src_slot}) -> 节点 {dst}.{dst_in_name}({dst_slot}) [{link_type}]")

    print(f"\n[3] 验证:")
    errors = []
    for link in links:
        link_id, src, src_slot, dst, dst_slot, link_type = link
        src = int(src)
        dst = int(dst)
        if src not in nodes:
            errors.append(f"link {link_id}: src 节点 {src} 不存在")
        if dst not in nodes:
            errors.append(f"link {link_id}: dst 节点 {dst} 不存在")
        if src in nodes and src_slot >= len(nodes[src]["outputs"]):
            errors.append(f"link {link_id}: src 节点 {src} 没有 output slot {src_slot}")
        if dst in nodes and dst_slot >= len(nodes[dst]["inputs"]):
            errors.append(f"link {link_id}: dst 节点 {dst} 没有 input slot {dst_slot}")

    # 验证每个 input 都连接到了
    for nid, n in nodes.items():
        for i, inp in enumerate(n["inputs"]):
            if inp.get("type") != "WIDGET" and inp.get("link") is None:
                errors.append(f"节点 {nid} input '{inp['name']}' 未连接")

    if errors:
        print(f"  [ERR] 发现 {len(errors)} 个错误:")
        for e in errors:
            print(f"    - {e}")
        return False
    else:
        print(f"  [OK] 所有连接都正确!")
        return True

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else [
        "workflows/anima_turbo_workflow_v2.json"
    ]
    all_ok = True
    for f in files:
        if not verify(f):
            all_ok = False
    sys.exit(0 if all_ok else 1)
