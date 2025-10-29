"""Interfaz base para todos los dispositivos."""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Dispositivo(ABC):
    """
    Clase base abstracta para dispositivos IoT.
    
    Attributes:
        _id_dispositivo: ID único del dispositivo
        _encendido: Estado on/off del dispositivo
    """

    _contador_id: int = 0

    def __init__(self):
        """Inicializa dispositivo con ID único."""
        Dispositivo._contador_id += 1
        self._id_dispositivo: int = Dispositivo._contador_id
        self._encendido: bool = False

    def get_id_dispositivo(self) -> int:
        """
        Obtiene ID del dispositivo.
        
        Returns:
            ID único
        """
        return self._id_dispositivo

    def is_encendido(self) -> bool:
        """
        Verifica si dispositivo está encendido.
        
        Returns:
            True si está encendido
        """
        return self._encendido

    def set_encendido(self, encendido: bool) -> None:
        """
        Establece estado del dispositivo.
        
        Args:
            encendido: True para encender, False para apagar
        """
        self._encendido = encendido
