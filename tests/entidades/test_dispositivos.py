import pytest
from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato
from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente
from python_smarthome.constantes import *

def test_dispositivo_base():
    d = LuzInteligente() # Or any other concrete class
    assert d.get_id_dispositivo() > 0
    assert not d.is_encendido()
    d.set_encendido(True)
    assert d.is_encendido()

def test_luz_inteligente():
    luz = LuzInteligente()
    assert luz.get_intensidad() == INTENSIDAD_MAX
    assert luz.get_color_rgb() == COLOR_INICIAL

    luz.set_intensidad(50)
    assert luz.get_intensidad() == 50

    with pytest.raises(ValueError):
        luz.set_intensidad(-10)

    with pytest.raises(ValueError):
        luz.set_intensidad(110)

    luz.set_color_rgb((10, 20, 30))
    assert luz.get_color_rgb() == (10, 20, 30)

    with pytest.raises(ValueError):
        luz.set_color_rgb((-1, 20, 30))

def test_termostato():
    termostato = Termostato()
    assert termostato.get_temperatura_objetivo() == TEMP_OBJETIVO_INICIAL

    termostato.set_temperatura_objetivo(25)
    assert termostato.get_temperatura_objetivo() == 25

    with pytest.raises(ValueError):
        termostato.set_temperatura_objetivo(TEMP_MIN - 1)

    with pytest.raises(ValueError):
        termostato.set_temperatura_objetivo(TEMP_MAX + 1)

def test_camara_seguridad():
    camara = CamaraSeguridad()
    assert camara.get_resolucion() == RESOLUCION_INICIAL
    assert camara.is_deteccion_movimiento_activa() == DETECCION_MOVIMIENTO_INICIAL
    assert not camara.is_grabando()

    camara.set_resolucion("720p")
    assert camara.get_resolucion() == "720p"

    camara.set_deteccion_movimiento(False)
    assert not camara.is_deteccion_movimiento_activa()

    camara.set_grabacion(True)
    assert camara.is_grabando()

def test_cerradura_inteligente():
    cerradura = CerraduraInteligente()
    assert cerradura.is_bloqueada()
    assert cerradura.get_bateria() == BATERIA_INICIAL
    assert cerradura.get_metodo_acceso() == METODO_ACCESO_INICIAL

    cerradura.desbloquear()
    assert not cerradura.is_bloqueada()

    cerradura.bloquear()
    assert cerradura.is_bloqueada()

    cerradura.set_metodo_acceso("huella")
    assert cerradura.get_metodo_acceso() == "huella"
