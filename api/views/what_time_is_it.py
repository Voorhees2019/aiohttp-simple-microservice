from aiohttp import web
from aiohttp_apispec import docs, response_schema
from datetime import datetime
from api import schema


class WhatTimeIsItView(web.View):
    @docs(
        tags=["Current Time"],
        summary="Display current time",
        description="Get current time in response",
    )
    @response_schema(
        schema=schema.TimeSuccessSchema(),
        code=200,
        description="Return success response with dict",
    )
    async def get(self):
        return web.json_response({'Current Time': datetime.now().strftime("%d-%m-%Y %H:%M:%S")})
