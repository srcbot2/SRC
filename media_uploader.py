from telegram import Bot
from config import BOT_TOKEN, TARGET_CHAT_IDS

bot = Bot(token=BOT_TOKEN)

def upload_media(paths, target_chat_ids=None):
    """
    Send given media files to one or more target chats.
    :param paths: list of file paths
    :param target_chat_ids: optional list of chat IDs (default: config.TARGET_CHAT_IDS)
    """
    if target_chat_ids is None:
        target_chat_ids = TARGET_CHAT_IDS

    for chat_id in target_chat_ids:
        for path in paths:
            try:
                with open(path, "rb") as f:
                    if path.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                        bot.send_photo(chat_id=chat_id, photo=f)
                    elif path.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
                        bot.send_video(chat_id=chat_id, video=f)
                    else:
                        bot.send_document(chat_id=chat_id, document=f)
                print(f"✅ Sent {path} to {chat_id}")
            except Exception as e:
                print(f"❌ Failed to send {path} to {chat_id}: {e}")

