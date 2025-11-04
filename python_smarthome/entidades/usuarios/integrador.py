"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: escena.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\escena.py
# ================================================================================

"""Entidad Escena - Representa una rutina o configuración guardada."""


class Escena:
    """
    Representa una escena que agrupa una serie de acciones.
    
    Attributes:
        _id_escena: ID de la escena
        _nombre: Nombre de la escena
        _descripcion: Descripción de la escena
    """

    def __init__(self, id_escena: int, nombre: str, descripcion: str):
        self._id_escena = id_escena
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id_escena(self) -> int:
        return self._id_escena

    def get_nombre(self) -> str:
        return self._nombre

    def get_descripcion(self) -> str:
        return self._descripcion


# ================================================================================
# ARCHIVO 3/4: nivel_acceso.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\nivel_acceso.py
# ================================================================================

"""Enum NivelAcceso - Define los niveles de permiso en el sistema."""

from enum import Enum


class NivelAcceso(Enum):
    """
    Enumeración para los niveles de acceso de usuario.
    """
    INVITADO = 1
    FAMILIAR = 2
    PROPIETARIO = 3
    ADMIN = 4
    SUPER = 5


# ================================================================================
# ARCHIVO 4/4: usuario.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\usuario.py
# ================================================================================

"""Entidad Usuario - Representa un usuario del sistema."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.usuarios.escena import Escena
    from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso


class Usuario:
    """
    Representa un usuario del sistema con su nivel de acceso y escenas.
    
    Attributes:
        _id_usuario: ID del usuario
        _nombre: Nombre del usuario
        _nivel_acceso: Nivel de acceso del usuario
        _escenas: Lista de escenas asignadas al usuario
    """

    def __init__(self, id_usuario: int, nombre: str, nivel_acceso: 'NivelAcceso', escenas: List['Escena']):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._nivel_acceso = nivel_acceso
        self._escenas = escenas

    def get_id_usuario(self) -> int:
        return self._id_usuario

    def get_nombre(self) -> str:
        return self._nombre

    def get_nivel_acceso(self) -> 'NivelAcceso':
        return self._nivel_acceso

    def get_escenas(self) -> List['Escena']:
        return self._escenas.copy()  # Defensive copy


