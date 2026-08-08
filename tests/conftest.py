# import pytest


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.failed and report.when == "call":
#         report.nodeid = ""
#         report.sections = []

#         if hasattr(report, "longrepr") and hasattr(report.longrepr, "reprcrash"):
#             report.longrepr.reprcrash.message = f"\n{report.longrepr.reprcrash.message}"
