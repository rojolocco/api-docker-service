from fastapi import FastAPI
import os


app = FastAPI(
    docs_url=None if os.getenv("API_ENV") == "production" else "/docs",
    redoc_url=None if os.getenv("API_ENV") == "production" else "/redoc",
    openapi_url=None if os.getenv("API_ENV") == "production" else "/openapi.json",
)


@app.get("/")
async def root():
    return {"message": "Hello Datapulse!!"}
