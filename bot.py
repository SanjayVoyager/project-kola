import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from downloader import VideoDownloader

class VideoDownloaderBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Welcome! Send me a video URL from any supported platform to download.')

    async def download_video(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = update.message.text
        chat_id = update.message.chat_id

        try:
            downloader = VideoDownloader(url)
            video_title = downloader.fetch_video_info()
            await update.message.reply_text(f'Downloading: {video_title} ...')
            file_path = downloader.download(save_path='/tmp')

            with open(file_path, 'rb') as video_file:
                await context.bot.send_video(chat_id=chat_id, video=video_file, supports_streaming=True)
            os.remove(file_path)

            await update.message.reply_text(f'Download complete: {video_title}')
        except Exception as e:
            await update.message.reply_text(f'An error occurred: {e}')

    def run(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.download_video))

        self.application.run_polling()
