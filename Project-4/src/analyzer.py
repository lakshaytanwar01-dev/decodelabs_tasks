import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

SYSTEM_INSTRUCTION = (
    "You are a cold, analytical Senior Code Quality Assurance Engineer.\n\n"
    "Analyze the supplied source code for:\n"
    "- Syntax errors\n"
    "- Logical bugs\n"
    "- Runtime errors\n"
    "- Security vulnerabilities\n"
    "- Performance problems\n"
    "- Code quality issues\n\n"
    "Your response MUST follow exactly this Markdown structure:\n\n"
    "## BUG_REPORT\n"
    "- Direct and concise bullet points only.\n"
    "- Explain every important bug or issue found.\n"
    "- Do not include greetings or conversational filler.\n\n"
    "## REFACTORED_CODE\n"
    "Return only one valid Markdown-fenced code block containing the "
    "corrected, optimized, and runnable version of the supplied code.\n\n"
    "Do not add any content outside these two sections."
)


def analyze_code(code, language):
    if not API_KEY:
        raise ValueError(
            "GEMINI_API_KEY was not found. Add it to the .env file."
        )

    client = genai.Client(api_key=API_KEY)

    prompt = (
        SYSTEM_INSTRUCTION
        + "\n\nProgramming language: "
        + language
        + "\n\nAnalyze the following source code:\n\n"
        + "```"
        + language
        + "\n"
        + code
        + "\n```\n"
    )

    interaction = client.interactions.create(
        model=MODEL,
        input=prompt,
    )

    if not interaction.output_text:
        raise ValueError("Gemini returned an empty response.")

    return interaction.output_text
