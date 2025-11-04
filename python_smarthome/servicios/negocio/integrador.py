"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: casa_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\casa_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: grupo_dispositivos.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\grupo_dispositivos.py
# ================================================================================

"""Contenedor genérico para agrupar dispositivos."""

from typing import Generic, List, Type, TypeVar

T = TypeVar('T')


class GrupoDispositivos(Generic[T]):
    """
    Clase genérica para agrupar dispositivos de un mismo tipo.
    """

    def __init__(self, tipo: Type[T], dispositivos: List[T]):
        self._tipo = tipo
        self._dispositivos = dispositivos

    def mostrar_contenido_grupo(self) -> None:
        """Muestra el contenido del grupo."""
        print(f"\n--- GRUPO DE DISPOSITIVOS: {self._tipo.__name__} ---")
        print(f"Cantidad: {len(self._dispositivos)}")
        for dispositivo in self._dispositivos:
            print(f"  - ID: {dispositivo.get_id_dispositivo()}")
        print("---------------------------------")


# ================================================================================
# ARCHIVO 4/4: modo_sistema.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\modo_sistema.py
# ================================================================================

"""Enum para los modos del sistema."""

from enum import Enum


class ModoSistema(Enum):
    """
    Enumeración para los diferentes modos del sistema.
    """
    NOCHE = "noche"
    VACACIONES = "vacaciones"
    FIESTA = "fiesta"
    CINE = "cine"


