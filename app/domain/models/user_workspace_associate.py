from sqlmodel import SQLModel, Field


class UserWorkspaceAssociate(
    SQLModel, table=True
):
    email_unal: str = Field(
        foreign_key="user_unal.email_unal", max_length=100, primary_key=True)
    cod_unit: str = Field(
        max_length=50, primary_key=True)
    cod_period: str = Field(
        foreign_key="period.cod_period", max_length=50, primary_key=True)
