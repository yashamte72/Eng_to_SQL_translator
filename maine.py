from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(
    api_key=""  # Replace with your actual API key
)

print("English to SQL Translator. Type 'exit' to quit.\n")

# Start the loop
while True:
    user_input = input("English: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Send prompt to GPT
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also use gpt-4 or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates natural language to SQL."},
            {"role": "user", "content": user_input}
        ]
    )

    # Print the generated SQL
    sql_query = completion.choices[0].message.content.strip()
    print("SQL:", sql_query, "\n")
