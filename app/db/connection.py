import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DATABASE_URL = "sqlite+aiosqlite://" + "//" + os.path.join(os.getcwd(), "db.db").replace("\\", "/").split(":/")[-1]


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
