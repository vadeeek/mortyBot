'''import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '1705861754:AAFrneQXDvFv0M_whCJWzJweOUrB2y7aRHA'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user))

@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
'''
import telebot
import random as rnd

bot = telebot.TeleBot('1936596416:AAGclJlD_RGHT7Fv6kuaj_pIvj9Cyh8cnBk')

@bot.message_handler(commands=['start'])
def welcome(message):
    '''photo = open('C:/Users/super/OneDrive/Рабочий стол/1.jpg', 'rb')'''
    bot.send_message(message.chat.id, "Ну привет ебать!")
    '''bot.send_photo(message.chat.id, photo)'''
   
@bot.message_handler(commands=['gay'])
def gay(message):
    rnd_proc = rnd.randrange(0,100)
    bot.reply_to(message, "Ты гей с вероятностью " + str(rnd_proc) + "%.")
    if rnd_proc <= 50:
            bot.send_message(message.chat.id, "Скорее всего ты нормальный(но может всё-таки пидорок).")
    elif rnd_proc > 50:
        bot.send_message(message.chat.id, "Будьте осторожны с ним, возможно ему нравится гачи, и он сможет устроить вам fisting ass☝🏻🍑")
    

@bot.message_handler(commands=['id'])
def getCHAT_id(message):
    print(message.chat.id)

'''
@bot.message_handler(func=lambda message: True)
def send_text(message):
    if message.text.lower() == "морти" or "бот" or "конч" or "мой сладкий" or "мой сладенький":
        bot.send_message(message.chat.id, "Звали?")
        if message.text.lower() == "иди нахуй":
            bot.send_message(message.chat.id, "Пошел сам нахуй, гондон! Я ухожу <3")
            bot.stop_polling()

    else:
        bot.reply_to(message.chat.id, "Я не выкупаю, что это!👆 Я пока слишком тупой. Идите нахуй☺️")
        bot.send_message(message.chat.id, )'''

bot.polling(none_stop=True)
'''
bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}</b>, бот.".format(message.from_user, bot.get_me()), parse_mode='html')
'''