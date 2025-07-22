import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Hello! I am your Job Bot. Use /jobs to see the latest jobs.")

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fetching latest jobs...")
    # Dummy jobs for now
    job_list = [
        "🖥️ Software Engineer - Google",
        "📱 Mobile Developer - Apple",
        "☁️ Cloud Engineer - AWS",
        "🤖 AI Engineer - OpenAI",
        "💻 Backend Developer - Microsoft"
    ]
    await update.message.reply_text("\n".join(job_list))

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("jobs", jobs))
    print("✅ Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
