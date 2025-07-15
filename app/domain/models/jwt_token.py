from sqlmodel import SQLModel, Field
from datetime import datetime


class Token(SQLModel, table=True):
    __tablename__ = "token"

    jwt_token: str = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
