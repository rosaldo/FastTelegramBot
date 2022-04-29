#!/usr/bin/env python3
# coding: utf-8

import sys

import uvicorn
from fastapi import FastAPI

import telegrambot
from fasttelegrambot import FastTelegramBotAPI

ftb = FastTelegramBotAPI()
ftbapi = FastAPI(title=ftb.title, version=ftb.version)


@ftbapi.get("/")
def raiz():
    return f"{ftb.title} {ftb.version}"


@ftbapi.post("/telegrambot/create")
async def telegrambot_create(tb_create: telegrambot.TelegramBotCreate):
    return ftb.telegrambot_create(tb_create)


@ftbapi.post("/telegrambot/getUserID")
async def telegrambot_get_user_id(tb_get_user_id: telegrambot.TelegramBotGetUserID):
    return ftb.telegrambot_get_user_id(tb_get_user_id)


@ftbapi.post("/telegrambot/active")
async def telegrambot_active(tb_active: telegrambot.TelegramBotActive):
    return ftb.telegrambot_active(tb_active)


@ftbapi.post("/telegrambot/status")
async def telegrambot_status(tb_status: telegrambot.TelegramBotStatus):
    return ftb.telegrambot_status(tb_status)


@ftbapi.post("/telegrambot/send_message")
async def telegrambot_send_message(tb_send_message: telegrambot.TelegramBotSendMessage):
    return ftb.telegrambot_send_message(tb_send_message)


def main():
    if len(sys.argv) == 1:
        host = ftb.local
        port = int(ftb.port)
    elif len(sys.argv) == 2:
        host = sys.argv[1]
        port = int(ftb.port)
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])

    uvicorn.run("fasttelegrambot_api:ftbapi", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()
