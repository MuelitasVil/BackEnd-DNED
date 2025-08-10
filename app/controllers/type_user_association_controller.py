from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.configuration.database import get_session
from app.utils.auth import get_current_user
from app.domain.models.type_user_association import TypeUserAssociation
from app.domain.dtos.type_user_association.type_user_association_input import (
    TypeUserAssociationInput
)
from app.service.crud.type_user_association_service import (
    TypeUserAssociationService
)

router = APIRouter(
    prefix="/type_user_associations",
    tags=["Type User Association"]
)


@router.get("/", response_model=List[TypeUserAssociation])
def list_associations(
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):
    return TypeUserAssociationService.get_all(session)


@router.get("/{email_unal}/{type_user_id}/{cod_period}",
            response_model=TypeUserAssociation)
def get_association(
    email_unal: str,
    type_user_id: str,
    cod_period: str,
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):
    assoc = TypeUserAssociationService.get_by_ids(
        email_unal,
        type_user_id,
        cod_period,
        session
    )
    if not assoc:
        raise HTTPException(status_code=404, detail="Association not found")
    return assoc


@router.post(
    "/",
    response_model=TypeUserAssociation,
    status_code=status.HTTP_201_CREATED
)
def create_association(
    data: TypeUserAssociationInput,
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):
    return TypeUserAssociationService.create(data, session)


@router.delete(
    "/{email_unal}/{type_user_id}/{cod_period}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_association(
    email_unal: str,
    type_user_id: str,
    cod_period: str,
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):
    deleted = TypeUserAssociationService.delete(
        email_unal,
        type_user_id,
        cod_period,
        session
    )
    if not deleted:
        raise HTTPException(status_code=404, detail="Association not found")
