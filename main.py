import telebot
import commandHandler
from settings import BOT_TOKEN, ADMIN_LIST

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def handle_message(message):

    uid = message.from_user.id

    if uid in ADMIN_LIST:
        response = commandHandler.handle_command(message.text)
        response_type = str(type(response))
    else:
        response = f'Insufficient Permissions (Your id: {uid})'  
        response_type = 'str'

    if 'str' in response_type:
        bot.send_message(message.chat.id, response)
    elif 'Image' in response_type:
        bot.send_photo(message.chat.id, response)
    


if __name__ == '__main__':
    bot.polling(none_stop=True)
