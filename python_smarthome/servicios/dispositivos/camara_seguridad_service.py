"""Servicio para gestionar cámaras de seguridad."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CamaraSeguridadService(DispositivoService):
    """
    Servicio para operaciones sobre cámaras de seguridad.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, camara: 'CamaraSeguridad') -> None:
        """
        Muestra datos de una cámara de seguridad.
        
        Args:
            camara: Cámara a mostrar
        """
        super().mostrar_datos(camara)
        print(f"Resolución: {camara.get_resolucion()}")
        print(f"Detección de Movimiento: {'activa' if camara.is_deteccion_movimiento_activa() else 'inactiva'}")
        print(f"Grabando: {'sí' if camara.is_grabando() else 'no'}")

    def encender(self, camara: 'CamaraSeguridad') -> None:
        """
        Enciende la cámara y la grabación.
        
        Args:
            camara: Cámara a encender
        """
        camara.set_encendido(True)
        camara.set_grabacion(True)

    def apagar(self, camara: 'CamaraSeguridad') -> None:
        """
        Apaga la cámara y la grabación.
        
        Args:
            camara: Cámara a apagar
        """
        camara.set_encendido(False)
        camara.set_grabacion(False)
