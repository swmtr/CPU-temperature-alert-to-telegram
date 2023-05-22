# This script will check the current temperature of the CPU and will notify you on Telegram if it reaches over certain threshold

import subprocess
import telegram
import asyncio
import re

# Telegram Bot API token
TOKEN = 'REPLACE YOUR TELEGRAM BOT API TOKEN'

# Telegram chat ID to send the notifications to
CHAT_ID = 'YOUR BOT CHAT ID'

# Check if the lm-sensors package is installed
try:
    subprocess.check_output(["sensors", "-v"])
except FileNotFoundError:
    print("Error: lm-sensors package is not installed. Please install it first.")
    exit(1)

# Run sensors and extract the CPU temperatures
output = subprocess.check_output(["sensors"]).decode("utf-8")
temperatures = []

# Define a regular expression pattern to extract temperature values
pattern = r'Core \d+:\s+\+?(\d+)\.\d+°C'

# Search for temperature values using the regular expression pattern
matches = re.findall(pattern, output)

# Convert the matched temperature strings to integers
temperatures = [int(match) for match in matches]

# Check if any core temperature is higher than 50
if any(temp > 50 for temp in temperatures):
    # Construct the message with CPU temperatures
    message = "❌ Alert CPU Temperatures ❌\n"
    for i, temperature in enumerate(temperatures, start=1):
        message += f"Core {i}: {temperature}\n"

    async def send_telegram_notification():
        # Send the notification to Telegram
        bot = telegram.Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)

    # Execute the send_telegram_notification coroutine using asyncio.run()
    asyncio.run(send_telegram_notification())
