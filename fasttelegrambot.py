#!/usr/bin/env python3
# coding: utf-8

import logging
import sys

from pydantic import BaseModel

import telegrambot

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("FastTelegramBot.log"), logging.StreamHandler(sys.stdout)],
)


class FastTelegramBotAPI(BaseModel):
    title = "Fast Telegram Bot"
    version = "1.0.0 alpha"
    local = "127.0.0.1"
    port = "7777"
    except_msg = "The system gave an error"

    def telegrambot_create(self, tb_create: telegrambot.TelegramBotCreate):
        try:
            res = tb_create.create()
            if res:
                return {"status": "success", "message": res}
            else:
                return {"status": "failure", "message": res}

        except Exception as e:
            logging.info(str(e))
            return {"status": self.except_msg, "error": e}

    def telegrambot_get_user_id(self, tb_get_user_id: telegrambot.TelegramBotGetUserID):
        try:
            res = tb_get_user_id.get_user_id()
            if res:
                return {"status": "success", "message": res}
            else:
                return {"status": "failure", "message": res}

        except Exception as e:
            logging.info(str(e))
            return {"status": self.except_msg, "error": e}

    def telegrambot_active(self, tb_active: telegrambot.TelegramBotActive):
        try:
            res = tb_active.set_active()
            if res:
                return {"status": "success", "message": res}
            else:
                return {"status": "failure", "message": res}

        except Exception as e:
            logging.info(str(e))
            return {"status": self.except_msg, "error": e}

    def telegrambot_status(self, tb_status: telegrambot.TelegramBotStatus):
        try:
            res = tb_status.status()
            if res:
                return {"status": "success", "message": res}
            else:
                return {"status": "failure", "message": res}

        except Exception as e:
            logging.info(str(e))
            return {"status": self.except_msg, "error": e}

    def telegrambot_send_message(self, tb_send_message: telegrambot.TelegramBotSendMessage):
        try:
            res = tb_send_message.send_message()
            if res:
                return {"status": "success", "message": res}
            else:
                return {"status": "failure", "message": res}

        except Exception as e:
            logging.info(str(e))
            return {"status": self.except_msg, "error": e}
