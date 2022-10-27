import telebot

bot = telebot.TeleBot('5628198910:AAHxjGDeDpyrZ9TJbcwpkM7Xz3x-8BSfJJs')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling(timeout=1000)