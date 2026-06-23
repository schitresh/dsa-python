import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed and report.when == "call":
        report.nodeid = ""

        if hasattr(report, "longrepr") and hasattr(report.longrepr, "reprcrash"):
            # 1. Capture the raw assertion comparison text
            clean_message = report.longrepr.reprcrash.message

            report.sections = []

            # 2. Inject a newline (\n) right before the comparison block
            # This drops the "assert == " layout directly onto the next line
            report.longrepr = f"\n{clean_message}"
