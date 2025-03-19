from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфиг synomed_api."""

    UMLS_API_KEY: str
    TRANSLATE_API_URL: str
    model_config = SettingsConfigDict(extra="ignore")


settings = Settings(_env_file="../.env", _env_nested_delimiter="__")
