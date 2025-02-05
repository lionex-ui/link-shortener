from aiohttp import web

from app.api.routes import setup_routes


async def create_app():
    app = web.Application(middlewares=[])

    setup_routes(app)

    return app
