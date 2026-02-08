from flask import Flask, request
import requests

TOKEN = "8307170677:AAFlXIJ1yiPO3m6I8ugTfWpIos3IiNAutMM"
CHAT_ID = "7961786489"

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get("message", "NO SIGNAL")

    text = f"""🔥 OTC SIGNAL 🔥

📊 {signal}
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
    app.run()
