from binary_node import BinaryNode, tree


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    walk(curr["left"], path)
    path.append(curr["value"])
    walk(curr["right"], path)

    return path


def in_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


expected = [
    5,
    7,
    10,
    15,
    20,
    29,
    30,
    45,
    50,
    100,
]
assert expected == in_order_search(tree)
