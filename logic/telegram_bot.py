import telebot
from db.database import init_table, add_user_if_not_exists

def init_tgBot(key):
    bot = telebot.TeleBot(key[0])

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        try:
            init_table()
            user = message.from_user
            add_user_if_not_exists(user.id, user.username, user.first_name)

            bot.send_message(message.chat.id, f"{user.first_name}, ты зарегистрирован в игре! Жди начала на терминале.")
        except Exception as e:
            print("Ошибка при обработке /start:", e)

    print("Бот запущен.")
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("Ошибка при запуске polling:", e)
