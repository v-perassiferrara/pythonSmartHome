"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: sensor_apertura_task.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_apertura_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: sensor_movimiento_task.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_movimiento_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: sensor_temperatura_task.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_temperatura_task.py
# ================================================================================

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


