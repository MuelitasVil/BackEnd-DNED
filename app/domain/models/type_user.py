from sqlmodel import SQLModel, Field
from typing import Optional


class TypeUser(SQLModel, table=True):
    type_user_id: str = Field(primary_key=True, max_length=50)
    name: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
