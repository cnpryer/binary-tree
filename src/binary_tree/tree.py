from __future__ import annotations

from typing import Any, Sequence

from binary_tree.node import (
    Node,
    _height_from_node,
)


class Tree:
    def __init__(self, root: Node | None = None) -> None:
        self.root = root
        self.height = 0 if not self.root else _height_from_node(self.root)

    @staticmethod
    def from_values(values: Sequence[Any]) -> Tree:
        return _tree_from_values(values) or Tree()

    def inverted(self, allow_copy: bool = True) -> Tree:
        if not self.root:
            return self
        if allow_copy:
            return Tree(self.root.inverted(allow_copy=allow_copy))
        self.root = self.root.inverted()
        return self

    def clone(self) -> Tree:
        tree = Tree()
        if self.root:
            tree.root = self.root.clone()
        return tree

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tree):
            return False
        return self.root == other.root

    def __str__(self) -> str:
        return str(self.root)


def _tree_from_values(values: Sequence[Any]) -> Tree | None:
    if not values:
        return None

    def gen_node(pos: int) -> Node | None:
        if len(values) <= pos or values[pos] is None:
            return None

        node = Node(values[pos])
        node.left = gen_node(2 * pos + 1)
        node.right = gen_node(2 * pos + 2)
        return node

    return Tree(gen_node(0))
