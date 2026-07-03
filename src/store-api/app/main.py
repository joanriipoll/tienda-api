from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Tienda API",
    description="API to manage products in a store.",
    version="1.0.0",
)


app.include_router(router)
