from sqlmodel import Session, select
from app.domain.models.user_workspace_associate import UserWorkspaceAssociate


class UserWorkspaceAssociateRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        associate: UserWorkspaceAssociate
    ) -> UserWorkspaceAssociate:
        self.session.add(associate)
        self.session.commit()
        self.session.refresh(associate)
        return associate

    def get_all(self):
        return self.session.exec(select(UserWorkspaceAssociate)).all()

    def get_by_keys(self, email_unal: str, cod_unit: str, cod_period: str):
        return self.session.get(
            UserWorkspaceAssociate,
            (email_unal, cod_unit, cod_period)
        )

    def delete(self, associate: UserWorkspaceAssociate):
        self.session.delete(associate)
        self.session.commit()
