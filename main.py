from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def post():
    return {"message": "hello from post"}


@app.put("/")
async def put():
    return {"message": "hello from put"}


@app.get("/users/")
async def list_users():
    return {"message": "list_users route"}


@app.get("/users/me")
async def get_current_user():
    return {"message": "current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetable = "vegetable"
    dairy = "dairy"


@app.get("/foods/{food_type}")
async def get_food(food_type: FoodEnum):
    if food_type == FoodEnum.vegetable:
        return {"food_type": food_type, "message": "you are healhy"}
    if food_type.value == "fruits":
        return {"food_type": food_type, "message": "healhy value"}
    return {"food_type": food_type, "message": "you are unhealthy"}
