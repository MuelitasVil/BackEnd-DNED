from sqlalchemy.orm import Session
from typing import List, Optional

from app.repository.unit_school_associate_repository import (
    UnitSchoolAssociateRepository,
)
from app.domain.models.unit_school_associate import UnitSchoolAssociate
from app.domain.dtos.unit_school_associate.unit_school_associate_input import (
    UnitSchoolAssociateInput
)


class UnitSchoolAssociateService:
    @staticmethod
    def get_all(session: Session) -> List[UnitSchoolAssociate]:
        return UnitSchoolAssociateRepository(session).get_all()

    @staticmethod
    def get_by_ids(
        cod_unit: str,
        cod_school: str,
        cod_period: str,
        session: Session
    ) -> Optional[UnitSchoolAssociate]:
        return UnitSchoolAssociateRepository(session).get_by_ids(
            cod_unit, cod_school, cod_period
        )

    @staticmethod
    def create(
        input_data: UnitSchoolAssociateInput,
        session: Session
    ) -> UnitSchoolAssociate:
        assoc = UnitSchoolAssociate(**input_data.model_dump())
        return UnitSchoolAssociateRepository(session).create(assoc)

    @staticmethod
    def delete(
        cod_unit: str,
        cod_school: str,
        cod_period: str,
        session: Session
    ) -> bool:
        return UnitSchoolAssociateRepository(session).delete(
            cod_unit,
            cod_school,
            cod_period
        )
