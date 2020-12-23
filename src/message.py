from telegram import Bot

SOCCER_BALL = "\U000026BD"
CORNER = "\U000026F3"


def mount_message(major, minor, type_message, league, status):

    message = f"""
<b>{type_message}: {major.name}</b>
Liga: {league}

{major.name} {major.goals} x {minor.goals} {minor.name}

{major.danger_attack} ataques perigosos em {status} minútos.
{major.on_target} chutes a gol {SOCCER_BALL}
{major.off_target} chutes fora {SOCCER_BALL}
{major.corners} cantos (escanteios) {CORNER}

Posse de bola {major.possession}% x {minor.possession}%

APM: {major.apm: .2f}
chance de gol: {major.opportunity_goals}
"""
    return message


def send_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
