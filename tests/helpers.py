from copy import deepcopy
import re

import pytest


class ClassVerifier:
    def __init__(self, klass):
        self.klass = klass

    # Testing Helpers

    def test_case(self, case, strategy=None):
        case_copy = deepcopy(case)
        klass_input = case_copy["input"]
        method_params = case_copy.get("params") or []

        if strategy:
            instance = self.klass(*klass_input, strategy=strategy)
        else:
            instance = self.klass(*klass_input)

        result = instance.perform(*method_params)
        self.assert_case(result, case, strategy)

    def assert_case(self, result, case, strategy=None):
        params_str = f"Params:   {case['params']}" if "params" in case else ""
        strategy_str = f"{strategy}" if strategy else ""

        assert result == case["expected"], (
            f"{strategy_str}\n"
            f"  Input:    {case['input']}\n"
            f"  {params_str}\n"
            f"  Expected: {case['expected']}\n"
            f"  Result:   {result}"
        )

    # Parameterization Helpers

    # Helps to parametrize the class verifier. Iterates over the strategies if mentioned in the class
    # being tested. And then iterates over each of the given cases.
    def parametrize_strategies_and_cases(self, cases):
        strategies = getattr(self.klass, "strategies", [None])

        def decorator(func):
            func = self._parametrize_strategies(
                func, strategies, prefix=self.klass_label()
            )
            func = self._parametrize_cases(func, cases)
            return func

        return decorator

    def parametrize_strategies(self, strategies):
        def decorator(func):
            return self._parametrize_strategies(
                func, strategies, prefix=f"{self.klass_label()}-run-"
            )

        return decorator

    def parametrize_cases(self, cases, strategy=None):
        prefix = self.klass_label()
        prefix = f"{prefix}-{strategy}-run-" if strategy else ""

        def decorator(func):
            return self._parametrize_cases(func, cases, prefix=prefix)

        return decorator

    # Apply parametrization for strategies (quick-sort-hoare, merge-sort-...)
    def _parametrize_strategies(self, func, strategies, prefix=""):
        func = pytest.mark.parametrize(
            "strategy", strategies, ids=lambda s: f"{prefix}{self.strategy_label(s)}"
        )(func)
        return func

    # Apply parametrization for cases (1, 2, 3...)
    def _parametrize_cases(self, func, cases, prefix=""):

        func = pytest.mark.parametrize(
            "case", cases, ids=lambda case: f"{prefix}{cases.index(case) + 1}"
        )(func)
        return func

    # Label Helpers

    def klass_name(self):
        pattern = re.compile(r"(?<!^)(?=[A-Z])")
        name = pattern.sub(" ", self.klass.__name__).title()
        return name

    # Converts ClassName to kebab-case
    def klass_label(self):
        return re.sub(r"(?<!^)(?=[A-Z])", "-", self.klass.__name__).lower()

    def strategy_label(self, strategy):
        return f"-{str(strategy).lower()}" if strategy else ""
