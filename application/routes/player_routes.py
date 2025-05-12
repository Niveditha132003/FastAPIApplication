from fastapi import APIRouter,HTTPException
from typing import List
from application.models.player import Player
from application.services.database import get_connection

router=APIRouter()
#Home page Route
@router.get("/home")
def home():
    return {"message":"Welcome to my web page"}



#add player Route
@router.post ("/add-player")
def add_player(player:Player):
    conn=get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO playertable(player_id,Player,Team,MatchNo,Vs_Team,Score,balls)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                        ,(player.player_id,player.Player,player.Team,player.MatchNo,player.Vs_Team,player.Score,player.Balls))

        return {"message":"Player added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    finally:
        conn.close()



#get all players Route
@router.get("/get-players",response_model=List[Player])
def get_players():
    conn=get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM playertable")
            rows = cur.fetchall()
            players = [Player(
                player_id=row[0],
                Player=row[1],
                Team=row[2],
                MatchNo=row[3],
                Vs_Team=row[4],
                Score=row[5],
                Balls=row[6]
            ) for row in rows]
        return players
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    finally:
        conn.close()



#get player by id Route
@router.get("/get-player/{id}",response_model=Player)
def get_player(id:int):
    conn=get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM playertable WHERE player_id = %s", (id,))
            row = cur.fetchone()
            if row:
                return Player(
                    player_id=row[0],
                    Player=row[1],
                    Team=row[2],
                    MatchNo=row[3],
                    Vs_Team=row[4],
                    Score=row[5],
                    Balls=row[6]
                )
            else:
                raise HTTPException(status_code=404, detail="Player not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

