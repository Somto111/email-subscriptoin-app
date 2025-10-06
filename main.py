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
#
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
#
#
# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
# import threading
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# # Store messages in memory
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
# @app.route('/get_messages', methods=['GET'])
# def get_messages():
#     return jsonify({
#         "messages": messages[-10:],
#         "count": len(messages)
#     })
#
#
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# # Polling function to get updates from Telegram
# def poll_telegram_updates():
#     print("🔄 Starting Telegram polling...")
#     offset = None
#
#     while True:
#         try:
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
#             params = {
#                 "timeout": 30,
#                 "offset": offset
#             }
#
#             print(f"📡 Polling Telegram... (offset: {offset})")
#             response = requests.get(url, params=params, timeout=35)
#             data = response.json()
#
#             if data.get("ok"):
#                 updates = data.get("result", [])
#                 print(f"📬 Received {len(updates)} updates")
#
#                 for update in updates:
#                     offset = update["update_id"] + 1
#
#                     if "message" in update:
#                         chat_id = str(update['message']['chat']['id'])
#                         text = update['message'].get('text', '')
#                         username = update['message']['from'].get('username', 'Unknown')
#                         first_name = update['message']['from'].get('first_name', 'User')
#
#                         print(f"✉️ New message from {username} ({first_name}): {text}")
#
#                         # Only store messages from your chat
#                         if chat_id == CHAT_ID:
#                             messages.append({
#                                 'text': text,
#                                 'username': username or first_name,
#                                 'chat_id': chat_id,
#                                 'timestamp': time.time()
#                             })
#                             print(f"💾 Message stored! Total messages: {len(messages)}")
#                         else:
#                             print(f"⚠️ Ignored message from different chat: {chat_id}")
#             else:
#                 print(f"❌ Telegram API error: {data}")
#
#         except Exception as e:
#             print(f"❌ Polling error: {e}")
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     # Start polling in background thread
#     print("🚀 Starting Flask app with Telegram polling...")
#     polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
#     polling_thread.start()
#
#     app.run(debug=True, port=5000, use_reloader=False)  # use_reloader=False prevents double threading



#
# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
# import threading
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7456725624"
#
# # Store messages in memory
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
#     """
#     Send a message from website -> Telegram
#     and also save it in local messages list.
#     """
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
#
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": user_message
#     }
#
#     try:
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         if response.status_code == 200 and telegram_data.get("ok"):
#             # Save sent message locally too
#             messages.append({
#                 'text': user_message,
#                 'username': "You",
#                 'chat_id': CHAT_ID,
#                 'timestamp': time.time()
#             })
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
# @app.route('/get_messages', methods=['GET'])
# def get_messages():
#     """
#     Return the last 20 messages for display in chat window.
#     """
#     return jsonify({
#         "messages": messages[-20:],
#         "count": len(messages)
#     })
#
#
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     """
#     Clear chat history in memory (resets chat window).
#     """
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# # Polling function to sync Telegram -> Flask memory
# def poll_telegram_updates():
#     print("🔄 Starting Telegram polling...")
#     offset = None
#
#     while True:
#         try:
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
#             params = {
#                 "timeout": 30,
#                 "offset": offset
#             }
#
#             response = requests.get(url, params=params, timeout=35)
#             data = response.json()
#
#             if data.get("ok"):
#                 updates = data.get("result", [])
#
#                 for update in updates:
#                     offset = update["update_id"] + 1
#
#                     if "message" in update:
#                         chat_id = str(update['message']['chat']['id'])
#                         text = update['message'].get('text', '')
#                         username = update['message']['from'].get('username', 'Unknown')
#                         first_name = update['message']['from'].get('first_name', 'User')
#
#                         # Save only messages from the configured chat
#                         if chat_id == CHAT_ID:
#                             messages.append({
#                                 'text': text,
#                                 'username': username or first_name,
#                                 'chat_id': chat_id,
#                                 'timestamp': time.time()
#                             })
#                             print(f"💾 Stored new Telegram message: {text}")
#             else:
#                 print(f"❌ Telegram API error: {data}")
#
#         except Exception as e:
#             print(f"❌ Polling error: {e}")
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     # Start Telegram polling in background thread
#     polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
#     polling_thread.start()
#
#     app.run(debug=True, port=5000, use_reloader=False)


# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
# import threading
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# # Store messages in memory
# messages = []
# last_processed_update_id = None
#
#
# @app.route('/')
# def home():
#     return render_template('chatbot.html')
#
#
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     """Send message to Telegram"""
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
#
#     # Send to Telegram
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": user_message
#     }
#
#     try:
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         if response.status_code == 200 and telegram_data.get("ok"):
#             print(f"✅ Sent to Telegram: {user_message}")
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
#         print(f"❌ Error: {e}")
#         return jsonify({
#             "status": "Error sending message",
#             "error": str(e),
#             "success": False
#         }), 500
#
#
# @app.route('/get_response', methods=['GET'])
# def get_response():
#     """Get latest bot response from Telegram"""
#     if messages:
#         latest = messages[-1]
#         return jsonify({
#             "response": latest['text'],
#             "success": True,
#             "timestamp": latest['timestamp']
#         })
#     return jsonify({
#         "response": None,
#         "success": False
#     })
#
#
# @app.route('/get_all_messages', methods=['GET'])
# def get_all_messages():
#     """Get all messages"""
#     return jsonify({
#         "messages": messages,
#         "count": len(messages)
#     })
#
#
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     """Clear message history"""
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# # Polling function to get updates from Telegram
# def poll_telegram_updates():
#     global last_processed_update_id
#     print("🔄 Starting Telegram polling...")
#     offset = None
#
#     while True:
#         try:
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
#             params = {
#                 "timeout": 30,
#                 "offset": offset
#             }
#
#             response = requests.get(url, params=params, timeout=35)
#             data = response.json()
#
#             if data.get("ok"):
#                 updates = data.get("result", [])
#
#                 for update in updates:
#                     offset = update["update_id"] + 1
#
#                     if "message" in update:
#                         message = update['message']
#                         chat_id = str(message['chat']['id'])
#                         text = message.get('text', '')
#                         message_id = message.get('message_id')
#
#                         # Only process messages from your chat
#                         if chat_id == CHAT_ID:
#                             # Avoid processing the same message twice
#                             if last_processed_update_id != message_id:
#                                 messages.append({
#                                     'text': text,
#                                     'timestamp': time.time(),
#                                     'message_id': message_id
#                                 })
#                                 last_processed_update_id = message_id
#                                 print(f"📨 New message from Telegram: {text}")
#
#         except Exception as e:
#             print(f"❌ Polling error: {e}")
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     print("🚀 Starting Flask app with Telegram polling...")
#     print(f"📱 Monitoring Telegram chat: {CHAT_ID}")
#
#     # Start polling in background thread
#     polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
#     polling_thread.start()
#
#     app.run(debug=True, port=5000, use_reloader=False)
#


# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
# import threading
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# # Store messages in memory
# messages = []
# last_processed_update_id = None
#
#
# @app.route('/')
# def home():
#     return render_template('chatbot.html')
#
#
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     """Send message to Telegram"""
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
#
#     # Send to Telegram
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": user_message
#     }
#
#     try:
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         if response.status_code == 200 and telegram_data.get("ok"):
#             print(f"✅ Sent to Telegram: {user_message}")
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
#         print(f"❌ Error: {e}")
#         return jsonify({
#             "status": "Error sending message",
#             "error": str(e),
#             "success": False
#         }), 500
#
#
# @app.route('/get_response', methods=['GET'])
# def get_response():
#     """Get latest bot response from Telegram"""
#     try:
#         if messages:
#             latest = messages[-1]
#             return jsonify({
#                 "response": latest['text'],
#                 "success": True,
#                 "timestamp": latest['timestamp']
#             }), 200
#         return jsonify({
#             "response": None,
#             "success": False
#         }), 200
#     except Exception as e:
#         return jsonify({
#             "response": None,
#             "success": False,
#             "error": str(e)
#         }), 200
#
#
# @app.route('/get_all_messages', methods=['GET'])
# def get_all_messages():
#     """Get all messages"""
#     return jsonify({
#         "messages": messages,
#         "count": len(messages)
#     })
#
#
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     """Clear message history"""
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# @app.errorhandler(404)
# def not_found(e):
#     """Handle 404 errors"""
#     return jsonify({"error": "Endpoint not found"}), 404
#
#
# @app.errorhandler(500)
# def server_error(e):
#     """Handle 500 errors"""
#     return jsonify({"error": "Internal server error"}), 500
#
#
# # Polling function to get updates from Telegram
# def poll_telegram_updates():
#     global last_processed_update_id
#     print("🔄 Starting Telegram polling...")
#     offset = None
#
#     while True:
#         try:
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
#             params = {
#                 "timeout": 30,
#                 "offset": offset
#             }
#
#             response = requests.get(url, params=params, timeout=35)
#             data = response.json()
#
#             if data.get("ok"):
#                 updates = data.get("result", [])
#
#                 for update in updates:
#                     offset = update["update_id"] + 1
#
#                     if "message" in update:
#                         message = update['message']
#                         chat_id = str(message['chat']['id'])
#                         text = message.get('text', '')
#                         message_id = message.get('message_id')
#
#                         # Only process messages from your chat
#                         if chat_id == CHAT_ID:
#                             # Avoid processing the same message twice
#                             if last_processed_update_id != message_id:
#                                 messages.append({
#                                     'text': text,
#                                     'timestamp': time.time(),
#                                     'message_id': message_id
#                                 })
#                                 last_processed_update_id = message_id
#                                 print(f"📨 New message from Telegram: {text}")
#
#         except Exception as e:
#             print(f"❌ Polling error: {e}")
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     print("🚀 Starting Flask app with Telegram polling...")
#     print(f"📱 Monitoring Telegram chat: {CHAT_ID}")
#
#     # Start polling in background thread
#     polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
#     polling_thread.start()
#
#     app.run(debug=True, port=5000, use_reloader=False)


# from flask import Flask, request, jsonify, render_template
# import requests
# from flask_cors import CORS
# import time
# import threading
#
# app = Flask(__name__)
# CORS(app)
#
# TELEGRAM_TOKEN = "7456725624:AAHmNYrGKRjY34Vb9MZgHwlFn-8uMqQqlKg"
# CHAT_ID = "7003841804"
#
# # Store messages in memory
# messages = []
# last_processed_update_id = None
# message_queue = []  # Queue for new responses
#
#
# @app.route('/')
# def home():
#     return render_template('telegram.html')
#
#
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     """Send message to Telegram"""
#     data = request.json
#     user_message = data.get("message")
#
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
#
#     # Clear the message queue before sending a new message
#     global message_queue
#     message_queue = []
#
#     # Send to Telegram
#     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": user_message
#     }
#
#     try:
#         response = requests.post(url, json=payload)
#         telegram_data = response.json()
#
#         if response.status_code == 200 and telegram_data.get("ok"):
#             print(f"✅ Sent to Telegram: {user_message}")
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
#         print(f"❌ Error: {e}")
#         return jsonify({
#             "status": "Error sending message",
#             "error": str(e),
#             "success": False
#         }), 500
#
#
# @app.route('/get_response', methods=['GET'])
# def get_response():
#     """Get latest bot response from Telegram"""
#     try:
#         if message_queue:
#             # Pop the first message from queue
#             response_msg = message_queue.pop(0)
#             print(f"📤 Sending response to web: {response_msg['text']}")
#             return jsonify({
#                 "response": response_msg['text'],
#                 "success": True,
#                 "timestamp": response_msg['timestamp']
#             }), 200
#         return jsonify({
#             "response": None,
#             "success": False
#         }), 200
#     except Exception as e:
#         return jsonify({
#             "response": None,
#             "success": False,
#             "error": str(e)
#         }), 200
#
#
# @app.route('/get_all_messages', methods=['GET'])
# def get_all_messages():
#     """Get all messages"""
#     return jsonify({
#         "messages": messages,
#         "count": len(messages)
#     })
#
#
# @app.route('/clear_messages', methods=['POST'])
# def clear_messages():
#     """Clear message history"""
#     global messages
#     messages = []
#     return jsonify({"status": "Messages cleared"})
#
#
# @app.errorhandler(404)
# def not_found(e):
#     """Handle 404 errors"""
#     return jsonify({"error": "Endpoint not found"}), 404
#
#
# @app.errorhandler(500)
# def server_error(e):
#     """Handle 500 errors"""
#     return jsonify({"error": "Internal server error"}), 500
#
#
# # Polling function to get updates from Telegram
# def poll_telegram_updates():
#     global last_processed_update_id, message_queue
#     print("🔄 Starting Telegram polling...")
#     offset = None
#
#     while True:
#         try:
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
#             params = {
#                 "timeout": 30,
#                 "offset": offset
#             }
#
#             response = requests.get(url, params=params, timeout=35)
#             data = response.json()
#
#             if data.get("ok"):
#                 updates = data.get("result", [])
#
#                 for update in updates:
#                     offset = update["update_id"] + 1
#
#                     if "message" in update:
#                         message = update['message']
#                         chat_id = str(message['chat']['id'])
#                         text = message.get('text', '')
#                         message_id = message.get('message_id')
#
#                         # Only process messages from your chat
#                         if chat_id == CHAT_ID:
#                             # Avoid processing the same message twice
#                             if last_processed_update_id != message_id:
#                                 msg_obj = {
#                                     'text': text,
#                                     'timestamp': time.time(),
#                                     'message_id': message_id
#                                 }
#                                 messages.append(msg_obj)
#                                 message_queue.append(msg_obj)  # Add to queue
#                                 last_processed_update_id = message_id
#                                 print(f"📨 New message from Telegram: {text}")
#                                 print(f"📊 Queue size: {len(message_queue)}")
#
#         except Exception as e:
#             print(f"❌ Polling error: {e}")
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     print("🚀 Starting Flask app with Telegram polling...")
#     print(f"📱 Monitoring Telegram chat: {CHAT_ID}")
#
#     # Start polling in background thread
#     polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
#     polling_thread.start()
#
#     app.run(debug=True, port=5000, use_reloader=False)


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
last_processed_update_id = None
message_queue = []  # Queue for new responses


@app.route('/')
def home():
    return render_template('chatbot.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    """Send message to Telegram"""
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Clear the message queue before sending a new message
    global message_queue
    message_queue = []

    # Send to Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": user_message
    }

    try:
        response = requests.post(url, json=payload)
        telegram_data = response.json()

        if response.status_code == 200 and telegram_data.get("ok"):
            print(f"✅ Sent to Telegram: {user_message}")
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
        print(f"❌ Error: {e}")
        return jsonify({
            "status": "Error sending message",
            "error": str(e),
            "success": False
        }), 500


@app.route('/get_response', methods=['GET'])
def get_response():
    """Get latest bot response from Telegram"""
    try:
        if message_queue:
            # Pop the first message from queue
            response_msg = message_queue.pop(0)
            print(f"📤 Sending response to web: {response_msg['text']}")
            return jsonify({
                "response": response_msg['text'],
                "success": True,
                "timestamp": response_msg['timestamp']
            }), 200
        return jsonify({
            "response": None,
            "success": False
        }), 200
    except Exception as e:
        return jsonify({
            "response": None,
            "success": False,
            "error": str(e)
        }), 200


@app.route('/get_all_messages', methods=['GET'])
def get_all_messages():
    """Get all messages"""
    return jsonify({
        "messages": messages,
        "count": len(messages)
    })


@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    """Clear message history"""
    global messages
    messages = []
    return jsonify({"status": "Messages cleared"})


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


# Polling function to get updates from Telegram
def poll_telegram_updates():
    global last_processed_update_id, message_queue
    print("🔄 Starting Telegram polling...")
    offset = None

    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
            params = {
                "timeout": 30,
                "offset": offset
            }

            response = requests.get(url, params=params, timeout=35)
            data = response.json()

            if data.get("ok"):
                updates = data.get("result", [])

                for update in updates:
                    offset = update["update_id"] + 1

                    if "message" in update:
                        message = update['message']
                        chat_id = str(message['chat']['id'])
                        text = message.get('text', '')
                        message_id = message.get('message_id')

                        # Check if message is from the bot itself
                        from_user = message.get('from', {})
                        is_bot = from_user.get('is_bot', False)

                        # Only process messages from your chat that are NOT from the bot
                        if chat_id == CHAT_ID and not is_bot:
                            # Avoid processing the same message twice
                            if last_processed_update_id != message_id:
                                msg_obj = {
                                    'text': text,
                                    'timestamp': time.time(),
                                    'message_id': message_id
                                }
                                messages.append(msg_obj)
                                message_queue.append(msg_obj)  # Add to queue
                                last_processed_update_id = message_id
                                print(f"📨 New message from Telegram user: {text}")
                                print(f"📊 Queue size: {len(message_queue)}")
                            else:
                                print(f"⏭️ Skipping duplicate message: {message_id}")
                        elif is_bot:
                            print(f"🤖 Ignoring bot's own message: {text}")

        except Exception as e:
            print(f"❌ Polling error: {e}")
            time.sleep(5)


if __name__ == '__main__':
    print("🚀 Starting Flask app with Telegram polling...")
    print(f"📱 Monitoring Telegram chat: {CHAT_ID}")

    # Start polling in background thread
    polling_thread = threading.Thread(target=poll_telegram_updates, daemon=True)
    polling_thread.start()

    app.run(debug=True, port=5000, use_reloader=False)