from typing import List, Tuple
from sqlmodel import Session
from sqlalchemy import text


def get_email_list_of_unit(
        session: Session,
        cod_unit: str,
        cod_period: str
) -> List[Tuple[str, str]]:
    stmt = (
        text("CALL get_email_list_of_unit(:unit, :period)")
        .bindparams(unit=cod_unit, period=cod_period)
    )
    rows = session.exec(stmt).all()
    # rows es lista de Row/tuplas (email, tipo)
    return [(r[0], r[1]) for r in rows]


def get_email_list_of_school(
    session: Session,
    cod_school: str,
    cod_period: str
) -> List[Tuple[str, str]]:
    stmt = (
        text("CALL get_email_list_of_school(:school, :period)")
        .bindparams(school=cod_school, period=cod_period)
    )
    rows = session.exec(stmt).all()
    return [(r[0], r[1]) for r in rows]


def get_email_list_of_headquarters(
    session: Session,
    cod_headquarters: str,
    cod_period: str
) -> List[Tuple[str, str]]:
    stmt = (
        text("CALL get_email_list_of_headquarters(:hq, :period)")
        .bindparams(hq=cod_headquarters, period=cod_period)
    )
    rows = session.exec(stmt).all()
    return [(r[0], r[1]) for r in rows]
