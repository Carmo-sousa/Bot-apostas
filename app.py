""" Válida as informações e envia as mensagens """
import time

from config import CHAT_ID, TELEGRAM_TOKEN, BASE_API_URL, header, params
from score_bing.api import live, request
from score_bing.message import mount_message, send_message
from score_bing.statistics import Statistics
from score_bing.team import Team

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated: list[str] = []


def bot() -> None:
    message: str = ""
    data: list[dict, str] = request(BASE_API_URL, header, params)

    if data:
        for row in data:
            row: dict = live(row)

            if not row:
                continue

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
                message = mount_message(
                    host,
                    guest,
                    "Oportunidades em escanteios",
                    statistic.league_name,
                    statistic.status,
                )
                send_message(TELEGRAM_TOKEN, CHAT_ID, message)
                repeated.append(_id)

            elif (
                guest.apm >= 1.0
                and guest.opportunity_goals >= 15
                and total_goals <= 2
                and _id not in repeated
            ):
                message = mount_message(
                    guest,
                    host,
                    "Oportunidades em escanteios",
                    statistic.league_name,
                    statistic.status,
                )
                send_message(TELEGRAM_TOKEN, CHAT_ID, message)
                repeated.append(_id)

            elif (
                host.apm >= 1.3
                and host.opportunity_goals > 15
                and total_goals <= 2
                and _id not in repeated
            ):
                message = mount_message(
                    host,
                    guest,
                    "Oportunidades em gol",
                    statistic.league_name,
                    statistic.status,
                )
                send_message(TELEGRAM_TOKEN, CHAT_ID, message)
                repeated.append(_id)

            elif (
                guest.apm >= 1.0
                and guest.opportunity_goals > 15
                and total_goals <= 2
                and _id not in repeated
            ):
                message = mount_message(
                    guest,
                    host,
                    "Oportunidades em gol",
                    statistic.league_name,
                    statistic.status,
                )
                send_message(TELEGRAM_TOKEN, CHAT_ID, message)
                repeated.append(_id)


if __name__ == "__main__":
    try:
        send_message(TELEGRAM_TOKEN, CHAT_ID, "Online")
        while True:
            bot()
            time.sleep(2)

    except Exception as e:
        send_message(TELEGRAM_TOKEN, CHAT_ID, e)
        print(e)

# https://api.telegram.org/bot1435718138:AAHRp7jhstIS2NV-FID_AmCcs-ZEcYJXpGE/getUpdates
