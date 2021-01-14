"""
Description:Responsável por enviar uma requisição para https://lv.scorebing.com/ajax/score/data e
            tratar os dados.

autor: romulocarmos@gmail.com
"""
import requests
from requests.models import Response


def request(url: str, header: dict, params: dict) -> dict:
    """
    Se o status da requisição for 200 retorna um dicionário com as informações de cada liga
    Caso sejá falso na retorna nada
    """
    try:
        rec: Response = requests.get(url, headers=header, params=params)
        status_code: int = rec.status_code

        if status_code == 200:
            data: dict = rec.json()
            print(type(data))
            return data.get("rs", {})

        elif status_code == 304:
            return {}
    except Exception as e:
        print(e)
        return {}

    return {}


def live(row: dict) -> dict:
    status: str = row.get("status", False)
    league: str = row.get("league", False)

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


def conditions(
    apm: int, opportunity_goals: int, total_goals: int, condition_type: str
) -> bool:
    """Verifica se as condições estão batendo if sim retorna true senão false."""

    if condition_type == "goals":
        if apm >= 1.3 and opportunity_goals > 15 and total_goals <= 2:
            return True

    elif condition_type == "corner":
        if apm >= 1.0 and opportunity_goals >= 15 and total_goals <= 2:
            return True

    return False
