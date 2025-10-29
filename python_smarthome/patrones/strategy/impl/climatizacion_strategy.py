"""Estrategia de climatización - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import TEMP_CONFORT_OBJETIVO


class ClimatizacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para termostatos.
    
    Ajusta la temperatura a un valor de confort.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Termostato',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de climatización.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Termostato a controlar
            evento: Evento disparador (ignorado)
        """
        dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)
