# Selection Sort
# This sort selects the smallest element from the unsorted array and puts it at the front.
#
# It is an unstable sort, since the swapping can place an element at any index.
#
# Time Complexity: O(n^2)
#   Best Case: O(n^2)
#   Worst Case: O(n^2)
# Auxiliary Space: O(1)
class SelectionSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        # In each iteration, the smallest element is brought to the front.
        for i in range(len(self.array)):
            # Find the index of the smallest element in the unsorted array (i, len) and swap it
            # to the front.
            smallest_at = i

            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[smallest_at]:
                    smallest_at = j

            self.swap_at(i, smallest_at)

        return self.array

    def swap_at(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
