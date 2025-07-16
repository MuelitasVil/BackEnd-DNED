from .controllers import (
    period_controller,
    user_workspace_controller,
    auth_controller,
    user_workspace_associate_controller
)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(period_controller.router)
app.include_router(user_workspace_controller.router)
app.include_router(auth_controller.router)
app.include_router(user_workspace_associate_controller.router)
