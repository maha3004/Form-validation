from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.sql import func
import enum

from .db.base import Base


class SummaryType(str, enum.Enum):
    next_day = "NEXT_DAY"
    post_class = "POST_CLASS"


class LessonSummary(Base):
    __tablename__ = "lesson_summaries"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(String(64), nullable=False, index=True)
    summary_type = Column(Enum(SummaryType), nullable=False)
    source_text = Column(Text, nullable=False)
    summary_text = Column(Text, nullable=False)
    generated_at = Column(DateTime(timezone=True), server_default=func.now())
