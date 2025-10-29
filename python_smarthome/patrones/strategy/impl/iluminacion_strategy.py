"""Estrategia de iluminación - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import (
    HORA_INICIO_NOCHE,
    HORA_FIN_NOCHE
)


class IluminacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para luces inteligentes.
    
    Ajusta intensidad según hora del día.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'LuzInteligente',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de iluminación.
        
        Modo noche (20:00-07:00): Intensidad 30%
        Modo día: Intensidad 100%
        
        Args:
            fecha: Fecha/hora actual
            dispositivo: Luz a controlar
            evento: Evento disparador (ignorado)
        """
        hora = fecha.hour
        
        # Verificar si es modo noche
        es_modo_noche = (HORA_INICIO_NOCHE <= hora) or (hora <= HORA_FIN_NOCHE)
        
        if es_modo_noche:
            dispositivo.set_intensidad(30)  # 30% en modo noche
        else:
            dispositivo.set_intensidad(100)  # 100% de día
