import logging
from telegram import Bot
import time
import threading


def send_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")


# message = '<del style="color: red">Hello!</del>'

message = f"""
<b>Chance de Gol: Time</b>

Campeonato
Time 01 0 x 1 Time 02

20 ataques perigosos em 30 minútos.
10 chutes a gol.
7 chutes fora.
3 cantos (escanteios).

Posse de bola: 60 x 50

<b>APM: 1,5</b>
<b>chance de gol: 15</b>
"""

# send_message('1478096349:AAH-QVCnNQMKikOY-kFnzzgS1HyJHWh4kfQ', 325105532, message)