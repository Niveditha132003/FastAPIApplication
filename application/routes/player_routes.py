from fastapi import APIRouter, HTTPException
from typing import List
from application.models.player import Player
from application.services.database import get_connection
from custom_logging.logger import logger                       # Importing custom logger

router = APIRouter()


# Home page Router returns a Welcome message
@router.get("/home")
def home():
    logger.info("/home endpoint accessed")
    return {"message": "Welcome to my web page"}




# Add player Route 
@router.post("/add-player")
def add_player(player: Player):
    logger.info(f"Attempting to add player: {player}")
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO playertable(player_id, Player, Team, MatchNo, Vs_Team, Score, balls)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                player.player_id, player.Player, player.Team,
                player.MatchNo, player.Vs_Team, player.Score, player.Balls
            ))
        logger.info(f"Player {player.player_id} added successfully")
        return {"message": "Player added successfully"}
    except Exception as e:
        logger.error(f"Error adding player {player.player_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        logger.info("Database connection closed after adding player")





# Get all players Route
@router.get("/get-players", response_model=List[Player])
def get_players():
    logger.info("/get-players endpoint accessed")
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM playertable")
            rows = cur.fetchall()
            players = [
                Player(
                    player_id=row[0],
                    Player=row[1],
                    Team=row[2],
                    MatchNo=row[3],
                    Vs_Team=row[4],
                    Score=row[5],
                    Balls=row[6]
                ) for row in rows
            ]
        logger.info(f"Retrieved {len(players)} players")
        return players
    except Exception as e:
        logger.error(f"Error fetching players: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        logger.info("Database connection closed after fetching players")






# Get player by ID Route
@router.get("/get-player/{id}", response_model=Player)
def get_player(id: int):
    logger.info(f"/get-player/{id} endpoint accessed")
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM playertable WHERE player_id = %s", (id,))
            row = cur.fetchone()
            if row:
                logger.info(f"Player {id} found")
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
                logger.warning(f"Player {id} not found")
                raise HTTPException(status_code=404, detail="Player not found")
    except Exception as e:
        logger.error(f"Error retrieving player {id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        logger.info(f"Database connection closed after retrieving player {id}")


