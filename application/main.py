from fastapi import FastAPI
from application.routes import player_routes  
from custom_logging.logger import setup_logger,logger  
# Setup logger using YAML config
setup_logger()


# Initialize FastAPI app
app = FastAPI()


# Startup log
@app.on_event("startup")
def on_startup():
    logger.info("Application has started.")


# Shutdown log
@app.on_event("shutdown")
def on_shutdown():
    logger.info("Application is shutting down.")


# Root endpoint logging
@app.get("/")
def read_root():
    logger.info("Root endpoint was accessed")
    return {"message": "Welcome to the application"}


# Routers
app.include_router(player_routes.router)







