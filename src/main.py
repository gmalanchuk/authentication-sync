import asyncio
from datetime import datetime

from fastapi import APIRouter, FastAPI

from src.api.include_routers import all_routers
from src.config import logger
from src.grpc_server import grpc_server


app = FastAPI(title="AuthenticationSync API", version="1.0.0", docs_url="/api/docs/")


async def include_routers(routers: tuple) -> None:
    """Includes all api specified in the all_routers tuple"""

    api_router = APIRouter(prefix="/api")

    for router in routers:
        api_router.include_router(router)

    app.include_router(api_router)


@app.on_event("startup")
async def startup() -> None:
    """Executed before the server starts"""

    start_time = datetime.now()

    await include_routers(all_routers)
    asyncio.create_task(grpc_server())

    end_time = datetime.now()

    logger.info(f"Startup time: {end_time - start_time}")
