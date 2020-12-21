from telegram import Bot
from telegram.ext import CommandHandler, Updater


def mount_message(major, minor, type_message, league, status):

    message = f"""
<b>{type_message}: {major.name}</b>
Liga: {league}

{major.name} {major.goals} x {minor.goals} {minor.name}

{major.danger_attack} ataques perigosos em {status} minútos.
{major.on_target} chutes a gol \U000026BD
{major.off_target} chutes fora \U000026BD
{major.corners} cantos (escanteios) \U000026F3

Posse de bola {major.possession}% x {minor.possession}%

APM: {major.apm: .2f}
chance de gol: {major.opportunity_goals}
"""
    return message


def send_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
