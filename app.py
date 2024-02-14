import telebot
import requests
import json



TOKEN = "6965433386:AAGfyNWNSjSyPo0pIsd-oenQHFgt_nWourE"

#API
headers= {
  "apikey": "LoS55C3ygIii5KlYo7prmMseWR01qQ4Y"
}

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUB',   
    'доллар': 'USD',
    'евро': 'EUR'
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, напишите боту сообщение в формате: \n<имя первой валюты> \
<имя второй валюты> \
<количество валюты> \
\nпервая валюта - исходная \
\nвторая валюта - в которую конвертировать\
\nСписок доступных валют: /values'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join ((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={keys[base]}&from={keys[quote]}&amount={amount}"', headers=headers)
    text = json.loads(r.content)[keys[base]]
    bot.send_message(message.chat.id, text)
    


bot.polling()