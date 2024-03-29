import telebot
import commandHandler

bot = telebot.TeleBot('bot_api_token')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    response = commandHandler.handle_command(message.text)
    response_type = str(type(response))
    if 'str' in response_type:
        bot.send_message(message.chat.id, response)
    elif 'Image' in response_type:
        bot.send_photo(message.chat.id, response)


if __name__ == '__main__':
    bot.polling(none_stop=True)
