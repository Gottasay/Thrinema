from fastapi import FastAPI
from movies.resources import router_m

app = FastAPI(title="Movies", version="1.0")
app.include_router(router_m)

