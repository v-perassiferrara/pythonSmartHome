from python_smarthome.servicios.negocio.casa_service import CasaService as CasaNegocioService
from python_smarthome.servicios.negocio.grupo_dispositivos import GrupoDispositivos
from python_smarthome.entidades.espacios.casa import Casa
from python_smarthome.entidades.espacios.habitacion import Habitacion
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato
from datetime import date

def test_casa_negocio_service():
    # Setup
    casa = Casa("Calle Falsa 789", 300.0, "Carlos Gomez")
    habitacion1 = Habitacion("Living")
    habitacion1.agregar_dispositivo(LuzInteligente())
    habitacion1.agregar_dispositivo(LuzInteligente())
    habitacion2 = Habitacion("Dormitorio")
    habitacion2.agregar_dispositivo(Termostato())
    casa.set_habitaciones([habitacion1, habitacion2])
    config = ConfiguracionCasa(3, casa, date.today(), "Carlos Gomez")

    service = CasaNegocioService()
    service.add_casa(config)

    # Test agrupar_por_tipo
    grupo_luces = service.agrupar_por_tipo(LuzInteligente)
    assert isinstance(grupo_luces, GrupoDispositivos)
    # Test mostrar_contenido_grupo (solo que no falle)
    grupo_luces.mostrar_contenido_grupo()

    grupo_termostatos = service.agrupar_por_tipo(Termostato)
    assert isinstance(grupo_termostatos, GrupoDispositivos)
    grupo_termostatos.mostrar_contenido_grupo()
