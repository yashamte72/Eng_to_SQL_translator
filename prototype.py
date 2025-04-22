from openai import OpenAI

client = OpenAI(
  api_key="YOUR API KEY HERE"  # Replace with your actual API key
  # Make sure to keep your API key secure and not expose it in public repositories.
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
