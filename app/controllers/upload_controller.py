from fastapi import APIRouter, Depends, File, UploadFile, status
from sqlmodel import Session
from openpyxl import Workbook

from app.configuration.database import get_session
from app.utils.auth import get_current_user
from app.utils.type_file_validation import readExcelFile

from app.service.excel.process_file import process_file


router = APIRouter(prefix="/upload_excel", tags=["Excel Upload"])


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_excel_file(
    cod_period: str,
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):

    wb: Workbook = await readExcelFile(file)
    # Save the data in the excel in database
    return process_file(wb, cod_period, session)
