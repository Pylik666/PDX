from os import remove
import telebot
from random import randint

bot = telebot.TeleBot("5502678175:AAGRpzTiRVoV8nt5VhgxCO3jzz0vP9eZbhg")

@bot.message_handler(commands=['mems'])
def memes(message):
    number = randint(1,11)
    with open(f'memes/{number}.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)

@bot.message_handler(commands=['mem'])
def memes(message):
    with open('memes/1.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет вот все мои команды /help, /start, /mem, /mems")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Данный бот повторяет все что вы напишите")

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id,message.text)

@bot.message_handler(content_types=['photo'])
def repeat_photo(message):
    file_id = message.photo[-1].file_id
    print(file_id)
    file_info = bot.get_file(file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('image.png','wb') as file:
        file.write(downloaded_file)
    with open('image.png','rb') as file:
        bot.send_photo(message.chat.id,file)
        remove('image.png')



bot.polling(non_stop=True)