from openpyxl.cell.cell import Cell
from typing import Any, Tuple
import unicodedata


def is_blank(v: Any) -> bool:
    return v is None or (isinstance(v, str) and v.strip() == "")


def get_file_text(v: Any) -> str:
    if v is None:
        return ""
    text = str(v).strip()
    text = text.replace('(', '').replace(')', '')
    return text


def get_value_from_row(row: Tuple[Cell, ...], col_idx: int) -> str:
    # La columna es 1-indexada
    return get_file_text(row[col_idx - 1].value)


# Función para normalizar la cadena: eliminar tildes y convertir a minúsculas
def normalize_string(s: str) -> str:
    """Normaliza una cadena eliminando tildes y convirtiéndola a minúsculas."""
    if s is None:
        return ""
    nfkd_form = unicodedata.normalize('NFKD', s)
    return (
        ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
        .lower()
    )
