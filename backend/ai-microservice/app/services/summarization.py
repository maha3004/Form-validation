from typing import Optional

from loguru import logger
from transformers import pipeline

from ..config import get_settings


class SummarizationService:
    def __init__(self, model_name: Optional[str] = None):
        self.settings = get_settings()
        self.model_name = model_name or self.settings.transformer_model_name
        logger.info(f"Loading summarization model: {self.model_name}")
        self.pipeline = pipeline(
            "summarization",
            model=self.model_name,
            tokenizer=self.model_name,
        )

    def summarize(
        self,
        text: str,
        max_length: Optional[int] = None,
        min_length: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> str:
        if not text.strip():
            raise ValueError("Input text must not be empty")

        max_len = max_length or self.settings.summary_max_length
        min_len = min_length or self.settings.summary_min_length
        temp = temperature or self.settings.summary_temperature

        logger.debug(
            "Generating summary with max_length={}, min_length={}, temperature={}",
            max_len,
            min_len,
            temp,
        )

        summary = self.pipeline(
            text,
            max_length=max_len,
            min_length=min_len,
            temperature=temp,
            do_sample=True,
        )

        return summary[0]["summary_text"]
