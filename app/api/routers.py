from fastapi import APIRouter

from app.api.endpoints import user_router, weather_router

main_router = APIRouter(prefix='/api/v1')

main_router.include_router(weather_router, prefix='/weather', tags=['weather'])

main_router.include_router(user_router, prefix='/user', tags=['user'])
