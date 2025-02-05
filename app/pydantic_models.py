import random
import string

from pydantic import BaseModel, HttpUrl


class CreateLink(BaseModel):
    short_code: str
    origin_url: HttpUrl

    def __init__(self, **data):
        data["short_code"] = "".join(random.choices(string.ascii_letters, k=6))
        super().__init__(**data)
