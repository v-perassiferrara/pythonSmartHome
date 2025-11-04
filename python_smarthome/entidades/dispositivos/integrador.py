"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: camara_seguridad.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\camara_seguridad.py
# ================================================================================

"""Entidad CamaraSeguridad - Dispositivo de vigilancia."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    RESOLUCION_INICIAL,
    DETECCION_MOVIMIENTO_INICIAL
)


class CamaraSeguridad(Dispositivo):
    """
    Cámara de seguridad con detección de movimiento.
    
    Attributes:
        _resolucion: Resolución de video (e.g., "1080p")
        _deteccion_movimiento: Estado de la detección de movimiento
        _grabacion: Estado de la grabación
    """

    def __init__(self):
        """Inicializa cámara con valores por defecto."""
        super().__init__()
        self._resolucion: str = RESOLUCION_INICIAL
        self._deteccion_movimiento: bool = DETECCION_MOVIMIENTO_INICIAL
        self._grabacion: bool = False

    def get_resolucion(self) -> str:
        """Obtiene la resolución de video."""
        return self._resolucion

    def set_resolucion(self, resolucion: str) -> None:
        """Establece la resolución de video."""
        self._resolucion = resolucion

    def is_deteccion_movimiento_activa(self) -> bool:
        """Verifica si la detección de movimiento está activa."""
        return self._deteccion_movimiento

    def set_deteccion_movimiento(self, activa: bool) -> None:
        """Activa o desactiva la detección de movimiento."""
        self._deteccion_movimiento = activa

    def is_grabando(self) -> bool:
        """Verifica si la cámara está grabando."""
        return self._grabacion

    def set_grabacion(self, grabando: bool) -> None:
        """Inicia o detiene la grabación."""
        self._grabacion = grabando


# ================================================================================
# ARCHIVO 3/6: cerradura_inteligente.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\cerradura_inteligente.py
# ================================================================================

"""Entidad CerraduraInteligente - Dispositivo de acceso."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    BATERIA_INICIAL,
    METODO_ACCESO_INICIAL
)


class CerraduraInteligente(Dispositivo):
    """
    Cerradura inteligente con control de acceso y batería.
    
    Attributes:
        _bloqueada: Estado de la cerradura (bloqueada/desbloqueada)
        _bateria: Nivel de batería (0-100%)
        _metodo_acceso: Método de acceso actual
    """

    def __init__(self):
        """Inicializa cerradura con valores por defecto."""
        super().__init__()
        self._bloqueada: bool = True
        self._bateria: int = BATERIA_INICIAL
        self._metodo_acceso: str = METODO_ACCESO_INICIAL

    def is_bloqueada(self) -> bool:
        """Verifica si la cerradura está bloqueada."""
        return self._bloqueada

    def bloquear(self) -> None:
        """Bloquea la cerradura."""
        self._bloqueada = True

    def desbloquear(self) -> None:
        """Desbloquea la cerradura."""
        self._bloqueada = False

    def get_bateria(self) -> int:
        """Obtiene el nivel de batería."""
        return self._bateria

    def get_metodo_acceso(self) -> str:
        """Obtiene el método de acceso."""
        return self._metodo_acceso

    def set_metodo_acceso(self, metodo: str) -> None:
        """Establece el método de acceso."""
        self._metodo_acceso = metodo


# ================================================================================
# ARCHIVO 4/6: dispositivo.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\dispositivo.py
# ================================================================================

"""Interfaz base para todos los dispositivos."""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Dispositivo(ABC):
    """
    Clase base abstracta para dispositivos IoT.
    
    Attributes:
        _id_dispositivo: ID único del dispositivo
        _encendido: Estado on/off del dispositivo
    """

    _contador_id: int = 0

    def __init__(self):
        """Inicializa dispositivo con ID único."""
        Dispositivo._contador_id += 1
        self._id_dispositivo: int = Dispositivo._contador_id
        self._encendido: bool = False

    def get_id_dispositivo(self) -> int:
        """
        Obtiene ID del dispositivo.
        
        Returns:
            ID único
        """
        return self._id_dispositivo

    def is_encendido(self) -> bool:
        """
        Verifica si dispositivo está encendido.
        
        Returns:
            True si está encendido
        """
        return self._encendido

    def set_encendido(self, encendido: bool) -> None:
        """
        Establece estado del dispositivo.
        
        Args:
            encendido: True para encender, False para apagar
        """
        self._encendido = encendido


# ================================================================================
# ARCHIVO 5/6: luz_inteligente.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\luz_inteligente.py
# ================================================================================

"""Entidad LuzInteligente - Dispositivo de iluminación."""

from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    INTENSIDAD_MIN,
    INTENSIDAD_MAX,
    COLOR_INICIAL
)


class LuzInteligente(Dispositivo):
    """
    Luz inteligente con control de intensidad y color.
    
    Attributes:
        _intensidad: Intensidad de la luz (0-100%)
        _color_rgb: Color RGB como tupla (R, G, B)
    """

    def __init__(self):
        """Inicializa luz inteligente con valores por defecto."""
        super().__init__()
        self._intensidad: int = INTENSIDAD_MAX
        self._color_rgb: Tuple[int, int, int] = COLOR_INICIAL

    def get_intensidad(self) -> int:
        """
        Obtiene intensidad de la luz.
        
        Returns:
            Intensidad (0-100%)
        """
        return self._intensidad

    def set_intensidad(self, intensidad: int) -> None:
        """
        Establece intensidad de la luz.
        
        Args:
            intensidad: Intensidad (0-100%)
            
        Raises:
            ValueError: Si intensidad fuera de rango
        """
        if not (INTENSIDAD_MIN <= intensidad <= INTENSIDAD_MAX):
            raise ValueError(
                f"Intensidad debe estar entre {INTENSIDAD_MIN} y {INTENSIDAD_MAX}"
            )
        self._intensidad = intensidad

    def get_color_rgb(self) -> Tuple[int, int, int]:
        """
        Obtiene color RGB.
        
        Returns:
            Tupla (R, G, B)
        """
        return self._color_rgb

    def set_color_rgb(self, color: Tuple[int, int, int]) -> None:
        """
        Establece color RGB.
        
        Args:
            color: Tupla (R, G, B) donde cada componente es 0-255
            
        Raises:
            ValueError: Si valores fuera de rango
        """
        r, g, b = color
        if not all(0 <= c <= 255 for c in [r, g, b]):
            raise ValueError("RGB components must be between 0 and 255")
        self._color_rgb = color


# ================================================================================
# ARCHIVO 6/6: termostato.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\termostato.py
# ================================================================================

"""Entidad Termostato - Dispositivo de climatización."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    TEMP_MIN,
    TEMP_MAX,
    TEMP_OBJETIVO_INICIAL
)


class Termostato(Dispositivo):
    """
    Termostato inteligente con control de temperatura.
    
    Attributes:
        _temperatura_objetivo: Temperatura deseada (°C)
    """

    def __init__(self):
        """Inicializa termostato con valores por defecto."""
        super().__init__()
        self._temperatura_objetivo: float = TEMP_OBJETIVO_INICIAL

    def get_temperatura_objetivo(self) -> float:
        """
        Obtiene temperatura objetivo.
        
        Returns:
            Temperatura objetivo (°C)
        """
        return self._temperatura_objetivo

    def set_temperatura_objetivo(self, temperatura: float) -> None:
        """
        Establece temperatura objetivo.
        
        Args:
            temperatura: Temperatura objetivo (°C)
            
        Raises:
            ValueError: Si temperatura fuera de rango
        """
        if not (TEMP_MIN <= temperatura <= TEMP_MAX):
            raise ValueError(
                f"Temperatura debe estar entre {TEMP_MIN} y {TEMP_MAX}"
            )
        self._temperatura_objetivo = temperatura


