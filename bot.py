from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Railway Variables থেকে আসবে
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    # Telegram ছাড়া অন্য POST ignore করবে
    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text_in = data["message"].get("text", "")

    if text_in == "/start":
        reply = "✅ Bot is LIVE!\nSend any message or TradingView signal."
    else:
        reply = f"""
🚨 OTC SIGNAL 🚨

📊 Signal: {text_in}
⏱ Timeframe: 1 Minute
🎯 Entry: Next Candle
⚠️ Risk: Manage Properly
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": chat_id,
        "text": reply
    })

    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Telegram Signal Bot Running ✅"

# 🚨 Railway এর জন্য MOST IMPORTANT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
