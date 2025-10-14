from typing import Optional
from sqlmodel import Session
from fastapi import HTTPException
from sqlalchemy import text

from app.domain.models.user_unal import UserUnal
from app.domain.dtos.user_unal.user_info import UserInfoAssociation

from app.service.crud.user_unal_service import UserUnalService


def get_info_user_via_sp(
    email_unal: str,
    session: Session
) -> Optional[UserInfoAssociation]:
    """
    Llama al SP GetUserAcademicData y procesa los resultados en un DTO
    agrupado por periodos.
    """

    user: UserUnal = UserUnalService.get_by_email(email_unal, session)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    stmt = (
        text("CALL GetUserAcademicData(:email)")
        .bindparams(email=email_unal)
    )

    result = session.exec(stmt).mappings().all()
    user_info = UserInfoAssociation(
        email_unal=email_unal,
        document=user.document,
        name=user.name,
        lastname=user.lastname,
        full_name=user.full_name,
        gender=user.gender,
        headquarters=user.headquarters,
        period_associations={}
    )

    print(result)

    temp_dict = {}
    for row in result:
        period = row['cod_period']
        if period not in temp_dict:
            temp_dict[period] = {}

        headquarters_cod = row['cod_headquarters']
        if headquarters_cod not in temp_dict[period]:
            temp_dict[period][headquarters_cod] = {}

        school_code = row['cod_school']
        if school_code not in temp_dict[period][headquarters_cod]:
            temp_dict[period][headquarters_cod][school_code] = []

        unit_code = row['cod_unit']
        if unit_code not in temp_dict[period][headquarters_cod][school_code]:
            temp_dict[period][headquarters_cod][school_code].append(unit_code)

    print(temp_dict)
    user_info.period_associations = temp_dict
    print(user_info)
    return user_info
