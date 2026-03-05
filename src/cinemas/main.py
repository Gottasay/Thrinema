from fastapi import FastAPI
from api.resources import router
app = FastAPI(title="Thrinema", version="1.0")
app.include_router(router)

