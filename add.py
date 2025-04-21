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
