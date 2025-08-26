from telethon.sync import TelegramClient
from config import API_ID, API_HASH

client = TelegramClient('session_name', API_ID, API_HASH)
client.start()

def scrape_messages(channel_link):
    entity = client.get_entity(channel_link)
    history = client(GetHistoryRequest(peer=entity, limit=1000, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    return history.messages
  
