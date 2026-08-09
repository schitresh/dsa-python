# Heap Sort
# This is a comparison based sort based on binary heap. It follows a process similar to the
# selection sort where the minimum element is found and placed at the beginning but using heap.
# A max heap has its largest element at the top. This property is used to identify the largest
# element at each iteration, pushing it to the last and then rebuilding the heap. Hence, each
# iteration finds the next largest element using the heap property.
#
# It is an unstable sort due to the swapping of elements.
#
# Time Complexity: O(n * log(n))
#   Best Case: O(n * log(n)), or O(n) if all elements are identical
#   Worst Case: O(n * log(n))
# Auxiliary Space: O(log(n)), due to recursive stack
class HeapSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        self.build_max_heap()

        # In a max heap, the largest value is at index 0. Hence, we can send the largest element
        # at the end and then rebuild the heap. In next iteration, the second largest element will
        # float to 0 again, which can again be pushed to last. This way the array will be sorted.
        for i in range(len(self.array) - 1, 0, -1):
            self.swap_at(0, i)
            self.max_heapify(0, i - 1)

        return self.array

    # Builds a max heap where every parent is larger than the children. In an array, the children
    # are at 2 * i + 1 and 2 * i + 2 for the parent at index i.
    def build_max_heap(self):
        # The leaves are already mini heaps since they have only a single element, so we need to
        # start building the heap from the last parent (non-leaf) nodes. The last element is at
        # n - 1 and the parent of a node is at (i - 1) / 2 since index starts at 0. So the last
        # parent will be at (n / 2) - 1.
        last_parent_at = len(self.array) // 2 - 1

        # Iteratively build heap from the last parent node to the root node at index 0
        for i in range(last_parent_at, -1, -1):
            self.max_heapify(i, len(self.array) - 1)

    # Heapifies a broken branch at a given index. If the heap property is not satisfied at the
    # given index, sink that element down till it reaches a position where max heap is again
    # established. Hence, heapifying each element starting from the last parent node establishes
    # a heap, as done in build_max_heap.
    def max_heapify(self, index, till):
        # For index 0, children will be at 1 & 2. For index 1, children will be at 3 & 4. And so on.
        left = index * 2 + 1
        right = left + 1

        # Establish the heap property at the current index by identifying the largest element
        # among the parent and the children.
        largest_at = index

        if left <= till and self.array[left] > self.array[largest_at]:
            largest_at = left

        if right <= till and self.array[right] > self.array[largest_at]:
            largest_at = right

        # If the largest element was not at index, swap it to the index. The swapped index then
        # need to be max heapified since the value has changed.
        if largest_at != index:
            self.swap_at(index, largest_at)
            self.max_heapify(largest_at, till)

    def swap_at(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
