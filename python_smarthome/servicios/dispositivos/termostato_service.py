"""Servicio para gestionar termostatos."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.climatizacion_strategy import ClimatizacionStrategy


class TermostatoService(DispositivoService):
    """
    Servicio para operaciones sobre termostatos.
    
    Usa estrategia de climatización para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de climatización."""
        super().__init__(ClimatizacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, termostato: 'Termostato') -> None:
        """
        Muestra datos de un termostato.
        
        Args:
            termostato: Termostato a mostrar
        """
        super().mostrar_datos(termostato)  # Datos comunes (ID, estado, tipo)
        print(f"Temperatura Objetivo: {termostato.get_temperatura_objetivo()}°C")

    def encender(self, termostato: 'Termostato') -> None:
        """
        Enciende el termostato.
        
        Args:
            termostato: Termostato a encender
        """
        termostato.set_encendido(True)

    def apagar(self, termostato: 'Termostato') -> None:
        """
        Apaga el termostato.
        
        Args:
            termostato: Termostato a apagar
        """
        termostato.set_encendido(False)