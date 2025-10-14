from typing import Optional
from sqlmodel import Session
from fastapi import HTTPException

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


def get_info_user_information(
    email_unal: str, session: Session, only_codes: bool = True
) -> Optional[UserInfoAssociation]:

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

    user_unal: UserUnal = UserUnalService.get_by_email(email_unal, session)
    if user_unal is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_units = UserUnitAssociateService.get_by_user(email_unal, session)
    if user_units is None:
        raise HTTPException(status_code=404, detail="User units not found")

    _process_user_units(
        user_units, periods, user_units_by_period, units, session
    )

    for unit in units:
        unit_schools = UnitSchoolAssociateService.get_by_unit(
            unit.cod_unit, session
        )

        if unit_schools is None:
            raise HTTPException(
                status_code=404, detail="Unit schools not found"
            )

    _process_unit_schools(
        unit_schools, periods, schools_by_period, schools, session
    )

    for school_headquarter in school_headquarters:
        headquarters_instance = HeadquartersService.get_by_id(
            school_headquarter.cod_headquarters, session
        )

        if headquarters_instance is None:
            raise HTTPException(
                status_code=404, detail="Headquarters not found"
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


def _process_user_units(
    user_units: list[UserUnitAssociate],
    periods: set[str],
    user_units_by_period: dict[str, list[UserUnitAssociate]],
    units: list[UnitUnal],
    session: Session
) -> None:
    """
    Procesa la lista de unidades asociadas al usuario y actualiza los periodos
    y unidades correspondientes.

    Args:
        user_units: Lista de asociaciones de unidades para un usuario.
        periods: Conjunto de periodos únicos encontrados.
        user_units_by_period: Diccionario que mapea cada periodo a sus unidades
            asociadas.
        units: Lista que almacenará las unidades.
        session: La sesión de la base de datos.

    Returns:
        None: Modifica directamente los parámetros `periods`,
        `user_units_by_period` y `units`."""

    for user_unit in user_units:
        # Agregar periodo si no está presente
        if user_unit.cod_period not in periods:
            periods.add(user_unit.cod_period)

        # Agregar la unidad al diccionario correspondiente al periodo
        if user_unit.cod_period not in user_units_by_period:
            user_units_by_period[user_unit.cod_period] = []

        # Obtener la unidad y agregarla a la lista de unidades
        unit = UnitUnalService.get_by_id(user_unit.cod_unit, session)
        if unit is None:
            raise HTTPException(status_code=404, detail="Unit not found")

        units.append(unit)

        # Asociar la unidad al periodo correspondiente
        user_units_by_period[user_unit.cod_period].append(user_unit)


def _process_unit_schools(
    unit_schools: list[UnitSchoolAssociate],
    periods: set[str],
    schools_by_period: dict[str, list[School]],
    schools: list[School],
    session: Session
) -> None:
    """
    Procesa la lista de escuelas asociadas a una unidad y actualiza los
    periodos y escuelas correspondientes.

    Args:
        unit_schools: Lista de asociaciones de escuelas para una unidad.
        periods: Conjunto de periodos únicos encontrados.
        schools_by_period: Diccionario que mapea cada periodo a sus escuelas
            asociadas.
        schools: Lista que almacenará las escuelas.
        session: La sesión de la base de datos.

    Returns:
        None: Modifica directamente los parámetros `periods`,
        `schools_by_period` y `schools`."""

    for unit_school in unit_schools:
        # Agregar periodo si no está presente
        if unit_school.cod_period not in periods:
            periods.add(unit_school.cod_period)

        # Agregar la escuela al diccionario correspondiente al periodo
        if unit_school.cod_period not in schools_by_period:
            schools_by_period[unit_school.cod_period] = []

        # Obtener la escuela y agregarla a la lista de escuelas
        school = SchoolService.get_by_id(
            unit_school.cod_school, session
        )

        if school is None:
            raise HTTPException(status_code=404, detail="School not found")

        if school not in schools:
            schools.append(school)

        # Asociar la escuela al periodo correspondiente
        schools_by_period[unit_school.cod_period].append(school)
