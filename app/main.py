from fastapi import FastAPI

from app.api.v1 import v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/v1")


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
