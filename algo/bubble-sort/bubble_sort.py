import random

def bubble_sort(arr: list[int]) -> list[int]:
    end = len(arr) -1

    while end > 0:
        start = 0
        while start < end:
            val = arr[start]
            next_val = arr[start + 1]

            if val > next_val:
                arr[start], arr[start + 1] = next_val, val
            
            start += 1
        
        end -= 1
    return arr



arr = random.sample(range(1, 10000), 1000)
sorted = arr.copy()
sorted.sort()
assert bubble_sort(arr) == sorted
