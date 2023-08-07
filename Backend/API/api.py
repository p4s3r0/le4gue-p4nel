from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

from db import *

app = FastAPI()

origins = ["*"]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

load_dotenv()

@app.get("/get_summoner_info")
def get_summoner_info(name: str = ""):
    if name == "": return "[ERROR] - invalid paramater"

    solo = getsummonerRankedSolo(name)
    flex = getSummonerRankedFlex(name)
    level = getSummonerBasic(name)

    return [solo, flex, level]


@app.get("/get_backend_status")
def get_backend_status():
    return getStatus()


@app.get("/get_ranking")
def get_ranking():
    return getRanking()


@app.get("/get_videos")
def get_videos():
    return getVideos()

