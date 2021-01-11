""" Válida as informações e envia as mensagens """
import time

from telegram import Bot
from config import CHAT_ID, TELEGRAM_TOKEN, BASE_API_URL, header, params
from score_bing.utils import live, request
from score_bing.message import Message
from score_bing.statistics import Statistics
from score_bing.team import Team

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated: list[str] = []
bot: Bot = Bot(TELEGRAM_TOKEN)


def start() -> None:
    message: str = ""
    data: list[dict, str] = request(BASE_API_URL, header, params)

    if data:
        for row in data:
            row: dict = live(row)

            if not row:
                break

            _id: str = row.get("id")
            statistic: Statistics = Statistics(row)

            host: Team = Team(statistic.host, statistic.status)
            guest: Team = Team(statistic.guest, statistic.status)

            total_goals: int = host.goals + guest.goals

            if (
                host.apm >= 1.0
                and host.opportunity_goals >= 15
                and total_goals <= 2
                and _id not in repeated
            ):

                message: Message = Message(
                    host,
                    guest,
                    "Oportunidades em escanteios",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif (
                guest.apm >= 1.0
                and guest.opportunity_goals >= 15
                and total_goals <= 2
                and _id not in repeated
            ):

                message: Message = Message(
                    guest,
                    host,
                    "Oportunidades em escanteios",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif (
                host.apm >= 1.3
                and host.opportunity_goals > 15
                and total_goals <= 2
                and _id not in repeated
            ):
                message: Message = Message(
                    host,
                    guest,
                    "Oportunidades em gol",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif (
                guest.apm >= 1.0
                and guest.opportunity_goals > 15
                and total_goals <= 2
                and _id not in repeated
            ):
                message: Message = Message(
                    guest,
                    host,
                    "Oportunidades em escanteios",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)


if __name__ == "__main__":
    try:
        bot.send_message(chat_id=CHAT_ID, text="Sistem online!")
        while True:
            start()
            time.sleep(2)

    except Exception as e:
        print(e)

# https://api.telegram.org/bot1435718138:AAHRp7jhstIS2NV-FID_AmCcs-ZEcYJXpGE/getUpdates
