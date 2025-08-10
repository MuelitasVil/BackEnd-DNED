from sqlalchemy.orm import Session
from typing import List, Optional

from app.repository.user_unit_associate_repository import (
    UserUnitAssociateRepository,
)
from app.domain.models.user_unit_associate import UserUnitAssociate
from app.domain.dtos.user_unit_associate.user_unit_associate_input import (
    UserUnitAssociateInput
)


class UserUnitAssociateService:
    @staticmethod
    def get_all(session: Session) -> List[UserUnitAssociate]:
        return UserUnitAssociateRepository(session).get_all()

    @staticmethod
    def get_by_ids(
        email_unal: str,
        cod_unit: str,
        cod_period: str,
        session: Session
    ) -> Optional[UserUnitAssociate]:
        return UserUnitAssociateRepository(session).get_by_ids(
            email_unal,
            cod_unit,
            cod_period
        )

    @staticmethod
    def create(
        input_data: UserUnitAssociateInput,
        session: Session
    ) -> UserUnitAssociate:
        association = UserUnitAssociate(**input_data.model_dump())
        return UserUnitAssociateRepository(session).create(association)

    @staticmethod
    def delete(
        email_unal: str,
        cod_unit: str,
        cod_period: str,
        session: Session
    ) -> bool:
        return UserUnitAssociateRepository(session).delete(
            email_unal,
            cod_unit,
            cod_period
        )
