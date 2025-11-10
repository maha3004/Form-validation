from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "AI Summarization Service"
    environment: str = "development"
    log_level: str = "INFO"

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "school_ai"
    db_user: str = "postgres"
    db_password: str = "postgres"

    aws_region: str = "us-east-1"
    s3_bucket: str = "ai-summarization-data"
    sns_topic_next_day: str = "arn:aws:sns:us-east-1:123456789012:next-day-topic"
    sns_topic_post_class: str = "arn:aws:sns:us-east-1:123456789012:post-class-topic"

    transformer_model_name: str = "google/pegasus-xsum"
    summary_max_length: int = 128
    summary_min_length: int = 32
    summary_temperature: float = 0.7

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
