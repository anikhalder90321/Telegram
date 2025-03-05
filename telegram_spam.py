from telethon import TelegramClient
import asyncio

# Replace with your Telegram API credentials
api_id = 123456  # Replace with your API ID
api_hash = "abcdef1234567890"  # Replace with your API Hash

# Create a Telegram client
client = TelegramClient("session_name", api_id, api_hash)

async def send_messages():
    await client.start()
    print("Logged in to Telegram!")

    # Replace with target username or group ID
    target = "username_or_group_id"

    # Message and spam count
    message = "Hello! This is an automated message."
    count = 100  # Set to unlimited if needed

    for i in range(count):
        await client.send_message(target, f"{message} [{i+1}]")
        print(f"Message {i+1} sent!")
        await asyncio.sleep(2)  # Adjust delay to avoid spam detection

    await client.disconnect()

# Run the script
asyncio.run(send_messages())
