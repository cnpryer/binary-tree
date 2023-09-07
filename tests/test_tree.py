from binary_tree import Tree
from binary_tree.utils import assert_tree_values


def test_tree_from_values() -> None:
    values = [1, 2, 3, 5]
    tree = Tree.from_values(values)
    assert_tree_values(tree, values)


def test_tree_inverted() -> None:
    values = [1, 2, 3, 5]
    tree = Tree.from_values(values).inverted()
    assert_tree_values(tree, [1, 3, 2, None, None, None, 5])
