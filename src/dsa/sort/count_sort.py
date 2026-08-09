# Count Sort
# Non-comparision based sort that works well if there is a limited range of values. It counts the
# frequency of the elements and places them in their correct position based on the frequency.
# The default version of count sort where the indexes are treated as values doesn't support sorting
# negative values. But it can be tweaked to sort negative values by considering the starting index
# of the count as the minimum value.
#
# It is a stable sort, but doesn't work on decimal values. The simpler variant of count sort is
# an unstable sort.
#
# Time Complexity: O(n + k), where k is the largest element
#   Best Case: O(n + k)
#   Worst Case: O(n + k)
# Auxiliary Space: O(k), to store the counts
class CountSort:
    strategies = ("unstable", "stable", "negative")

    def __init__(self, array, strategy="negative"):
        self.array = array
        self.strategy = strategy

    def perform(self):
        if self.strategy == "unstable":
            self.unstable_sort()
        elif self.strategy == "stable":
            self.stable_sort()
        else:
            self.negative_sort()

        return self.array

    # The simple count sort is unstable, because the counts are stored for each value of the array
    # and the array is updated based on count array only. The indexes of the count array act as
    # the values of the original array.
    def unstable_sort(self):
        max_val = max(self.array)
        counts = [0] * (max_val + 1)

        for val in self.array:
            counts[val] += 1

        idx = 0
        for val in range(len(counts)):
            for _ in range(counts[val]):
                self.array[idx] = val
                idx += 1

    # To make the count sort stable, the count array is converted into a positional array. By
    # calculating the cumulative sum, it can determine the positions of each item. This is because
    # summing up the previous counts will determine how many places before the current item are
    # occupied in the sorted array.
    # For example, if the count of 0 is 2 and of 1 is 3, the positional array will track 2 for 0
    # and 5 for 1. That means the positions 1 & 2 in the sorted array will have 0, and the
    # positions 3, 4, & 5 will have 1.
    def stable_sort(self):
        max_val = max(self.array)
        counts = [0] * (max_val + 1)

        for val in self.array:
            counts[val] += 1

        # Convert the count array into a positional array using cumulative sum of the counts
        for val in range(len(counts) - 1):
            counts[val + 1] += counts[val]

        # Iterate from the end of the array to place the items which occur later in the original
        # array into a later position in the sorted array. Since the positional (or count) array
        # stores the maximum position of each value, we can maintain the original order by iterating
        # from the end. We can keep decrementing the position when the value is considered to
        # determine the next position when the same value comes up again.
        # This is more prominently visible when the data type is not integer but objects, pairs,
        # etc. and are sorted based on a particular value. For example, (a, 1) and (b, 1) when
        # sorted by the second element will maintain the correct order by placing the pair with a
        # before the one with b, since the second value is the same (1).
        sorted_array = [None] * len(self.array)
        for i in range(len(self.array) - 1, -1, -1):
            val = self.array[i]
            sorted_idx = counts[val] - 1
            sorted_array[sorted_idx] = val
            counts[val] -= 1

        for i in range(len(self.array)):
            self.array[i] = sorted_array[i]

    def negative_sort(self):
        min_val = min(self.array)
        max_val = max(self.array)
        val_range = max_val - min_val
        counts = [0] * (val_range + 1)

        for val in self.array:
            counts[val - min_val] += 1

        for idx in range(len(counts) - 1):
            counts[idx + 1] += counts[idx]

        sorted_array = [None] * len(self.array)
        for i in range(len(self.array) - 1, -1, -1):
            val = self.array[i]
            sorted_idx = counts[val - min_val] - 1
            sorted_array[sorted_idx] = val
            counts[val - min_val] -= 1

        for i in range(len(self.array)):
            self.array[i] = sorted_array[i]
