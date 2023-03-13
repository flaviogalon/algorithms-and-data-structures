def _binary_with_indexes(values: list[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1

    mid_position = (low + high) // 2

    if values[mid_position] == target:
        return mid_position
    if values[mid_position] > target:
        return _binary_with_indexes(values, low, mid_position - 1, target)
    else:
        return _binary_with_indexes(values, mid_position + 1, high, target)


def binary_search(values: list[int], target) -> int:
    return _binary_with_indexes(values, 0, len(values) - 1, target)


l = [1, 2, 3, 4, 5, 6, 7, 8]

assert binary_search(l, 1) == 0
assert binary_search(l, 4) == 3
assert binary_search(l, 8) == 7
assert binary_search(l, 9) == -1
