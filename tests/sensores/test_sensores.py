import time
from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
from python_smarthome.sensores.sensor_apertura_task import SensorAperturaTask
from python_smarthome.patrones.observer.observer import Observer

class MockObserver(Observer):
    def __init__(self):
        self.evento_recibido = None

    def actualizar(self, evento):
        self.evento_recibido = evento

def test_sensor_movimiento():
    sensor = SensorMovimientoTask()
    observer = MockObserver()
    sensor.agregar_observador(observer)

    sensor.start()
    time.sleep(0.1) # Dar tiempo al thread para que se ejecute
    sensor.detener()
    sensor.join()

    assert observer.evento_recibido is not None

def test_sensor_temperatura():
    sensor = SensorTemperaturaTask()
    observer = MockObserver()
    sensor.agregar_observador(observer)

    sensor.start()
    time.sleep(0.1)
    sensor.detener()
    sensor.join()

    assert observer.evento_recibido is not None

def test_sensor_apertura():
    sensor = SensorAperturaTask()
    observer = MockObserver()
    sensor.agregar_observador(observer)

    sensor.start()
    time.sleep(0.1)
    sensor.detener()
    sensor.join()

    assert observer.evento_recibido is not None
