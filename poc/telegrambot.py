#!/usr/bin/env python3
# coding: utf-8

# https://towardsdatascience.com/bring-your-telegram-chatbot-to-the-next-level-c771ec7d31e4
# https://github.com/gcatanese/TelegramBotDemo

from telebot import TeleBot

CHAVE_API = "token:telegrambot"

bot = TeleBot(CHAVE_API)


@bot.message_handler(commands=["eco"])
def response(mensagem):
    bot.send_message(mensagem.chat.id, mensagem.text)


@bot.message_handler(commands=["mens"])
def response(mensagem):
    bot.send_message(mensagem.chat.id, mensagem)


@bot.message_handler(commands=["bot"])
def response(mensagem):
    bot.send_message(mensagem.chat.id, bot.get_me())


@bot.message_handler(commands=["user"])
def response(mensagem):
    bot.send_message(mensagem.chat.id, bot.get_chat(mensagem.chat.id))


menu = """
Olá ... escolha uma das opções:
    /bot:
    /eco:
    /mens:
    /user:
"""


def verify(mensagem):
    if mensagem.text == "menu":
        return True
    else:
        return False


@bot.message_handler(func=verify)
def response(mensagem):
    bot.send_message(mensagem.chat.id, menu)


def start(mensagem):
    mens = mensagem.text
    mens = mens.replace("/start ", "")
    if mens == "auth":
        return True
    else:
        mens = "você não está autorizado"
        bot.send_message(mensagem.chat.id, mens)


@bot.message_handler(func=start)
def response(mensagem):
    mens = str(mensagem.chat.id) + ": você está autorizado"
    bot.send_message(mensagem.chat.id, mens)


bot.polling()
