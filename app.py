import threading

from src.message import *
from src.apiController import *
from config import TELEGRAM_TOKEN, BASE_API_URL

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated = []


def bot():
    send_message(TELEGRAM_TOKEN, 325105532, f"Estou on!")

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "pragma": "no-cache",
    }

    params = {"mt": 0, "nr": 1}

    try:
        while True:
            rec = request(BASE_API_URL, header, params)
            if rec:
                data = rec
                for item in data:
                    live = is_live(item)
                    if live:
                        _id = live.get("id")
                        statistic = get_statistic(live)
                        league = statistic["league_name"]
                        status = statistic["time"]

                        team_h = statistic["host"]
                        goals_h = statistic["goals"]["hg"]
                        on_target_h = statistic["on_target"]["hso"]
                        off_garget_h = statistic["off_target"]["hsf"]
                        danger_attack_h = statistic["danger_attack"]["hd"]
                        corners_h = statistic["corners"]["hc"]
                        possessions_h = statistic["possessions"]["hqq"]
                        # print(possessions_h)

                        opportunity_goals_h = chance_de_gol(
                            on_target_h, off_garget_h, corners_h
                        )
                        apm_h = apm(status, on_target_h)

                        team_g = statistic["guest"]
                        goals_g = statistic["goals"]["gg"]
                        on_target_g = statistic["on_target"]["gso"]
                        off_garget_g = statistic["off_target"]["gsf"]
                        danger_attack_g = statistic["danger_attack"]["gd"]
                        corners_g = statistic["corners"]["gc"]
                        possessions_g = statistic["possessions"]["gqq"]

                        opportunity_goals_g = chance_de_gol(
                            corners_g, off_garget_g, on_target_g
                        )
                        apm_g = apm(status, danger_attack_g)

                        if apm_h >= 1 and opportunity_goals_h >= 15:
                            message = mount_message(
                                "Chance de Gol:",
                                league,
                                status,
                                team_h,
                                goals_h,
                                goals_g,
                                team_g,
                                on_target_h,
                                off_garget_h,
                                danger_attack_h,
                                corners_h,
                                possessions_h,
                                possessions_g,
                                apm_h,
                                opportunity_goals_h,
                            )
                            send_message(TELEGRAM_TOKEN, 325105532, message)

    except Exception as e:
        print("Erro: Bot")
        send_message(TELEGRAM_TOKEN, 325105532, f"Erro no programa\n{e}")


if __name__ == "__main__":
    threading.Thread(target=bot).start()
