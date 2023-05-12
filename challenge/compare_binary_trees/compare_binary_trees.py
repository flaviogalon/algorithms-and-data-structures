from data_structure.binary_tree.binary_node import BinaryNode, tree, another_tree


def compare(a: BinaryNode | None, b: BinaryNode | None) -> bool:
    if not a and not b:
        return True

    if not a or not b:
        return False

    if a["value"] != b["value"]:
        return False

    return compare(a["left"], b["left"]) and compare(a["right"], b["right"])


assert compare(tree, tree) == True
assert compare(tree, another_tree) == False
