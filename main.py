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


@app.get("/items/")
async def list_items():
    return {"message": "list_items route"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
