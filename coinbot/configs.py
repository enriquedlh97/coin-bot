"""Configurations.

See morea bout this approach here:
https://rednafi.github.io/digressions/python/2020/06/03/python-configs.html
"""
from pathlib import Path

from pydantic import BaseModel, BaseSettings, Field


class AppConfig(BaseModel):
    """Application COnfigurations.

    These variables will be loaded from the .env file. However, if
    there is a shell environment variable having the same name,
    that will take precedence.
    """

    COINBOT_CHANNEL: str = "#bot-dev"


class GlobalConfig(BaseSettings):
    """Global COnfigurations."""

    APP_CONFIG: AppConfig = AppConfig()

    # define global variables with the Field class
    ENV_STATE: str | None = Field(None, env="ENV_STATE")
    SLACK_TOKEN: str | None = Field(env="SLACK_TOKEN")
    SLACK_EVENTS_TOKEN: str | None = Field(env="SLACK_EVENTS_TOKEN")

    # environment specific variables do not need the Field class
    HOST: str | None = None
    PORT: int | None = None
    # REDIS_HOST: Optional[str] = None
    # REDIS_PORT: Optional[int] = None
    # REDIS_PASS: Optional[str] = None

    class Config:
        """Loads the dotenv file."""

        env_file: Path = Path(Path(__file__).resolve().parent / ".env")


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        """Sets the environment prefix."""

        env_prefix: str = "DEV_"


class StageConfig(GlobalConfig):
    """Staging configurations."""

    class Config:
        """Sets the environment prefix."""

        env_prefix: str = "STAGE_"


class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        """Sets the environment prefix."""

        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: str | None) -> None:
        """Constructor."""
        self.env_state: str | None = env_state

    def __call__(self) -> DevConfig | ProdConfig | StageConfig:
        """Gets the correspodngin configuration.

        :raises ValueError: If the 'env_state' variable is not one of
            'dev', prod, or 'stage'.
        :return: Configuration.
        """
        if self.env_state == "dev":
            return DevConfig()  # type: ignore

        elif self.env_state == "prod":
            return ProdConfig()  # type: ignore

        elif self.env_state == "stage":
            return StageConfig()  # type: ignore

        raise ValueError("'env_state' must be one of 'dev', prod, or 'stage'")


config = FactoryConfig(GlobalConfig().ENV_STATE)()  # type: ignore

# This is useful for inspecting thr active configuration class, can be
# commented in production.
print(config.__repr__())
