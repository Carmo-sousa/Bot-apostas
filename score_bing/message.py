""" Responsável por formatar as menssagens e enviar """
from telegram import Bot

from .team import Team

SOCCER_BALL: str = "\U000026BD"
CORNER: str = "\U000026F3"


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


class Message:
    def __init__(
        self,
        major: Team,
        minor: Team,
        message_type: str,
        league: str,
        status: str,
        bot: Bot,
    ):
        self.major = major
        self.minor = minor
        self.message_type = message_type
        self.league = league
        self.status = status
        self.bot = bot

    def mount_message(self):

        message = f"""
        <b>{self.message_type}: {self.major.name}</b>
        Liga: {self.league}

        {self.major.name} {self.major.goals} x {self.minor.goals} {self.minor.name}

        {self.major.danger_attack} ataques perigosos em {self.status} minútos.
        {self.major.on_target} chutes a gol {SOCCER_BALL}
        {self.major.off_target} chutes fora {SOCCER_BALL}
        {self.major.corners} cantos (escanteios) {CORNER}

        Posse de bola {self.major.possession}% x {self.minor.possession}%

        APM: {self.major.apm: .2f}
        chance de gol: {self.major.opportunity_goals}
        """
        return message

    def send(self, chat_id):
        message = self.mount_message()
        self.bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
