import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '6416227615:AAG6WpsPt0GgZzzlxIFOj2m9T0aBZ0NTb0I'

# List of video URLs
video_urls = [
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164269845889>
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164241156841>
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164052413165>
    "https://cdn.discordapp.com/attachments/1101163334692245546/1101164246101925>
]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send /reel to get a random video!")

def reel(update: Update, context: CallbackContext) -> None:
    random_video_url = random.choice(video_urls)
    update.message.reply_video(random_video_url)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reel", reel))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()