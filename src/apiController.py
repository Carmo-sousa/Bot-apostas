"""
Description:Responsável por enviar uma requisição para https://lv.scorebing.com/ajax/score/data e
            tratar os dados.

autor: romulocarmos@gmail.com
"""
import requests
import time
import threading


def posse_de_bola(posse):
    if posse >= 60:
        return True
    else:
        return False


# def apm(tempo, qnt_ataques_perigosos, condicao_apm):
#     apm = qnt_ataques_perigosos / tempo
#     if apm >= condicao_apm:
#         return apm
#     else:
#         return False


def apm(tempo, qnt_ataques_perigosos):
    apm = int(qnt_ataques_perigosos) / int(tempo)
    return apm


def chance_de_gol(corners, off_target, on_target):
    chance = int(corners) + int(off_target) + int(on_target)
    return chance


def request(url, header, params):
    try:
        rec = requests.get(url, headers=header, params=params)
        status_code = rec.status_code
        if status_code == 200:
            rec = rec.json()
            return rec.get("rs")
        elif status_code == 304:
            return False
    except Exception as e:
        print('Função: request')
        print(e)
        return False


def is_live(row):
    status = row.get("status", False)
    league = row.get("league", False)

    if (
        not status
        or status == "-1"
        or status == "全"
        or status == "FT"
        or status == "NS"
    ):
        return False

    if not league:
        return False

    return row


def in_list(list, id_league):
    if id_league in list:
        return True
    else:
        return False


def mount_message(
    type_message,
    league,
    status,
    team_h,
    goals_h,
    goals_g,
    team_g,
    on_target,
    off_garget,
    danger_attack,
    corners,
    possessions_h,
    possessions_g,
    apm,
    opportunity_goals,
):
    message = f"""
    <b>{type_message}:</b>
    {league}
    {team_h} {goals_h} X {goals_g} {team_g}

    {danger_attack} ataques perigosos em {status} minútos.
    {on_target} chutes a gol.
    {off_garget} chutes fora.
    {corners} cantos (escanteios).

    Posse de bola {possessions_h} x {possessions_g};

    APM = {apm: .2f};
    chance de gol = {opportunity_goals};
    """

    return message


def get_statistic(row):
    _league = row.get("league")
    _events_graph = row.get("events_graph")
    _events = _events_graph.get("events", [])
    _host = row.get("host")
    _guest = row.get("guest")
    _plus = row.get("plus")
    _goals_h = 0
    _goals_g = 0
    _corners_h = 0
    _corners_g = 0

    for event in _events:
        event_type = event.get("t")
        if event_type == "hg":
            _goals_h += 1

        elif event_type == "gg":
            _goals_g += 1

        elif event_type == "hc":
            _corners_h += 1

        elif event_type == "gc":
            _corners_g += 1

    host = {
        "id": row.get("id"),
        "time": _events_graph.get("status"),
        "league_name": _league.get("fn"),
        "host": _host.get("n"),
        "guest": _guest.get("n"),
        "on_target": _plus.get("hso", 0),
        "off_target": _plus.get("hsf", 0),
        "danger_attack": _plus.get("hd", 0),
        "attacks": _plus.get("ha", 0),
        "possessions":  _plus.get("hqq", 0),
        "corners": _corners_h,
        "goals": _goals_h,
    }

    guest = {
        "id": row.get("id"),
        "time": _events_graph.get("status"),
        "league_name": _league.get("fn"),
        "host": _host.get("n"),
        "guest": _guest.get("n"),
        "on_target": _plus.get("gso", 0),
        "off_target": _plus.get("gsf", 0),
        "danger_attack": _plus.get("gd", 0),
        "attacks": _plus.get("ga", 0),
        "possessions": _plus.get("gqq", 0),
        "corners": _corners_g,
        "goals": _goals_g,
    }

    return host, guest


def update_statistic(last_update, new_statistic):
    _plus = new_statistic.get("plus", {})
    _events_graph = new_statistic.get("events_graph", {})

    # if _events_graph:
    _events = _events_graph.get("events") or False
    _time = _events_graph.get("status", last_update["time"])
    last_update["time"] = _time

    for event in _events:
        event_type = event.get("t")
        if event_type == "hp":
            # _goals_h += 1
            last_update["goals"][event_type] += 1

        elif event_type == "gp":
            # _goals_g += 1
            last_update["goals"][event_type] += 1

        elif event_type == "hc":
            # _corners_h += 1
            last_update["corners"][event_type] += 1

        elif event_type == "gc":
            # _corners_g += 1
            last_update["corners"][event_type] += 1

    if _plus:
        on_target = {
            "hso": _plus.get("hso", last_update["on_target"]["hso"]),
            "gso": _plus.get("gso", last_update["on_target"]["gso"]),
        }

        off_target = {
            "hsf": _plus.get("hsf", last_update["off_target"]["hsf"]),
            "gsf": _plus.get("gsf", last_update["off_target"]["gsf"]),
        }

        danger_attacks = {
            "hd": _plus.get("hd", last_update["danger_attack"]["hd"]),
            "gd": _plus.get("gd", last_update["danger_attack"]["gd"]),
        }

        attacks = {
            "ha": _plus.get("ha", last_update["attacks"]["ha"]),
            "ga": _plus.get("ga", last_update["attacks"]["ga"]),
        }

        possessions = {
            "hqq": _plus.get("hqq", last_update["possessions"]["hqq"]),
            "gqq": _plus.get("gqq", last_update["possessions"]["gqq"]),
        }

        last_update["on_target"] = on_target
        last_update["off_target"] = off_target
        last_update["danger_attack"] = danger_attacks
        last_update["attacks"] = attacks
        last_update["possessions"] = possessions

    return last_update


def remove_statistic(statistics, id_statistic):
    for statistic in statistics:
        if statistic["id"] == id_statistic:
            index = statistics.index(statistic)
            statistics.pop(index)

    return statistics


class Team:
    def __init__(self, team: dict):
        self._league = team["league_name"]
        self._status = team["time"]
        self._name = team["name"]
        self._goals = team["goals"]
        self._on_target = team["on_target"]
        self._off_garget = team["off_target"]
        self._danger_attack = team["danger_attack"]
        self._corners = team["corners"]
        self._possessions = team["possessions"]

    def apm(self):
        return int(self._danger_attack) / int(self._status)

    def opportunity_goals(self):
        return int(self._corners) + int(self._on_target) + int(self._off_garget)
