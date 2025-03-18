from routers.term.api import TermApi
from settings import settings


class MedBasesAPI:
    """Api для обращений к med_base_api."""

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint
        self.term = TermApi(api_endpoint)




med_base_api = MedBasesAPI(api_endpoint=settings.med_base_url)