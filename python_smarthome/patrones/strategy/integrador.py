"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: automation_strategy.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\automation_strategy.py
# ================================================================================

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


