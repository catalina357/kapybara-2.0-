#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import API_TOKEN
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove,Message)

API_TOKEN = '<api_token>'

keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text = 'Моя кнопка', request_location=True)
button2 = KeyboardButton (text = 'Моя кнопка 2')
# button3 = KeyboardButton (text = 'Моя кнопка 3')
keyboard.add(button)
keyboard.add(button2)
keyboard.add('1', '2')
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
