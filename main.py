import os
from dotenv import load_dotenv
from bot import VideoDownloaderBot

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    # Get the bot token from environment variable
    TOKEN = os.getenv('TELE_BOT_TOKEN')
    if not TOKEN:
        raise ValueError("No TELEGRAM_BOT_TOKEN provided")

    bot = VideoDownloaderBot(TOKEN)
    bot.run()
