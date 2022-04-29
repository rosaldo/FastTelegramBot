#!/usr/bin/env python3
# coding: utf-8

from pydantic import BaseModel
from telebot import TeleBot
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.update import Update

telegrambot_list = {}


class telegrambot:
    active = ""
    bot_token = ""
    name = ""
    owner = ""
    group_users = []
    group_block = []

    def send_message(self, recipients: list, message: str):
        for to in recipients:
            TeleBot(self.bot_token).send_message(to, message)


class TelegramBotCreate(BaseModel):
    active = ""
    bot_token = ""
    name = ""
    owner = ""
    group_users = []
    group_block = []

    def create(self):
        if self.bot_token not in telegrambot_list:
            tgbl = telegrambot()
            tgbl.active = self.active
            tgbl.bot_token = self.bot_token
            tgbl.name = self.name
            tgbl.owner = self.owner
            tgbl.group_users = self.group_users
            tgbl.group_block = self.group_block
            telegrambot_list.update({self.bot_token: tgbl})
            return tgbl


class TelegramBotGetUserID(BaseModel):
    bot_token = ""
    owner_token = ""
    timeout = ""

    def get_user_id(self):
        if self.bot_token in telegrambot_list:
            updater = Updater(self.bot_token, use_context=True)
            updater.dispatcher.add_handler(CommandHandler("start", self._get_user_id))
            updater.start_polling(timeout=int(self.timeout))
            if updater.running:
                bot = TeleBot(self.bot_token).get_me().username
                token = self.owner_token
                timeout = self.timeout
                return f"Running in https://t.me/{bot}?start={token} with timeout of {timeout}sec"

    def _get_user_id(self, update: Update, context: CallbackContext):
        mess = update.message.text
        mess = mess.replace("/start ", "")
        if self.bot_token in telegrambot_list:
            tgbl = telegrambot_list.get(self.bot_token)
            if mess == self.owner_token and update.message.chat.id not in tgbl.group_users:
                tgbl.group_users.append(update.message.chat.id)
            elif update.message.chat.id not in tgbl.group_block:
                tgbl.group_block.append(update.message.chat.id)


class TelegramBotActive(BaseModel):
    bot_token = ""
    active = ""

    def set_active(self):
        if self.bot_token in telegrambot_list:
            tgbl = telegrambot_list.get(self.bot_token)
            tgbl.active = self.active
            return tgbl


class TelegramBotStatus(BaseModel):
    bot_token = ""

    def status(self):
        if self.bot_token in telegrambot_list:
            return telegrambot_list.get(self.bot_token)


class TelegramBotSendMessage(BaseModel):
    bot_token = ""
    recipients = []
    message = ""

    def send_message(self):
        if self.bot_token in telegrambot_list:
            tgbl = telegrambot_list.get(self.bot_token)
            recipients = [to for to in self.recipients if to in tgbl.group_users]
            if tgbl.active and recipients:
                tgbl.send_message(recipients, self.message)
                return "Message send"
