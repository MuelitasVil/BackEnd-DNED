from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class Period(SQLModel, table=True):
    cod_period: str = Field(default=None, primary_key=True, max_length=50)
    initial_date: Optional[date] = None
    final_date: Optional[date] = None
    description: Optional[str] = Field(default=None, max_length=255)
