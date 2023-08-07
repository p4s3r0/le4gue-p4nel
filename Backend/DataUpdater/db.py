from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

import DBtables.Status as Status
import DBtables.SummonerBasic as SummonerBasic
import DBtables.SummonerDev as SummonerDev
import DBtables.SummonerRankedFlex as SummonerRankedFlex
import DBtables.SummonerRankedSolo as SummonerRankedSolo
import DBtables.Ranking as Ranking
import DBtables.Summoners as Summoners


load_dotenv()
SQL_DATABASE_CLIENT = os.getenv("SQL_DATABASE_CLIENT")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_URL = os.getenv("SQL_URL")
SQL_PORT = os.getenv("SQL_PORT")
SQL_DB_NAME = os.getenv("SQL_DB_NAME")

# connect to database
conn = f"{SQL_DATABASE_CLIENT}://{SQL_USER}:{SQL_PASSWORD}@{SQL_URL}:{SQL_PORT}/{SQL_DB_NAME}"
engine = create_engine(conn, echo=True)

def setStatus(to: bool):
    Status.setStatus(engine, to)

def setSummonerBasic(name: str, profileIconId: int, level: int):
    SummonerBasic.setSummonerBasic(engine, name=name, profileIconId=profileIconId, level=level)

def setSummonerDev(name: str, accountId: int, id: int, puuid):
    SummonerDev.setSummonerDev(engine, name=name, accountId=accountId, id=id, puuid=puuid)

def setSummonerRankedFlex(name: str, tier: str, rank: str, wins: int, losses: int, hotStreak: bool, LP: int):
    SummonerRankedFlex.setSummonerRankedFlex(engine, name=name, tier=tier, rank=rank, wins=wins, losses=losses, hotStreak=hotStreak, LP=LP)

def setSummonerRankedSolo(name: str, tier: str, rank: str, wins: int, losses: int, hotStreak: bool, LP: int):
    SummonerRankedSolo.setSummonerRankedSolo(engine, name=name, tier=tier, rank=rank, wins=wins, losses=losses, hotStreak=hotStreak, LP=LP)

def setRanking(name: str, ranking: int):
    Ranking.setRanking(engine, name=name, ranking=ranking)



    
def getSummonerDev(name):
    return SummonerDev.getSummonerDev(engine, name)

def getSummoners():
    return Summoners.getSummoners(engine)


        
