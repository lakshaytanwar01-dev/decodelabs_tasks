import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key securely from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Gemini model
MODEL_NAME = "gemini-3.6-flash"

# In-memory conversation history
conversation_history = []

# Number of complete conversation turns to remember
MAX_TURNS = 5


def trim_history():
    """Keep only the most recent complete conversation turns."""
    max_messages = MAX_TURNS * 2

    if len(conversation_history) > max_messages:
        del conversation_history[:-max_messages]


def generate_response(user_input):
    """Generate an AI response using the conversation history."""

    # Add user message to memory
    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # Keep history within the allowed limit
    trim_history()

    # Send conversation history to Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=conversation_history
    )

    assistant_response = response.text

    # Add AI response to memory
    conversation_history.append({
        "role": "model",
        "parts": [{"text": assistant_response}]
    })

    # Keep history within the allowed limit
    trim_history()

    return assistant_response


def display_header():
    """Display the chatbot interface header."""
    print("\n" + "=" * 60)
    print("          🤖 CUSTOM AI CHATBOT WITH MEMORY")
    print("=" * 60)
    print("  Powered by Gemini")
    print("  Type 'exit' to end the conversation")
    print("=" * 60 + "\n")


def main():
    display_header()

    while True:
        try:
            user_input = input("You  ➜ ").strip()

            # Validate empty input
            if not user_input:
                print("⚠️  Please enter a message.\n")
                continue

            # Exit command
            if user_input.lower() == "exit":
                print("\n" + "=" * 60)
                print("🤖 Chatbot: Goodbye! Have a great day! 👋")
                print("=" * 60)
                break

            # Generate AI response
            response = generate_response(user_input)

            print(f"\n🤖 AI   ➜ {response}\n")

        except KeyboardInterrupt:
            print("\n\n🤖 Chatbot: Goodbye! 👋")
            break

        except Exception as error:
            print(f"\n❌ Error: {error}\n")


if __name__ == "__main__":
    main()