from fastapi import FastAPI
from app.api.endpoints import __all__ as endpoints

app = FastAPI(title="FastAPI Tools for AI")


for router in endpoints:
    app.include_router(router)
