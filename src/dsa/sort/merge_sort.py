# Merge Sort
# This sort uses the approach of divide and conquer. It keeps partitioning the array into two halfs,
# and sorts each of the halves individually. Both the halfs are finally merged back to sort the
# whole range of the current partition.
#
# It is a 'stable sort' since the order is preserved.
#
# Time Complexity: O(n * log(n))
#   Best Case: O(n * log(n))
#   Worst Case: O(n * log(n))
# Auxiliary Space: O(n)
#   Required for temporary array used during merging
class MergeSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        self.partition_and_merge(0, len(self.array) - 1)
        return self.array

    # The array is continuously partitioned through recursion. The recursion ultimately reaches
    # the one element arrays which are merged to get a sorted array.
    # Each sorted array is merged with it's corresponding half to get the next level of sorted
    # range. This way the whole array is sorted through continuous merging.
    def partition_and_merge(self, start, end):
        if start >= end:
            return

        # Partition the current array from mid and sort them individually.
        mid = start + (end - start) // 2
        self.partition_and_merge(start, mid)
        self.partition_and_merge(mid + 1, end)

        # Merge the two halves back to get the sorted range.
        self.sort_and_merge(start, mid, end)

    # Merges the left and right halves of the partitioned array. The method iterates over the halves
    # linearly by maintaining respective pointers. Since both the halves are already sorted
    # individually, it compares the current pointers of both the halves to identify the next
    # smallest element in each iteration.
    def sort_and_merge(self, start, mid, end):
        left = start
        right = mid + 1
        merged = []

        # Merge by identifying the smallest element from both the arrays
        # If equal, prefer the left index to keep the sort stable.
        while left <= mid and right <= end:
            if self.array[left] <= self.array[right]:
                merged.append(self.array[left])
                left += 1
            else:
                merged.append(self.array[right])
                right += 1

        # Iterate over the remaining left half in case right was completely iterated above
        while left <= mid:
            merged.append(self.array[left])
            left += 1

        # Iterate over the remaining right half in case left was completely iterated above
        while right <= end:
            merged.append(self.array[right])
            right += 1

        # Update the original array with the updated merged values to get the sorted range
        for i in range(len(merged)):
            self.array[start + i] = merged[i]
