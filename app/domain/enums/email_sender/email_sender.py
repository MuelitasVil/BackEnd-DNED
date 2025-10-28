from enum import Enum


# Definir el mapeo de sedes y su orden
class OrgType(Enum):
    GLOBAL = "GLOBAL"
    HEADQUARTERS = "HEADQUARTERS"
    SCHOOL = "SCHOOL"
    UNIT = "UNIT"


class OrgLevel(Enum):
    PREGRADO = "PRE"
    POSGRADO = "POS"
    ANY = "ANY"


class Role(Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"
