import telebot
import requests

BOT_TOKEN = "9024050414:AAGPCjnylI4TEPRyng75qPXpQSY3sBBa-hg"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🔥 Welcome to PRINCE FREE LIKE BOT 07\n\n"
        "Use /info UID to check player details\n"
        "Use /like UID for Like service status"
    )

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(
        message,
        "Player details service is not connected yet.\n"
        "An authorized Free Fire player-data API is required."
    )

@bot.message_handler(commands=['like'])
def like(message):
    bot.reply_to(
        message,
        "Like service is currently unavailable.\n"
        "An authorized Garena Like API is required."
    )

print("PRINCE FREE LIKE BOT 07 is running!")

bot.infinity_polling()
