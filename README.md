# Eng_to_SQL_translator
 # 🧠 English to SQL Translator

A simple web app that uses OpenAI's GPT model to translate natural language (English) queries into SQL queries.

![Image](https://github.com/user-attachments/assets/b6006d55-71ba-4947-9d09-f56b29a08179)
---

## 🚀 Features

- Translate plain English into valid SQL statements
- Built using Flask and OpenAI's API
- Easy-to-use web interface

---

## 📁 Project Structure


Eng_to_SQL_translator/
│
├── app.py                  # Main Flask backend
├── templates/
│   └── index.html          # Frontend HTML (with embedded JS)
└── README.md               # This file

---

## 🧰 Requirements

- Python 3.7+
- Flask
- OpenAI Python SDK

Install them using:

pip install flask openai

---

## 🔑 Setup OpenAI API Key

Get your API key from https://platform.openai.com/account/api-keys

Update app.py with your key:

client = OpenAI(
    api_key="your-api-key-here"
)

---

## 🏁 Running the App

1. Clone the repo:

   git clone https://github.com/yashamte72/Eng_to_SQL_translator.git
   cd Eng_to_SQL_translator

2. Install dependencies:

   pip install flask openai

3. Run the server:

   python app.py

4. Open your browser and go to:

   http://127.0.0.1:5000

---

## 🧪 Example Usage

Input:
Show me all customers who made a purchase in the last 30 days.

Output:
SELECT * FROM customers WHERE purchase_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

---.

---

## ✨ Credits

Built with ❤️ using:
- Flask: https://flask.palletsprojects.com/
- OpenAI GPT: https://platform.openai.com/

---
## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.



## 📬 Feedback

Have suggestions or improvements? Feel free to open an issue or pull request!
