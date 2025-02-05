from aiohttp import web
from app.create_app import create_app


if __name__ == "__main__":
    web.run_app(create_app(), host="localhost", port=8000)
