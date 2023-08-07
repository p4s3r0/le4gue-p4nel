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
    


def setSummonerRankedFlex(engine, name: str, tier: str, rank: str, wins: int, losses: int, hotStreak: bool, LP: int):
    print("START")
    already_there = False
    with engine.connect() as conn:
        query = select(SummonerRankedFlex).filter(SummonerRankedFlex.name == name)
        for _ in conn.execute(query):
            already_there = True

    if already_there:
        with Session(engine) as session:
            session.query(SummonerRankedFlex).filter(SummonerRankedFlex.name == name).update(
                {'tier': tier, 
                 'rank': rank,
                 'wins': wins,
                 'losses': losses,
                 'hotStreak': hotStreak,
                 'LP': LP})
            
            session.commit()
            print(f"setSummonerRankedFlex[{name}]: already there, updated to -> {tier=}, {rank=}, {wins=}, {losses=}, {hotStreak=}, {LP=}")
            return
    
    with Session(engine) as session:
        basic = SummonerRankedFlex(
            name=name,
            tier=tier,
            wins=wins,
            losses=losses,
            hotStreak=hotStreak,
            LP=LP,
        ) 
        session.add(basic)
        session.commit()
        print(f"setSummonerRankedFlex[{name}]: added new, with values -> {tier=}, {rank=}, {wins=}, {losses=}, {hotStreak=}, {LP=}")


