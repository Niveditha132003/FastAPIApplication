# Final Project

## Description
This project is a web application built using FastAPI and Snowflake. It provides APIs for managing player data, including adding players, retrieving all players, and fetching player details by ID.

## Features
- Add new players to the database.
- Retrieve all players' details.
- Fetch a specific player's details by ID.
- Snowflake integration for database management.

## Installation and Execution

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Final_Project

2. Install dependencies:
   pip install -r requirements.txt

3. Set up the Snowflake database:
Update the get_connection function in application/services/snowflake_insertion.py with your Snowflake credentials.
Run the script to create and populate the playertable:
python application/services/snowflake_insertion.py

4. Start the FastAPI server:
uvicorn application.main:app --reload

5. Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs

6. API Endpoints
      1. Home
         URL: /home
         Method: GET
         Description: Returns a welcome message.

      2. Add Player
         URL: /add-player
         Method: POST
         Description: Adds a new player to the database.
         Request Body Example:
         {
        "player_id": 1,
        "Player": "Virat",
        "Team": "RCB",
        "MatchNo": 1,
        "Vs_Team": "KKR",
        "Score": 60,
        "Balls": 40
          }


      3. Get All Players
         URL: /get-players
         Method: GET
         Description: Retrieves all players from the database.

      4. Get Player by ID
         URL: /get-player/{id}
         Method: GET
         Description: Fetches details of a specific player by their ID

7. Project Structure
Final_Project/
├── application/
│   ├── main.py                # Entry point for the FastAPI app
│   ├── routes/
│   │   └── player_routes.py   # API routes for player management
│   ├── models/
│   │   └── player.py          # Pydantic models for player data
│   ├── services/
│   │   └── snowflake_insertion.py # Snowflake database setup and insertion
├── [README.md]                # Project documentation
├── [requirements.txt]         # Python dependencies

8. Requirements
Python 3.8+
FastAPI
Uvicorn
Snowflake Connector

9. License
This project is licensed under the MIT License. See the LICENSE file for details

10. Author
Niveditha
        






