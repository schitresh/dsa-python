# Linear Search
# Linear search iterates over the elements of a given array to find a given key.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class LinearSearch:
    strategies = ("regular", "sentinel")

    def __init__(self, array, strategy="sentinel"):
        self.array = array
        self.strategy = getattr(self, f"{strategy}_strategy")

    def perform(self, key):
        return self.strategy(key)

    # Regular linear search use the regular for loop and finds the key
    # Comparisons: 2n + 1
    # n + 1 comparisons to run the loop (checking that index is not out of bounds)
    # n comparisons to compare array items and key
    def regular_strategy(self, key):
        for i in range(len(self.array)):
            if self.array[i] == key:
                return i

        return -1

    # Sentinel linear search optimizes over the regular search by reducing the number of
    # comparisons. It does so by removing the index comparison for checking whether the length
    # of the array has reached. It utilizes the key by putting it at the end and breaks the loop
    # when the key is found either earlier or at the end.
    # Comparisons: n + 2
    # n comparisons to compare array items and key
    # 2 comparisons after the loop to check if key is found
    def sentinel_strategy(self, key):
        last_val = self.array[-1]
        self.array[-1] = key

        idx = 0
        while self.array[idx] != key:
            idx += 1

        if idx < len(self.array) - 1 or last_val == key:
            return idx

        return -1
