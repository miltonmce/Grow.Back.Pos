from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
