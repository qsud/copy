import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

# Telegram API credentials
API_ID = "10647635"  # Replace with your API ID
API_HASH = "1c14e1c8cc585cb65dc9180a36089bd6"

GROUP_ID = -1002415943593  # Replace with your group ID

# Initialize Telegram client without saving session
client = TelegramClient('anon', API_ID, API_HASH)

@client.on(events.NewMessage(chats=GROUP_ID))
async def forward_bot_messages(event):
    sender = await event.get_sender()
    if sender.bot:
        if event.message.message:
            await client.send_message(GROUP_ID, event.message.message)
        elif event.message.media:
            await client.send_file(GROUP_ID, event.message.media, caption=event.message.message)

async def login():
    print("=== Telegram Account Login ===")
    phone_number = input("Enter your phone number (with country code, e.g., +123456789): ")
    try:
        await client.start(phone=phone_number)
    except SessionPasswordNeededError:
        print("Your account is protected with two-factor authentication.")
        password = input("Enter your password: ")
        await client.sign_in(password=password)
    except Exception as e:
        print(f"Error during login: {e}")
        return

async def main():
    await login()
    print("Successfully connected to Telegram!")
    print(f"Listening for bot messages in group {GROUP_ID}...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    while True:
        try:
            import asyncio
            asyncio.run(main())
        except Exception as e:
            print(f"Error occurred: {e}. Restarting in 3 seconds...")
            time.sleep(3)
