from python_smarthome.entidades.espacios.casa import Casa
from python_smarthome.entidades.espacios.habitacion import Habitacion
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from datetime import date

def test_casa():
    casa = Casa(direccion="Calle Falsa 123", superficie=150.0, propietario="Juan Perez")
    assert casa.get_direccion() == "Calle Falsa 123"
    assert casa.get_superficie() == 150.0
    assert casa.get_propietario() == "Juan Perez"
    assert casa.get_habitaciones() == []
    assert casa.get_usuarios() == []

    habitacion1 = Habitacion(nombre="Living")
    habitacion2 = Habitacion(nombre="Cocina")
    casa.set_habitaciones([habitacion1, habitacion2])
    assert len(casa.get_habitaciones()) == 2

def test_habitacion():
    habitacion = Habitacion(nombre="Dormitorio")
    assert habitacion.get_nombre() == "Dormitorio"
    assert habitacion.get_dispositivos() == []

    luz = LuzInteligente()
    habitacion.agregar_dispositivo(luz)
    assert len(habitacion.get_dispositivos()) == 1

    luces = [LuzInteligente(), LuzInteligente()]
    habitacion.agregar_dispositivos(luces)
    assert len(habitacion.get_dispositivos()) == 3

def test_configuracion_casa():
    casa = Casa(direccion="Calle Falsa 123", superficie=150.0, propietario="Juan Perez")
    config = ConfiguracionCasa(id_config=1, casa=casa, fecha_instalacion=date.today(), propietario="Juan Perez")

    assert config.get_id_config() == 1
    assert config.get_casa() == casa
    assert config.get_fecha_instalacion() == date.today()
    assert config.get_propietario() == "Juan Perez"
