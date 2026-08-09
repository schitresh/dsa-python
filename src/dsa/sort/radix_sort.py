# Radix Sort
# A linear sorting algorithm that processes elements digit by digit. It distributes elements into
# buckets based on digit values. All the places (determined by the largest element) are iterated
# and sorted iteratively using count sort. The elements are sorted by ones place, then tens place,
# and so on sorts using the stable count sort, which preserves the previous order and sorts the
# complete array.
#
# It is a stable sort since it derives from the stability of count sort itself.
#
# Given d is the number of digits, b is the base of the number system used
# If k is the max element, then d = logb(k)
# Time Complexity: O(d * (n + b))
#   Best Case: O(d * (n + b))
#   Worst Case: O(d * (n + b))
# Auxiliary Space: O(n + b)
class RadixSort:
    def __init__(self, array):
        self.array = array

    # Iterate over all the places (depending on maximum value) and count sort them
    def perform(self):
        max_val = max(self.array)
        total_places = len(str(max_val))

        for i in range(total_places):
            self.count_sort_at_place(i + 1)

        return self.array

    # Stable count sort is used that supports negative integers as well. The counts array helps
    # tracking count of the digits at the current place. And the sorted index determined by this
    # counts array can help us copy the actual element from the array to the new sorted array.
    def count_sort_at_place(self, place):
        # A digit can have minimum value of -9 and maximum value of 9. Hence, the total number of
        # possible digits can be 19. The counts array thus represents -9 at index 0 and 9 at
        # index 18. The index for a digit will be digit - min_val or digit + 9.
        min_val = -9
        counts = [0] * 19

        for val in self.array:
            digit = self.digit_at(val, place)
            counts[digit - min_val] += 1

        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]

        sorted_array = [None] * len(self.array)
        # Use counts array to determine the sorted index and copy the actual element using this
        # sorted index while iterating over the original array.
        for i in range(len(self.array) - 1, -1, -1):
            val = self.array[i]
            digit = self.digit_at(val, place)
            sorted_idx = counts[digit - min_val] - 1
            sorted_array[sorted_idx] = val
            counts[digit - min_val] -= 1

        for i in range(len(self.array)):
            self.array[i] = sorted_array[i]

    def digit_at(self, val, place):
        if val == 0:
            return 0

        # Get the digit at the given place
        place_divider = 10 ** (place - 1)
        digit = (abs(val) // place_divider) % 10
        # Determine the sign (positive or negative) using val // abs(val) returning -1 or 1
        return digit * (val // abs(val))
