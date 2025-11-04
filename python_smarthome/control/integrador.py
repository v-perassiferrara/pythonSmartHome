"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\control
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\control\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: automation_control_task.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\control\automation_control_task.py
# ================================================================================

"""Controlador de automatización - Thread + OBSERVER pattern."""

import threading
import time
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
    from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
    from python_smarthome.entidades.espacios.habitacion import Habitacion
    from python_smarthome.servicios.espacios.habitacion_service import HabitacionService

from python_smarthome.patrones.observer.observer import Observer
from python_smarthome.constantes import (
    INTERVALO_CONTROL_AUTOMATION,
    HORA_INICIO_NOCHE,
    HORA_FIN_NOCHE,
    TEMP_CONFORT_MIN,
    TEMP_CONFORT_MAX
)


class AutomationControlTask(threading.Thread, Observer):
    """
    Controlador de automatización.
    
    Thread daemon que observa sensores y ejecuta acciones automáticas.
    Implementa OBSERVER pattern (observa movimiento y temperatura).
    """

    def __init__(
        self,
        sensor_movimiento: 'SensorMovimientoTask',
        sensor_temperatura: 'SensorTemperaturaTask',
        habitacion: 'Habitacion',
        habitacion_service: 'HabitacionService'
    ):
        """
        Inicializa controlador.
        
        Args:
            sensor_movimiento: Sensor de movimiento (Observable[bool])
            sensor_temperatura: Sensor de temperatura (Observable[float])
            habitacion: Habitación a controlar
            habitacion_service: Servicio de habitación
        """
        threading.Thread.__init__(self, daemon=True)
        
        # Inyección de dependencias
        self._sensor_movimiento = sensor_movimiento
        self._sensor_temperatura = sensor_temperatura
        self._habitacion = habitacion
        self._habitacion_service = habitacion_service
        
        # Estado interno
        self._ultimo_movimiento: bool = False
        self._ultima_temperatura: float = 22.0
        self._detenido = threading.Event()
        
        # Suscribirse a sensores (OBSERVER)
        self._sensor_movimiento.agregar_observador(self)
        self._sensor_temperatura.agregar_observador(self)

    def actualizar(self, evento: Any) -> None:
        """
        Recibe notificaciones de sensores (OBSERVER).
        
        Args:
            evento: bool (movimiento) o float (temperatura)
        """
        if isinstance(evento, bool):
            # Movimiento
            self._ultimo_movimiento = evento
        elif isinstance(evento, float):
            # Temperatura
            self._ultima_temperatura = evento

    def run(self) -> None:
        """Loop principal del controlador."""
        print("[CONTROL] Controlador de automatizacion iniciado")
        
        while not self._detenido.is_set():
            self._evaluar_y_ejecutar()
            time.sleep(INTERVALO_CONTROL_AUTOMATION)
        
        print("[CONTROL] Controlador de automatizacion detenido")

    def _evaluar_y_ejecutar(self) -> None:
        """Evalúa condiciones y ejecuta acciones."""
        hora_actual = datetime.now().hour
        es_modo_noche = (HORA_INICIO_NOCHE <= hora_actual) or (hora_actual <= HORA_FIN_NOCHE)
        
        # Condición 1: Movimiento detectado en modo noche
        if self._ultimo_movimiento and es_modo_noche:
            print(f"[CONTROL] Movimiento en modo noche - Ajustando luces")
            self._habitacion_service.ajustar_luces_modo_noche(self._habitacion)
        
        # Condición 2: Temperatura fuera de rango confort
        if not (TEMP_CONFORT_MIN <= self._ultima_temperatura <= TEMP_CONFORT_MAX):
            print(f"[CONTROL] Temp fuera de confort ({self._ultima_temperatura}C) - Ajustando")
            self._habitacion_service.ajustar_climatizacion(self._habitacion)

    def detener(self) -> None:
        """Detiene el controlador de forma graceful."""
        self._detenido.set()

