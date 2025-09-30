# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# @app.route('/')
# def home():
#     return render_template('telegram.html')
#
# @app.route('/send_message', methods=['GET','POST'])
# def send_message():
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({
#             "error": "No message"
#         }),400
#     url=f"https://api.telegram.org/bot7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg/sendMessage"
#     payload ={
#         "chat_id": CHAT_ID,
#         "text": f"New message from website: {user_message}"
#     }
#     # requests.post(url, json=payload)
#     #
#     # return jsonify({
#     #     "status": "Message sent"
#     # })
#     try:
#         # Send request to Telegram
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         # Check if Telegram accepted the message
#         if response.status_code == 200 and telegram_data.get("ok"):
#             return jsonify({
#                 "status": "Message sent successfully",
#                 "success": True
#             }), 200
#         else:
#             return jsonify({
#                 "status": "Failed to send message",
#                 "error": telegram_data.get("description", "Unknown error"),
#                 "success": False
#             }), 500
#
#     except Exception as e:
#         return jsonify({
#             "status": "Error sending message",
#             "error": str(e),
#             "success": False
#         }), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# # Store messages in memory (use a database in production)
# messages = []
#
#
# @app.route('/')
# def home():
#     return render_template('telegram.html')
#
#
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
#
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": f"New message from website: {user_message}"
#     }
#
#     try:
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         if response.status_code == 200 and telegram_data.get("ok"):
#             return jsonify({
#                 "status": "Message sent successfully",
#                 "success": True
#             }), 200
#         else:
#             return jsonify({
#                 "status": "Failed to send message",
#                 "error": telegram_data.get("description", "Unknown error"),
#                 "success": False
#             }), 500
#
#     except Exception as e:
#         return jsonify({
#             "status": "Error sending message",
#             "error": str(e),
#             "success": False
#         }), 500
#
#
# # Webhook endpoint - Telegram will send updates here
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     try:
#         update = request.json
#         print("Received update:", update)
#
#         # Check if message exists
#         if 'message' in update:
#             chat_id = update['message']['chat']['id']
#             text = update['message'].get('text', '')
#             username = update['message']['from'].get('username', 'Unknown')
#
#             # Store the message
#             messages.append({
#                 'text': text,
#                 'username': username,
#                 'chat_id': chat_id,
#                 'timestamp': time.time()
#             })
#
#             print(f"Stored message from {username}: {text}")
#
#         return jsonify({"status": "ok"}), 200
#     except Exception as e:
#         print(f"Webhook error: {e}")
#         return jsonify({"error": str(e)}), 500
#
#
# # Get recent messages from Telegram
# @app.route('/get_messages', methods=['GET'])
# def get_messages():
#     # Return last 10 messages
#     return jsonify({
#         "messages": messages[-10:],
#         "count": len(messages)
#     })
#
#
# # Clear old messages
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS
import time
import threading

app = Flask(__name__)
CORS(app)

TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
CHAT_ID = "7003841804"

# Store messages in memory
messages = []


@app.route('/')
def home():
    return render_template('telegram.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"New message from website: {user_message}"
    }

    try:
        response = requests.post(url, json=payload)
        telegram_data = response.json()

        if response.status_code == 200 and telegram_data.get("ok"):
            return jsonify({
                "status": "Message sent successfully",
                "success": True
            }), 200
        else:
            return jsonify({
                "status": "Failed to send message",
                "error": telegram_data.get("description", "Unknown error"),
                "success": False
            }), 500

    except Exception as e:
        return jsonify({
            "status": "Error sending message",
            "error": str(e),
            "success": False
        }), 500


@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({
        "messages": messages[-10:],
        "count": len(messages)
    })


@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    global messages
    messages = []
    return jsonify({"status": "Messages cleared"})


# Polling function to get updates from Telegram
def poll_telegram_updates():
    print("🔄 Starting Telegram polling...")
    offset = None

    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
            params = {
                "timeout": 30,
                "offset": offset
            }

            print(f"📡 Polling Telegram... (offset: {offset})")
            response = requests.get(url, params=params, timeout=35)
            data = response.json()

            if data.get("ok"):
                updates = data.get("result", [])
                print(f"📬 Received {len(updates)} updates")

                for update in updates:
                    offset = update["update_id"] + 1

                    if "message" in update:
                        chat_id = str(update['message']['chat']['id'])
                        text = update['message'].get('text', '')
                        username = update['message']['from'].get('username', 'Unknown')
                        first_name = update['message']['from'].get('first_name', 'User')

                        print(f"✉️ New message from {username} ({first_name}): {text}")

                        # Only store messages from your chat
                        if chat_id == CHAT_ID:
                            messages.append({
                                'text': text,
                                'username': username or first_name,
                                'chat_id': chat_id,
                                'timestamp': time.time()
                            })
                            print(f"💾 Message stored! Total messages: {len(messages)}")
                        else:
                            print(f"⚠️ Ignored message from different chat: {chat_id}")
            else:
                print(f"❌ Telegram API error: {data}")

        except Exception as e:
            print(f"❌ Polling error: {e}")
            time.sleep(5)


if __name__ == '__main__':
    # Start polling in background thread
    print("🚀 Starting Flask app with Telegram polling...")
    polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
    polling_thread.start()

    app.run(debug=True, port=5000, use_reloader=False)  # use_reloader=False prevents double threading