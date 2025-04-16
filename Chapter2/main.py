from fastapi import FastAPI

app = FastAPI()


@app.get("/countries/{country_name}")
async def country(country_name: int):
    return {"country_name": country_name}
