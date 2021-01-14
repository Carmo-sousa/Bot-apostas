""" Válida as informações e envia as mensagens """
import time

from telegram import Bot
from config import CHAT_ID, TELEGRAM_TOKEN, BASE_API_URL, header, params
from score_bing.utils import live, request, conditions  # type: ignore
from score_bing.message import Message  # type: ignore
from score_bing.statistics import Statistics  # type: ignore
from score_bing.team import Team  # type: ignore

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated = []
bot = Bot(TELEGRAM_TOKEN)


def start() -> None:
    data = request(BASE_API_URL, header, params)

    if data:
        for row in data:
            row = live(row)

            if not row:
                break

            _id = row.get("id")
            statistic: Statistics = Statistics(row)

            host = Team(statistic.host, statistic.status)
            guest = Team(statistic.guest, statistic.status)

            total_goals = host.goals + guest.goals

            # Condições de escanteio do host
            corners_conditions_h = conditions(
                host.apm, host.opportunity_goals, total_goals, "corners"
            )

            # Condições de escanteio do guest
            corners_conditions_g = conditions(
                guest.apm, guest.opportunity_goals, total_goals, "corners"
            )

            # Condições de gol do host
            goals_conditions_h = conditions(
                host.apm, host.opportunity_goals, total_goals, "goals"
            )

            # Condições de gol do guest
            goals_conditions_g = conditions(
                guest.apm, guest.opportunity_goals, total_goals, "goals"
            )

            if corners_conditions_h and _id not in repeated:
                message = Message(
                    host,
                    guest,
                    "corners",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif corners_conditions_g and _id not in repeated:
                message = Message(
                    guest,
                    host,
                    "corners",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif goals_conditions_h and _id not in repeated:
                message = Message(
                    host,
                    guest,
                    "goals",
                    statistic.league_name,
                    statistic.status,
                    bot,
                )

                message.send(CHAT_ID)
                repeated.append(_id)

            elif goals_conditions_g and _id not in repeated:
                message = Message(
                    guest,
                    host,
                    "goals",
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
