from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass

# STATUS
class Ranking(Base):
    __tablename__ = "ranking"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    ranking: Mapped[int] = mapped_column(Integer)
    

def getRanking(engine):
    ranking = list()
    with engine.connect() as conn:
        query = select(Ranking)
        for data in conn.execute(query):
            summ = {
                "name": data[0],
                "ranking": data[1]
                }
            ranking.append(summ)
    return ranking

