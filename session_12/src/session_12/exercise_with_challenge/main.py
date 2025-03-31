from fastapi import FastAPI
import logging

logger = logging.getLogger("fastapi_app")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("/app/logs/app.log")
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "FastAPI app is running!"}
