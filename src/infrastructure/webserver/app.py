from fastapi import FastAPI

from src.infrastructure.webserver.routers import user_router

app = FastAPI(
    title="API",
    openapi_url="/docs/openapi.json",
    docs_url="/docs/swagger.yml",
    root_path="/api"
)


app.include_router(user_router, prefix="/users")
