"""
Hackathon Auto-Grader
Reads per-lab pytest JSON reports, computes score per lab, and writes
a Markdown summary to $GITHUB_STEP_SUMMARY.
"""
import json
import os
import glob
from pathlib import Path

LABS = [
    ("lab-01-api-fetcher", "Lab 01: API Fetcher"),
    ("lab-02-llm-json",    "Lab 02: LLM JSON Output"),
    ("lab-03-toon-convert","Lab 03: TOON Converter"),
    ("lab-04-vehicle-detect","Lab 04: Vehicle Detection"),
    ("lab-05-rag-qa",      "Lab 05: RAG Q&A"),
]
POINTS_PER_LAB = 20

def get_lab_score(lab_dir: str) -> dict:
    # Use the pattern test_results_{lab_dir}.json
    report_file = f"test_results_{lab_dir}.json"
    if not Path(report_file).exists():
        return {"passed": 0, "total": 0}

    try:
        with open(report_file) as f:
            data = json.load(f)
            tests = data.get("tests", [])
            passed = sum(1 for t in tests if t.get("outcome") == "passed")
            total = len(tests)
            return {"passed": passed, "total": total}
    except Exception as e:
        print(f"Error reading {report_file}: {e}")
        return {"passed": 0, "total": 0}

def score_labs() -> list[dict]:
    results = []
    for lab_dir, lab_name in LABS:
        score_data = get_lab_score(lab_dir)
        passed = score_data["passed"]
        total = score_data["total"]
        points = round((passed / total) * POINTS_PER_LAB) if total > 0 else 0
        
        results.append({
            "name": lab_name,
            "passed": passed,
            "total": total,
            "points": points,
            "max": POINTS_PER_LAB,
        })
    return results

def build_summary(results: list[dict]) -> str:
    total_points = sum(r["points"] for r in results)
    max_points = len(LABS) * POINTS_PER_LAB
    pct = round((total_points / max_points) * 100) if max_points else 0

    lines = [
        "# 🎓 Hackathon Lab Score Report",
        "",
        f"## 🏆 Total Score: `{total_points} / {max_points}` ({pct}%)",
        "",
        "| Lab | Tests Passed | Points |",
        "|-----|-------------|--------|",
    ]
    for r in results:
        # Success if at least one test exists and all passed
        status = "✅" if r["passed"] == r["total"] and r["total"] > 0 else ("⚠️" if r["passed"] > 0 else "❌")
        # Handle cases where no tests were found
        if r["total"] == 0:
            status = "❌"
        lines.append(f"| {status} {r['name']} | {r['passed']}/{r['total']} | {r['points']}/{r['max']} |")

    lines += [
        "",
        "---",
        "> **Tip:** Push again after fixing failing tests — your score will update automatically.",
    ]
    return "\n".join(lines)

def main():
    results = score_labs()
    summary = build_summary(results)

    # Print to console for debugging
    print(summary)

    # Write to GitHub Step Summary
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if summary_file:
        with open(summary_file, "a") as f:
            f.write(summary)

if __name__ == "__main__":
    main()
