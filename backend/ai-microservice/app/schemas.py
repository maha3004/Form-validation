from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from .models import SummaryType


class SummarizeRequest(BaseModel):
    lesson_id: str
    content: str
    summary_type: SummaryType
    max_length: Optional[int] = None
    min_length: Optional[int] = None


class SummaryResponse(BaseModel):
    id: int
    lesson_id: str
    summary_type: SummaryType
    summary_text: str
    generated_at: datetime

    class Config:
        from_attributes = True


class SummaryCreate(BaseModel):
    lesson_id: str
    summary_type: SummaryType
    source_text: str
    summary_text: str
