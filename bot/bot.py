from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from unidecode import unidecode

# Não precisamos mais de BytesIO se vamos ler do disco
# from io import BytesIO

# Importamos os para lidar com caminhos de arquivo
import os

perfuracao_keywords = ['perfuracao','poço']
estrutura_keywords = ['estrutura','cano', 'tubo', 'revestimento', 'revestido']
tipo_keywords = ['simples','padrao','grande']


TOKEN = "7566851462:AAHF4TACvtHyYbDRf7_HlqgRBxbQXGLjmzk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o bot de orçamentos. Envie a mensagem com os dados da obra.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text
    await update.message.reply_text(f"Recebi sua mensagem: {mensagem}\nAgora vou interpretar e gerar o orçamento...")
    mensagem = unidecode(mensagem.lower())
    for keyword in tipo_keywords:
        
        if keyword in mensagem:
            if keyword == "simples":
                await update.message.reply_text(f"Aqui está um orçamento de poço {keyword}")
                
            if keyword == "padrao":
                await update.message.reply_text(f"Aqui está um orçamento de poço {keyword}")
            if keyword == "grande":
                await update.message.reply_text(f"Aqui está um orçamento de poço {keyword}")
    

async def pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # --- CORREÇÃO AQUI ---
    # Define o caminho para o arquivo PDF
    # 'os.path.join' é usado para construir caminhos de forma segura em diferentes SOs
    # 'os.path.dirname(__file__)' obtém o diretório do script atual
    # Depois navegamos para '..' (diretório acima) e então para 'TEMPLATES/TESTE.PDF'
    pdf_path = os.path.join(os.path.dirname(__file__),'..', 'budget', 'teste.pdf')

    # Verifica se o arquivo realmente existe antes de tentar enviar
    if os.path.exists(pdf_path):
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=open(pdf_path, 'rb'), # Abre o arquivo em modo binário de leitura
            filename='orcamento.pdf' # O nome que o usuário verá no Telegram
        )
        await update.message.reply_text("Orçamento em PDF enviado!")
    else:
        await update.message.reply_text(f"Erro: O arquivo PDF '{pdf_path}' não foi encontrado. Por favor, verifique o caminho.")
    # --- FIM DA CORREÇÃO ---

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()