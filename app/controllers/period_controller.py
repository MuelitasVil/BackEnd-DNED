from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.configuration.database import get_session
from app.repository.period_repository import PeriodRepository
from app.domain.models.period import Period
from app.domain.dtos.period.period_input import PeriodInput

router = APIRouter(prefix="/periods", tags=["Periods"])

@router.get("/", response_model=List[Period])
def list_periods(session: Session = Depends(get_session)):
    repo = PeriodRepository(session)
    return repo.get_all()

@router.get("/{cod_period}", response_model=Period)
def get_period(cod_period: str, session: Session = Depends(get_session)):
    repo = PeriodRepository(session)
    period = repo.get_by_id(cod_period)
    if not period:
        raise HTTPException(status_code=404, detail="Period not found")
    return period

@router.post("/", response_model=Period, status_code=status.HTTP_201_CREATED)
def create_period(data: PeriodInput, session: Session = Depends(get_session)):
    repo = PeriodRepository(session)
    period = Period(cod_period=data.cod_period, **data.dict(exclude_unset=True))
    return repo.create(period)

@router.patch("/{cod_period}", response_model=Period)
def update_period(cod_period: str, data: PeriodInput, session: Session = Depends(get_session)):
    repo = PeriodRepository(session)
    updated = repo.update(cod_period, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Period not found")
    return updated

@router.delete("/{cod_period}", status_code=status.HTTP_204_NO_CONTENT)
def delete_period(cod_period: str, session: Session = Depends(get_session)):
    repo = PeriodRepository(session)
    deleted = repo.delete(cod_period)
    if not deleted:
        raise HTTPException(status_code=404, detail="Period not found")
