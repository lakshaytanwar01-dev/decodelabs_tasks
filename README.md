# 🤖 Automated Copywriting & Tone Transformer

A Python-based Generative AI application that automatically creates marketing copy from a raw product description.

The generated copy can be customized according to the target platform, tone, temperature, and Top-P settings.

## 🎯 Project Objective

The objective of this project is to build an automated copywriting system that takes product information and generates marketing content suitable for different platforms.

The project supports:

- Product name
- Product description
- Target platform
- Desired tone
- Temperature
- Top-P

Supported platforms:

- LinkedIn
- Instagram
- Email

## ✨ Features

- 🤖 AI-generated marketing copy using Google Gemini
- 📝 Dynamic prompt template generation
- 🎯 Platform-specific copy generation
- 🎨 Custom tone control
- 🌡️ Temperature control
- 🔬 Top-P control
- ✅ Input validation using Pydantic
- ⚡ Asynchronous API requests
- 🔄 Concurrent bulk generation
- 📄 CSV input for bulk generation
- 💾 JSON output for generated results
- 🔁 Automatic retry with exponential backoff

## 🛠️ Technologies Used

- Python
- Google Gemini API
- `google-genai`
- Pydantic
- `asyncio`
- Tenacity
- `python-dotenv`
- `argparse`
- CSV / JSON

## 🏗️ Project Architecture

```text
User Input / CSV
       ↓
Argument Parsing
       ↓
Pydantic Validation
       ↓
Dynamic Prompt Compiler
       ↓
Gemini API
       ↓
Generated Marketing Copy
       ↓
Terminal / JSON Output