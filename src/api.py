"""
Description:Responsável por enviar uma requisição para https://lv.scorebing.com/ajax/score/data e
            tratar os dados.

autor: romulocarmos@gmail.com
"""
import requests


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
        or status == "HT"
    ):
        return False

    if not league:
        return False

    return row
