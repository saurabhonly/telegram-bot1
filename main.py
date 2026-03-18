import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 🔐 Token from Railway Variables
TOKEN = os.getenv("BOT_TOKEN")

# 🧠 Logging setup (errors dekhne ke liye)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 👋 Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hello!\n\nBot chal raha hai 🚀")

# ℹ️ Help command
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("/start - Bot start\n/help - Help menu")

# 🤖 Auto reply (jo bhi message aaye uska reply)
def auto_reply(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"📩 Tumne likha: {text}")

# ❌ Error handler
def error(update: Update, context: CallbackContext):
    logging.error(f"Update {update} caused error {context.error}")

# 🚀 Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Auto reply handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    # Error handler
    dp.add_error_handler(error)

    print("✅ Bot started successfully...")
    
    updater.start_polling()
    updater.idle()

# ▶️ Run
if __name__ == "__main__":
    main()
