from sqlalchemy.orm import Session
from typing import List, Optional

from app.repository.unit_unal_repository import UnitUnalRepository
from app.domain.models.unit_unal import UnitUnal
from app.domain.dtos.unit_unal.unit_unal_input import UnitUnalInput


class UnitUnalService:
    @staticmethod
    def get_all(session: Session) -> List[UnitUnal]:
        return UnitUnalRepository(session).get_all()

    @staticmethod
    def get_by_id(cod_unit: str, session: Session) -> Optional[UnitUnal]:
        return UnitUnalRepository(session).get_by_id(cod_unit)

    @staticmethod
    def create(input_data: UnitUnalInput, session: Session) -> UnitUnal:
        unit = UnitUnal(**input_data.model_dump(exclude_unset=True))
        return UnitUnalRepository(session).create(unit)

    @staticmethod
    def update(
        cod_unit: str,
        input_data: UnitUnalInput,
        session: Session
    ) -> Optional[UnitUnal]:
        return UnitUnalRepository(session).update(cod_unit, input_data)

    @staticmethod
    def delete(cod_unit: str, session: Session) -> bool:
        return UnitUnalRepository(session).delete(cod_unit)
