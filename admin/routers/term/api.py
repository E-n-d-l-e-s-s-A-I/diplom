import requests as re
from routers.term.schemas import Term, TermBase


class TermApi:
    """Api для обращений к эндпоинтам медицинских терминов."""

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint + "/term/"

    def get_terms(self) -> list[Term]:
        terms_raw = re.get(self.api_endpoint).json()
        terms: list[Term] = [Term(**term) for term in terms_raw]
        return terms

    def get_term(self, id: str) -> Term:
        term_raw = re.get(self.api_endpoint + id).json()
        return Term(**term_raw)

    def create_term(self, term_data: TermBase) -> bool:
        response = re.post(self.api_endpoint, json=term_data.model_dump())
        if response.status_code != 200:
            raise Exception(response.text)

        return True

    def update_term(self, id: str, term_data: TermBase) -> bool:
        response = re.put(self.api_endpoint + str(id), json=term_data.model_dump())
        if response.status_code != 200:
            raise Exception(response.text)

        return True

    def delete_term(self, id: str) -> bool:
        response = re.delete(self.api_endpoint + str(id))
        if response.status_code != 200:
            raise Exception(response.text)

        return True