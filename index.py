import os
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ====== CONFIG ======
BOT_TOKEN = "8377097614:AAGt8MOFJfzdYCtpikwNK_noCsenKXVTUY0"   # 🔴 Replace with your token
DOWNLOAD_DIR = "/tmp"          # Directory for temporary downloads
CHAT_ID = "5933203565"         # Optional: restrict bot to your chat
# ====================

def start(update, context):
    update.message.reply_text("👋 Send me a file URL and I'll fetch it using Aria2 🚀")

def handle_message(update, context):
    url = update.message.text.strip()

    if not url.startswith("http"):
        update.message.reply_text("⚠️ Please send a valid URL.")
        return

    try:
        filename = url.split("/")[-1].split("?")[0] or "downloaded_file"
        local_filename = os.path.join(DOWNLOAD_DIR, filename)

        update.message.reply_text(f"⬇️ Downloading with Aria2: {filename} ...")

        # Run aria2c with 16 connections
        result = subprocess.run(
            ["aria2c", "-x", "16", "-s", "16", "-d", DOWNLOAD_DIR, "-o", filename, url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode != 0:
            update.message.reply_text(f"❌ Aria2 failed:\n{result.stderr.decode()}")
            return

        # Send file to Telegram
        with open(local_filename, "rb") as f:
            context.bot.send_document(chat_id=update.message.chat_id, document=f)

        update.message.reply_text("✅ File sent successfully!")

        # Delete file after sending
        os.remove(local_filename)

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
