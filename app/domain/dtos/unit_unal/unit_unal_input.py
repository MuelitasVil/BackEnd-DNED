from pydantic import BaseModel
from typing import Optional


class UnitUnalInput(BaseModel):
    cod_unit: str
    cod_facultad: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type_unit: Optional[str] = None
