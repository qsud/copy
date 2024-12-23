import time
from telethon import TelegramClient, events

API_ID = "10647635"
API_HASH = "1c14e1c8cc585cb65dc9180a36089bd6"
PHONE_NUMBER = "919955711670"

GROUP_ID = -1002415943593

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=GROUP_ID))

async def forward_bot_messages(event):
    sender = await event.get_sender() 

    if sender.bot:
        if event.message.message:
            await client.send_message(GROUP_ID, event.message.message)
        elif event.message.media:
            await client.send_file(GROUP_ID, event.message.media, caption=event.message.message)

async def main():
    print("Connecting to Telegram...")
    await client.start(phone=PHONE_NUMBER)  # Authenticate the user
    print(f"Connected! Listening for bot messages in group {GROUP_ID}...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    while True:
        try:
            import asyncio
            asyncio.run(main())
        except Exception as e:
            print(f"Error occurred: {e}. Restarting in 3 seconds...")
            time.sleep(3)
