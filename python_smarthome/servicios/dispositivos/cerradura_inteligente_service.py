"""Servicio para gestionar cerraduras inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CerraduraInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre cerraduras inteligentes.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Muestra datos de una cerradura inteligente.
        
        Args:
            cerradura: Cerradura a mostrar
        """
        super().mostrar_datos(cerradura)  # Datos comunes (ID, estado, tipo)
        print(f"Batería: {cerradura.get_bateria()}%")
        print(f"Estado: {'bloqueada' if cerradura.is_bloqueada() else 'desbloqueada'}")

    def bloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Bloquea la cerradura.
        
        Args:
            cerradura: Cerradura a bloquear
        """
        cerradura.bloquear()

    def desbloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Desbloquea la cerradura.
        
        Args:
            cerradura: Cerradura a desbloquear
        """
        cerradura.desbloquear()