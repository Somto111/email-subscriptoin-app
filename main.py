from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
CHAT_ID = "7003841804"

@app.route('/')
def home():
    return render_template('telegram.html')

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({
            "error": "No message"
        }),400
    url=f"https://api.telegram.org/bot7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg/sendMessage"
    payload ={
        "chat_id": CHAT_ID,
        "text": f"New message from website: {user_message}"
    }
    requests.post(url, json=payload)

    return jsonify({
        "status": "Message sent"
    })


if __name__ == '__main__':
    app.run(debug=True)