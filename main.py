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
async def get_user(user_id: int):
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


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Baz2"},
]


@app.get("/items/")
async def list_items(skip: int = 0, limit: int = 5):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def get_item(
    item_id: str, sample_query_param: str, query: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if query:
        item.update({"query": query})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
    user_id: int, item_id: str, query: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if query:
        item.update({"query": query})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
