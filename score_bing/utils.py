"""
Description:Responsável por enviar uma requisição para https://lv.scorebing.com/ajax/score/data e
            tratar os dados.

autor: romulocarmos@gmail.com
"""
import requests


def request(url, header, params) -> dict:
    """
    Se o status da requisição for 200 retorna um dicionário com as informações de cada liga
    Caso sejá falso na retorna nada
    """
    try:
        rec = requests.get(url, headers=header, params=params)
        status_code = rec.status_code

        if status_code == 200:
            rec = rec.json()
            return rec.get("rs")

        elif status_code == 304:
            return {}
    except Exception as e:
        return {}


def live(row) -> dict:
    status = row.get("status", False)
    league = row.get("league", False)

    if (
        not status
        or not league
        or status == "-1"
        or status == "全"
        or status == "FT"
        or status == "NS"
        or status == "HT"
    ):
        return {}

    return row


def conditions(apm, opportunity_goals, total_goals):
    # host.apm >= 1.3
    # and host.opportunity_goals > 15
    # and total_goals <= 2
    pass
