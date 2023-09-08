from binary_tree import Tree
from binary_tree.utils import assert_tree_values, node_is_balanced


def test_tree_from_values() -> None:
    values = [1, 2, 3, 5]
    tree = Tree.from_values(values)
    assert_tree_values(tree, values)


def test_tree_inverted() -> None:
    values = [1, 2, 3, 5]
    tree = Tree.from_values(values).inverted()
    assert_tree_values(tree, [1, 3, 2, None, None, None, 5])


def test_tree_height() -> None:
    values = [1, 2, 3, None, None, None, 3]
    tree = Tree.from_values(values)
    assert tree.height == 3, tree.height


def test_tree_is_balanced() -> None:
    tree = Tree.from_values([3, 9, 20, None, None, 15, 7])
    assert node_is_balanced(tree.root), False

    tree = Tree.from_values([1, 2, 2, 3, 3, None, None, 4, 4])
    assert not node_is_balanced(tree.root), True
