from data_structure.binary_tree.binary_node import BinaryNode, tree


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    path.append(curr["value"])
    walk(curr["left"], path)
    walk(curr["right"], path)

    return path


def pre_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


expected = [
    20,
    10,
    5,
    7,
    15,
    50,
    30,
    29,
    45,
    100,
]
