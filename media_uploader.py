from config import TARGET_CHAT_IDS

def upload_media(paths):
    for path in paths:
        for chat_id in TARGET_CHAT_IDS:
            try:
                client.send_file(chat_id, path)
            except Exception as e:
                with open("logs/forward.log", "a") as log:
                    log.write(f"[FAIL] {chat_id}: {e}\n")
