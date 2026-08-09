# Bucket Sort
# This sort arranges the given elements in a set of buckets. These buckets are determined based
# on the number of buckets and the range of the values. Then each bucket is individually sorted
# using standard sorting algorithms, and then combined to give us the sorted array.
# The number of buckets is usually chosen to be the length of the array to keep it evenly
# distributed and avoid large individual buckets. The bucket is determined by normalizing the
# value under consideration depending on the value range and the bucket count.
#
# Stability depends on the underlying sort algorithm used for individual buckets.
#
# Time Complexity: O(n + k), where k is number of buckets
#   Best Case: O(n + k)
#   Worst Case: O(n^2) or O(n * log(n)), depending on the sort used for sorting individual buckets
# Auxiliary Space: O(n + k)
class BucketSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        # Establish the bucket range
        bucket_count = len(self.array)
        buckets = [[] for _ in range(bucket_count)]

        # Determine the value range
        max_val = max(self.array)
        min_val = min(self.array)
        value_range = max_val - min_val
        if value_range == 0:
            return self.array

        for i in range(len(self.array)):
            val = self.array[i]
            # Normalize the value to find a valid bucket range between 0 & k - 1. In simple terms
            # it positions the value on the value range, finds the unit value, and scales it to
            # the bucket range.
            # 'val - min_val' shifts the number to the appropriate position on the value range.
            # '/ value_range' normalizes the number to a decimal percentage between 0 and 1.
            # '* (k - 1)' scales the number across indices 0 through k - 1.
            bucket = int(((val - min_val) / value_range) * (bucket_count - 1))
            buckets[bucket].append(val)

        idx = 0
        # Sort the individual buckets and combine them
        for bucket in buckets:
            bucket.sort()

            for val in bucket:
                self.array[idx] = val
                idx += 1

        return self.array
