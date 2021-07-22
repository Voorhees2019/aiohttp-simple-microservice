from aiohttp import web
from datetime import datetime


class WhatTimeIsItView(web.View):
    @staticmethod
    async def get():
        return web.json_response({'Current Time': datetime.now().strftime("%d-%m-%Y %H:%M:%S")})
