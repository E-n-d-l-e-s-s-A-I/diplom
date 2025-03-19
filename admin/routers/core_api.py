from routers.term.api import TermApi
from routers.extract.api import ExtractApi
from settings import settings


class MedBasesAPI:
    """Api для обращений к med_base_api."""

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint
        self.term = TermApi(api_endpoint)

class ModelAPI:
    """Api для обращений к model_api."""

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint
        self.extract = ExtractApi(api_endpoint)


med_base_api = MedBasesAPI(api_endpoint=settings.med_base_url)
model_api = ModelAPI(api_endpoint=settings.MODEL_API_URL)