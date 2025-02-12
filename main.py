from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router  # Import for api_router
from app.core.config import settings  # Import for settings
from api.endpoints import books  # Import for books

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)
app.include_router(books.router)  # Include the new books router

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
