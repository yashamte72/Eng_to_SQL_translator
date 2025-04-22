from openai import OpenAI

client = OpenAI(
  api_key=""
)

print("Chat with GPT-4o Mini. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("GPT:", completion.choices[0].message.content.strip())
