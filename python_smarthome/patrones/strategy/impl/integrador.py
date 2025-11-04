"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: climatizacion_strategy.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\climatizacion_strategy.py
# ================================================================================

"""Estrategia de climatización - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import TEMP_CONFORT_OBJETIVO


class ClimatizacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para termostatos.
    
    Ajusta la temperatura a un valor de confort.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Termostato',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de climatización.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Termostato a controlar
            evento: Evento disparador (ignorado)
        """
        dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)


# ================================================================================
# ARCHIVO 3/4: iluminacion_strategy.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\iluminacion_strategy.py
# ================================================================================

"""Estrategia de iluminación - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import (
    HORA_INICIO_NOCHE,
    HORA_FIN_NOCHE
)


class IluminacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para luces inteligentes.
    
    Ajusta intensidad según hora del día.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'LuzInteligente',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de iluminación.
        
        Modo noche (20:00-07:00): Intensidad 30%
        Modo día: Intensidad 100%
        
        Args:
            fecha: Fecha/hora actual
            dispositivo: Luz a controlar
            evento: Evento disparador (ignorado)
        """
        hora = fecha.hour
        
        # Verificar si es modo noche
        es_modo_noche = (HORA_INICIO_NOCHE <= hora) or (hora <= HORA_FIN_NOCHE)
        
        if es_modo_noche:
            dispositivo.set_intensidad(30)  # 30% en modo noche
        else:
            dispositivo.set_intensidad(100)  # 100% de día


# ================================================================================
# ARCHIVO 4/4: seguridad_strategy.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\seguridad_strategy.py
# ================================================================================

"""Estrategia de seguridad - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class SeguridadStrategy(AutomationStrategy):
    """
    Estrategia de automatización para dispositivos de seguridad.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: Any,
        evento: Any
    ) -> None:
        """
        Ejecuta acción de seguridad.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Dispositivo a controlar
            evento: Evento disparador (ignorado)
        """
        # Para cámaras, enciende la grabación
        if hasattr(dispositivo, 'set_grabacion'):
            dispositivo.set_grabacion(True)
        
        # Para cerraduras, las bloquea
        if hasattr(dispositivo, 'bloquear'):
            dispositivo.bloquear()


