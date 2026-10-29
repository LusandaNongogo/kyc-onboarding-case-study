import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from uat_report import must_requirements, summary, uncovered  # noqa: E402

BRD = """
| BR-01 | Start with OTP. | Must |
| BR-02 | Validate ID. | Must |
| BR-03 | Nice to have. | Could |
"""


def test_must_requirements_only():
    assert must_requirements(BRD) == ["BR-01", "BR-02"]


def test_uncovered():
    tests = [{"requirement": "BR-01"}]
    assert uncovered(tests, BRD) == ["BR-02"]


def test_summary_counts_retests():
    tests = [
        {"status": "Pass", "retest_result": ""},
        {"status": "Fail", "retest_result": "Pass"},
        {"status": "Fail", "retest_result": "Not retested"},
        {"status": "Blocked", "retest_result": "Not retested"},
    ]
    defects = [
        {"defect_id": "D1", "severity": "High", "title": "a", "status": "Fixed and retested"},
        {"defect_id": "D2", "severity": "Critical", "title": "b", "status": "Open"},
    ]
    s = summary(tests, defects)
    assert s["first_run_pass_rate"] == 0.25
    assert s["current_pass_rate"] == 0.5
    assert s["open_critical_or_high"] == 1
