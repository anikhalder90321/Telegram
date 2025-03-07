from telethon import TelegramClient
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Initialize Rich Console
console = Console()

# Replace with your Telegram API credentials
api_id = input("Enter your api id : ")  # Your API ID
api_hash = input("Enter your api hash : ")  # Your API Hash

# Create Telegram client
client = TelegramClient("styled_session", api_id, api_hash)

async def send_message():
    await client.start()

    console.print(Panel.fit("[bold cyan]📩 Telegram Auto Message Sender 📩[/bold cyan]"))

    target = Prompt.ask("[bold yellow]🔹 Enter Telegram username or group ID[/bold yellow]")
    message = Prompt.ask("[bold yellow]💬 Enter your message[/bold yellow]")
    count = int(Prompt.ask("[bold yellow]🔢 Enter how many times to send[/bold yellow]"))
    delay = int(Prompt.ask("[bold yellow]⏳ Enter delay time (in seconds) between messages[/bold yellow]"))

    console.print("\n[bold green]✅ Sending messages...[/bold green]\n")

    for i in range(count):
        await client.send_message(target, f"{message} [{i+1}]")
        console.print(f"[bold blue]📨 Message {i+1} sent![/bold blue]")
        await asyncio.sleep(delay)

    console.print("\n[bold green]🎉 All messages sent successfully! 🎉[/bold green]")
    await client.disconnect()

# Run the async function
asyncio.run(send_message())
