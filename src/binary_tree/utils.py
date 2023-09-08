from typing import Any, Sequence
from binary_tree import Tree
from binary_tree.node import Node


def node_is_balanced(node: Node) -> bool:
    def gen_height(node: Node | None) -> int:
        if not node:
            return 0

        left_height = gen_height(node.left)
        if left_height < 0:
            return -1

        right_height = gen_height(node.right)
        if right_height < 0:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return gen_height(node) > 0


def assert_tree_values(tree: Tree, values: Sequence[Any]) -> None:
    other = Tree.from_values(values)
    assert tree == other, f"{tree} != {other}"
