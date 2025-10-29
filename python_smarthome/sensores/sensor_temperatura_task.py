"""Sensor de temperatura - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_AMBIENTE_MIN,
    TEMP_AMBIENTE_MAX
)


class SensorTemperaturaTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura que mide la temperatura ambiente.
    
    Thread daemon que notifica mediciones cada INTERVALO_SENSOR_TEMPERATURA segundos.
    Implementa OBSERVER pattern como Observable[float].
    """

    def __init__(self):
        """Inicializa sensor de temperatura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de temperatura iniciado")
        
        while not self._detenido.is_set():
            # Medir temperatura (aleatorio para simulación)
            temperatura = self._medir_temperatura()
            
            # Notificar a observadores
            self.notificar_observadores(temperatura)
            
            print(f"[SENSOR] Temperatura medida: {temperatura:.2f}°C")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
        
        print("[SENSOR] Sensor de temperatura detenido")

    def _medir_temperatura(self) -> float:
        """
        Mide la temperatura (simulación).
        
        Returns:
            Temperatura en °C
        """
        return random.uniform(TEMP_AMBIENTE_MIN, TEMP_AMBIENTE_MAX)

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()
