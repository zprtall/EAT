from fastapi import FastAPI
import redis
app = FastAPI(title="app", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "OK"}



r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
