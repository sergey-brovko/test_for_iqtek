from pydantic_settings import BaseSettings
import yaml
from pathlib import Path


class Settings(BaseSettings):
    repository_type: str
    database: dict | None = None

    @classmethod
    def from_yaml(cls, path: str = "../config.yaml"):
        config_path = Path(path)
        with config_path.open() as f:
            config_data = yaml.safe_load(f)["repository"]
            return cls(**config_data)

settings = Settings.from_yaml()