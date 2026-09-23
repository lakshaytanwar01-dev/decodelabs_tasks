# 🎨 Multimodal Image Generation Studio

A Python-based text-to-image application that converts natural-language prompts into generated digital artwork using the Hugging Face Inference API.

## 🚀 Project Overview

The Multimodal Image Generation Studio demonstrates how a natural-language description can be programmatically converted into an AI-generated image.

The project uses:

- **Python**
- **Hugging Face Inference API**
- **FLUX.1-schnell**
- **Pillow**
- **python-dotenv**

The application accepts a text prompt from the command line, sends it to an image-generation model, receives the generated image, saves it locally as a PNG file, and verifies the resulting image.

## ✨ Features

- Natural-language text-to-image generation
- Hugging Face Inference API integration
- FLUX.1-schnell image-generation model
- Configurable image output directory
- Environment-variable based API authentication
- PNG image saving
- Image integrity verification using Pillow
- Command-line interface
- Basic error handling

## 🏗️ Architecture

```text
User Prompt
     │
     ▼
Command-Line Interface
     │
     ▼
Prompt Validation
     │
     ▼
Hugging Face Inference API
     │
     ▼
FLUX.1-schnell
     │
     ▼
Generated Image
     │
     ▼
Local PNG File
     │
     ▼
Pillow Integrity Verification