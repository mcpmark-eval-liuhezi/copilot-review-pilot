# Copilot Review Pilot — Example Change

This small script is intentionally simple so we canWalking into Friday's meeting with a concrete, working demo of GitHub Copilot code review.

## What this script does

`hello_review.py` prints a friendly greeting and a short summary of the pilot repo state.
It exists purely as a landing page for our live demo of automated Copilot code reviews.

```python
#!/usr/bin/env python3
"""Minimal example script used to demo GitHub Copilot code review."""

def main() -> None:
    print("✅ Copilot Review Pilot demo script is running.")
    print("   Repo: mcpmark-eval-liuhezi/copilot-review-pilot")
    print("   Branch: pilot-change")
    print("   PR: open PR #1 (pilot-change -> main)")
    print("   Status: awaiting Copilot code review request.")


if __name__ == "__main__":
    main()
```

## How to run it

```bash
python3 hello_review.py
```

Expected output:

```
✅ Copilot Review Pilot demo script is running.
   Repo: mcpmark-eval-liuhezi/copilot-review-pilot
   Branch: pilot-change
   PR: open PR #1 (pilot-change -> main)
   Status: awaiting Copilot code review request.
```

## Purpose

This commit exists to let us show the team, live, how a Copilot review request
behaves on a real pull request: an automated reviewer comment with suggested
improvements, lane-by-lane feedback, and a merge decision that humans still own.

## Try it yourself

1. Open a PR from `pilot-change` into `main`.
2. Click **Request a Copilot review** (or use the API to request one).
3. Watch Copilot post a review with line-level comments.
4. Discuss whether this fits our team's workflow.
