# Binary Search
# Binary search is applied only on a sorted array. Since the elements are ordered, the direction
# of the search can be determined whether the element under consideration is smaller or larger
# than the search key. Binary search utilizes this property by considering the mid element first.
# If the mid element is larger, then the key can only be present in the left subarray. Similarly,
# if it's smaller, then the key can only be present in the right subarray. This process is repeated
# until the key is found or all valid range has been considered.
#
# Time Complexity: O(log(n))
# Auxiliary Space: O(1)
# Comparisons: 2 * log(n) excluding the while condition
class BinarySearch:
    strategies = ("recursive", "iterative")

    def __init__(self, array, strategy="iterative"):
        self.array = array
        self.strategy = getattr(self, f"{strategy}_strategy")

    def perform(self, key):
        return self.strategy(key)

    # Time Complexity: O(log(n))
    # Auxiliary Space: O(log(n)) due to recursion stack
    def recursive_strategy(self, key):
        return self.recursive_search_at(key, 0, len(self.array) - 1)

    def recursive_search_at(self, key, left, right):
        if left > right:
            return -1

        # If left & right are large, they may overflow if summed. So instead use substraction
        # methed to calculate mid.
        mid = left + (right - left) // 2

        if key < self.array[mid]:
            return self.recursive_search_at(key, left, mid - 1)

        if key > self.array[mid]:
            return self.recursive_search_at(key, mid + 1, right)

        return mid

    # Time Complexity: O(log(n))
    # Auxiliary Space: O(1)
    def iterative_strategy(self, key):
        left = 0
        right = len(self.array) - 1

        # Keep partitioning the search area by half till the key is found.
        # Run the loop for left = right as well to check the last remaining single element.
        # Running till left < right will leave out that last element.
        while left <= right:
            # If left & right are large, they may overflow if summed. So instead use substraction
            # methed to calculate mid.
            mid = left + (right - left) // 2

            if key < self.array[mid]:
                right = mid - 1
            elif key > self.array[mid]:
                left = mid + 1
            else:
                return mid

        return -1
