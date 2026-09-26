from rich.console import Console
from rich.markdown import Markdown


console = Console()


def render_result(bug_report, refactored_code, language):
    markdown_output = (
        "## BUG_REPORT\n\n"
        + bug_report
        + "\n\n"
        + "## REFACTORED_CODE\n\n"
        + "```"
        + language
        + "\n"
        + refactored_code
        + "\n```\n"
    )

    console.print(Markdown(markdown_output))