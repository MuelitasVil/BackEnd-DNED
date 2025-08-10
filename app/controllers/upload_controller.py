from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlmodel import Session
from io import BytesIO
from openpyxl import load_workbook

from app.configuration.database import get_session
from app.utils.auth import get_current_user

router = APIRouter(prefix="/upload_excel", tags=["Excel Upload"])


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_excel_file(
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
    user_email: str = Depends(get_current_user)
):
    if not file.filename.endswith((".xlsx", ".xlsm")):
        raise HTTPException(
            status_code=400,
            detail="El archivo debe ser .xlsx o .xlsm"
        )

    try:
        contents = await file.read()
        excel_io = BytesIO(contents)

        wb = load_workbook(excel_io)
        sheet = wb.active

        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))

        return {
            "filename": file.filename,
            "total_rows": len(data),
            "columns": len(data[0]) if data else 0,
            "preview": data[:5]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar el archivo: {str(e)}"
        )
