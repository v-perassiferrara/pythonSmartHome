"""Sensor de movimiento - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import INTERVALO_SENSOR_MOVIMIENTO


class SensorMovimientoTask(threading.Thread, Observable[bool]):
    """
    Sensor de movimiento que detecta presencia.
    
    Thread daemon que notifica detecciones cada INTERVALO_SENSOR_MOVIMIENTO segundos.
    Implementa OBSERVER pattern como Observable[bool].
    """

    def __init__(self):
        """Inicializa sensor de movimiento."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de movimiento iniciado")
        
        while not self._detenido.is_set():
            # Detectar movimiento (aleatorio para simulación)
            movimiento = self._detectar_movimiento()
            
            # Notificar a observadores
            self.notificar_observadores(movimiento)
            
            if movimiento:
                print(f"[SENSOR] Movimiento detectado: {movimiento}")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_MOVIMIENTO)
        
        print("[SENSOR] Sensor de movimiento detenido")

    def _detectar_movimiento(self) -> bool:
        """
        Detecta movimiento (simulación).
        
        Returns:
            True si hay movimiento, False si no
        """
        return random.choice([True, False])

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()
