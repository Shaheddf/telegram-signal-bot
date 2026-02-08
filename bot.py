from flask import Flask, request
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello! Bot is live 🚀")
