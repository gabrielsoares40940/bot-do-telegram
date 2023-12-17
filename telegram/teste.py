from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater

arquivo = open("token.txt")
token = arquivo.read()
arquivo.close()
updater = Updater(token)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()