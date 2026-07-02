from fastapi import FastAPI
import redis
from app.api.meal import router as meal_router


app = FastAPI(title="app", version="1.0.0")
app.include_router(meal_router)
@app.get("/")
async def root():
    return {"message": "OK"}



r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
