from telethon import TelegramClient
import asyncio

# Replace with your actual API credentials
api_id = input("Enter api id :")  # Replace with your API ID
api_hash = input("Enter api hash :")  # Replace with your API Hash

# Create Telegram client
client = TelegramClient("manual_session", api_id, api_hash)

async def send_message():
    await client.start()

    # User input for recipient and message
    target = input("Enter Telegram username or group ID: ")
    message = input("Enter your message: ")
    count = int(input("Enter how many times to send: "))

    for i in range(count):
        await client.send_message(target, f"{message}")
        print(f"Message {i+1} sent!")
        await asyncio.sleep(2)  # Delay to avoid spam detection

    await client.disconnect()

# Run the async function
asyncio.run(send_message())
