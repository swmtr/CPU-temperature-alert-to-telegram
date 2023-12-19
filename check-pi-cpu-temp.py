#!/home/wing/venv/bin/python3

# This script will check the current temperature of Raspberry Pi's CPU and will notify you on Telegram if it reaches over certain threshold

import subprocess
import telegram
import asyncio
import re

# Telegram Bot API token
TOKEN = 'FILL IN YOUR OWN TOKEN'

# Telegram chat ID to send the notifications to
CHAT_ID = 'FILL IN YOUR OWN ID'

# Execute the vcgencmd measure_temp command
output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
# Extract the temperature value with decimal
temperature = re.search(r"\d+\.\d", output).group(0)

# Check if any core temperature is higher than 50
if (float(temperature) > 45):
    # Construct the message with CPU temperatures
    message = f"❌ PI Alert CPU Temperatures ❌\n CPU: {temperature} C"

    async def send_telegram_notification():
        # Send the notification to Telegram
        bot = telegram.Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)

    # Execute the send_telegram_notification coroutine using asyncio.run()
    asyncio.run(send_telegram_notification())
