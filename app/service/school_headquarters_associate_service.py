from sqlalchemy.orm import Session
from typing import List, Optional

from app.repository.school_headquarters_associate_repository import (
    SchoolHeadquartersAssociateRepository
) 
from app.domain.models.school_headquarters_associate import (
    SchoolHeadquartersAssociate
)
from app.domain.dtos.school_headquarters_associate.school_headquarters_associate_input import (  # noqa: E501 ignora error flake8
    SchoolHeadquartersAssociateInput
)


class SchoolHeadquartersAssociateService:
    @staticmethod
    def get_all(session: Session) -> List[SchoolHeadquartersAssociate]:
        return SchoolHeadquartersAssociateRepository(session).get_all()

    @staticmethod
    def get_by_ids(
        cod_school: str,
        cod_headquarters: str,
        cod_period: str,
        session: Session
    ) -> Optional[SchoolHeadquartersAssociate]:
        return SchoolHeadquartersAssociateRepository(session).get_by_ids(
            cod_school,
            cod_headquarters,
            cod_period
        )

    @staticmethod
    def create(
        input_data: SchoolHeadquartersAssociateInput,
        session: Session
    ) -> SchoolHeadquartersAssociate:
        assoc = SchoolHeadquartersAssociate(**input_data.model_dump())
        return SchoolHeadquartersAssociateRepository(session).create(assoc)

    @staticmethod
    def delete(
        cod_school: str,
        cod_headquarter: str,
        cod_period: str,
        session: Session
    ) -> bool:
        return SchoolHeadquartersAssociateRepository(session).delete(
            cod_school,
            cod_headquarter,
            cod_period
        )
