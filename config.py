import os

from dotenv import load_dotenv

load_dotenv()

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "pragma": "no-cache",
}

params = {"mt": 0, "nr": 1}

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_API_URL = os.getenv("BASE_API_URL")
CHAT_ID_TEST = os.getenv("CHAT_ID_TEST")
CHAT_ID = os.getenv("CHAT_ID")
