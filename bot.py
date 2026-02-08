from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("8307170677:AAF1h-t7acfbBIZRKdjJjOriOduQXFfzPtI")
CHAT_ID = os.environ.get("7961786489")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json or {}
    signal = data.get("message", "NO SIGNAL")

    text = f"""
🔥 OTC SIGNAL 🔥

📊 Pair: {signal}
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

