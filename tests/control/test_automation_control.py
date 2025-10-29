import time
import pytest
from unittest.mock import Mock
from python_smarthome.control.automation_control_task import AutomationControlTask
from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
from python_smarthome.entidades.espacios.habitacion import Habitacion
from python_smarthome.servicios.espacios.habitacion_service import HabitacionService

def test_automation_control_task():
    # Mocks
    sensor_movimiento = Mock(spec=SensorMovimientoTask)
    sensor_temperatura = Mock(spec=SensorTemperaturaTask)
    habitacion = Mock(spec=Habitacion)
    habitacion_service = Mock(spec=HabitacionService)

    # Instancia de la tarea
    task = AutomationControlTask(
        sensor_movimiento=sensor_movimiento,
        sensor_temperatura=sensor_temperatura,
        habitacion=habitacion,
        habitacion_service=habitacion_service
    )

    # Test de actualización de eventos
    task.actualizar(True) # Movimiento
    assert task._ultimo_movimiento is True

    task.actualizar(25.0) # Temperatura
    assert task._ultima_temperatura == 25.0

    # Test del método run y _evaluar_y_ejecutar
    task.start()
    time.sleep(0.1)
    task.detener()
    task.join()

    # Verificar que los métodos de habitacion_service fueron llamados
    # Esto es un poco más complejo y podría requerir más setup
    # Por ahora, nos aseguramos que el thread corre y se detiene
    assert not task.is_alive()
