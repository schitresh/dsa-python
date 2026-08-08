# Sorting

The standard sorting algorithms are:

1. Selection Sort: Finds the smallest value and puts it at front
2. Bubble Sort: Keeps swapping the adjacent values till the largest one reaches the end
3. Insertion Sort: Finds the sorted place in the subarray before the current element
4. Merge Sort: Continuously divide the array in two halves and re-merge to form a sorted range
5. Quick Sort
6. Heap Sort
7. Count Sort
8. Radix Sort
9. Bucket Sort

## Types of Sorting

### By Modification Type

- In-place Sorting
  - In-place sorting modifies the given array directly without using an auxiliary array.
  - Hence, it uses constant space.
  - Examples: selection sort, bubble sort, insertion sort, heap sort
- Out-of-place Sorting
  - Out-of-place sorting requires auxiliary space to hold copies or additional data for sorting.
  - Examples: merge sort, couting sort, radix sort, bucket sort

### By Data Size

- Internal Sorting
  - When all the data is placed in the main memory or internal memory, it's internal sorting.
  - It cannot take input beyond its size and the data should fit in the internal memory.
  - Example: selection sort, bubble sort, insertion sort, heap sort, quick sort
- External Sorting
  - When all the data cannot be placed in memory at a time, it's external sorting.
  - It is used for the massive amount of data that cannot fit in the internal memory.
  - Examples: merge sort, external radix sort

### By Element Order

- Stable sorting
  - When two same elements appears in their original order after sorting
  - Examples: bubble sort, insertion sort, merge sort
- Unstable sorting
  - When two same elements appear in a different order after sorting
  - Examples: quick sort, heap sort, shell sort

## Sorting Techniques

- Comparison based
  - The values of the data are strictly compared with each other to decide the order
  - Examples: selection sort, bubble sort, insertion sort, merge sort, quick sort, heap sort
- Non-comparison based
  - Uses specific assumptions about the nature of the data (like integer ranges or string lengths)
    to sort elements into buckets or mathematical slots without ever directly comparing two values
  - Examples: counting sort, radix sort, bucket sort

## Languages

### Python

```py
array = [5, 3, 6, 7, 8, 2, 9]

# Sorts the original array
array.sort()
array.sort(key = lambda x: x * 2)
array.sort(reverse = True)

# Duplicates the array and sorts, without affecting the original one
array = sorted(array)
array = sorted(key = lambda x: x * 2)
array = sorted(reverse = True)

# String sort
string = 'hello world'
string = ''.join(sorted(string))
```

### Ruby

```rb
array = [5, 3, 6, 7, 8, 2, 9]
array.sort # Duplicates the array
array.sort! # Updates the original array

# Sorts with a custom criteria
# <=> is the sorting operator
# It returns 0 if x = y, -1 if x < y, 1 if x > y
array.sort { |x, y| x <=> y }

# String sort
string = 'hello world'
string.chars.sort.join
```
