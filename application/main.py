from fastapi import FastAPI
from application.routes.player_routes import router as player_router

app = FastAPI()

app.include_router(player_router)




