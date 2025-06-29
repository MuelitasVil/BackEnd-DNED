from typing import Optional
from pydantic import BaseModel
from datetime import date

class PeriodInput(BaseModel):
    initial_date: Optional[date] = None
    final_date: Optional[date] = None
    description: Optional[str] = None
