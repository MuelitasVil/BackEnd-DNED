from typing import Union
from .controllers import period_controller 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(period_controller.router)
