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
    
    Inyecta una estrategia de automatización (STRATEGY PATTERN).
    """

    def __init__(self, strategy: 'AutomationStrategy'):
        """
        Inicializa servicio con estrategia de automatización.
        
        Args:
            strategy: Estrategia de automatización a usar
        """
        self._estrategia_automation = strategy

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos comunes de un dispositivo.
        
        Args:
            dispositivo: Dispositivo a mostrar
        """
        tipo_dispositivo = type(dispositivo).__name__
        print(f"Dispositivo: {tipo_dispositivo}")
        print(f"ID: {dispositivo.get_id_dispositivo()}")
        print(f"Estado: {'encendido' if dispositivo.is_encendido() else 'apagado'}")

    def ejecutar_automatizacion(self, dispositivo: 'Dispositivo', evento: Any) -> None:
        """
        Delega la ejecución de la automatización a la estrategia (STRATEGY PATTERN).
        
        Este método demuestra el uso del patrón STRATEGY:
        - El servicio NO sabe cómo automatizar
        - Delega la decisión a la estrategia inyectada
        - Permite cambiar el algoritmo en tiempo de ejecución
        
        Args:
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        self._estrategia_automation.ejecutar_accion(datetime.now(), dispositivo, evento)

    def get_estrategia(self) -> 'AutomationStrategy':
        """
        Obtiene la estrategia actual (útil para testing).
        
        Returns:
            Estrategia de automatización
        """
        return self._estrategia_automation

    def set_estrategia(self, strategy: 'AutomationStrategy') -> None:
        """
        Cambia la estrategia en tiempo de ejecución (demuestra flexibilidad del patrón).
        
        Args:
            strategy: Nueva estrategia a usar
        """
        self._estrategia_automation = strategy