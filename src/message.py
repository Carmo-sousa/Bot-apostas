import logging
from telegram import Bot
import time
import threading


def send_message(token, chat_id, message):
    for _ in range(1, 6):
        bot = Bot(token=token)
        bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
