from fastapi import FastAPI
from pydantic import BaseModel


class Data(BaseModel):
    x: float
    y: float


app = FastAPI()


@app.get("/")
def index():
    return {"meseage": "hello deta"}


@app.post("/")
def calc(data: Data):
    z = data.x * data.y
    return {"result": z}
