from aiohttp import web

from app.services.url import create_link, get_link
from app.services.health_check import health_check


def setup_routes(app: web.Application):
    app.router.add_get("/healthcheck", health_check)
    app.router.add_post("/urls", create_link)
    app.router.add_get("/urls/{short_code}", get_link)
