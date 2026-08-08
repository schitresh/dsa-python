from copy import deepcopy
import re

import pytest


# Helps to parametrize the class verifier. Iterates over the strategies if mentioned in the class
# being tested. And then iterates over each of the given cases.
def parametrize_class_verifier(verifier, cases):
    strategies = getattr(verifier.klass, "strategies", [None])

    def decorator(func):
        # Apply parametrization for strategies (quick-sort-hoare, merge-sort-default...)
        func = pytest.mark.parametrize(
            "strategy", strategies, ids=lambda s: verifier.case_label(s)
        )(func)

        # Apply parametrization for cases(1, 2, 3...)
        func = pytest.mark.parametrize(
            "case", cases, ids=lambda case: f"{cases.index(case) + 1}"
        )(func)

        return func

    return decorator


class ClassVerifier:
    def __init__(self, klass):
        self.klass = klass

    def test_case(self, case, strategy=None):
        case = deepcopy(case)
        klass_input = case["input"]
        method_params = case.get("params") or []

        if strategy:
            instance = self.klass(*klass_input, strategy=strategy)
        else:
            instance = self.klass(*klass_input)

        result = instance.perform(*method_params)
        self.assert_case(result, case, strategy)

    def assert_case(self, result, case, strategy=None):
        params_str = f"Params: {case['params']}" if "params\n" in case else "\n"
        strategy_str = f"{strategy}\n" if strategy else "\n"

        assert result == case["expected"], (
            f"{strategy_str}"
            f"  Input:    {case['input']}\n"
            f"  {params_str}"
            f"  Expected: {case['expected']}\n"
            f"  Result:   {result}"
        )

    def klass_label(self):
        pattern = re.compile(r"(?<!^)(?=[A-Z])")
        name = pattern.sub(" ", self.klass.__name__).title()
        return name

    def case_label(self, strategy=None) -> str:
        """
        Converts ClassName to kebab-case and appends strategy or 'default'.
        Example: QuickSort + 'hoare' -> 'quick-sort-hoare'
                 MergeSort + None    -> 'merge-sort'
        """
        # Convert CamelCase to kebab-case
        kebab_name = re.sub(r"(?<!^)(?=[A-Z])", "-", self.klass.__name__).lower()
        # Use strategy name if present, otherwise default to empty string
        strategy_label = f"-{str(strategy).lower()}" if strategy else ""

        return f"{kebab_name}{strategy_label}"
