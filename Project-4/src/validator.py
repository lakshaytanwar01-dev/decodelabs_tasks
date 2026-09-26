import re


def validate_response(response):
    required_sections = [
        "## BUG_REPORT",
        "## REFACTORED_CODE",
    ]

    for section in required_sections:
        if section not in response:
            raise ValueError(
                f"Invalid Gemini response: missing {section}"
            )

    bug_report_start = response.index("## BUG_REPORT") + len("## BUG_REPORT")
    refactored_start = response.index("## REFACTORED_CODE")

    bug_report = response[bug_report_start:refactored_start].strip()
    refactored_section = response[refactored_start:].strip()

    code_match = re.search(
        r"```([a-zA-Z0-9_+-]*)\s*\n(.*?)```",
        refactored_section,
        re.DOTALL,
    )

    if not code_match:
        raise ValueError(
            "Invalid Gemini response: REFACTORED_CODE must contain "
            "one Markdown-fenced code block."
        )

    refactored_code = code_match.group(2).strip()

    if not bug_report:
        raise ValueError("BUG_REPORT section is empty.")

    if not refactored_code:
        raise ValueError("REFACTORED_CODE section is empty.")

    return {
        "bug_report": bug_report,
        "refactored_code": refactored_code,
        "language": code_match.group(1) or "text",
    }