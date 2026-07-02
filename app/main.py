from fastapi import FastAPI
import redis
from app.api.meal import router as meal_router
from app.api.body import router as body_router
from app.api.dish import router as dish_router
from app.api.library import router as library_router
from app.api.product import router as product_router
from app.api.target import router as target_router


app = FastAPI(title="app", version="1.0.0")
app.include_router(meal_router)
app.include_router(body_router)
app.include_router(dish_router)
app.include_router(library_router)
app.include_router(product_router)
app.include_router(target_router)
@app.get("/")
async def root():
    return {"message": "OK"}



r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
