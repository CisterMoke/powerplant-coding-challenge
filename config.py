from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    host: str = Field(default='localhost')
    port: int = Field(default=8888)
    debug: bool = Field(default=False)

    model_config = SettingsConfigDict(env_prefix='app_')