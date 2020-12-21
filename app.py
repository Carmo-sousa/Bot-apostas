import time

from telegram import Update
from telegram.ext import MessageHandler, Updater, CommandHandler

from src.message import *
from src.api import *
from src.statistics import Statistics
from src.team import Team
from config import CHAT_ID, TELEGRAM_TOKEN, BASE_API_URL, header, params

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated = []

def bot():
    rec = request(BASE_API_URL, header, params)
    if rec:
        data = rec
        for item in data:
            live = is_live(item)
            if live:
                _id = live.get("id")
                statistic = Statistics(live)

                host = Team(statistic.host, statistic.status)
                guest = Team(statistic.guest, statistic.status)

                total_goals = host.goals + guest.goals

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
        send_message(TELEGRAM_TOKEN, 325105532, "Tô on")
        while True:
            bot()
            time.sleep(2)
    except Exception as e:
        send_message(TELEGRAM_TOKEN, 325105532, e)
