from .controllers import (
    period_controller,
    user_workspace_controller,
    auth_controller,
    user_workspace_associate_controller,
    user_unal_controller,
    unit_unal_controller,
    user_unit_associate_controller,
    school_controller,
    unit_school_associacte_controller
)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(auth_controller.router)
app.include_router(period_controller.router)
app.include_router(user_workspace_controller.router)
app.include_router(user_workspace_associate_controller.router)
app.include_router(user_unal_controller.router)
app.include_router(unit_unal_controller.router)
app.include_router(user_unit_associate_controller.router)
app.include_router(school_controller.router)
app.include_router(unit_school_associacte_controller.router)
