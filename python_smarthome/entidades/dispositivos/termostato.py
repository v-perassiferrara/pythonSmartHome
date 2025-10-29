"""Entidad Termostato - Dispositivo de climatización."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    TEMP_MIN,
    TEMP_MAX,
    TEMP_OBJETIVO_INICIAL
)


class Termostato(Dispositivo):
    """
    Termostato inteligente con control de temperatura.
    
    Attributes:
        _temperatura_objetivo: Temperatura deseada (°C)
    """

    def __init__(self):
        """Inicializa termostato con valores por defecto."""
        super().__init__()
        self._temperatura_objetivo: float = TEMP_OBJETIVO_INICIAL

    def get_temperatura_objetivo(self) -> float:
        """
        Obtiene temperatura objetivo.
        
        Returns:
            Temperatura objetivo (°C)
        """
        return self._temperatura_objetivo

    def set_temperatura_objetivo(self, temperatura: float) -> None:
        """
        Establece temperatura objetivo.
        
        Args:
            temperatura: Temperatura objetivo (°C)
            
        Raises:
            ValueError: Si temperatura fuera de rango
        """
        if not (TEMP_MIN <= temperatura <= TEMP_MAX):
            raise ValueError(
                f"Temperatura debe estar entre {TEMP_MIN} y {TEMP_MAX}"
            )
        self._temperatura_objetivo = temperatura
