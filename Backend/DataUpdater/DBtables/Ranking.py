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
    

def setRanking(engine, name, ranking):
    already_there = False
    with engine.connect() as conn:
        query = select(Ranking).filter(Ranking.name == name)
        for _ in conn.execute(query):
            already_there = True
        
    if already_there:
        with Session(engine) as session:
            session.query(Ranking).filter(Ranking.name == name).update({'ranking': ranking})
            session.commit()
            print(f"Ranking[{name}]: already there, updated to -> {ranking=}")
            return
    
    with Session(engine) as session:
        status = Ranking(
            name=name,
            ranking=ranking
        )
        session.add(status)
        session.commit()
        print(f"Ranking[{name}]: added new ranking with value -> {name=}, {ranking=}")

