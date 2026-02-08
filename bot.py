from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.get_json()

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            if text == "/start":
                send_message(
                    chat_id,
                    "✅ Bot is LIVE!\nSend any signal like:\n\nBUY EURUSD"
                )
            else:
                send_message(
                    chat_id,
                    f"🚨 OTC SIGNAL 🚨\n\n📊 Signal: {text}\n⏱ Timeframe: 1 Minute\n🎯 Entry: Next Candle"
                )

        return "ok"

    return "Telegram Signal Bot Running ✅"
