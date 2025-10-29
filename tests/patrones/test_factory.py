import pytest
from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato
from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

def test_crear_luz():
    luz = DispositivoFactory.crear_dispositivo("LuzInteligente")
    assert isinstance(luz, LuzInteligente)

def test_crear_termostato():
    termostato = DispositivoFactory.crear_dispositivo("Termostato")
    assert isinstance(termostato, Termostato)

def test_crear_camara():
    camara = DispositivoFactory.crear_dispositivo("CamaraSeguridad")
    assert isinstance(camara, CamaraSeguridad)

def test_crear_cerradura():
    cerradura = DispositivoFactory.crear_dispositivo("CerraduraInteligente")
    assert isinstance(cerradura, CerraduraInteligente)

def test_crear_dispositivo_desconocido():
    with pytest.raises(ValueError):
        DispositivoFactory.crear_dispositivo("TipoInexistente")
