"""Entidad Casa - Representa una propiedad."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion
    from python_smarthome.entidades.usuarios.usuario import Usuario


class Casa:
    """
    Representa una casa con dirección, superficie y habitaciones.
    
    Attributes:
        _direccion: Dirección de la casa
        _superficie: Superficie en m²
        _propietario: Nombre del propietario
        _habitaciones: Lista de habitaciones en la casa
        _usuarios: Lista de usuarios autorizados
    """

    def __init__(self, direccion: str, superficie: float, propietario: str):
        self._direccion = direccion
        self._superficie = superficie
        self._propietario = propietario
        self._habitaciones: List['Habitacion'] = []
        self._usuarios: List['Usuario'] = []

    def get_direccion(self) -> str:
        return self._direccion

    def get_superficie(self) -> float:
        return self._superficie

    def get_propietario(self) -> str:
        return self._propietario

    def get_habitaciones(self) -> List['Habitacion']:
        return self._habitaciones.copy()  # Defensive copy

    def set_habitaciones(self, habitaciones: List['Habitacion']) -> None:
        self._habitaciones = habitaciones

    def get_usuarios(self) -> List['Usuario']:
        return self._usuarios.copy()  # Defensive copy

    def set_usuarios(self, usuarios: List['Usuario']) -> None:
        self._usuarios = usuarios
