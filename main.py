import telebot

# جایگزین کنید با توکن بات خود
bot = telebot.TeleBot('7077424292:AAFvzqp3EOtXiRXJRS76hRqZ8fTrVIvPx1U')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"سلام {message.from_user.first_name}! شناسه چت شما: {message.chat.id}")

bot.polling()