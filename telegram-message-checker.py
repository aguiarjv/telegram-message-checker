import os
import requests
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

# Loading environment variables
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SEARCH_WORDS = [word.strip() for word in os.getenv("SEARCH_WORDS").lower().split(",")]

# Getting bot id
BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/"
response = requests.get(BOT_URL + "getMe")

if response.ok:
    BOT_ID = response.json().get("result").get("id")
else:
    BOT_ID = None

# Setting up client
client = TelegramClient("anon", TELEGRAM_API_ID, TELEGRAM_API_HASH)


def bot_send_message(user_id, message):
    url = BOT_URL + "sendMessage"
    payload = {"chat_id": user_id, "text": message}

    response = requests.post(url, json=payload)
    if response.ok:
        print("Message sent")
    else:
        print("Error sending message")


# Listening on new messages
@client.on(events.NewMessage(incoming=True))
async def new_message_handler(event):
    if BOT_ID is None:
        return

    me = await client.get_me()
    sender = await event.get_sender()

    if sender.id != BOT_ID:
        for word in SEARCH_WORDS:
            if word in event.raw_text.lower():
                bot_send_message(me.id, event.raw_text)
                break


client.start()
client.run_until_disconnected()
