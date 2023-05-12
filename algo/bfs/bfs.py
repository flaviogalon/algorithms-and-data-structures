from collections import deque

from data_structure.binary_tree.binary_node import BinaryNode, tree


def bfs(head: BinaryNode, needle: int) -> bool:
    queue = deque([head])
    while len(queue):
        curr: BinaryNode = queue.popleft()

        if not curr:
            continue

        if curr["value"] == needle:
            return True

        if curr["left"]:
            queue.append(curr["left"])

        if curr["right"]:
            queue.append(curr["right"])
    return False


assert bfs(tree, 45) == True
assert bfs(tree, 7) == True
assert bfs(tree, 69) == False
