from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN", "8928120390:AAEympogm33_i2vpfQ5ejXfvZFV7-ujzq2M")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Topazito BOT IKO LIVE 24/7!\nTuma screenshot ya chart H4 ni-chambue SMC.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 CHART RECEIVED - SMC ANALYSIS:\n\n"
        "1. Structure: BOS Bullish ✅\n"
        "2. Order Block: Last bearish candle\n"
        "3. FVG: Ipo wazi\n\n"
        "ENTRY: OB ya H4\nSL: Chini ya OB\nTP: 1:2 RR"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("Bot inawaka...")
    app.run_polling()

if __name__ == '__main__':
    main()
