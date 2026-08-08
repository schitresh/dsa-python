# Insertion Sort
# This sort iterates over all the elements and inserts them at their correct place. For the element
# under consideration, all the elements before it are sorted and the current element is inserted
# before the next largest element.
# Consider the second element, the first element is obviously sorted and the second element is
# either inserted before or remains at its place. Similary, each element is inserted at its sorted
# place in the sorted sub-array one by one.
#
# It is a stable sort, since the adjacent values are moved linearly and the element is inserted
# at its sorted place.
#
# Time Complexity: O(n^2)
#   Best: O(n^2)
#   Worst: O(n^2)
# Auxiliary Space: O(1)
class InsertionSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        for i in range(1, len(self.array)):
            curr = self.array[i]
            j = i

            # Find the index at which the next largest element to the current element is present.
            # Until that element is found, keep moving the elements to the next place in order to
            # make space for the current element. This way, when we find the next largest element,
            # all the subsequent elements would have moved one place further, making space for the
            # current element.
            while j > 0 and curr < self.array[j - 1]:
                self.array[j] = self.array[j - 1]
                j -= 1

            # Place the current element
            self.array[j] = curr

        return self.array
