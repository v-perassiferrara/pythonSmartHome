"""Servicio base para todos los dispositivos."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
    from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class DispositivoService(ABC):
    """
    Clase base abstracta para servicios de dispositivos.
    
    Injecta una estrategia de automatización.
    """

    def __init__(self, strategy: 'AutomationStrategy'):
        self._strategy = strategy

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos comunes de un dispositivo.
        
        Args:
            dispositivo: Dispositivo a mostrar
        """
        print(f"ID: {dispositivo.get_id_dispositivo()}")
        print(f"Estado: {'encendido' if dispositivo.is_encendido() else 'apagado'}")

    def ejecutar_automatizacion(self, dispositivo: 'Dispositivo', evento: Any) -> None:
        """
        Delega la ejecución de la automatización a la estrategia.
        
        Args:
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        self._strategy.ejecutar_accion(datetime.now(), dispositivo, evento)
