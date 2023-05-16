from data_structure.binary_tree.binary_node import BinaryNode, tree


def _search(current: BinaryNode | None, needle: int) -> bool:
    if not current:
        return False

    if current["value"] == needle:
        return True

    if current["value"] < needle:
        return _search(current["right"], needle)
    return _search(current["left"], needle)


def dfs(head: BinaryNode, needle: int) -> bool:
    return _search(head, needle)


assert dfs(tree, 45) == True
assert dfs(tree, 7) == True
assert dfs(tree, 69) == False
