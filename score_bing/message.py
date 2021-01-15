""" Responsável por formatar as menssagens e enviar """
from telegram import Bot

from score_bing.team import Team  # type: ignore

SOCCER_BALL: str = "\U000026BD"
CORNER: str = "\U000026F3"


class Message:
    def __init__(
        self,
        major: Team,
        minor: Team,
        message_type: str,
        league: str,
        status: str,
        bot: Bot,
    ) -> None:
        _types: dict = {
            "corners": "Oportunidades em escanteios",
            "goals": "Oportunidades em gol",
        }

        self.major = major
        self.minor = minor
        self.message_type = _types[message_type]
        self.league = league
        self.status = status
        self.bot = bot

    @property
    def mount_message(self) -> str:

        message: str = f"""
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

    def send(self, chat_id: str) -> None:
        self.bot.send_message(
            chat_id=chat_id, text=self.mount_message, parse_mode="HTML"
        )
