"""Entidad ConfiguracionCasa - Agrupa toda la configuración de una casa."""

from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.casa import Casa


class ConfiguracionCasa:
    """
    Agrupa la configuración completa de una casa inteligente.
    
    Attributes:
        _id_config: ID de la configuración
        _casa: La casa configurada
        _fecha_instalacion: Fecha de instalación
        _propietario: Propietario de la configuración
    """

    def __init__(self, id_config: int, casa: 'Casa', fecha_instalacion: date, propietario: str):
        self._id_config = id_config
        self._casa = casa
        self._fecha_instalacion = fecha_instalacion
        self._propietario = propietario

    def get_id_config(self) -> int:
        return self._id_config

    def get_casa(self) -> 'Casa':
        return self._casa

    def get_fecha_instalacion(self) -> date:
        return self._fecha_instalacion

    def get_propietario(self) -> str:
        return self._propietario
