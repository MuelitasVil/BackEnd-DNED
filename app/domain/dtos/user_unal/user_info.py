from pydantic import BaseModel
from typing import List, Optional


class UserInfoAssociation(BaseModel):
    email_unal: str
    name: str
    lastname: str
    full_name: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[str] = None
    headquarters: Optional[str] = None
    period_associations: List[dict]
