"""Enum para los modos del sistema."""

from enum import Enum


class ModoSistema(Enum):
    """
    Enumeración para los diferentes modos del sistema.
    """
    NOCHE = "noche"
    VACACIONES = "vacaciones"
    FIESTA = "fiesta"
    CINE = "cine"
