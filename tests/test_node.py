from binary_tree import Node


def test_node_eq() -> None:
    node1 = Node(1)
    node2 = Node(1)
    assert node1 == node2, f"{node1} != {node2}"

    node1 = Node(1, left=Node(2))
    node2 = Node(1)
    assert node1 != node2, f"{node1} == {node2}"


def test_node_inverted() -> None:
    node = Node(1, left=Node(2), right=Node(3))
    original = node.clone()
    inverted = node.inverted()
    assert node == original, f"{node} != {original}"
    assert inverted, None
    assert inverted.left, None
    assert inverted.right, None
    assert inverted.value == 1, inverted.value
    assert inverted.left.value == 3, inverted.left.value
    assert inverted.right.value == 2, inverted.right.value
