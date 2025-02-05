from aiohttp import web
from aiohttp.web_request import Request


async def health_check(request: Request):
    return web.json_response(
        {"status": "Ok"},
        status=200
    )
