from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass

# SummonerBasic
class SummonerBasic(Base):
    __tablename__ = "summoner-basic"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    profileIconId: Mapped[int] = mapped_column(Integer)
    level: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"SummonerBasic - name: { self.name }, profileIconId: {self.profileIconId}, level: {self.level}"
    


def getSummonerBasic(engine, name: str):
    with engine.connect() as conn:
        query = select(SummonerBasic).filter(SummonerBasic.name == name)
        for data in conn.execute(query):
            return {
                "name": data[0],
                "profileIconId": data[1],
                "level": data[2]
            }
    return False


    




