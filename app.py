from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Load from .env
load_dotenv()  

# 2. Get key safely
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key missing! Create .env file")

# 3. Initialize client
client = OpenAI(api_key=api_key)

def chatbot():
    print("✨ AI: Hello! Type 'exit' to end.")
    messages = [{"role": "system", "content": "You're a helpful AI."}]

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("✨ AI: Goodbye!")
                break

            messages.append({"role": "user", "content": user_input})
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Note: "turbo" not "turbo"
                messages=messages,
                temperature=0.7
            )
            
            print(f"✨ AI: {response.choices[0].message.content}")
            
    except Exception as e:
        print(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    chatbot()