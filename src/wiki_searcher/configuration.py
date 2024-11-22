from pydantic import Field
from pydantic_settings import BaseSettings


class BaseSettingsConfig(BaseSettings):
    model_config = {
        "env_nested_delimiter": "__",
    }


class Configuration(BaseSettingsConfig):
    MODEL_REPO_ID: str = Field()
    HF_API_TOKEN: str = Field()

    model_config = {
        "env_prefix": "",
    }
