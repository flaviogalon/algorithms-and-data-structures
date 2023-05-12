from binary_node import BinaryNode, tree


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    walk(curr["left"], path)
    walk(curr["right"], path)
    path.append(curr["value"])

    return path


def post_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


expected = [
    7,
    5,
    15,
    10,
    29,
    45,
    30,
    100,
    50,
    20,
]
assert expected == post_order_search(tree)
