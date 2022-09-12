### Sorting Algorithm

```
Process of arranging items systematically
```

    Comparison-based Sorting Algorithms:
        Bubble Sort
        Selection Sort
        Insertion Sort
        Merge Sort
        Quick Sort
        Random Quick Sort
    Not Comparison-based Sorting Algorithms:
        Counting Sort
        Radix Sort

=> **Inversion** in a sequence is defined as a pair of elements that are out of order with respect to the ordering relation

```
sorting algorithm is a sequence of operations that reduces inversions to 0.
```

=> **stability** of sorting algorithms is that it will preserve the order of equal elements.

### Bubble sort

- repeatedly comparing pairs of adjacent elements and then swapping their positions
- stable
- **T(n) - O(n^2), S(n) - O(1)**

### Selection sort

- finds the smallest element's index and swaps the value
- unstable because the order changes

```
ip -> 2 2' 1
op -> 1 2' 2
```

- **T(n) - O(n^2), S(n) - O(1)**

### Insertion sort

- places an unsorted element at its suitable place in each iteration.
- stable
- **T(n) -> O(n^2) S(n) -> O(1)**

###

```
python's sort and sorted functions  uses timsort

T(n) => Nlog(N)
S(N) => O(N)
```

### Reference

- https://www.programiz.com/dsa/bubble-sort
