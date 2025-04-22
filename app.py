from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="your api key here"  # Replace with your actual key
)

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    english_input = data.get("question")

    # Send request to GPT model
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also use gpt-4 or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Translate natural language to SQL."},
            {"role": "user", "content": english_input}
        ]
    )

    # Extract and return SQL query
    sql = completion.choices[0].message.content.strip()
    return jsonify({"sql": sql})

if __name__ == "__main__":
    app.run(debug=True)
