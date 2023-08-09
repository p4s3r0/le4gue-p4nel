from riotwatcher import LolWatcher
import time
from datetime import datetime
from dotenv import load_dotenv
import os

from db import *
# global variables
load_dotenv()
api_key = os.getenv("API_KEY")
watcher = LolWatcher(api_key)



# -----------------------------------------------------------------------------
def addPlayer(name):
    try:
        summoner = watcher.summoner.by_name("euw1", name)
    except Exception as e:
        print(f"[ERROR] -> [{datetime.today()}]  -  {e} at addPlayer")
        

    setSummonerBasic(name, profileIconId=summoner["profileIconId"], level=summoner["summonerLevel"])
    setSummonerDev(name, accountId=summoner["accountId"], id=summoner["id"], puuid=summoner["puuid"])





# -----------------------------------------------------------------------------
def updateSummonerStats(name):
    summoner_id = getSummonerDev(name)["id"]

    try:
        both_rankeds = watcher.league.by_summoner("euw1", summoner_id)
    except Exception as e:
        print(f"[ERROR] -> [{datetime.today()}]  -  {e} at updateSummonerStats")

    riot_LP_solo = {}
    riot_LP_flex = {}

    for stat in both_rankeds:
        if stat["queueType"] == "RANKED_SOLO_5x5":
            riot_LP_solo = stat
        elif stat["queueType"] == "RANKED_FLEX_SR":
            riot_LP_flex = stat

    
    rank_points = 0    
    if riot_LP_flex.get("tier") is not None:
        setSummonerRankedFlex(name=name, 
                            tier=riot_LP_flex["tier"], 
                            rank=riot_LP_flex["rank"],
                            wins=riot_LP_flex["wins"],
                            losses=riot_LP_flex["losses"],
                            hotStreak=riot_LP_flex["hotStreak"],
                            LP=riot_LP_flex["leaguePoints"])

        rank_points += (calcRankedPlace([riot_LP_flex["tier"], riot_LP_flex["rank"], riot_LP_flex["leaguePoints"]])) / 5

    
    if riot_LP_solo.get("tier") is not None:
        setSummonerRankedSolo(name=name, 
                            tier=riot_LP_solo["tier"], 
                            rank=riot_LP_solo["rank"],
                            wins=riot_LP_solo["wins"],
                            losses=riot_LP_solo["losses"],
                            hotStreak=riot_LP_solo["hotStreak"],
                            LP=riot_LP_solo["leaguePoints"])
        
        rank_points += calcRankedPlace([riot_LP_solo["tier"], riot_LP_solo["rank"], riot_LP_solo["leaguePoints"]])
    
    setRanking(name=name, ranking=rank_points)

    


    

# -----------------------------------------------------------------------------
def calcRankedPlace(new_rank):
    tier = {
        "IRON": 1,
        "BRONZE": 2,
        "SILVER": 3,
        "GOLD": 4,
        "PLATINUM": 5,
        "EMERALD": 6,
        "DIAMOND": 7,
        "MASTER": 8
    }

    rank = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5
    }
    return tier[new_rank[0]] * 10000 + (5-rank[new_rank[1]]) * 1000 + new_rank[2]




# -----------------------------------------------------------------------------
def main():
    while True:
        summoners = getSummoners()

        for p in summoners:
            print(f"[{datetime.today()}]  - Adding Player {p}")
            addPlayer(p)

        while True:
            print(f"\n[{datetime.today()}]  - Waking up")

            for p in summoners:
                print(f"[{datetime.today()}]  - updating {p}")
                updateSummonerStats(p)
            
            print(f"[{datetime.today()}]  - Going to sleep")
            time.sleep(10)
            if len(getSummonerDev()) != len(summoners):
                break;



if __name__ == "__main__":
    try:
        setStatus(True)
        main()
    except Exception as e:
        print(f"[ERROR] -> [{datetime.today()}]  -  {e}")
        setStatus(False)