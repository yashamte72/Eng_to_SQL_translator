from openai import OpenAI

client = OpenAI(
  api_key="-your api key here-"
)

user_input = input("Enter your message to GPT-4o Mini: ")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": user_input}
  ]
)

print(completion.choices[0].message)
