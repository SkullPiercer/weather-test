from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime

from app.core.db import Base

class WeatherCity(Base):
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    weather: Mapped[str] = mapped_column(String(255), nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)