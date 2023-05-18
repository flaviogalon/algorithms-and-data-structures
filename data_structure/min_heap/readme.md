# MinHeap

Graph representation:

```mermaid
graph TD;
    id1((6))-->id2((7));
    id1-->id3((12));
    id2-->id4((10));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
```

Array representation:

`[6, 7, 12, 10, 15, 17]`

## Insert
Insertion works by adding new node to bottom of the tree and heapifying it up.
Will compare recently added node (will be called current) to its parents. If any parent is smaller then current, swap it. Repeat until this condition is satisfied.

### Step 1: insert `5` at the bottom
```mermaid
graph TD;
    id1((6))-->id2((7));
    id1-->id3((12));
    id2-->id4((10));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((5));
```
### Step 2: Compare with father node
```mermaid
graph TD;
    id1((6))-->id2((7));
    id1-->id3((12));
    id2-->id4((10));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((5));
    id8-- Is < than father! Swap -->id4
```
### Step 3: Swap
```mermaid
graph TD;
    id1((6))-->id2((7));
    id1-->id3((12));
    id2-->id4((5));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
```
### Step 4: Compare with father node
```mermaid
graph TD;
    id1((6))-->id2((7));
    id1-->id3((12));
    id2-->id4((5));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
    id4-- Is < than father! SWAP -->id2;
```
### Step 5: Swap
```mermaid
graph TD;
    id1((6))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
```
### Step 6: Compare with father node
```mermaid
graph TD;
    id1((6))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
    id2-- Is < than father! FINISHED -->id1
```
### Final result
```mermaid
graph TD;
    id1((6))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
```

## Delete
Deletion is done by removing the root node, putting the most recent added node to root's position and heapifying it down. Since the 2 level of the tree already contains the smallest values compared to the old root, one of those will be promoted to root. We need then to adjust its children to balance the tree.

### Step 1: Remove root
```mermaid
graph TD;
    id1((X))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10));
```
### Step 2: Swap last added node with root and call it current
```mermaid
graph TD;
    id1((X))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id4-->id8((10*));
    id8-- will take root's position -->id1
```
```mermaid
graph TD;
    id1((10*))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
```
### Step 3: Pick the min() between children nodes and compare to current
```mermaid
graph TD;
    id1((10*))-->id2((5));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id2-- Is < than root! SWAP -->id1
```
### Step 4: Swap
```mermaid
graph TD;
    id1((5))-->id2((10*));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
```
### Step 5: Compare current with its children, swap with the smallest
```mermaid
graph TD;
    id1((5))-->id2((10*));
    id1-->id3((12));
    id2-->id4((7));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
    id2-- is > than children! SWAP -->id4;
```
### Step 6: Swap
```mermaid
graph TD;
    id1((5))-->id2((7));
    id1-->id3((12));
    id2-->id4((10*));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
```
### Step 7: No children to compare. Final result
```mermaid
graph TD;
    id1((5))-->id2((7));
    id1-->id3((12));
    id2-->id4((10));
    id2-->id5((15));
    id3-->id6((17));
    id3-->id7((21));
```
