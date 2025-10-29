"""Entidad CamaraSeguridad - Dispositivo de vigilancia."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    RESOLUCION_INICIAL,
    DETECCION_MOVIMIENTO_INICIAL
)


class CamaraSeguridad(Dispositivo):
    """
    Cámara de seguridad con detección de movimiento.
    
    Attributes:
        _resolucion: Resolución de video (e.g., "1080p")
        _deteccion_movimiento: Estado de la detección de movimiento
        _grabacion: Estado de la grabación
    """

    def __init__(self):
        """Inicializa cámara con valores por defecto."""
        super().__init__()
        self._resolucion: str = RESOLUCION_INICIAL
        self._deteccion_movimiento: bool = DETECCION_MOVIMIENTO_INICIAL
        self._grabacion: bool = False

    def get_resolucion(self) -> str:
        """Obtiene la resolución de video."""
        return self._resolucion

    def set_resolucion(self, resolucion: str) -> None:
        """Establece la resolución de video."""
        self._resolucion = resolucion

    def is_deteccion_movimiento_activa(self) -> bool:
        """Verifica si la detección de movimiento está activa."""
        return self._deteccion_movimiento

    def set_deteccion_movimiento(self, activa: bool) -> None:
        """Activa o desactiva la detección de movimiento."""
        self._deteccion_movimiento = activa

    def is_grabando(self) -> bool:
        """Verifica si la cámara está grabando."""
        return self._grabacion

    def set_grabacion(self, grabando: bool) -> None:
        """Inicia o detiene la grabación."""
        self._grabacion = grabando
