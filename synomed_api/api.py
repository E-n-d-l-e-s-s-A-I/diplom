import requests
from settings import settings


class API:
    """Класс для обращений к внешним API."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.translate_api_url = settings.TRANSLATE_API_URL
        self.ulms_url = "https://uts-ws.nlm.nih.gov/rest"

    def get_synonyms(self, term: str) -> list[str]:
        """Получает синонимы термина."""

        query = {"apiKey": self.api_key, "string": term}
        response = requests.get(f"{self.ulms_url}/search/2024AB", params=query)
        response = response.json()
        return [syn["name"] for syn in response["result"]["results"]]

    def translate_ru_to_eng(self, term: str) -> list[str]:
        """Переводит текст на английский язык."""

        query = {"text": term}
        response = requests.get(
            f"{self.translate_api_url}/translate_ru_to_eng", params=query
        )
        return response.json()

    def translate_eng_to_ru(self, term: str) -> str:
        """Переводит текст на русский язык."""

        query = {"text": term}
        response = requests.get(
            f"{self.translate_api_url}/translate_eng_to_ru", params=query
        )
        return response.json()
