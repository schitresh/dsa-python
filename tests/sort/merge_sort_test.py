from dsa.sort import MergeSort
from tests.helpers import verify_class

CASES = [{"input": [[0, -2, 3]], "expected": [-2, 0, 3]}]


def test_merge_sort():
    verify_class(MergeSort, CASES)
