from typing import Any, AsyncIterator

import aioredis
from aiohttp import web
from aiohttp.web_app import Application

__all__ = ("create_app",)

from api.routes import setup_routes
from .docs import setup_docs, swagger
from .middlewares import get_middlewares


async def create_app(config: dict[str, Any]) -> Application:
    """Create and configure application."""

    # Create application with setting to allow to upload files up to 5 MB
    app = web.Application(
        client_max_size=config["uploads_max_size"],
        middlewares=get_middlewares(config)
    )

    # Store config
    app["config"] = config
    # print(app["config"])

    # Setup routes
    setup_routes(app=app)

    # Setup swagger
    from aiohttp_apispec import setup_aiohttp_apispec
    setup_aiohttp_apispec(
        app=app,
        title="API Documentation",
        version="v1",
        url="/api-docs/swagger.json",
    )

    # Setup extensions objects
    app.cleanup_ctx.extend([redis_client])

    # Swagger API documentation
    app.on_startup.append(swagger)

    # Database connection will be here

    return app


async def redis_client(app: Application) -> AsyncIterator[None]:
    uri = app["config"]["redis_uri"]
    app["redis"] = redis = await aioredis.create_redis_pool(uri)

    yield

    redis.close()
    await redis.wait_closed()
