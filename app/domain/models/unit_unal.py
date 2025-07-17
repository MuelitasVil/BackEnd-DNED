from sqlmodel import SQLModel, Field
from typing import Optional


class UnitUnal(SQLModel, table=True):
    cod_unit: str = Field(primary_key=True, max_length=50)
    email_unal: Optional[str] = Field(default=None, max_length=100)
    name: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    type_unit: Optional[str] = Field(default=None, max_length=50)
