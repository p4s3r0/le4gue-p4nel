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
class Summoners(Base):
    __tablename__ = "summoners"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    

def getSummoners(engine):
    summoners = list()
    with engine.connect() as conn:
        query = select(Summoners)
        for summ in conn.execute(query):
            summoners.append(summ[0])
    return summ
        
