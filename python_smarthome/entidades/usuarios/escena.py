"""Entidad Escena - Representa una rutina o configuración guardada."""


class Escena:
    """
    Representa una escena que agrupa una serie de acciones.
    
    Attributes:
        _id_escena: ID de la escena
        _nombre: Nombre de la escena
        _descripcion: Descripción de la escena
    """

    def __init__(self, id_escena: int, nombre: str, descripcion: str):
        self._id_escena = id_escena
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id_escena(self) -> int:
        return self._id_escena

    def get_nombre(self) -> str:
        return self._nombre

    def get_descripcion(self) -> str:
        return self._descripcion
