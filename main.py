import os
import pathlib

import uvicorn

from src.infrastructure.database.sqlalchemy.config import engine
from src.infrastructure.database.sqlalchemy.models import Base
from src.infrastructure.webserver.app import app
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine


def execute():
    # Base.metadata.create_all(engine)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        access_log=False
    )


if __name__ == "__main__":
    execute()
