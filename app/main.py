import os
import uvicorn
from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import get_settings

# from app.core.db import *

settings = get_settings()

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION)
app.include_router(main_router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)