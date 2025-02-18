# main.py
from fastapi import FastAPI
from api import api_router  # <--- Import the router from api package

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")  # <--- Include it in your app
