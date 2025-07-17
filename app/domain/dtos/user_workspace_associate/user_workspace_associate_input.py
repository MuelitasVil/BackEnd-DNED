from pydantic import BaseModel, EmailStr


class UserWorkspaceAssociateInput(BaseModel):
    email_unal: EmailStr
    cod_period: str
