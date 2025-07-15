# app/repository/user_workspace_repository.py
from sqlalchemy.orm import Session
from app.domain.models.user_workspace import UserWorkspace


class UserWorkspaceRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(UserWorkspace).all()

    def get_by_id(self, workspace_id: str):
        return self.session.get(UserWorkspace, workspace_id)

    def create(self, workspace: UserWorkspace):
        self.session.add(workspace)
        self.session.commit()
        self.session.refresh(workspace)
        return workspace

    def update(self, workspace_id: str, data):
        workspace = self.get_by_id(workspace_id)
        if not workspace:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(workspace, key, value)
        self.session.commit()
        return workspace

    def delete(self, workspace_id: str):
        workspace = self.get_by_id(workspace_id)
        if not workspace:
            return False
        self.session.delete(workspace)
        self.session.commit()
        return True
