from enum import Enum
from typing import List


# Definir el mapeo de sedes y su orden
class SedeEnum(Enum):
    SEDE_BOGOTA = (1, "SEDE BOGOTÁ")
    SEDE_MANIZALES = (2, "SEDE MANIZALES")
    SEDE_MEDELLÍN = (3, "SEDE MEDELLÍN")
    SEDE_PALMIRA = (4, "SEDE PALMIRA")
    SEDE_AMAZONIA = (5, "SEDE AMAZONÍA")
    SEDE_CARIBE = (6, "SEDE CARIBE")
    SEDE_ORINOQUÍA = (7, "SEDE ORINOQUÍA")
    SEDE_TUMACO = (8, "SEDE TUMACO")
    SEDE_DE_LA_PAZ = (9, "SEDE DE LA PAZ")

    def __init__(self, number, _name):
        self.number = number
        self._name = _name

    @classmethod
    def is_valid_sede(cls, sede_value: str) -> bool:
        """
        Valida si el valor de la sede proporcionado existe en el Enum SedeEnum.
        :param sede_value: El valor de la sede (con tildes, mayúsculas, etc.).
        :return: True si la sede existe, False en caso contrario.
        """
        # Comparar directamente el string con los nombres de los miembros
        # del Enum
        name_members = [member._name for member in cls]
        if sede_value in name_members:
            return True
        return False

    @classmethod
    def get_by_name(cls, name: str):
        """
        Obtiene un miembro del Enum a partir del nombre de la sede.
        :param name: El nombre de la sede (como cadena, e.g., "SEDE BOGOTÁ").
        :return: El miembro correspondiente del Enum.
        """
        # Comparar el nombre ingresado con el atributo _name del Enum
        for member in cls:
            if member._name == name:
                return member
        return None  # Si no se encuentra el nombre, se retorna None


class EstudianteActivos(Enum):
    NOMBRES_APELLIDOS = 1
    EMAIL = 2
    SEDE = 3
    FACULTAD = 4
    COD_PLAN = 5
    PLAN = 6
    TIPO_NIVEL = 7

    @classmethod
    def validate_headers(cls, headers: List[str]) -> bool:
        """
        Verifica si todos los encabezados en `headers` están en el Enum.
        No requiere que estén en orden, pero sí que estén todos presentes.
        """
        # Normalizamos las cadenas para evitar errores por
        # mayúsculas/minúsculas/espacios

        normalized_headers = {h.strip().upper() for h in headers if h}
        enum_headers = {e.name for e in cls}
        return enum_headers.issubset(normalized_headers)
