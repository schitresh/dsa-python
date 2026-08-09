from dsa.sort import QuickSort
from tests.helpers import ClassVerifier

VERIFIER = ClassVerifier(QuickSort)

CASES = [
    {"input": [[0, -2, 3, -1, 4]], "expected": [-2, -1, 0, 3, 4]},
    {"input": [[4, 5, 9, 8, 7, 3, 2, 1, 6]], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"input": [[3, 2, 1, 0, -1, -2, -3]], "expected": [-3, -2, -1, 0, 1, 2, 3]},
    {"input": [[12, 14, 8, -7, 15, -12]], "expected": [-12, -7, 8, 12, 14, 15]},
]


@VERIFIER.parametrize_strategies_and_cases(CASES)
def test_cases(strategy, case):
    VERIFIER.test_case(case, strategy)
