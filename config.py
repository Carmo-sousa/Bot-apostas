import os
import logging

from dotenv import load_dotenv

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

logger.info("Configurando as váriaveis de ambiente.")
load_dotenv()

header: dict = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "pragma": "no-cache",
}

params = {"mt": 0, "nr": 1}

TELEGRAM_TOKEN: str = str(os.getenv("TELEGRAM_TOKEN"))
BASE_API_URL: str = str(os.getenv("BASE_API_URL"))
CHAT_ID_TEST: str = str(os.getenv("CHAT_ID_TEST"))
CHAT_ID: str = str(os.getenv("CHAT_ID"))


class BaseConfig:
    pass


class DevConfig:
    pass


class ProdConfg:
    pass
