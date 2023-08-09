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
class SummonerRankedFlex(Base):
    __tablename__ = "summoner-ranked-flex"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    tier: Mapped[str] = mapped_column(String(16))
    rank: Mapped[str] = mapped_column(String(5))
    wins: Mapped[int] = mapped_column(Integer)
    losses: Mapped[int] = mapped_column(Integer)
    hotStreak: Mapped[bool] = mapped_column(Boolean)
    LP: Mapped[int] = mapped_column(Integer)
    


def getSummonerRankedFlex(engine, name: str):
    with engine.connect() as conn:
        query = select(SummonerRankedFlex).filter(SummonerRankedFlex.name == name)
        for data in conn.execute(query):
            return {
                "name": data[0],
                "tier": data[1],
                "rank": data[2],
                "wins": data[3],
                "losses": data[4],
                "hotStreak": data[5],
                "LP": data[6],
            }
    return None


    




