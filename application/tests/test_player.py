from fastapi.testclient import TestClient
from application.main import app
from unittest.mock import patch,MagicMock
from application.services.database import get_connection


#TestCase-Home
client=TestClient(app)
def test_home():
    response=client.get("/home")
    assert response.status_code==200
    assert response.json()=={"message":"Welcome to my web page"}






#TestCase-AddPlayer
@patch("application.routes.player_routes.get_connection") 
def test_add_player_success(mock_get_connection):
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_get_connection.return_value = mock_conn
    player_data = {
        "player_id": 75,
        "Player": "Prathiksha",
        "Team": "Quest",
        "MatchNo": 1,
        "Vs_Team": "Sark",
        "Score": 0,
        "Balls": 2
    }
    response = client.post("/add-player", json=player_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Player added successfully"}
    expected_sql = """
                        INSERT INTO playertable(player_id,Player,Team,MatchNo,Vs_Team,Score,balls)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    expected_params = (
        player_data["player_id"],
        player_data["Player"],
        player_data["Team"],
        player_data["MatchNo"],
        player_data["Vs_Team"],
        player_data["Score"],
        player_data["Balls"],
    )
    mock_cursor.execute.assert_called_once_with(expected_sql, expected_params)









#TestCase-Get all players
@patch("application.routes.player_routes.get_connection")  # patch from where it's used
def test_get_all_players(mock_get_connection):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_get_connection.return_value = mock_conn
    mock_cursor.fetchall.return_value = [
        (1, "Prathiksha", "Quest", 1, "Sark", 30, 20),
        (2, "Revanth", "Titans", 2, "Spartans", 50, 40)
    ]
    response = client.get("/get-players")
    assert response.status_code == 200
    assert response.json() == [
        {
            "player_id": 1,
            "Player": "Prathiksha",
            "Team": "Quest",
            "MatchNo": 1,
            "Vs_Team": "Sark",
            "Score": 30,
            "Balls": 20
        },
        {
            "player_id": 2,
            "Player": "Revanth",
            "Team": "Titans",
            "MatchNo": 2,
            "Vs_Team": "Spartans",
            "Score": 50,
            "Balls": 40
        }
    ]
    mock_cursor.execute.assert_called_once_with("SELECT * FROM playertable")









#TestCase to get Player on ID
@patch("application.routes.player_routes.get_connection")
def test_player_on_id(mock_get_connection):
    mock_conn=MagicMock()
    mock_cursor=MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_get_connection.return_value = mock_conn
    mock_cursor.fetchone.return_value=(1,"Prathiksha","Quest",1,"Sark",30,20)
    response=client.get("/get-player/1")
    assert response.status_code==200
    assert response.json()=={
        "player_id": 1,
        "Player": "Prathiksha",
        "Team": "Quest",
        "MatchNo": 1,
        "Vs_Team": "Sark",
        "Score": 30,
        "Balls": 20,
    }
    mock_cursor.execute.assert_called_once_with("SELECT * FROM playertable WHERE player_id = %s", (1,))





    










