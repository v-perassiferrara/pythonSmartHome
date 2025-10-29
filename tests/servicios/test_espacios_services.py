import os
import pytest
from datetime import date
from python_smarthome.servicios.espacios.casa_service import CasaService
from python_smarthome.servicios.espacios.habitacion_service import HabitacionService
from python_smarthome.servicios.espacios.configuracion_casa_service import ConfiguracionCasaService
from python_smarthome.entidades.espacios.casa import Casa
from python_smarthome.entidades.espacios.habitacion import Habitacion
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
from python_smarthome.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException
from python_smarthome.constantes import MAX_DISPOSITIVOS_HABITACION, DIRECTORIO_DATA, EXTENSION_DATA

def test_casa_service():
    casa_service = CasaService()
    casa = casa_service.crear_casa_con_habitaciones(
        direccion="Calle Falsa 123",
        superficie=150.0,
        propietario="Juan Perez",
        nombres_habitaciones=["Living", "Cocina"]
    )
    assert isinstance(casa, Casa)
    assert len(casa.get_habitaciones()) == 2

def test_habitacion_service():
    habitacion_service = HabitacionService()
    habitacion = Habitacion("Dormitorio")

    habitacion_service.instalar(habitacion, "LuzInteligente", 2)
    assert len(habitacion.get_dispositivos()) == 2

    with pytest.raises(CapacidadInsuficienteException):
        habitacion_service.instalar(habitacion, "Termostato", MAX_DISPOSITIVOS_HABITACION)


def test_configuracion_casa_service():
    config_service = ConfiguracionCasaService()
    casa = Casa(direccion="Calle Falsa 456", superficie=200.0, propietario="Maria Garcia")
    config = ConfiguracionCasa(id_config=2, casa=casa, fecha_instalacion=date.today(), propietario="Maria Garcia")

    # Test persistencia
    config_service.persistir(config)
    nombre_archivo = f"Maria Garcia{EXTENSION_DATA}"
    ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)
    assert os.path.exists(ruta_archivo)

    # Test lectura
    config_leida = config_service.leer_configuracion("Maria Garcia")
    assert isinstance(config_leida, ConfiguracionCasa)
    assert config_leida.get_propietario() == "Maria Garcia"

    # Test mostrar datos (solo verificamos que no lance error)
    try:
        config_service.mostrar_datos(config_leida)
    except Exception as e:
        pytest.fail(f"mostrar_datos no deberia lanzar error: {e}")

    # Limpieza
    os.remove(ruta_archivo)
