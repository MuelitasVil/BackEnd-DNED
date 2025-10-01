from openpyxl import Workbook, worksheet
from pytest import Session
from app.domain.enums.files.estudiante_activos import EstudianteActivos
from app.service.excel.case_estudiantes_activos import case_estudiantes_activos
from fastapi import HTTPException

from app.service.crud.period_service import PeriodService


def process_file(file: Workbook, cod_period: str, session: Session) -> bool:
    first_sheet_name: str = file.sheetnames[0]
    ws: worksheet = file[first_sheet_name]

    period = PeriodService.get_by_code(session, cod_period)
    if not period:
        raise HTTPException(status_code=400, detail={
            "error": f"El periodo con código {cod_period} no existe",
            "message": "Verifique el código del periodo"
        })

    headers = get_headers(ws)
    if not headers:
        return False

    if EstudianteActivos.validate_headers(headers):
        return case_estudiantes_activos(ws, cod_period, session)

    raise HTTPException(status_code=400, detail={
        "error": f"La hoja {first_sheet_name} no tiene una estructura válida",
        "headers": headers,
        "message": (
            "El programa siempre toma la primera hoja, verifique si la "
            "primera hoja es la que contiene la información"
        )
    })


def get_headers(ws: worksheet) -> list[str]:
    return [cell.value for cell in ws[1]]
