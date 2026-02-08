import os
import requests
from flask import Flask, request

app = Flask(__name__)

# 🔐 Bot token from Railway Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram API base
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


# ✅ Root route (Railway health check)
@app.route("/", methods=["GET"])
def home():
    return "Bot is running ✅", 200


# ✅ Telegram webhook route
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data:
        return "No data", 400

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Simple reply
        send_message(chat_id, f"You said: {text}")

    return "OK", 200


# 📤 Send message function
def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)


# 🚀 Run app (Railway compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
