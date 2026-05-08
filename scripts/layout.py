#!/usr/bin/env python3

import argparse
import json
import math
import shlex
import subprocess
import sys
from collections import defaultdict, deque
from typing import Dict, Iterable, List, Sequence, Tuple

PIXELS_PER_INCH = 72.0
DEFAULT_DIRECTION = "TD"
DEFAULT_H_GAP = 80.0
DEFAULT_V_GAP = 100.0
CANVAS_PADDING = 40.0
GROUP_PADDING = 20.0
GROUP_TITLE_HEIGHT = 32.0
DEFAULT_NODE_WIDTH = 160.0
DEFAULT_NODE_HEIGHT = 50.0
VALID_DIRECTIONS = {"TD", "LR", "BT", "RL"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read graph JSON from stdin and emit positioned JSON to stdout."
    )
    parser.add_argument(
        "--direction",
        choices=sorted(VALID_DIRECTIONS),
        help="Layout direction override (TD, LR, BT, RL).",
    )
    parser.add_argument(
        "--spacing",
        type=parse_spacing,
        help="Optional spacing override as h_gap,v_gap (for example: 80,100).",
    )
    return parser.parse_args()


def parse_spacing(value: str) -> Tuple[float, float]:
    parts = [part.strip() for part in value.split(",")]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("spacing must be formatted as h_gap,v_gap")
    try:
        h_gap = float(parts[0])
        v_gap = float(parts[1])
    except ValueError as exc:
        raise argparse.ArgumentTypeError("spacing values must be numeric") from exc
    if h_gap <= 0 or v_gap <= 0:
        raise argparse.ArgumentTypeError("spacing values must be positive")
    return h_gap, v_gap


def emit_error(message: str, exit_code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(exit_code)


def round_number(value: float) -> int:
    return int(round(value))


def normalize_direction(value: str) -> str:
    direction = (value or DEFAULT_DIRECTION).upper()
    return direction if direction in VALID_DIRECTIONS else DEFAULT_DIRECTION


def load_graph(stdin_text: str) -> dict:
    if not stdin_text.strip():
        emit_error("Error: expected JSON graph description on stdin.")
    try:
        data = json.loads(stdin_text)
    except json.JSONDecodeError as exc:
        emit_error(f"Error: malformed JSON: {exc}")
    if not isinstance(data, dict):
        emit_error("Error: input JSON must be an object.")
    return data


def normalize_graph(data: dict, args: argparse.Namespace) -> dict:
    direction = normalize_direction(args.direction or data.get("direction") or DEFAULT_DIRECTION)
    spacing = args.spacing or (DEFAULT_H_GAP, DEFAULT_V_GAP)

    raw_nodes = data.get("nodes") or []
    raw_edges = data.get("edges") or []
    raw_groups = data.get("groups") or []

    if not isinstance(raw_nodes, list) or not isinstance(raw_edges, list) or not isinstance(raw_groups, list):
        emit_error("Error: nodes, edges, and groups must be arrays.")

    nodes = []
    seen_ids = set()
    for raw_node in raw_nodes:
        if not isinstance(raw_node, dict):
            emit_error("Error: each node must be an object.")
        node_id = str(raw_node.get("id", "")).strip()
        if not node_id:
            emit_error("Error: every node requires a non-empty id.")
        if node_id in seen_ids:
            emit_error(f"Error: duplicate node id: {node_id}")
        seen_ids.add(node_id)
        width = positive_number(raw_node.get("width", DEFAULT_NODE_WIDTH), "node width", node_id)
        height = positive_number(raw_node.get("height", DEFAULT_NODE_HEIGHT), "node height", node_id)
        nodes.append(
            {
                "id": node_id,
                "label": str(raw_node.get("label", node_id)),
                "width": width,
                "height": height,
            }
        )

    node_ids = {node["id"] for node in nodes}
    edges = []
    for raw_edge in raw_edges:
        if not isinstance(raw_edge, dict):
            emit_error("Error: each edge must be an object.")
        source = str(raw_edge.get("source", "")).strip()
        target = str(raw_edge.get("target", "")).strip()
        if not source or not target:
            emit_error("Error: every edge requires source and target.")
        if source not in node_ids or target not in node_ids:
            emit_error(f"Error: edge references unknown node: {source}->{target}")
        edge = {"source": source, "target": target}
        for key in ("label", "id"):
            if key in raw_edge:
                edge[key] = raw_edge[key]
        edges.append(edge)

    groups = []
    for raw_group in raw_groups:
        if not isinstance(raw_group, dict):
            emit_error("Error: each group must be an object.")
        group_id = str(raw_group.get("id", "")).strip()
        if not group_id:
            emit_error("Error: every group requires a non-empty id.")
        members = [str(member).strip() for member in raw_group.get("members", []) if str(member).strip()]
        for member in members:
            if member not in node_ids:
                emit_error(f"Error: group {group_id} references unknown node: {member}")
        groups.append(
            {
                "id": group_id,
                "label": str(raw_group.get("label", group_id)),
                "members": members,
            }
        )

    return {
        "direction": direction,
        "spacing": {"h_gap": spacing[0], "v_gap": spacing[1]},
        "nodes": nodes,
        "edges": edges,
        "groups": groups,
    }


def positive_number(value: object, field_name: str, context: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        emit_error(f"Error: {field_name} for {context} must be numeric.")
    if number <= 0:
        emit_error(f"Error: {field_name} for {context} must be positive.")
    return number


def dot_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_dot(graph: dict) -> str:
    h_gap = graph["spacing"]["h_gap"] / PIXELS_PER_INCH
    v_gap = graph["spacing"]["v_gap"] / PIXELS_PER_INCH
    lines = [
        "digraph G {",
        f"  graph [rankdir={graph['direction']}, nodesep={h_gap:.4f}, ranksep={v_gap:.4f}, pad=0, margin=0, splines=polyline];",
        '  node [shape=box, fixedsize=true, margin=0, style="rounded,filled", color="#cbd5e1", fillcolor="#ffffff", fontname="Arial"];',
        '  edge [color="#64748b"];',
    ]

    group_members = {member for group in graph["groups"] for member in group["members"]}
    for group in graph["groups"]:
        lines.append(f"  subgraph {dot_quote('cluster_' + group['id'])} {{")
        lines.append(f"    label={dot_quote(group['label'])};")
        lines.append('    style="rounded,dashed";')
        lines.append('    color="#cbd5e1";')
        for member in group["members"]:
            lines.append(f"    {dot_quote(member)};")
        lines.append("  }")

    for node in graph["nodes"]:
        if node["id"] not in group_members:
            lines.append(f"  {dot_quote(node['id'])};")
        width_inches = node["width"] / PIXELS_PER_INCH
        height_inches = node["height"] / PIXELS_PER_INCH
        lines.append(
            f"  {dot_quote(node['id'])} [label={dot_quote(node['label'])}, width={width_inches:.4f}, height={height_inches:.4f}];"
        )

    for edge in graph["edges"]:
        if edge.get("label"):
            lines.append(
                f"  {dot_quote(edge['source'])} -> {dot_quote(edge['target'])} [label={dot_quote(str(edge['label']))}];"
            )
        else:
            lines.append(f"  {dot_quote(edge['source'])} -> {dot_quote(edge['target'])};")
    lines.append("}")
    return "\n".join(lines)


def run_graphviz(graph: dict) -> dict:
    dot_source = build_dot(graph)
    try:
        result = subprocess.run(
            ["dot", "-Tplain"],
            input=dot_source,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        raise RuntimeError("graphviz-dot-not-found")

    if result.returncode != 0:
        stderr = (result.stderr or "").strip() or "dot failed"
        raise RuntimeError(stderr)
    return parse_graphviz_plain(result.stdout, graph)


def parse_graphviz_plain(plain_text: str, graph: dict) -> dict:
    node_lookup = {node["id"]: node for node in graph["nodes"]}
    graph_scale = 1.0
    graph_width = 0.0
    graph_height = 0.0
    nodes_out: Dict[str, dict] = {}
    edge_points: Dict[Tuple[str, str, int], List[List[float]]] = {}
    edge_counts: Dict[Tuple[str, str], int] = defaultdict(int)

    for raw_line in plain_text.splitlines():
        line = raw_line.strip()
        if not line or line == "stop":
            continue
        parts = shlex.split(line)
        if not parts:
            continue
        kind = parts[0]
        if kind == "graph" and len(parts) >= 4:
            graph_scale = float(parts[1])
            graph_width = float(parts[2]) * graph_scale * PIXELS_PER_INCH
            graph_height = float(parts[3]) * graph_scale * PIXELS_PER_INCH
        elif kind == "node" and len(parts) >= 6:
            node_id = parts[1]
            if node_id not in node_lookup:
                continue
            cx = float(parts[2]) * graph_scale * PIXELS_PER_INCH
            cy = graph_height - (float(parts[3]) * graph_scale * PIXELS_PER_INCH)
            width = node_lookup[node_id]["width"]
            height = node_lookup[node_id]["height"]
            nodes_out[node_id] = {
                "id": node_id,
                "x": cx - (width / 2.0),
                "y": cy - (height / 2.0),
                "width": width,
                "height": height,
            }
        elif kind == "edge" and len(parts) >= 4:
            source = parts[1]
            target = parts[2]
            point_count = int(parts[3])
            values = parts[4 : 4 + point_count * 2]
            points = []
            for index in range(0, len(values), 2):
                px = float(values[index]) * graph_scale * PIXELS_PER_INCH
                py = graph_height - (float(values[index + 1]) * graph_scale * PIXELS_PER_INCH)
                points.append([px, py])
            edge_index = edge_counts[(source, target)]
            edge_counts[(source, target)] += 1
            edge_points[(source, target, edge_index)] = points

    if len(nodes_out) != len(graph["nodes"]):
        raise RuntimeError("graphviz output did not include every node")

    edges_out = []
    edge_instances: Dict[Tuple[str, str], int] = defaultdict(int)
    for edge in graph["edges"]:
        key = (edge["source"], edge["target"])
        edge_index = edge_instances[key]
        edge_instances[key] += 1
        points = edge_points.get((edge["source"], edge["target"], edge_index), [])
        source_node = nodes_out[edge["source"]]
        target_node = nodes_out[edge["target"]]
        source_point = boundary_point(source_node, graph["direction"], is_source=True)
        target_point = boundary_point(target_node, graph["direction"], is_source=False)
        if len(points) >= 2:
            points[0] = source_point
            points[-1] = target_point
        else:
            points = [source_point, target_point]
        edge_out = {"source": edge["source"], "target": edge["target"], "points": points}
        if "label" in edge:
            edge_out["label"] = edge["label"]
        if "id" in edge:
            edge_out["id"] = edge["id"]
        edges_out.append(edge_out)

    return {"nodes": list(nodes_out.values()), "edges": edges_out}


def fallback_layout(graph: dict) -> dict:
    ordered_nodes, layers = assign_layers(graph)
    grouped_layers = order_layers(graph, layers, ordered_nodes)
    nodes_out = place_nodes(graph, grouped_layers)
    edges_out = build_fallback_edges(graph, nodes_out)
    return {"nodes": list(nodes_out.values()), "edges": edges_out}


def assign_layers(graph: dict) -> Tuple[List[str], Dict[str, int]]:
    node_ids = [node["id"] for node in graph["nodes"]]
    adjacency: Dict[str, List[str]] = {node_id: [] for node_id in node_ids}
    indegree: Dict[str, int] = {node_id: 0 for node_id in node_ids}

    for edge in graph["edges"]:
        adjacency[edge["source"]].append(edge["target"])
        indegree[edge["target"]] += 1

    queue = deque([node_id for node_id in node_ids if indegree[node_id] == 0])
    order: List[str] = []
    remaining_indegree = dict(indegree)
    while queue:
        node_id = queue.popleft()
        order.append(node_id)
        for neighbor in adjacency[node_id]:
            remaining_indegree[neighbor] -= 1
            if remaining_indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) < len(node_ids):
        for node_id in node_ids:
            if node_id not in order:
                order.append(node_id)

    index_lookup = {node_id: index for index, node_id in enumerate(order)}
    layers = {node_id: 0 for node_id in node_ids}
    for node_id in order:
        for neighbor in adjacency[node_id]:
            if index_lookup[node_id] < index_lookup[neighbor]:
                layers[neighbor] = max(layers[neighbor], layers[node_id] + 1)

    return order, layers


def order_layers(graph: dict, layers: Dict[str, int], ordered_nodes: Sequence[str]) -> Dict[int, List[str]]:
    layer_map: Dict[int, List[str]] = defaultdict(list)
    for node_id in ordered_nodes:
        layer_map[layers[node_id]].append(node_id)

    incoming: Dict[str, List[str]] = defaultdict(list)
    outgoing: Dict[str, List[str]] = defaultdict(list)
    for edge in graph["edges"]:
        outgoing[edge["source"]].append(edge["target"])
        incoming[edge["target"]].append(edge["source"])

    base_order = {node_id: index for index, node_id in enumerate(ordered_nodes)}
    group_rank = build_group_rank(graph)
    max_layer = max(layer_map.keys(), default=0)

    for layer_index in range(1, max_layer + 1):
        prev_layer_positions = {node_id: idx for idx, node_id in enumerate(layer_map[layer_index - 1])}

        def forward_key(node_id: str) -> Tuple[float, int, int]:
            parents = [prev_layer_positions[parent] for parent in incoming[node_id] if parent in prev_layer_positions]
            barycenter = sum(parents) / len(parents) if parents else base_order[node_id]
            return barycenter, group_rank.get(node_id, 10**6), base_order[node_id]

        layer_map[layer_index].sort(key=forward_key)

    for layer_index in range(max_layer - 1, -1, -1):
        next_layer_positions = {node_id: idx for idx, node_id in enumerate(layer_map[layer_index + 1])}

        def backward_key(node_id: str) -> Tuple[float, int, int]:
            children = [next_layer_positions[child] for child in outgoing[node_id] if child in next_layer_positions]
            barycenter = sum(children) / len(children) if children else base_order[node_id]
            return barycenter, group_rank.get(node_id, 10**6), base_order[node_id]

        layer_map[layer_index].sort(key=backward_key)

    return dict(sorted(layer_map.items()))


def build_group_rank(graph: dict) -> Dict[str, int]:
    rank = {}
    for group_index, group in enumerate(graph["groups"]):
        for member_index, member in enumerate(group["members"]):
            rank.setdefault(member, group_index * 1000 + member_index)
    return rank


def place_nodes(graph: dict, layers: Dict[int, List[str]]) -> Dict[str, dict]:
    node_lookup = {node["id"]: node for node in graph["nodes"]}
    h_gap = graph["spacing"]["h_gap"]
    v_gap = graph["spacing"]["v_gap"]
    direction = graph["direction"]
    nodes_out: Dict[str, dict] = {}

    if direction in {"TD", "BT"}:
        layer_metrics = []
        max_row_width = 0.0
        for layer_index in sorted(layers):
            members = layers[layer_index]
            widths = [node_lookup[node_id]["width"] for node_id in members]
            heights = [node_lookup[node_id]["height"] for node_id in members]
            row_width = sum(widths) + max(0, len(widths) - 1) * h_gap
            row_height = max(heights) if heights else 0.0
            max_row_width = max(max_row_width, row_width)
            layer_metrics.append((layer_index, members, row_width, row_height))

        current_y = 0.0
        total_height = 0.0
        for idx, (_, _, _, row_height) in enumerate(layer_metrics):
            total_height += row_height
            if idx < len(layer_metrics) - 1:
                total_height += v_gap

        for _, members, row_width, row_height in layer_metrics:
            current_x = (max_row_width - row_width) / 2.0
            for node_id in members:
                node = node_lookup[node_id]
                nodes_out[node_id] = {
                    "id": node_id,
                    "x": current_x,
                    "y": current_y + (row_height - node["height"]) / 2.0,
                    "width": node["width"],
                    "height": node["height"],
                }
                current_x += node["width"] + h_gap
            current_y += row_height + v_gap

        if direction == "BT":
            for node in nodes_out.values():
                node["y"] = total_height - node["height"] - node["y"]
    else:
        layer_metrics = []
        max_column_height = 0.0
        for layer_index in sorted(layers):
            members = layers[layer_index]
            widths = [node_lookup[node_id]["width"] for node_id in members]
            heights = [node_lookup[node_id]["height"] for node_id in members]
            column_width = max(widths) if widths else 0.0
            column_height = sum(heights) + max(0, len(heights) - 1) * v_gap
            max_column_height = max(max_column_height, column_height)
            layer_metrics.append((layer_index, members, column_width, column_height))

        current_x = 0.0
        total_width = 0.0
        for idx, (_, _, column_width, _) in enumerate(layer_metrics):
            total_width += column_width
            if idx < len(layer_metrics) - 1:
                total_width += h_gap

        for _, members, column_width, column_height in layer_metrics:
            current_y = (max_column_height - column_height) / 2.0
            for node_id in members:
                node = node_lookup[node_id]
                nodes_out[node_id] = {
                    "id": node_id,
                    "x": current_x + (column_width - node["width"]) / 2.0,
                    "y": current_y,
                    "width": node["width"],
                    "height": node["height"],
                }
                current_y += node["height"] + v_gap
            current_x += column_width + h_gap

        if direction == "RL":
            for node in nodes_out.values():
                node["x"] = total_width - node["width"] - node["x"]

    return nodes_out


def build_fallback_edges(graph: dict, nodes_out: Dict[str, dict]) -> List[dict]:
    edges_out = []
    for edge in graph["edges"]:
        source_node = nodes_out[edge["source"]]
        target_node = nodes_out[edge["target"]]
        points = route_edge(source_node, target_node, graph["direction"])
        edge_out = {"source": edge["source"], "target": edge["target"], "points": points}
        if "label" in edge:
            edge_out["label"] = edge["label"]
        if "id" in edge:
            edge_out["id"] = edge["id"]
        edges_out.append(edge_out)
    return edges_out


def boundary_point(node: dict, direction: str, is_source: bool) -> List[float]:
    x = node["x"]
    y = node["y"]
    width = node["width"]
    height = node["height"]

    if direction == "TD":
        return [x + width / 2.0, y + height] if is_source else [x + width / 2.0, y]
    if direction == "BT":
        return [x + width / 2.0, y] if is_source else [x + width / 2.0, y + height]
    if direction == "LR":
        return [x + width, y + height / 2.0] if is_source else [x, y + height / 2.0]
    return [x, y + height / 2.0] if is_source else [x + width, y + height / 2.0]


def route_edge(source_node: dict, target_node: dict, direction: str) -> List[List[float]]:
    start = boundary_point(source_node, direction, is_source=True)
    end = boundary_point(target_node, direction, is_source=False)

    if direction in {"TD", "BT"}:
        if abs(start[0] - end[0]) < 1e-6:
            return [start, end]
        mid_y = (start[1] + end[1]) / 2.0
        return [start, [start[0], mid_y], [end[0], mid_y], end]

    if abs(start[1] - end[1]) < 1e-6:
        return [start, end]
    mid_x = (start[0] + end[0]) / 2.0
    return [start, [mid_x, start[1]], [mid_x, end[1]], end]


def compute_group_boxes(nodes: Sequence[dict], groups: Sequence[dict]) -> List[dict]:
    node_lookup = {node["id"]: node for node in nodes}
    boxes = []
    for group in groups:
        members = [node_lookup[member] for member in group["members"] if member in node_lookup]
        if not members:
            continue
        min_x = min(node["x"] for node in members) - GROUP_PADDING
        min_y = min(node["y"] for node in members) - GROUP_PADDING - GROUP_TITLE_HEIGHT
        max_x = max(node["x"] + node["width"] for node in members) + GROUP_PADDING
        max_y = max(node["y"] + node["height"] for node in members) + GROUP_PADDING
        label_width = max(0.0, len(group["label"]) * 8.0)
        min_width = label_width + GROUP_PADDING * 2.0
        width = max(max_x - min_x, min_width)
        boxes.append(
            {
                "id": group["id"],
                "label": group["label"],
                "x": min_x,
                "y": min_y,
                "width": width,
                "height": max_y - min_y,
            }
        )
    return boxes


def apply_canvas_padding(layout: dict, groups: Sequence[dict]) -> dict:
    nodes = [dict(node) for node in layout["nodes"]]
    edges = [{**edge, "points": [point[:] for point in edge["points"]]} for edge in layout["edges"]]
    group_boxes = compute_group_boxes(nodes, groups)

    min_x, min_y, max_x, max_y = collect_bounds(nodes, edges, group_boxes)
    dx = CANVAS_PADDING - min_x
    dy = CANVAS_PADDING - min_y

    for node in nodes:
        node["x"] += dx
        node["y"] += dy
    for edge in edges:
        for point in edge["points"]:
            point[0] += dx
            point[1] += dy
    for group in group_boxes:
        group["x"] += dx
        group["y"] += dy

    canvas_width = max(CANVAS_PADDING * 2.0, max_x + dx + CANVAS_PADDING)
    canvas_height = max(CANVAS_PADDING * 2.0, max_y + dy + CANVAS_PADDING)

    return {
        "nodes": finalize_nodes(nodes),
        "edges": finalize_edges(edges),
        "groups": finalize_groups(group_boxes),
        "canvas": {"width": round_number(canvas_width), "height": round_number(canvas_height)},
    }


def collect_bounds(nodes: Sequence[dict], edges: Sequence[dict], groups: Sequence[dict]) -> Tuple[float, float, float, float]:
    min_x = 0.0
    min_y = 0.0
    max_x = 0.0
    max_y = 0.0
    initialized = False

    def include(x0: float, y0: float, x1: float, y1: float) -> None:
        nonlocal min_x, min_y, max_x, max_y, initialized
        if not initialized:
            min_x, min_y, max_x, max_y = x0, y0, x1, y1
            initialized = True
            return
        min_x = min(min_x, x0)
        min_y = min(min_y, y0)
        max_x = max(max_x, x1)
        max_y = max(max_y, y1)

    for node in nodes:
        include(node["x"], node["y"], node["x"] + node["width"], node["y"] + node["height"])
    for edge in edges:
        for point in edge["points"]:
            include(point[0], point[1], point[0], point[1])
    for group in groups:
        include(group["x"], group["y"], group["x"] + group["width"], group["y"] + group["height"])

    if not initialized:
        return 0.0, 0.0, 0.0, 0.0
    return min_x, min_y, max_x, max_y


def finalize_nodes(nodes: Iterable[dict]) -> List[dict]:
    return [
        {
            "id": node["id"],
            "x": round_number(node["x"]),
            "y": round_number(node["y"]),
            "width": round_number(node["width"]),
            "height": round_number(node["height"]),
        }
        for node in nodes
    ]


def finalize_edges(edges: Iterable[dict]) -> List[dict]:
    finalized = []
    for edge in edges:
        entry = {
            "source": edge["source"],
            "target": edge["target"],
            "points": [[round_number(point[0]), round_number(point[1])] for point in edge["points"]],
        }
        if "label" in edge:
            entry["label"] = edge["label"]
        if "id" in edge:
            entry["id"] = edge["id"]
        finalized.append(entry)
    return finalized


def finalize_groups(groups: Iterable[dict]) -> List[dict]:
    return [
        {
            "id": group["id"],
            "label": group["label"],
            "x": round_number(group["x"]),
            "y": round_number(group["y"]),
            "width": round_number(group["width"]),
            "height": round_number(group["height"]),
        }
        for group in groups
    ]


def main() -> int:
    args = parse_args()
    graph = normalize_graph(load_graph(sys.stdin.read()), args)

    try:
        layout = run_graphviz(graph)
    except RuntimeError as exc:
        print(f"Warning: graphviz unavailable ({exc}); using fallback layered layout.", file=sys.stderr)
        layout = fallback_layout(graph)

    output = apply_canvas_padding(layout, graph["groups"])
    json.dump(output, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
