from fastapi import FastAPI

from .api.item import router as item_router

app = FastAPI()
app.include_router(item_router)
