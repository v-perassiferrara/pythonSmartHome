"""Excepción de capacidad insuficiente."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class CapacidadInsuficienteException(SmartHomeException):
    """
    Excepción lanzada cuando no hay capacidad para instalar dispositivos.
    
    Attributes:
        _capacidad_requerida: Dispositivos requeridos
        _capacidad_disponible: Dispositivos disponibles
    """

    def __init__(
        self,
        capacidad_requerida: int,
        capacidad_disponible: int
    ):
        """
        Inicializa excepción.
        
        Args:
            capacidad_requerida: Dispositivos que se intentaron instalar
            capacidad_disponible: Dispositivos que caben
        """
        self._capacidad_requerida = capacidad_requerida
        self._capacidad_disponible = capacidad_disponible
        
        mensaje_usuario = MensajesException.CAPACIDAD_INSUFICIENTE_USUARIO.format(
            requerida=capacidad_requerida,
            disponible=capacidad_disponible
        )
        
        mensaje_tecnico = MensajesException.CAPACIDAD_INSUFICIENTE_TECNICO.format(
            requerida=capacidad_requerida,
            disponible=capacidad_disponible
        )
        
        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_capacidad_requerida(self) -> int:
        """Obtiene capacidad requerida."""
        return self._capacidad_requerida

    def get_capacidad_disponible(self) -> int:
        """Obtiene capacidad disponible."""
        return self._capacidad_disponible
