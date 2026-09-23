# 🤖 Custom AI Chatbot with Memory

A conversational AI chatbot built using Python and the Google Gemini API.

This project demonstrates how a stateless Large Language Model (LLM) can be transformed into a contextual chatbot by maintaining conversation history in an in-memory Python list.

## 🎯 Project Objective

The objective of this project is to build a chatbot that remembers previous user messages during a live session.

The project focuses on:

- API integration with a frontier LLM
- In-memory conversation history
- Stateful conversation management
- Context preservation
- Input validation
- Sliding-window memory management

## ✨ Features

- 🤖 AI-powered conversations using Google Gemini
- 🧠 Remembers previous messages during the active session
- 💬 Maintains user and AI conversation history
- 🔄 Sends previous conversation context with new requests
- 🛡️ Secure API-key handling using environment variables
- ⚠️ Empty-input validation
- 📦 Sliding-window history to limit stored messages
- 🚪 Simple `exit` command to end the session

## 🛠️ Technologies Used

- Python
- Google Gemini API
- `google-genai`
- `python-dotenv`

## 🏗️ How It Works

The chatbot maintains an in-memory conversation history:

```text
User Input
    ↓
Add message to conversation_history
    ↓
Send conversation history to Gemini
    ↓
Generate AI response
    ↓
Add AI response to conversation_history
    ↓
Display response
```

Because previous interactions are included in subsequent API requests, the chatbot can understand references to earlier messages.

## 🧠 Memory Architecture

The project uses a Python list to maintain conversation history.

Each user interaction is stored with its role and message content:

```python
{
    "role": "user",
    "parts": [{"text": "My name is Lakshay"}]
}
```

The AI response is stored similarly:

```python
{
    "role": "model",
    "parts": [{"text": "Hello Lakshay!"}]
}
```

The conversation history is then passed back to the Gemini model for the next response.

### Sliding Window

To prevent the conversation history from growing indefinitely, the project keeps only the most recent conversation turns.

```python
MAX_TURNS = 5
```

This provides a simple FIFO/sliding-window approach to conversation memory.

## 📂 Project Structure

```text
Generative-AI-Project-1/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── screenshots/
    ├── chatbot.png
    └── memory-test.png
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Generative-AI-Project-1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your actual API key to GitHub.

### 4. Run the chatbot

```bash
python app.py
```

## 💬 Example

```text
============================================================
          🤖 CUSTOM AI CHATBOT WITH MEMORY
============================================================
  Powered by Gemini
  Type 'exit' to end the conversation
============================================================

You ➜ My name is Lakshay

🤖 AI ➜ Hello Lakshay! It's great to meet you.

You ➜ I am doing a Generative AI internship.

🤖 AI ➜ That's awesome! ...

You ➜ What is my name?

🤖 AI ➜ Your name is Lakshay!
```

The final question demonstrates that the chatbot retained information from an earlier interaction.

## 📸 Screenshots

### Chatbot Interface

![Chatbot Interface](screenshots/chatbot.png)

### Memory Test

![Memory Test](screenshots/memory-test.png)

## 🔐 Security

The Gemini API key is stored in a `.env` file and excluded from Git using `.gitignore`.

The repository contains `.env.example` only as a template.

## 🚀 Future Improvements

- Web-based chat interface
- Persistent conversation storage
- Streaming responses
- Conversation export
- Multiple chat sessions
- User authentication
- RAG-based knowledge retrieval

## 👨‍💻 Project

**Generative AI Internship — Project 1**

**Project:** Custom AI Chatbot with Memory