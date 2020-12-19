import threading

from src.message import *
from src.api import *
from src.statistics import Statistics
from config import TELEGRAM_TOKEN, BASE_API_URL, header, params

# Guarda o id dos jogos que já tiveram seu alerta emitido
repeated = []

def bot():
    send_message(TELEGRAM_TOKEN, 325105532, "Estou on!")
    try:
        rec = request(BASE_API_URL, header, params)
        if rec:
            data = rec
            for item in data:
                live = is_live(item)
                if live:
                    _id = live.get("id")
                    statistic = Statistics(live)

    except Exception as e:
        print("Erro: Bot")
        print(e)


if __name__ == "__main__":
    threading.Thread(target=bot).start()
