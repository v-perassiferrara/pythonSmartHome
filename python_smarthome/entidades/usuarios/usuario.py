"""Entidad Usuario - Representa un usuario del sistema."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.usuarios.escena import Escena
    from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso


class Usuario:
    """
    Representa un usuario del sistema con su nivel de acceso y escenas.
    
    Attributes:
        _id_usuario: ID del usuario
        _nombre: Nombre del usuario
        _nivel_acceso: Nivel de acceso del usuario
        _escenas: Lista de escenas asignadas al usuario
    """

    def __init__(self, id_usuario: int, nombre: str, nivel_acceso: 'NivelAcceso', escenas: List['Escena']):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._nivel_acceso = nivel_acceso
        self._escenas = escenas

    def get_id_usuario(self) -> int:
        return self._id_usuario

    def get_nombre(self) -> str:
        return self._nombre

    def get_nivel_acceso(self) -> 'NivelAcceso':
        return self._nivel_acceso

    def get_escenas(self) -> List['Escena']:
        return self._escenas.copy()  # Defensive copy
