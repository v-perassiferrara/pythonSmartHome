"""Estrategia de seguridad - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class SeguridadStrategy(AutomationStrategy):
    """
    Estrategia de automatización para dispositivos de seguridad.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: Any,
        evento: Any
    ) -> None:
        """
        Ejecuta acción de seguridad.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Dispositivo a controlar
            evento: Evento disparador (ignorado)
        """
        # Para cámaras, enciende la grabación
        if hasattr(dispositivo, 'set_grabacion'):
            dispositivo.set_grabacion(True)
        
        # Para cerraduras, las bloquea
        if hasattr(dispositivo, 'bloquear'):
            dispositivo.bloquear()
