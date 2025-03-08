import os

# Clear terminal screen (works on both Windows & Linux/macOS)
os.system('cls' if os.name == 'nt' else 'clear')
import os
import json
import time
import asyncio
from telethon import TelegramClient
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

# Console setup for stylish output
console = Console()

# BIG ASCII Art Title for TELEGRAM BOMBER
console.print(Text("""
████████╗███████╗██╗     ███████╗ ██████╗  █████╗ ███╗   ███╗    
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗████╗ ████║    
   ██║   █████╗  ██║     █████╗  ██║  ███╗███████║██╔████╔██║    
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██║██║╚██╔╝██║    
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║    
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝    
""", style="bold red"))

console.print("[bold cyan] Welcome to TELEGRAM BOMBER[/bold cyan]\n")
console.print("[bold green] Follow the instructions below to proceed...[/bold green]\n")

# File to store API credentials
CONFIG_FILE = "config.json"

# Function to load API credentials
def load_api_credentials():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save API credentials
def save_api_credentials(api_id, api_hash):
    with open(CONFIG_FILE, "w") as file:
        json.dump({"api_id": api_id, "api_hash": api_hash}, file)

# Load credentials or ask for input
creds = load_api_credentials()
if "api_id" in creds and "api_hash" in creds:
    api_id, api_hash = creds["api_id"], creds["api_hash"]
    console.print("[green]✔ API credentials loaded from file.[/green]")
else:
    api_id = Prompt.ask("[bold cyan]Enter your Telegram API ID[/bold cyan]")
    api_hash = Prompt.ask("[bold cyan]Enter your Telegram API Hash[/bold cyan]")
    save_api_credentials(api_id, api_hash)
    console.print("[green]✔ API credentials saved![/green]")

# Initialize Telegram Client
client = TelegramClient("telegram_auto_sender", api_id, api_hash)

async def main():
    await client.start()

    # Get user inputs
    recipients = Prompt.ask("[bold cyan]Enter recipient usernames (comma-separated)[/bold cyan]").split(",")
    message = Prompt.ask("[bold cyan]Enter the message to send[/bold cyan]")
    quantity = int(Prompt.ask("[bold cyan]Enter how many times to send each message[/bold cyan]"))
    delay = float(Prompt.ask("[bold cyan]Enter delay time (in seconds) between messages[/bold cyan]"))

    console.print("\n[bold red]🚀 Starting TELEGRAM BOMBER...[/bold red]\n")

    try:
        for recipient in recipients:
            recipient = recipient.strip()
            for i in range(quantity):
                try:
                    await client.send_message(recipient, message)
                    console.print(f"[green]✔ Message {i+1} sent to {recipient}[/green]")
                    time.sleep(delay)  # Delay between messages
                except Exception as e:
                    console.print(f"[red]❌ Failed to send to {recipient}: {e}[/red]")
                    break  # Stop further sending to avoid issues
    except KeyboardInterrupt:
        console.print("\n[bold yellow]⚠️ Process interrupted by user (CTRL+C). Exiting safely...[/bold yellow]")
    finally:
        console.print("\n[bold green]✅ Bombing session completed![/bold green]\n")
        await client.disconnect()

# Run the script
with client:
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]⚠️ Program forcefully stopped by user![/bold yellow]")
        console.print("[bold green]✅ Exiting safely...[/bold green]")
