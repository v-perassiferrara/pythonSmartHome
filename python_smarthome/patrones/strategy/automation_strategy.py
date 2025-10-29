"""Interfaz Strategy para automatización - STRATEGY pattern."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class AutomationStrategy(ABC):
    """
    Interfaz para estrategias de automatización.
    
    Implementa STRATEGY pattern.
    """

    @abstractmethod
    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Dispositivo', 
        evento: Any
    ) -> None:
        """
        Ejecuta acción de automatización.
        
        Args:
            fecha: Fecha/hora actual
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        pass
