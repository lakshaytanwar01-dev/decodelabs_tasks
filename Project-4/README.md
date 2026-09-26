# Intelligent Code Reviewer & Explainer

An AI-powered developer utility that analyzes source code, identifies bugs and code-quality issues, and generates an optimized/refactored version of the code.

## Objective

The project demonstrates an automated code analysis pipeline using a Large Language Model (LLM). It accepts a raw source-code file, sends the code to Gemini with strict analytical instructions, validates the structured response, and renders the result in Markdown with syntax highlighting.

## Features

- Supports Python, JavaScript, and Java source files
- Reads source code as a raw string payload
- Detects syntax errors, logical bugs, runtime errors, security vulnerabilities, performance problems, and code-quality issues
- Generates a structured bug report
- Generates refactored and optimized code
- Validates the required response structure
- Renders the result with Rich Markdown
- Handles common file-ingestion errors
- Keeps the Gemini API key in an environment variable

## Architecture

The application follows an IPO-style pipeline:

### 1. Input / Ingest

- Reads the source-code file from the local filesystem
- Validates the file path
- Validates the supported file extension
- Converts the source file into a raw string payload

### 2. Processing / Context Orchestration

- Sends the source code to Gemini
- Provides strict analytical instructions
- Uses the source code as context
- Requests bug analysis and refactored code

### 3. Output / Deterministic Markdown

- Validates the Gemini response
- Checks for the required sections
- Extracts the bug report
- Extracts the refactored code
- Renders the final result using Rich Markdown

## Project Structure

```text
Project 4/
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── validator.py
│   └── renderer.py
│
├── samples/
│   └── buggy_code.py
│
├── outputs/
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md