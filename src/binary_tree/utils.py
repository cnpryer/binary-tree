from typing import Any, Sequence

from binary_tree import Tree


def assert_tree_values(tree: Tree, values: Sequence[Any]) -> None:
    other = Tree.from_values(values)
    assert tree == other, f"{tree} != {other}"
