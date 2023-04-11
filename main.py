import telebot

a = telebot.TeleBot("5624515371:AAGKpjNwEebG6XrbBFvsdU5hULFZJ12GHEI")


@a.message_handler(commands=['start'])
def startWork(message):
    tid = message.chat.id
    a.send_message(tid, "start work!")


a.polling()
