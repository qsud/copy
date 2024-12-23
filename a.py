import os
import asyncio
from telethon import TelegramClient, events

API_ID = "10647635"
API_HASH = "1c14e1c8cc585cb65dc9180a36089bd6"

GROUP_ID = -1002415943593
SESSION_FILE = "session_name"  # Name of the session file

# Remove existing session file (force fresh session every run)
if os.path.exists(f"{SESSION_FILE}.session"):
    os.remove(f"{SESSION_FILE}.session")

client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

@client.on(events.NewMessage(chats=GROUP_ID))
async def forward_bot_messages(event):
    sender = await event.get_sender()
    if sender.bot:
        if event.message.message:
            await client.send_message(GROUP_ID, event.message.message)
        elif event.message.media:
            await client.send_file(GROUP_ID, event.message.media, caption=event.message.message)

async def main():
    print("First-time login required.")
    phone_number = input("Enter your phone number (with country code, e.g., +123456789): ")
    await client.start(phone=phone_number)  # Prompt for OTP
    print(f"Authentication successful! Listening for bot messages in group {GROUP_ID}...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    while True:
        try:
            import asyncio
            asyncio.run(main())
        except Exception as e:
            print(f"Error occurred: {e}. Restarting in 3 seconds...")
            time.sleep(3)
