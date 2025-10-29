"""Enum NivelAcceso - Define los niveles de permiso en el sistema."""

from enum import Enum


class NivelAcceso(Enum):
    """
    Enumeración para los niveles de acceso de usuario.
    """
    INVITADO = 1
    FAMILIAR = 2
    PROPIETARIO = 3
    ADMIN = 4
    SUPER = 5
