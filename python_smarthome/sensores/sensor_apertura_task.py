"""Sensor de apertura - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import INTERVALO_SENSOR_APERTURA


class SensorAperturaTask(threading.Thread, Observable[bool]):
    """
    Sensor de apertura que detecta si una puerta o ventana está abierta.
    
    Thread daemon que notifica detecciones cada INTERVALO_SENSOR_APERTURA segundos.
    Implementa OBSERVER pattern como Observable[bool].
    """

    def __init__(self):
        """Inicializa sensor de apertura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de apertura iniciado")
        
        while not self._detenido.is_set():
            # Detectar apertura (aleatorio para simulación)
            apertura = self._detectar_apertura()
            
            # Notificar a observadores
            self.notificar_observadores(apertura)
            
            if apertura:
                print(f"[SENSOR] Apertura detectada: {apertura}")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_APERTURA)
        
        print("[SENSOR] Sensor de apertura detenido")

    def _detectar_apertura(self) -> bool:
        """
        Detecta apertura (simulación).
        
        Returns:
            True si hay apertura, False si no
        """
        return random.choice([True, False])

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()
