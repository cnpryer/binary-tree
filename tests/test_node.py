from binary_tree import Node


def test_node_eq() -> None:
    node1 = Node(1)
    node2 = Node(1)
    assert node1 == node2, f"{node1} != {node2}"

    node1 = Node(1, left=Node(2))
    node2 = Node(1)
    assert node1 != node2, f"{node1} == {node2}"


def test_tree_inverted() -> None:
    node = Node(1, left=Node(2), right=Node(3)).inverted()
    assert node, None
    assert node.left, None
    assert node.right, None
    assert node.value == 1, node.value
    assert node.left.value == 3, node.left.value
    assert node.right.value == 2, node.right.value
