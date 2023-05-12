def partition(arr: list[int], lo: int, hi: int) -> int:
    """Will pick up a pivot point and weak sort the array such as everything left the
    pivot is <= pivot value.

    Obs: the right portion of the array will be unsorted.
    """
    pivot = arr[hi]
    idx = lo - 1

    # iterate over the array putting everything <= pivot value in the lower portion
    # of the array
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    # every value up until idx is <= pivot, so let's place pivot right after it
    idx += 1
    # last swap, get the pivot on its correct position
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return

    pivot_idx = partition(arr, lo, hi)
    # Recursion left of the pivot
    quick_sort(arr, lo, pivot_idx - 1)
    # Recursion right of the pivot
    quick_sort(arr, pivot_idx + 1, hi)


unsorted_lists = [[10, 14, 28, 11, 7, 16, 30, 50, 25, 18], [9, 3, 7, 4, 69, 420, 42]]

for unsorted_list in unsorted_lists:
    expected_list = sorted(unsorted_list)
    quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    assert unsorted_list == expected_list
