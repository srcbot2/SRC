from flask import Flask
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from telegram_userbot.channel_scraper import scrape_messages
from telegram_userbot.media_extractor import extract_media
from telegram_userbot.media_uploader import upload_media
import threading

app = Flask(__name__)

# Telegram command handler
async def forward_channel(update, context):
    try:
        link = context.args[0]
        messages = scrape_messages(link)
        paths = extract_media(messages)
        upload_media(paths)  # ye sab target chats me bhej dega
        await update.message.reply_text("✅ Forward complete to all target chats.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# Telegram bot setup
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("forward_channel", forward_channel))

def run_bot():
    application.run_polling()

# Run Telegram bot in background thread
threading.Thread(target=run_bot, daemon=True).start()

# Health check route
@app.route("/")
def index():
    return "🚀 Telegram Bot is running on Render!"


