from __future__ import annotations
from collections import deque
from typing import Any


class Node:
    def __init__(
        self, value: Any = None, left: Node | None = None, right: Node | None = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def _invert_node(node: Node | None) -> Node | None:
    if not node:
        return None

    node.left, node.right = _invert_node(node.right), _invert_node(node.left)
    return node


def _height_from_node(node: Node | None) -> int:
    if not node:
        return 0
    queue, height = deque([node]), 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1
    return height


def _compare_nodes_eq(node: Node | None, other: Node | None) -> bool:
    if not node and not other:
        return True
    if not node or not other:
        return False

    if node.value != other.value:
        return False

    return _compare_nodes_eq(node.left, other.left) and _compare_nodes_eq(
        node.right, other.right
    )


def _node_to_string(node: Node | None) -> str:
    if not node:
        return "None"

    result = str(node.value)
    if node.left or node.right:
        result += f"[{_node_to_string(node.left)}, {_node_to_string(node.right)}]"

    return result
