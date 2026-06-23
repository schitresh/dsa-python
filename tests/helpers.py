from copy import deepcopy
import re


def print_class_name(klass):
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    name = pattern.sub(" ", klass.__name__).title()
    print(name)


def verify_class(klass, cases):
    for case in cases:
        case = deepcopy(case)
        klass_input = case["input"]
        method_params = case.get("params") or []

        result = klass(*klass_input).perform(*method_params)
        assert result == case["expected"], (
            f"Expected: {case['expected']}",
            f"Result: {result}",
        )
