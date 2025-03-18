import os
from pathlib import Path

from dotenv import load_dotenv

class Envi:
    def __init__(self) -> None:
        # Загрузка переменных окружения из файла .env
        env_path = Path(".") / ".env"
        load_dotenv(dotenv_path=env_path)

        # Получение переменных окружения
        self.telegram_api = os.getenv("TOKEN")