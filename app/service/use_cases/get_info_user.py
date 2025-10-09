from typing import Optional
from sqlmodel import Session

from app.service.crud.user_unal_service import UserUnalService
from app.service.crud.unit_unal_service import UnitUnalService
from app.service.crud.school_service import SchoolService
from app.service.crud.headquarters_service import HeadquartersService
from app.service.crud.user_unit_associate_service import (
    UserUnitAssociateService
)
from app.service.crud.unit_school_associate_service import ( 
    UnitSchoolAssociateService
)
from app.service.crud.school_headquarters_associate_service import (
    SchoolHeadquartersAssociateService
)

from app.domain.models.user_unal import UserUnal
from app.domain.models.unit_unal import UnitUnal
from app.domain.models.school import School
from app.domain.models.headquarters import Headquarters
from app.domain.models.user_unit_associate import UserUnitAssociate
from app.domain.models.unit_school_associate import UnitSchoolAssociate
from app.domain.models.school_headquarters_associate import (  # noqa: E501 ignora error flake8
    SchoolHeadquartersAssociate
)


from app.domain.dtos.user_unal.user_info import UserInfoAssociation
from app.utils.entity_manager import get_entity_or_raise


def get_info_user_information(
    email_unal: str, session: Session, only_codes: bool = True
) -> Optional[UserInfoAssociation]:
    user_unal: UserUnal = get_entity_or_raise(
        UserUnalService, email_unal, "User"
    )

    units: list[UnitUnal] = []
    schools: list[School] = []
    headquarters: list[Headquarters] = []

    user_units: list[UserUnitAssociate] = []
    unit_schools: list[UnitSchoolAssociate] = []
    school_headquarters: list[SchoolHeadquartersAssociate] = []

    user_units_by_period: dict[str, list[UserUnitAssociate]] = {}
    schools_by_period: dict[str, list[School]] = {}
    headquarters_by_period: dict[str, list[Headquarters]] = {}

    period_associations: dict[str, dict] = {}
    periods: set[str] = set()

    user_units = get_entity_or_raise(
        UserUnitAssociateService, email_unal, "User Unit"
    )

    for user_unit in user_units:
        if user_unit.cod_period not in periods:
            periods.add(user_unit.cod_period)

        unit = get_entity_or_raise(UnitUnalService, user_unit.cod_unit, "Unit")
        units.append(unit)

    for unit in units:
        unit_schools = get_entity_or_raise(
            UnitSchoolAssociateService, unit.cod_unit, "Unit School"
        )

    for unit_school in unit_schools:
        school = get_entity_or_raise(
            SchoolService, unit_school.cod_school, "School"
        )
        if school not in schools:
            schools.append(school)

    for school in schools:
        school_headquarters = get_entity_or_raise(
            SchoolHeadquartersAssociateService,
            school.cod_school,
            "School Headquarters"
        )

    for school_headquarter in school_headquarters:
        headquarters_instance = get_entity_or_raise(
            HeadquartersService,
            school_headquarter.cod_headquarters,
            "Headquarters"
        )
        if headquarters_instance not in headquarters:
            headquarters.append(headquarters_instance)

    for period in periods:
        if period not in period_associations:
            period_associations[period] = {}

    if only_codes:
        units = [UnitUnal(cod_unit=unit.cod_unit) for unit in units]
        schools = [School(cod_school=school.cod_school) for school in schools]
        headquarters = [
            Headquarters(cod_headquarters=headquarter.cod_headquarters)
            for headquarter in headquarters
        ]

    return UserInfoAssociation(
        email_unal=email_unal,
        name=user_unal.name,
        lastname=user_unal.lastname,
        full_name=user_unal.full_name,
        gender=user_unal.gender,
        birth_date=user_unal.birth_date,
        headquarters=user_unal.headquarters,

    )