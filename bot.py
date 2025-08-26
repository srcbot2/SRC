from flask import Flask
from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN
from telegram_userbot.channel_scraper import scrape_messages
from telegram_userbot.media_extractor import extract_media
from telegram_userbot.media_uploader import upload_media

app = Flask(__name__)  # WSGI entry point for Gunicorn

def forward_channel(update, context):
    try:
        link = context.args[0]
        messages = scrape_messages(link)
        paths = extract_media(messages)
        upload_media(paths)
        update.message.reply_text("✅ Forward complete.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

# Telegram bot setup
updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler("forward_channel", forward_channel))

# Start polling in background thread
import threading
threading.Thread(target=updater.start_polling).start()

# Optional health check route
@app.route('/')
def index():
    return "Bot is running"
