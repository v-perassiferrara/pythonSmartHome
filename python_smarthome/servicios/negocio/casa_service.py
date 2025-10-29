"""Servicio de negocio para gestionar múltiples casas."""

from typing import Dict, List, Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo

from python_smarthome.servicios.negocio.grupo_dispositivos import GrupoDispositivos

T = TypeVar('T', bound='Dispositivo')


class CasaService:
    """
    Servicio de negocio para operaciones sobre múltiples casas.
    """

    def __init__(self):
        self._casas: Dict[str, 'ConfiguracionCasa'] = {}

    def add_casa(self, config: 'ConfiguracionCasa') -> None:
        """Agrega una casa al servicio."""
        direccion = config.get_casa().get_direccion()
        self._casas[direccion] = config

    def agrupar_por_tipo(self, tipo: Type[T]) -> GrupoDispositivos[T]:
        """
        Agrupa todos los dispositivos de un tipo específico de todas las casas.
        """
        dispositivos_agrupados: List[T] = []
        for config in self._casas.values():
            for habitacion in config.get_casa().get_habitaciones():
                for dispositivo in habitacion.get_dispositivos():
                    if isinstance(dispositivo, tipo):
                        dispositivos_agrupados.append(dispositivo)
        return GrupoDispositivos(tipo, dispositivos_agrupados)
