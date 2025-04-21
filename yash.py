

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot():
    print("✨ AI: Hello! Type 'exit' to end.")
    messages = [{"role": "system", "content": "You're a helpful AI."}]

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("✨ AI: Goodbye!")
                break

            messages.append({"role": "user", "content": user_input})
            
            # Using the new API format
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )
            
            print(f"✨ AI: {response.choices[0].message.content}")
            
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
            break

if __name__ == "__main__":
    chatbot()