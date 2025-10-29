from python_smarthome.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from python_smarthome.servicios.dispositivos.termostato_service import TermostatoService
from python_smarthome.servicios.dispositivos.camara_seguridad_service import CamaraSeguridadService
from python_smarthome.servicios.dispositivos.cerradura_inteligente_service import CerraduraInteligenteService
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato
from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

def test_luz_inteligente_service():
    service = LuzInteligenteService()
    luz = LuzInteligente()

    service.encender(luz)
    assert luz.is_encendido()
    assert luz.get_intensidad() == 100

    service.apagar(luz)
    assert not luz.is_encendido()
    assert luz.get_intensidad() == 0

    service.ajustar_intensidad(luz, 50)
    assert luz.get_intensidad() == 50

    service.cambiar_color(luz, (10, 20, 30))
    assert luz.get_color_rgb() == (10, 20, 30)

    # Test mostrar_datos (solo que no falle)
    service.mostrar_datos(luz)

def test_termostato_service():
    service = TermostatoService()
    termostato = Termostato()

    service.encender(termostato)
    assert termostato.is_encendido()

    service.apagar(termostato)
    assert not termostato.is_encendido()

    # Test mostrar_datos (solo que no falle)
    service.mostrar_datos(termostato)

def test_camara_seguridad_service():
    service = CamaraSeguridadService()
    camara = CamaraSeguridad()

    service.encender(camara)
    assert camara.is_encendido()
    assert camara.is_grabando()

    service.apagar(camara)
    assert not camara.is_encendido()
    assert not camara.is_grabando()

    # Test mostrar_datos (solo que no falle)
    service.mostrar_datos(camara)

def test_cerradura_inteligente_service():
    service = CerraduraInteligenteService()
    cerradura = CerraduraInteligente()

    service.desbloquear(cerradura)
    assert not cerradura.is_bloqueada()

    service.bloquear(cerradura)
    assert cerradura.is_bloqueada()

    # Test mostrar_datos (solo que no falle)
    service.mostrar_datos(cerradura)
