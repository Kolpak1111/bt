import telebot
bot = telebot.TeleBot('1569831737:AAGE5IL52odhw_uUgZlRYjd5vZQJwguGe34')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "������":
        bot.send_message(message.from_user.id,
                        "������, ��� � ���� ���� ������?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "������ ������")
    else:
        bot.send_message(message.from_user.id,
                     "� ���� �� �������. ������ /help.")
bot.polling(none_stop=True, interval=0)
        