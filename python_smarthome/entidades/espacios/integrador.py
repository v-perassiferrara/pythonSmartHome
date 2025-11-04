"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: casa.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\casa.py
# ================================================================================

"""Entidad Casa - Representa una propiedad."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion
    from python_smarthome.entidades.usuarios.usuario import Usuario


class Casa:
    """
    Representa una casa con dirección, superficie y habitaciones.
    
    Attributes:
        _direccion: Dirección de la casa
        _superficie: Superficie en m²
        _propietario: Nombre del propietario
        _habitaciones: Lista de habitaciones en la casa
        _usuarios: Lista de usuarios autorizados
    """

    def __init__(self, direccion: str, superficie: float, propietario: str):
        self._direccion = direccion
        self._superficie = superficie
        self._propietario = propietario
        self._habitaciones: List['Habitacion'] = []
        self._usuarios: List['Usuario'] = []

    def get_direccion(self) -> str:
        return self._direccion

    def get_superficie(self) -> float:
        return self._superficie

    def get_propietario(self) -> str:
        return self._propietario

    def get_habitaciones(self) -> List['Habitacion']:
        return self._habitaciones.copy()  # Defensive copy

    def set_habitaciones(self, habitaciones: List['Habitacion']) -> None:
        self._habitaciones = habitaciones

    def get_usuarios(self) -> List['Usuario']:
        return self._usuarios.copy()  # Defensive copy

    def set_usuarios(self, usuarios: List['Usuario']) -> None:
        self._usuarios = usuarios


# ================================================================================
# ARCHIVO 3/4: configuracion_casa.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\configuracion_casa.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: habitacion.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\habitacion.py
# ================================================================================

"""Entidad Habitacion - Representa un espacio dentro de una casa."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class Habitacion:
    """
    Representa una habitación con un nombre y dispositivos.
    
    Attributes:
        _nombre: Nombre de la habitación
        _dispositivos: Lista de dispositivos en la habitación
    """

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List['Dispositivo'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List['Dispositivo']:
        return self._dispositivos.copy()  # Defensive copy

    def agregar_dispositivo(self, dispositivo: 'Dispositivo') -> None:
        self._dispositivos.append(dispositivo)

    def agregar_dispositivos(self, dispositivos: List['Dispositivo']) -> None:
        self._dispositivos.extend(dispositivos)


