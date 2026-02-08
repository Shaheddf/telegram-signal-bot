from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("8307170677:AAF1h-t7acfbBIZRKdjJjOriOduQXFfzPtI")
CHAT_ID = os.environ.get("7961786489")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    signal = data.get("message", "NO SIGNAL")

    text = f"""
🚨 OTC SIGNAL 🚨

📊 Signal: {signal}
⏱ Timeframe: 1 Minute
🎯 Entry: Next Candle
⚠️ Risk: Manage Properly
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Telegram Signal Bot Running ✅"

if __name__ == "__main__":
    app.run()
