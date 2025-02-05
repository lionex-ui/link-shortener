from sqlalchemy import Column, Integer, VARCHAR, String

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    short_code = Column(VARCHAR(6), nullable=False, unique=True)
    origin_url = Column(String, nullable=False, unique=False)
    clicks = Column(Integer, nullable=False, unique=False, default=0)
