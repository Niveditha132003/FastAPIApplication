from pydantic import BaseModel
class Player(BaseModel):
    player_id: int
    Player: str
    Team: str
    MatchNo: int
    Vs_Team: str
    Score: int
    Balls: int
