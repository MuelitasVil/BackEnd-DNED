from sqlmodel import Session, insert, select
from typing import List, Optional

from app.domain.models.email_sender_headquarters import EmailSenderHeadquarters


class EmailSenderHeadquartersRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(
            self, start: int = 0, limit: int = 100
    ) -> List[EmailSenderHeadquarters]:
        return self.session.exec(
            select(EmailSenderHeadquarters).offset(start).limit(limit)).all()

    def get_by_id(
        self,
        sender_id: str,
        cod_headquarters: str
    ) -> Optional[EmailSenderHeadquarters]:
        return self.session.get(
            EmailSenderHeadquarters,
            (sender_id, cod_headquarters)
        )

    def create(
        self,
        assoc: EmailSenderHeadquarters
    ) -> EmailSenderHeadquarters:
        self.session.add(assoc)
        self.session.commit()
        self.session.refresh(assoc)
        return assoc

    def delete(self, sender_id: str, cod_headquarters: str) -> bool:
        assoc = self.get_by_id(sender_id, cod_headquarters)
        if assoc:
            self.session.delete(assoc)
            self.session.commit()
            return True
        return False

    def bulk_insert_ignore(
        self, headquarter_emails: List[EmailSenderHeadquarters]
    ):
        """
        Inserta múltiples usuarios en la tabla.
        Si encuentra PK duplicada (email_unal), ignora ese registro.
        """
        stmt = insert(EmailSenderHeadquarters).values(
            [u.model_dump() for u in headquarter_emails]
        )
        stmt = stmt.prefix_with("IGNORE")
        self.session.exec(stmt)
        self.session.commit()
