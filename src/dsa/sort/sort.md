# Sorting

The standard sorting algorithms are:

1. Selection Sort

- Finds the smallest value and puts it at the front
- Time Complexity: O(N^2)
- Type: Unstable, In-Place, Comparison-based

2. Bubble Sort

- Keeps swapping adjacent values till the largest one reaches the end
- Time Complexity: O(N^2)
- Type: Stable, In-Place, Comparison-based

3. Insertion Sort

- Finds the sorted place for the current element in the subarray before it
- Time Complexity: O(N^2)
- Type: Stable, In-Place, Comparison-based

4.  Merge Sort

- Continuously divides the array into two halves and re-merges them in sorted order
- Time Complexity: O(N log N)
- Type: Stable, Out-of-Place, Comparison-based

5. Quick Sort

- Picks a pivot to partition elements into smaller and larger subsets, then sorts them recursively
- Time Complexity: O(N log N)
- Type: Unstable, In-Place, Comparison-based

6. Heap Sort

- Builds a max-heap from the array and repeatedly extracts the maximum element to the end
- Time Complexity: O(N log N)
- Type: Unstable, In-Place, Comparison-based

7. Count Sort

- Counts element occurrences in a frequency array and calculates exact target indices using prefix sums
- Time Complexity: O(N + k) (where k is the value range)
- Type: Stable (standard variant), Out-of-Place, Non-Comparison / Linear-time

8. Radix Sort

- Sorts numbers digit by digit from least to most significant using a stable subroutine
- Time Complexity: O(d \* (N + b)) (where d is digits, b is base)
- Type: Stable, Out-of-Place, Non-Comparison / Linear-time

9. Bucket Sort

- Distributes numbers into bounded interval buckets, sorts each bucket individually, and concatenates them
- Time Complexity: O(N + k) (where k is the number of buckets)
- Type: Stable (if inner sort is stable), Out-of-Place, Non-Comparison / Linear-time

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
