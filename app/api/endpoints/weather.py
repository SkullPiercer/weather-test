from typing import Optional, List
from datetime import datetime
from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.get_weather import fetch_weather
from app.core.db import get_async_session
from app.db.crud.weather import CRUDWeather

router = APIRouter()

@router.get('/')
async def get_weather(
    city: str = Query(..., min_length=3),
    session: AsyncSession = Depends(get_async_session)
):
    return await fetch_weather(city=city, session=session)


@router.get("/history", response_model=List[dict])
async def get_weather_history(
    city: Optional[str] = Query(None, description="Фильтр по городу"),
    date_from: Optional[datetime] = Query(None, description="Начальная дата (YYYY-MM-DD)"),
    date_to: Optional[datetime] = Query(None, description="Конечная дата (YYYY-MM-DD)"),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить историю запросов погоды
    """
    records = await CRUDWeather(session).get_all(city, date_from, date_to)
    return [
        {"city": r.city, "weather": r.weather, "time": r.time.isoformat()}
        for r in records
    ]