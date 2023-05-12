# Bubble Sort
Will sort an array by comparing adjacent elements.

## Algorithm
- Set a pointer to the first element of the array   [start]
- Set a pointer to the last element of the array    [end]
- Compare element at pointer with next position
- Is there a next position? If yes, compare, if no return to [start]
- Is the element greater than next?
  - Yes: swap
  - N: continue
- Is [start] == [end]?
  - Yes: [start] == 0 & [end]--
  - No: [start]++
- Is end == 0?
  - Yes: finish -> array sorted
  - No: continue

At each pass the goal is to push the largest unsorted number to the end of the array.

## Example
[1, 3, 8, 2, 4]
 |
 Is 1 greater than 3? NO -> move forward

[1, 3, 8, 2, 4]
    |
    Is 3 greater than 8? NO -> move forward

[1, 3, 8, 2, 4]
       |
       Is 8 greater than 2? YES -> swap

[1, 3, 2, 8, 4]
          |
          Is 8 greater than 4? YES -> swap

[1, 3, 2, 4, 8]
             | End of array -> end of first pass
...
          