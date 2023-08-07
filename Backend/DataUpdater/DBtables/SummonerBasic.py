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
    


def setSummonerBasic(engine, name: str, profileIconId: int, level: int):
    already_there = False
    with engine.connect() as conn:
        query = select(SummonerBasic).filter(SummonerBasic.name == name)
        for _ in conn.execute(query):
            already_there = True

    if already_there:
        with Session(engine) as session:
            session.query(SummonerBasic).filter(SummonerBasic.name == name).update({'profileIconId': profileIconId, 'level': level})
            session.commit()
            print(f"PLAYER[{name}]: already there, updated to -> {profileIconId=}, {level=}")
            return
    
    with Session(engine) as session:
        basic = SummonerBasic(
            name=name,
            profileIconId=profileIconId,
            level=level
        ) 
        session.add(basic)
        session.commit()
        print(f"PLAYER[{name}]: added new, with value -> {profileIconId=}, {level=}")


