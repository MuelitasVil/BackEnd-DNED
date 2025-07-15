from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.configuration.database import get_session
from app.domain.models.period import Period
from app.domain.dtos.period.period_input import PeriodInput
from app.service.period_service import PeriodService

router = APIRouter(prefix="/periods", tags=["Periods"])


@router.get("/", response_model=List[Period])
def list_periods(session: Session = Depends(get_session)):
    return PeriodService.get_all(session)


@router.get("/{cod_period}", response_model=Period)
def get_period(cod_period: str, session: Session = Depends(get_session)):
    period = PeriodService.get_by_id(cod_period, session)
    if not period:
        raise HTTPException(status_code=404, detail="Period not found")
    return period


@router.post("/", response_model=Period, status_code=status.HTTP_201_CREATED)
def create_period(data: PeriodInput, session: Session = Depends(get_session)):
    return PeriodService.create_period(data, session)


@router.patch("/{cod_period}", response_model=Period)
def update_period(
    cod_period: str,
    data: PeriodInput,
    session: Session = Depends(get_session)
):
    updated = PeriodService.update_period(cod_period, data, session)
    if not updated:
        raise HTTPException(status_code=404, detail="Period not found")
    return updated


@router.delete("/{cod_period}", status_code=status.HTTP_204_NO_CONTENT)
def delete_period(cod_period: str, session: Session = Depends(get_session)):
    deleted = PeriodService.delete_period(cod_period, session)
    if not deleted:
        raise HTTPException(status_code=404, detail="Period not found")
