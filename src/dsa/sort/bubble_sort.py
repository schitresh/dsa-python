# Bubble Sort
# This sort keeps swapping the adjacent elements till the smallest element bubbles up at the front.
# In each iteration, the largest element is pushed at the end by continuous swapping.
#
# It is a stable sort since only the adjacent elements are swapped keeping the original order
# unchanged.
#
# Time Complexity: O(n^2)
#   Best Case: O(n)
#   Worst Case: O(n^2)
# Auxiliary Space: O(1)
class BubbleSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        for i in range(len(self.array)):
            swapped = True

            # The largest element will always be pushed at the end. So, avoid the last position
            # of the previous iteration, which will be len - i since i starts from 0.
            for j in range(len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.swap_at(j, j + 1)
                    swapped = True

            # If no element is swapped, it means the array is sorted. Optimization to avoid futile
            # iterations.
            if not swapped:
                break

        return self.array

    def swap_at(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
