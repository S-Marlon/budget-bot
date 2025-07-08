from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7566851462:AAHF4TACvtHyYbDRf7_HlqgRBxbQXGLjmzk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o bot de orçamentos. Envie a mensagem com os dados da obra.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text
    await update.message.reply_text(f"Recebi sua mensagem: {mensagem}\nAgora vou interpretar e gerar o orçamento...")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
