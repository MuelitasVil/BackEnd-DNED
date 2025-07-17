from sqlmodel import Session
from app.domain.dtos.user_workspace_associate.user_workspace_associate_input import (  # noqa: E501
    UserWorkspaceAssociateInput
)
from app.domain.models.user_workspace_associate import UserWorkspaceAssociate
from app.repository.user_workspace_associate_repository import (
    UserWorkspaceAssociateRepository
)


class UserWorkspaceAssociateService:
    @staticmethod
    def create(input_data: UserWorkspaceAssociateInput, session: Session):
        associate = UserWorkspaceAssociate(**input_data.model_dump())
        return UserWorkspaceAssociateRepository(session).create(associate)

    @staticmethod
    def get_all(session: Session):
        return UserWorkspaceAssociateRepository(session).get_all()

    @staticmethod
    def delete(
        email_unal: str,
        cod_unit: str,
        cod_period: str,
        session: Session
    ):
        repo = UserWorkspaceAssociateRepository(session)
        associate = repo.get_by_keys(email_unal, cod_unit, cod_period)
        if associate:
            repo.delete(associate)
            return True
        return False
