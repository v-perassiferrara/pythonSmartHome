"""Servicio para gestionar luces inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.iluminacion_strategy import IluminacionStrategy


class LuzInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre luces inteligentes.
    
    Usa estrategia de iluminación para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de iluminación."""
        super().__init__(IluminacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, luz: 'LuzInteligente') -> None:
        """
        Muestra datos de una luz inteligente.
        
        Args:
            luz: Luz a mostrar
        """
        super().mostrar_datos(luz)  # Datos comunes (ID, estado, tipo)
        print(f"Intensidad: {luz.get_intensidad()}%")
        r, g, b = luz.get_color_rgb()
        print(f"Color RGB: ({r}, {g}, {b})")

    def encender(self, luz: 'LuzInteligente') -> None:
        """
        Enciende luz con intensidad máxima.
        
        Args:
            luz: Luz a encender
        """
        luz.set_encendido(True)
        luz.set_intensidad(100)

    def apagar(self, luz: 'LuzInteligente') -> None:
        """
        Apaga luz.
        
        Args:
            luz: Luz a apagar
        """
        luz.set_encendido(False)
        luz.set_intensidad(0)

    def ajustar_intensidad(self, luz: 'LuzInteligente', intensidad: int) -> None:
        """
        Ajusta intensidad de la luz.
        
        Args:
            luz: Luz a ajustar
            intensidad: Nueva intensidad (0-100%)
        """
        luz.set_intensidad(intensidad)

    def cambiar_color(self, luz: 'LuzInteligente', color: tuple) -> None:
        """
        Cambia color de la luz.
        
        Args:
            luz: Luz a ajustar
            color: Tupla RGB (R, G, B)
        """
        luz.set_color_rgb(color)