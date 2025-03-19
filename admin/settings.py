from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфиг admin."""

    med_base_url: str
    MODEL_API_URL: str
    model_config = SettingsConfigDict(extra="ignore")


settings = Settings(_env_file="../.env", _env_nested_delimiter="__")