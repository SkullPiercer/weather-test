from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from typing import Optional, List

from app.db.models.wether import WeatherCity

class CRUDWeather:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, city: str, weather: str):
        new_record = WeatherCity(city=city, weather=weather)
        self.session.add(new_record)
        await self.session.commit()
        await self.session.refresh(new_record)
        return new_record

    async def get_all(
        self,
        city: Optional[str] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
    ) -> List[WeatherCity]:
        query = select(WeatherCity)

        if city:
            query = query.where(WeatherCity.city.ilike(f"%{city}%"))
        if date_from:
            query = query.where(WeatherCity.time >= date_from)
        if date_to:
            query = query.where(WeatherCity.time <= date_to)

        result = await self.session.execute(query.order_by(WeatherCity.time.desc()))
        return result.scalars().all()
