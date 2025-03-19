import requests as re


class ExtractApi:
    """Api для обращений к извлечения терминов."""

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint

    def extract_terms(self, text: str) -> list[str]:
        query = {"text": text}
        terms = re.get(self.api_endpoint + "/extract", params=query).json()
        return terms