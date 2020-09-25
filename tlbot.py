from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from decouple import config

def free_text_handler(update, context): #exemplo de comando com texto livre
    mensagem = update.message.text #decide aqui o que tu vai fazer com a mensagem
    print(mensagem)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Se tô eu e o gol, é gol!")

def start(update, context): #exemplo de comando com / algo
    print(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")



updater = Updater(token=config('BOT_HTTP_TOKEN'), use_context=True)
updater.start_polling()
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start) #mensagem /start
dispatcher.add_handler(start_handler)

free_text_handler = MessageHandler(Filters.text & (~Filters.command), free_text_handler) #mensagem livre
dispatcher.add_handler(free_text_handler)
