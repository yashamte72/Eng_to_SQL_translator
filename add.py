from flask import Flask, request, jsonify, render_template
import openai

#INITIALIZE FLask App
app = Flask (__name__)

#add your openai API key here
openai.api_key = "my_key for security reasons github does not allow to push openai key" 

#home Rute: serves the HTML CODES from the templates folder
@app.route('/')
def home():
    return render_template('index.html')

#translate route: handle english to sql via post
@app.route('/translate', methods=['POST'])
def translate():
    #get the english text from the request
    english_text = request.json["text"]

    #send the english text to openai API for translation
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Convert English to SQL"},
            {"role": "user", "content": english_text}
        ]
    )

    #get the SQL text from the response
    sql_query = response.choices[0].message.content.strip()

    #return the SQL text as a JSON response
    return jsonify({"sql": sql_query})

#run the app
if __name__ == '__main__':
    app.run(debug=True)