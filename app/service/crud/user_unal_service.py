from sqlalchemy.orm import Session
from typing import List, Optional

from app.repository.user_unal_repository import UserUnalRepository
from app.domain.models.user_unal import UserUnal
from app.domain.dtos.user_unal.user_unal_input import UserUnalInput


class UserUnalService:
    @staticmethod
    def get_all(session: Session) -> List[UserUnal]:
        return UserUnalRepository(session).get_all()

    @staticmethod
    def get_by_email(email_unal: str, session: Session) -> Optional[UserUnal]:
        return UserUnalRepository(session).get_by_email(email_unal)

    @staticmethod
    def create(input_data: UserUnalInput, session: Session) -> UserUnal:
        user = UserUnal(**input_data.model_dump(exclude_unset=True))
        return UserUnalRepository(session).create(user)

    @staticmethod
    def update(
        email_unal: str,
        input_data: UserUnalInput,
        session: Session
    ) -> Optional[UserUnal]:
        return UserUnalRepository(session).update(email_unal, input_data)

    @staticmethod
    def delete(email_unal: str, session: Session) -> bool:
        return UserUnalRepository(session).delete(email_unal)
