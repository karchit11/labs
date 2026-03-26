"""
Hackathon Auto-Grader V3 (UX Enhanced)
Reads per-lab pytest JSON reports, computes score, and writes
a Markdown summary with visual status indicators.
"""
import json
import os
from pathlib import Path

LABS = [
    ("lab-01-api-fetcher", "Lab 01: API Fetcher"),
    ("lab-02-llm-json",    "Lab 02: LLM JSON Output"),
    ("lab-03-toon-convert","Lab 03: TOON Converter"),
    ("lab-04-vehicle-detect","Lab 04: Vehicle Detection"),
    ("lab-05-rag-qa",      "Lab 05: RAG Q&A"),
    ("lab-06-healthcare-agents", "Lab 06: Healthcare Agents"),
]
POINTS_PER_LAB = 20

def get_lab_score(lab_dir: str) -> dict:
    report_file = f"test_results_{lab_dir}.json"
    if not Path(report_file).exists():
        return {"passed": 0, "total": 0, "status": "MISSING"}

    try:
        with open(report_file) as f:
            data = json.load(f)
            tests = data.get("tests", [])
            passed = sum(1 for t in tests if t.get("outcome") == "passed")
            total = len(tests)
            
            # Status Logic
            if total == 0: status = "ERROR"
            elif passed == total: status = "PASS"
            elif passed > 0: status = "PARTIAL"
            else: status = "FAIL"
            
            return {"passed": passed, "total": total, "status": status}
    except Exception:
        return {"passed": 0, "total": 0, "status": "ERROR"}

def score_labs() -> list[dict]:
    results = []
    for lab_dir, lab_name in LABS:
        s = get_lab_score(lab_dir)
        points = round((s["passed"] / s["total"]) * POINTS_PER_LAB) if s["total"] > 0 else 0
        results.append({
            "name": lab_name,
            "passed": s["passed"],
            "total": s["total"],
            "points": points,
            "max": POINTS_PER_LAB,
            "status": s["status"]
        })
    return results

def build_summary(results: list[dict]) -> str:
    total_points = sum(r["points"] for r in results)
    max_points = len(LABS) * POINTS_PER_LAB
    pct = round((total_points / max_points) * 100) if max_points else 0

    # Indicator mapping
    icons = {"PASS": "✅", "PARTIAL": "🟡", "FAIL": "❌", "MISSING": "⚪", "ERROR": "❓"}

    lines = [
        "# 🎓 AI Hackathon 2026: Lab Score Report",
        "",
        f"## 🏆 Progress Score: `{total_points} / {max_points}` (**{pct}%**)",
        "",
        "| Status | Lab | Tests Passed | Score |",
        "|:---:|-----|:---:|:---:|",
    ]
    for r in results:
        icon = icons.get(r["status"], "❓")
        lines.append(f"| {icon} | {r['name']} | `{r['passed']}/{r['total']}` | `{r['points']}/{r['max']}` |")

    lines += [
        "",
        "---",
        "### 💡 Next Steps",
        "> **✅ PASS**: Great job! Move to the next lab or explore starter kits.",
        "> **🟡 PARTIAL**: You're close! Check the logs for specific failing test cases.",
        "> **❌ FAIL / ⚪ MISSING**: Implement the TODOs in `solution.py` and push again.",
        "",
        "**[View Detailed Logs](https://github.com/Inmodel-Labs/labs/actions)**"
    ]
    return "\n".join(lines)

def main():
    results = score_labs()
    summary = build_summary(results)
    print(summary)

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as f:
            f.write(summary)

if __name__ == "__main__":
    main()
