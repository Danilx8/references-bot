import telebot
from telebot.util import quick_markup

bot = telebot.TeleBot("5624515371:AAGKpjNwEebG6XrbBFvsdU5hULFZJ12GHEI")
bot.set_my_commands([
    telebot.types.BotCommand("/start", "main menu"),
])

references_markup = quick_markup({
        'Тестирование': {'callback_data': 'qa'},
        'Веб': {'callback_data': 'web'},
        'DevOps': {'callback_data': 'dev_ops'}},
        row_width=1)

@bot.message_handler(commands=['start'])
def initialize(message):
    tid = message.chat.id
    bot.send_message(tid, '<b>Привет!</b>\n\nВыбери желаемую опцию из приведённых ниже:', parse_mode='HTML',
                     reply_markup=references_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    request = call.data
    references_markup_back = quick_markup({
        'Назад': {'callback_data': 'references_back'}
    })
    if request == 'references_back':
        bot.edit_message_text('Выбери желаемую опцию из приведённых ниже', reply_markup=references_markup,
                              chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif request == 'qa':
        bot.edit_message_text('<b>Полезные источники для начинающих тестировщиков:</b>\n\n'
                              '1: <a href="https://t.me/qajuniors">Чат в телеграме для начинающих тестировщиков</a>\n'
                              '2: <a href="https://www.youtube.com/channel/UC3qNyZvUNc_vdoah9J2wSyw">Полезный канал '
                              'на Youtube про тестирование</a>\n'
                              '3: <a href="https://testingpodcast.com/">Интересный подкаст про тестирование на '
                              'английском</a>\n', parse_mode='HTML', reply_markup=references_markup_back,
                              chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif request == 'web':
        bot.edit_message_text('<b>Полезные источники для начинающих веб-разработчиков:</b>\n\n'
                              '1: <a href="https://www.udemy.com/course/html-css-from-zero/">Курс по технологиям'
                              'HTML и CSS</a>\n'
                              '2: <a href="https://www.coursera.org/specializations/razrabotka-interfeysov">'
                              'Курс по разработке интерфейсов с помощью JavaScript </a>\n'
                              '3: <a href="https://www.youtube.com/playlist?list=PLu6MFGxDdilhKzUePH96oqhedQXROTNmg">'
                              'Четырёхчасовой курс на Youtube, погружающий в TypeScript</a>\n', parse_mode='HTML',
                              reply_markup=references_markup_back, chat_id=call.message.chat.id,
                              message_id=call.message.message_id)
    elif request == 'dev_ops':
        bot.edit_message_text('<b>Полезные источники для начинающих DevOps-инженеров:</b>\n\n'
                              '1: <a href="https://habr.com/ru/companies/skillfactory/articles/509344/">'
                              'Статья на Хабре о DevOps</a>\n'
                              '2: <a href="https://proglib.io/p/top-10-aktualnyh-knig-po-devops-ot-novichka-do-professionala-2021-09-30">'
                              'Список книг для изучения DevOps на любом уровне </a>\n'
                              '3: <a href="https://tproger.ru/curriculum/devops/"> План обучения DevOps</a>',
                              parse_mode='HTML', reply_markup=references_markup_back, chat_id=call.message.chat.id,
                              message_id=call.message.message_id)


bot.infinity_polling()
