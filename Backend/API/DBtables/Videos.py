from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String


class Base(DeclarativeBase):
    pass

# STATUS
class Videos(Base):
    __tablename__ = "videos"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    link: Mapped[str] = mapped_column(String(1024))


def getVideos(engine):
    with engine.connect() as conn:
        query = select(Videos)
        videos = list()
        for data in conn.execute(query):
            videos.append({
                "name": data[0],
                "link": data[1]
                })
        return videos
    return False

