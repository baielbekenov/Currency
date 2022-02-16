import telebot
import config
from telebot import types
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['USD'])
def USD(func=lambda call:True):
    Dollar_Som = (config.dol_som)
    headers = (config.user_agent)
    full_page = requests.get(Dollar_Som, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "blockquote-classic"})
    return convert[0].text


@bot.message_handler(commands=['EUR'])
def EUR(func=lambda call:True):
    EUR_SOM = (config.eur_som)
    headers = (config.user_agent)
    full_page = requests.get(EUR_SOM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class":"blockquote-classic"})
    return convert[0].text

@bot.message_handler(commands=['RUB'])
def RUB(func=lambda call:True):
    RUB_SOM = (config.rub_som)
    headers = (config.user_agent)
    full_page = requests.get(RUB_SOM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class":"blockquote-classic"})
    return convert[0].text

def KZT(func=lambda call:True):
    KZT_SOM = (config.kzt_som)
    headers = (config.user_agent)
    full_page = requests.get(KZT_SOM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "blockquote-classic"})
    return convert[0].text

def BTC(func=lambda call:True):
    BTC_SOM = (config.btc_som)
    headers = (config.user_agent)
    full_page = requests.get(BTC_SOM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "blockquote-classic"})
    return convert[0].text

@bot.message_handler(commands=['start'])
def send_message(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("USD")
    btn2 = types.KeyboardButton("EUR")
    btn3 = types.KeyboardButton("RUB")
    btn4 = types.KeyboardButton("KZT")
    btn5 = types.KeyboardButton("BTC")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Сейчас курс: " + USD(), reply_markup=markup)
    bot.send_message(message.chat.id, "Сейчас курс: " + EUR(), reply_markup=markup)
    bot.send_message(message.chat.id, "Сейчас курс: " + RUB(), reply_markup=markup)
    bot.send_message(message.chat.id, "Сейчас курс: " + KZT(), reply_markup=markup)
    bot.send_message(message.chat.id, "Сейчас курс: " + BTC(), reply_markup=markup)




# RUN
bot.polling(none_stop=True)




