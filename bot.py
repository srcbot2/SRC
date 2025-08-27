from flask import Flask
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from telegram_userbot.channel_scraper import scrape_messages
from telegram_userbot.media_extractor import extract_media
from telegram_userbot.media_uploader import upload_media
from env_validator import validate_env  # 🔐 Env check added
import threading
import logging

# 🔧 Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("🚀 Bot startup initiated")

# ✅ Validate environment before anything else
validate_env()

# 🌐 Flask app for health check
app = Flask(__name__)

@app.route("/")
def index():
    return "🚀 Telegram Bot is running on Render!"

@app.route("/health")
def health():
    return {"status": "ok"}

# 🤖 Telegram command handler
async def forward_channel(update, context):
    try:
        link = context.args[0]
        logger.info(f"[FORWARD] Scraping messages from: {link}")
        messages = scrape_messages(link)
        paths = extract_media(messages)
        upload_media(paths)
        await update.message.reply_text("✅ Forward complete to all target chats.")
    except Exception as e:
        logger.error(f"[ERROR] {e}")
        await update.message.reply_text(f"❌ Error: {e}")

# 🛠️ Telegram bot setup
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("forward_channel", forward_channel))

def run_bot():
    try:
        logger.info("📡 Starting Telegram polling...")
        application.run_polling()
    except Exception as e:
        logger.error(f"[BOT CRASH] {e}")

# 🧵 Run Telegram bot in background thread
threading.Thread(target=run_bot, daemon=True).start()


