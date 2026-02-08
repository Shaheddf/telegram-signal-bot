from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    # Safety check
    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text_in = data["message"].get("text", "")

    if text_in.startswith("/start"):
        reply = "✅ Bot is LIVE!\nSend any signal text."
    else:
        reply = f"""🚨 OTC SIGNAL 🚨

📊 Signal: {text_in}
⏱ Timeframe: 1 Minute
🎯 Entry: Next Candle
⚠️ Risk: Manage Properly
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": reply
    })

    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Telegram Signal Bot Running ✅"

if __name__ == "__main__":
    app.run()
