from aiohttp import web
from aiohttp.web_request import Request

from sqlalchemy import select

from pydantic import ValidationError

from app.db import connection, models
from app.pydantic_models import CreateLink


async def create_link(request: Request):
    data = await request.json()

    try:
        validated_data = CreateLink(**data)
    except ValidationError:
        return web.json_response(
            {"error": "Incorrect \"origin_url\""},
            status=400
        )

    short_code = validated_data.short_code
    origin_url = str(validated_data.origin_url)

    url = models.Url(
        short_code=short_code,
        origin_url=origin_url
    )

    async with connection.async_session_maker() as session:
        session.add(url)
        await session.commit()

    scheme = request.scheme
    host = request.host

    return web.json_response(
        {"url": f"{scheme}://{host}/{short_code}"},
        status=200
    )


async def get_link(request: Request):
    short_code = request.match_info["short_code"]

    async with connection.async_session_maker() as session:
        url = await session.scalar(
            select(models.Url)
            .filter(
                models.Url.short_code == short_code
            )
        )

        origin_url = url.origin_url
        url.clicks += 1

        await session.commit()

    return web.HTTPFound(origin_url)
