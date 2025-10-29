"""Entidad Habitacion - Representa un espacio dentro de una casa."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class Habitacion:
    """
    Representa una habitación con un nombre y dispositivos.
    
    Attributes:
        _nombre: Nombre de la habitación
        _dispositivos: Lista de dispositivos en la habitación
    """

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List['Dispositivo'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List['Dispositivo']:
        return self._dispositivos.copy()  # Defensive copy

    def agregar_dispositivo(self, dispositivo: 'Dispositivo') -> None:
        self._dispositivos.append(dispositivo)

    def agregar_dispositivos(self, dispositivos: List['Dispositivo']) -> None:
        self._dispositivos.extend(dispositivos)
