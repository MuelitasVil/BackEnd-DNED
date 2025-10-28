from sqlmodel import Session, insert, select
from typing import List, Optional

from app.domain.models.email_sender_school import EmailSenderSchool


class EmailSenderSchoolRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[EmailSenderSchool]:
        return self.session.exec(select(EmailSenderSchool)).all()

    def get_by_id(
        self,
        sender_id: str,
        cod_school: str
    ) -> Optional[EmailSenderSchool]:
        return self.session.get(EmailSenderSchool, (sender_id, cod_school))

    def create(self, assoc: EmailSenderSchool) -> EmailSenderSchool:
        self.session.add(assoc)
        self.session.commit()
        self.session.refresh(assoc)
        return assoc

    def delete(self, sender_id: str, cod_school: str) -> bool:
        assoc = self.get_by_id(sender_id, cod_school)
        if assoc:
            self.session.delete(assoc)
            self.session.commit()
            return True
        return False

    def bulk_insert_ignore(
        self, headquarter_emails: List[EmailSenderSchool]
    ):
        """
        Inserta múltiples usuarios en la tabla.
        Si encuentra PK duplicada (email_unal), ignora ese registro.
        """
        stmt = insert(EmailSenderSchool).values(
            [u.model_dump() for u in headquarter_emails]
        )
        stmt = stmt.prefix_with("IGNORE")
        self.session.exec(stmt)
        self.session.commit()
