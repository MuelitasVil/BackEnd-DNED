from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserWorkspaceInput(BaseModel):
    user_workspace_id: str
    space: str
    last_connection: Optional[datetime] = None
    active: bool = True
