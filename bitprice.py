from telegram.ext import Updater
from telegram.ext import CommandHandler
from datetime import datetime
import requests

now = datetime.now()

updater = Updater(token='556100706:AAEd3gFtUcu9iU51xnmdTJGgNKbJHw8QNjc')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Welcome to bitcoinPrice Bot")

def price(bot ,update ):
    currency = 'USD'
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    response = requests.get('https://api.coinbase.com/v2/prices/buy?currency={0}'.format(currency))
    bot.sendMessage(chat_id=update.message.chat_id, text='at {0} every {1} is {2} {3}'.format(
        date, response.json()['data']['base'], response.json()['data']['amount']
        , response.json()['data']['currency']))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

price_handler = CommandHandler('price', price)
dispatcher.add_handler(price_handler)

updater.start_polling()
updater.idle()
updater.stop()