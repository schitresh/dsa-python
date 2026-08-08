from random import randint


# Quick Sort
# This sort takes a divide and conquer approach that picks a pivot and paritions the array around
# it. First a pivot is choosen and all the values smaller than it are put to its left and the
# values larger than it are put to its right. That means, the left and right subarrays or partitions
# can now be sorted individually. Both the partitions are then further partitioned through by
# choosen a new pivot within them.
#
# It is an unstable sort as the elements are swapped depending on the partition.
#
# Best partition scheme is to choose pivot randomly. This is because the worst case performance
# of quick sort is O(n^2), when the array is already sorted. The splits are balanced out when the
# pivot is chosen randomly.
#
# Time Complexity: O(n * log(n))
#   Best Case: O(n * log(n))
#   Worst Case: O(n^2)
# Auxiliary Space: O(log(n)), due to the recursive stack
#   Best Case: O(log(n))
#   Worst Case: O(n)
class QuickSort:
    strategies = ("lomuto", "hoare")

    def __init__(self, array, strategy="hoare"):
        self.array = array
        self.strategy = strategy

    def perform(self):
        self.partition_and_sort(0, len(self.array) - 1)
        return self.array

    # First a pivot is picked and the elements are arranged around it, smaller ones to the left
    # and larger ones to the right. Then, these left and right partitions are again partitioned
    # through a new pivot between them. Doing this continuously sorts the array till it reaches
    # the maximum depth (one element subarray).
    def partition_and_sort(self, start, end):
        if start >= end:
            return

        pivot = self.pivot_and_sort(start, end)
        self.partition_and_sort(start, pivot)
        self.partition_and_sort(pivot + 1, end)

    def pivot_and_sort(self, start, end):
        if self.strategy == "lomuto":
            return self.lomuto_pivot(start, end)
        else:
            return self.hoare_pivot(start, end)

    # Lomuto's algorithm chooses a pivot and moves it to the start or end. This makes it easy to
    # move the elements around without dissecting or duplicating the array.
    # It then iterates through the array maintaining a partition point, before which all the values
    # are smaller than the pivot. If the current value is smaller than the pivot, then we switch
    # its place at the partition point and move the point forward.
    # This way, all the elements before the partition point are smaller than the pivot and the ones
    # after & including it are larger.
    def lomuto_pivot(self, start, end):
        # Choose a random pivot and swap it at the start to make it easy to move elements around
        pivot = randint(start, end)
        self.swap_at(start, pivot)

        # Initialize the partition point (before which all elements are smaller than pivot)
        pivot_val = self.array[start]
        partition_point = start + 1

        # Iterate through the range and maintain the partition point, swapping smaller elements
        for i in range(start + 1, end + 1):
            if self.array[i] < pivot_val:
                self.swap_at(partition_point, i)
                partition_point += 1

        # Move the pivot back to its correct position, that is, just before the partition point.
        pivot = partition_point - 1
        self.swap_at(start, pivot)
        return pivot

    # Hoare's algorithm chooses a pivot and partitions by swapping the elements from the both ends.
    # The swapping from both ends by comparing with pivot value partitions the array at the meeting
    # point. The swapping also means that the final pivot element may end up somewhere else, but
    # the meeting point becomes the new pivot.
    # It is more efficient than Lomuto's algorithm. Lomuto's algo swaps the elements more often
    # whenever the value is smaller than pivot, even if it's at the right side of partition. In
    # contrast, Hoare's algo swaps only when the values are uneven while partitioning.
    def hoare_pivot(self, start, end):
        # Choose a pivot and track its value because the swapping may replace the pivot from its
        # original index
        pivot = randint(start, end)
        pivot_val = self.array[pivot]

        left = start
        right = end

        # The pointers move from both ends and they are swapped only if left one is larger than the
        # pivot and right once is smaller.
        # This always guarantees that left subarray and right subarray will always be partitioned.
        # But we cannot track the original pivot here, since moving elements around it would mean
        # dissecting or duplicating the array. Because on the there may end up more smaller values
        # than we have places for in the left.
        # But since left and right move linearly while keeping the strict comparison with pivot
        # value, the array will be partitioned at the meeting of the left & right pointer, which
        # becomes our new pivot to be returned.
        while True:
            while self.array[left] < pivot_val:
                left += 1

            while pivot_val < self.array[right]:
                right -= 1

            if left >= right:
                return right

            self.swap_at(left, right)
            left += 1
            right -= 1

    def swap_at(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
