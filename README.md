


# Final Project

## Description
This is a application built using FastAPI and Snowflake. It provides APIs for managing player data, including adding players, retrieving all players, and fetching player details by ID.

## Features
- Add new players to the database.
- Retrieve all players' details.
- Fetch a specific player's details by ID.
- Snowflake integration for database management.

## Installation and Execution

1. Clone the repository:

   git clone https://github.com/Niveditha132003/FastAPIApplication.git
   ```bash
   cd Final_Project
   ```


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Set up the Snowflake database:
create .env file inside application folder to use your snowflake credentials.
Run the script to create and populate the playertable:
python3 application/services/snowflake_insertion.py


5. Start the FastAPI server:

   ```bash
   uvicorn application.main:app --reload
   ```

6. Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs


7. API Endpoints
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

```text

8. Project Structure


Final_Project/
├── application/
│   ├── main.py                   # Entry point for the FastAPI app
│   ├── .env                      # Environment variables file
│   ├── routes/
│   │   └── player_routes.py      # API routes for player management
│   ├── models/
│   │   └── player.py             # Pydantic models for player data
│   ├── services/
│   │   ├── snowflake_insertion.py  # Snowflake DB insertion
│   │   └── database.py             # Snowflake DB connection
├── custom_logging/
│   ├── logger.py                 # Custom logger setup
│   └── loggerconfig.yaml         # Logger configuration
├── logs/                         # Log files directory
├── .dockerignore                 # Docker build exclusions
├── .gitignore                    # Git tracking exclusions
├── Dockerfile                    # Docker build configuration
├── README.md                     # Project documentation
├── requirements.txt              # Python 
```





8. Requirements
Python 3.8+
FastAPI
Uvicorn
Snowflake Connector
Pydantic
PyYAML


9. Logging
Custom logging is configured using `custom_logging/logger.py` and `custom_logging/loggerconfig.yaml`.  
- **RotatingFileHandler** is used to write logs to files in the `logs/` directory, automatically rotating and retaining up to 3 backup log files.
- **StreamHandler** is used to output logs to the console (stdout).


10. License
This project is licensed under the MIT License. See the LICENSE file for details


11. Author
Niveditha
        






