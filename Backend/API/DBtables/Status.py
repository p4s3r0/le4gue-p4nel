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
    

def getStatus(engine):
    with engine.connect() as conn:
        query = select(Status)
        for data in conn.execute(query):
            return {
                "status": data[0]
                }
    return False

