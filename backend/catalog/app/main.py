from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router
from database import Base, engine
import os

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# static_dir = os.path.join(BASE_DIR, "static", "img")

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
# app.mount("/img", StaticFiles(directory=static_dir), name="img")

