from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy import Boolean


class Base(DeclarativeBase):
    pass

# STATUS
class Status(Base):
    __tablename__ = "status"

    status: Mapped[bool] = mapped_column(Boolean, primary_key=True)

    def __repr__(self) -> str:
        return f"STATUS - status: { self.status }"
    


def setStatus(engine, to: bool):
    already_there = False
    with engine.connect() as conn:
        query = select(Status)
        for _ in conn.execute(query):
            already_there = True
        
    if already_there:
        with Session(engine) as session:
            session.query(Status).update({'status': to})
            session.commit()
            print(f"STATUS: already there, updated to -> {to}")
            return
    
    with Session(engine) as session:
        status = Status(
            status=to
        )
        session.add(status)
        session.commit()
        print(f"STATUS: added new status with value -> {to}")


