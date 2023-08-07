from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

import DBtables.Status as Status
import DBtables.SummonerBasic as SummonerBasic
import DBtables.SummonerDev as SummonerDev
import DBtables.SummonerRankedFlex as SummonerRankedFlex
import DBtables.SummonerRankedSolo as SummonerRankedSolo
import DBtables.Ranking as Ranking
import DBtables.Videos as Videos

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


def getStatus():
    return Status.getStatus(engine)

def getSummonerBasic(name):
    return SummonerBasic.getSummonerBasic(engine, name)

def getSummonerDev(name):
    return SummonerDev.getSummonerDev(engine, name)

def getSummonerRankedFlex(name):
    return SummonerRankedFlex.getSummonerRankedFlex(engine, name)

def getsummonerRankedSolo(name):
    return SummonerRankedSolo.getSummonerRankedSolo(engine, name)

def getRanking():
    return Ranking.getRanking(engine)


def getVideos():
    return Videos.getVideos(engine)

        
