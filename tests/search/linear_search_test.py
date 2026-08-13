from dsa.search import LinearSearch
from tests.helpers import ClassVerifier

VERIFIER = ClassVerifier(LinearSearch)

CASES = [
    {"input": [[4, 5, 6, 7, 8, 9]], "params": [8], "expected": 4},
    {"input": [[4, 5, 6, 7, 8, 9]], "params": [4], "expected": 0},
    {"input": [[4, 5, 6, 7, 8, 9]], "params": [2], "expected": -1},
]


@VERIFIER.parametrize_strategies_and_cases(CASES)
def test_cases(strategy, case):
    VERIFIER.test_case(case, strategy)
