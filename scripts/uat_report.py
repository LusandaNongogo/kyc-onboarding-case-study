"""Summarise the UAT run and check requirement coverage.

Reads uat/test_cases.csv, uat/defect_log.csv and docs/01_brd.md, prints a
summary and lists any Must requirement with no test case. Run from the
repo root:

    py scripts/uat_report.py
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def must_requirements(brd_text):
    """IDs of requirements marked Must in the BRD tables."""
    return re.findall(r"^\| (BR-\d+) \|.*\| Must \|$", brd_text, flags=re.M)


def summary(tests, defects):
    first = Counter(t["status"] for t in tests)
    current = Counter(
        "Pass" if t["status"] == "Pass" or t["retest_result"] == "Pass" else t["status"]
        for t in tests
    )
    open_defects = [d for d in defects if d["status"] == "Open"]
    return {
        "test_cases": len(tests),
        "first_run": dict(first),
        "first_run_pass_rate": first["Pass"] / len(tests),
        "after_retest": dict(current),
        "current_pass_rate": current["Pass"] / len(tests),
        "defects": len(defects),
        "defects_by_severity": dict(Counter(d["severity"] for d in defects)),
        "open_defects": [(d["defect_id"], d["severity"], d["title"]) for d in open_defects],
        "open_critical_or_high": sum(d["severity"] in ("Critical", "High") for d in open_defects),
    }


def uncovered(tests, brd_text):
    covered = {t["requirement"] for t in tests}
    return [r for r in must_requirements(brd_text) if r not in covered]


def main():
    tests = load(ROOT / "uat" / "test_cases.csv")
    defects = load(ROOT / "uat" / "defect_log.csv")
    brd = (ROOT / "docs" / "01_brd.md").read_text(encoding="utf-8")

    s = summary(tests, defects)
    print(f"Test cases: {s['test_cases']}")
    print(f"First run: {s['first_run']}  pass rate {s['first_run_pass_rate']:.0%}")
    print(f"After retest: {s['after_retest']}  pass rate {s['current_pass_rate']:.0%}")
    print(f"Defects: {s['defects']}  by severity {s['defects_by_severity']}")
    print("Open defects:")
    for d in s["open_defects"]:
        print(f"  {d[0]} [{d[1]}] {d[2]}")

    gaps = uncovered(tests, brd)
    print("Must requirements with no test case:", ", ".join(gaps) if gaps else "none")
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
