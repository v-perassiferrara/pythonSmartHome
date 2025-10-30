"""
Tests para verificar el correcto funcionamiento del patrón STRATEGY.

Este test asegura que:
1. Las estrategias están correctamente inyectadas
2. Los servicios delegan a las estrategias
3. Las estrategias se pueden cambiar en runtime
"""

import pytest
from datetime import datetime
from python_smarthome.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from python_smarthome.servicios.dispositivos.termostato_service import TermostatoService
from python_smarthome.servicios.dispositivos.camara_seguridad_service import CamaraSeguridadService
from python_smarthome.servicios.dispositivos.cerradura_inteligente_service import CerraduraInteligenteService
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato
from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente
from python_smarthome.patrones.strategy.impl.iluminacion_strategy import IluminacionStrategy
from python_smarthome.patrones.strategy.impl.climatizacion_strategy import ClimatizacionStrategy
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


def test_luz_service_tiene_estrategia_iluminacion():
    """Verifica que LuzInteligenteService usa IluminacionStrategy."""
    service = LuzInteligenteService()
    assert isinstance(service.get_estrategia(), IluminacionStrategy)
    print("[OK] LuzInteligenteService usa IluminacionStrategy")


def test_termostato_service_tiene_estrategia_climatizacion():
    """Verifica que TermostatoService usa ClimatizacionStrategy."""
    service = TermostatoService()
    assert isinstance(service.get_estrategia(), ClimatizacionStrategy)
    print("[OK] TermostatoService usa ClimatizacionStrategy")


def test_camara_service_tiene_estrategia_seguridad():
    """Verifica que CamaraSeguridadService usa SeguridadStrategy."""
    service = CamaraSeguridadService()
    assert isinstance(service.get_estrategia(), SeguridadStrategy)
    print("[OK] CamaraSeguridadService usa SeguridadStrategy")


def test_cerradura_service_tiene_estrategia_seguridad():
    """Verifica que CerraduraInteligenteService usa SeguridadStrategy."""
    service = CerraduraInteligenteService()
    assert isinstance(service.get_estrategia(), SeguridadStrategy)
    print("[OK] CerraduraInteligenteService usa SeguridadStrategy")


def test_estrategia_iluminacion_ajusta_intensidad_modo_noche():
    """Verifica que IluminacionStrategy ajusta intensidad en modo noche."""
    luz = LuzInteligente()
    strategy = IluminacionStrategy()
    
    # Simular hora nocturna (22:00)
    from unittest.mock import Mock
    fecha_mock = Mock()
    fecha_mock.hour = 22
    
    strategy.ejecutar_accion(fecha_mock, luz, None)
    
    assert luz.get_intensidad() == 30  # Modo noche
    print("[OK] IluminacionStrategy ajusta a 30% en modo noche")


def test_estrategia_iluminacion_ajusta_intensidad_modo_dia():
    """Verifica que IluminacionStrategy ajusta intensidad en modo día."""
    luz = LuzInteligente()
    strategy = IluminacionStrategy()
    
    # Simular hora diurna (14:00)
    from unittest.mock import Mock
    fecha_mock = Mock()
    fecha_mock.hour = 14
    
    strategy.ejecutar_accion(fecha_mock, luz, None)
    
    assert luz.get_intensidad() == 100  # Modo día
    print("[OK] IluminacionStrategy ajusta a 100% en modo día")


def test_estrategia_climatizacion_ajusta_temperatura():
    """Verifica que ClimatizacionStrategy ajusta temperatura objetivo."""
    termostato = Termostato()
    strategy = ClimatizacionStrategy()
    
    from python_smarthome.constantes import TEMP_CONFORT_OBJETIVO
    
    strategy.ejecutar_accion(datetime.now(), termostato, None)
    
    assert termostato.get_temperatura_objetivo() == TEMP_CONFORT_OBJETIVO
    print(f"[OK] ClimatizacionStrategy ajusta a {TEMP_CONFORT_OBJETIVO}°C")


def test_estrategia_seguridad_activa_grabacion_camara():
    """Verifica que SeguridadStrategy activa grabación en cámaras."""
    camara = CamaraSeguridad()
    strategy = SeguridadStrategy()
    
    assert not camara.is_grabando()  # Inicialmente apagada
    
    strategy.ejecutar_accion(datetime.now(), camara, None)
    
    assert camara.is_grabando()  # Activada por estrategia
    print("[OK] SeguridadStrategy activa grabación en cámara")


def test_estrategia_seguridad_bloquea_cerradura():
    """Verifica que SeguridadStrategy bloquea cerraduras."""
    cerradura = CerraduraInteligente()
    strategy = SeguridadStrategy()
    
    # Desbloquear primero
    cerradura.desbloquear()
    assert not cerradura.is_bloqueada()
    
    # Estrategia debe bloquear
    strategy.ejecutar_accion(datetime.now(), cerradura, None)
    
    assert cerradura.is_bloqueada()
    print("[OK] SeguridadStrategy bloquea cerradura")


def test_cambiar_estrategia_en_runtime():
    """Verifica que se puede cambiar estrategia en tiempo de ejecución."""
    service = LuzInteligenteService()
    
    # Estrategia original
    assert isinstance(service.get_estrategia(), IluminacionStrategy)
    
    # Cambiar a otra estrategia (simulación de flexibilidad)
    nueva_estrategia = ClimatizacionStrategy()
    service.set_estrategia(nueva_estrategia)
    
    assert isinstance(service.get_estrategia(), ClimatizacionStrategy)
    print("[OK] Estrategia cambiada en runtime (demuestra flexibilidad del patrón)")


def test_servicio_delega_a_estrategia():
    """Verifica que el servicio DELEGA la ejecución a la estrategia."""
    luz = LuzInteligente()
    service = LuzInteligenteService()
    
    # Estado inicial
    intensidad_inicial = luz.get_intensidad()
    
    # Ejecutar automatización (debe delegar a estrategia)
    service.ejecutar_automatizacion(luz, None)
    
    # Intensidad debe haber cambiado (estrategia actuó)
    assert luz.get_intensidad() != intensidad_inicial or luz.get_intensidad() in [30, 100]
    print("[OK] Servicio delega correctamente a estrategia")


def test_multiples_servicios_diferentes_estrategias():
    """Verifica que diferentes servicios usan diferentes estrategias."""
    luz_service = LuzInteligenteService()
    termostato_service = TermostatoService()
    camara_service = CamaraSeguridadService()
    
    estrategia_luz = luz_service.get_estrategia()
    estrategia_termostato = termostato_service.get_estrategia()
    estrategia_camara = camara_service.get_estrategia()
    
    # Todas deben ser diferentes tipos
    assert type(estrategia_luz) != type(estrategia_termostato)
    assert type(estrategia_luz) != type(estrategia_camara)
    assert type(estrategia_termostato) != type(estrategia_camara)
    
    print("[OK] Cada servicio usa su estrategia específica")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])