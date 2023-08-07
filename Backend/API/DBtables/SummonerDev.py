from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String


class Base(DeclarativeBase):
    pass

# SummonerBasic
class SummonerDev(Base):
    __tablename__ = "summoner-dev"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    accountId: Mapped[str] = mapped_column(String(255))
    id: Mapped[str] = mapped_column(String(255))
    puuid: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"SummonerDev - name: { self.name }, accountId: {self.accountId}, id: {self.id}, puuid: {self.puuid}"
    
    

def getSummonerDev(engine, name: str):
    with engine.connect() as conn:
        query = select(SummonerDev).filter(SummonerDev.name == name)
        for data in conn.execute(query):
            return {
                "name": data[0],
                "accountId": data[1],
                "id": data[2],
                "puuid": data[3]
            }
    return False


    




