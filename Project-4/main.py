import argparse
from pathlib import Path

from src.analyzer import analyze_code
from src.validator import validate_response
from src.renderer import render_result


SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".js": "javascript",
    ".java": "java",
}


def read_code_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(SUPPORTED_EXTENSIONS.keys())
        raise ValueError(
            f"Unsupported file type: {path.suffix}. "
            f"Supported types: {supported}"
        )

    try:
        return path.read_text(encoding="utf-8")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except UnicodeDecodeError:
        raise ValueError(
            f"Could not decode {file_path} as UTF-8."
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI-powered Code Reviewer and Explainer"
    )

    parser.add_argument(
        "file",
        help="Path to the source code file"
    )

    args = parser.parse_args()

    try:
        code = read_code_file(args.file)

        file_extension = Path(args.file).suffix.lower()
        language = SUPPORTED_EXTENSIONS[file_extension]

        print(f"\nAnalyzing: {args.file}")
        print(f"Language: {language}")
        print("Sending code to Gemini...\n")

        response = analyze_code(code, language)

        result = validate_response(response)

        render_result(
            result["bug_report"],
            result["refactored_code"],
            result["language"],
        )

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()