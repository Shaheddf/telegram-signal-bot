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
        print(data)  # 👈 debug log

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            if text == "/start":
                send_message(
                    chat_id,
                    "✅ Bot is LIVE!\n\nSend signal like:\nBUY EURUSD"
                )
            else:
                send_message(
                    chat_id,
                    f"🚨 OTC SIGNAL 🚨\n\n📊 {text}\n⏱ 1 Minute\n🎯 Next Candle"
                )

        return "ok"

    return "Telegram Signal Bot Running ✅"


# 🔥 MOST IMPORTANT PART
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
