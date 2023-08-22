import random
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '6028447687:AAGJtVpsUDL6KAzDzcm6LPT5nYN9rjQwTuQ'

# List of video URLs
video_urls = [
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164269845889",
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164241156841",
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164052413165",
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164246101925",
]

# List of allowed video extensions
allowed_extensions = ['.mp4', '.mov']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send /reel to get a random video!")

def reel(update: Update, context: CallbackContext) -> None:
    # Filter video URLs by allowed extensions
    valid_video_urls = [url for url in video_urls if any(url.endswith(ext) for ext in allowed_extensions)]
    
    if valid_video_urls:
        random_video_url = random.choice(valid_video_urls)
        update.message.reply_video(random_video_url)
    else:
        update.message.reply_text("No valid videos available.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reel", reel))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
