"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: camara_seguridad_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\camara_seguridad_service.py
# ================================================================================

"""Servicio para gestionar cámaras de seguridad."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CamaraSeguridadService(DispositivoService):
    """
    Servicio para operaciones sobre cámaras de seguridad.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, camara: 'CamaraSeguridad') -> None:
        """
        Muestra datos de una cámara de seguridad.
        
        Args:
            camara: Cámara a mostrar
        """
        super().mostrar_datos(camara)  # Datos comunes (ID, estado, tipo)
        print(f"Resolución: {camara.get_resolucion()}")
        print(f"Detección de Movimiento: {'activa' if camara.is_deteccion_movimiento_activa() else 'inactiva'}")
        print(f"Grabando: {'sí' if camara.is_grabando() else 'no'}")

    def encender(self, camara: 'CamaraSeguridad') -> None:
        """
        Enciende la cámara y la grabación.
        
        Args:
            camara: Cámara a encender
        """
        camara.set_encendido(True)
        camara.set_grabacion(True)

    def apagar(self, camara: 'CamaraSeguridad') -> None:
        """
        Apaga la cámara y la grabación.
        
        Args:
            camara: Cámara a apagar
        """
        camara.set_encendido(False)
        camara.set_grabacion(False)

# ================================================================================
# ARCHIVO 3/7: cerradura_inteligente_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\cerradura_inteligente_service.py
# ================================================================================

"""Servicio para gestionar cerraduras inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CerraduraInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre cerraduras inteligentes.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Muestra datos de una cerradura inteligente.
        
        Args:
            cerradura: Cerradura a mostrar
        """
        super().mostrar_datos(cerradura)  # Datos comunes (ID, estado, tipo)
        print(f"Batería: {cerradura.get_bateria()}%")
        print(f"Estado: {'bloqueada' if cerradura.is_bloqueada() else 'desbloqueada'}")

    def bloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Bloquea la cerradura.
        
        Args:
            cerradura: Cerradura a bloquear
        """
        cerradura.bloquear()

    def desbloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Desbloquea la cerradura.
        
        Args:
            cerradura: Cerradura a desbloquear
        """
        cerradura.desbloquear()

# ================================================================================
# ARCHIVO 4/7: dispositivo_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\dispositivo_service.py
# ================================================================================

"""Servicio base para todos los dispositivos."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
    from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class DispositivoService(ABC):
    """
    Clase base abstracta para servicios de dispositivos.
    
    Inyecta una estrategia de automatización (STRATEGY PATTERN).
    """

    def __init__(self, strategy: 'AutomationStrategy'):
        """
        Inicializa servicio con estrategia de automatización.
        
        Args:
            strategy: Estrategia de automatización a usar
        """
        self._estrategia_automation = strategy

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos comunes de un dispositivo.
        
        Args:
            dispositivo: Dispositivo a mostrar
        """
        tipo_dispositivo = type(dispositivo).__name__
        print(f"Dispositivo: {tipo_dispositivo}")
        print(f"ID: {dispositivo.get_id_dispositivo()}")
        print(f"Estado: {'encendido' if dispositivo.is_encendido() else 'apagado'}")

    def ejecutar_automatizacion(self, dispositivo: 'Dispositivo', evento: Any) -> None:
        """
        Delega la ejecución de la automatización a la estrategia (STRATEGY PATTERN).
        
        Este método demuestra el uso del patrón STRATEGY:
        - El servicio NO sabe cómo automatizar
        - Delega la decisión a la estrategia inyectada
        - Permite cambiar el algoritmo en tiempo de ejecución
        
        Args:
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        self._estrategia_automation.ejecutar_accion(datetime.now(), dispositivo, evento)

    def get_estrategia(self) -> 'AutomationStrategy':
        """
        Obtiene la estrategia actual (útil para testing).
        
        Returns:
            Estrategia de automatización
        """
        return self._estrategia_automation

    def set_estrategia(self, strategy: 'AutomationStrategy') -> None:
        """
        Cambia la estrategia en tiempo de ejecución (demuestra flexibilidad del patrón).
        
        Args:
            strategy: Nueva estrategia a usar
        """
        self._estrategia_automation = strategy

# ================================================================================
# ARCHIVO 5/7: dispositivo_service_registry.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\dispositivo_service_registry.py
# ================================================================================

"""Registry de servicios - SINGLETON + REGISTRY patterns."""

from threading import Lock
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
    from python_smarthome.entidades.dispositivos.termostato import Termostato
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

# Imports reales (no circulares)
from python_smarthome.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from python_smarthome.servicios.dispositivos.termostato_service import TermostatoService
from python_smarthome.servicios.dispositivos.camara_seguridad_service import CamaraSeguridadService
from python_smarthome.servicios.dispositivos.cerradura_inteligente_service import CerraduraInteligenteService


class DispositivoServiceRegistry:
    """
    Registry de servicios de dispositivos.
    
    Implementa SINGLETON pattern (instancia única) y REGISTRY pattern (dispatch polimórfico).
    Thread-safe mediante double-checked locking.
    """

    _instance: 'DispositivoServiceRegistry' = None
    _lock = Lock()

    def __new__(cls):
        """
        Crea o retorna instancia única (SINGLETON).
        
        Returns:
            Instancia única del registry
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'DispositivoServiceRegistry':
        """
        Obtiene instancia única del registry.
        
        Returns:
            Instancia única
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """Inicializa servicios específicos (llamado una sola vez)."""
        # Importar clases de entidades
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
        from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

        # Crear servicios
        self._luz_service = LuzInteligenteService()
        self._termostato_service = TermostatoService()
        self._camara_service = CamaraSeguridadService()
        self._cerradura_service = CerraduraInteligenteService()

        # Registry de handlers (REGISTRY PATTERN)
        self._encender_handlers = {
            LuzInteligente: self._encender_luz,
            Termostato: self._encender_termostato,
            CamaraSeguridad: self._encender_camara,
            CerraduraInteligente: self._encender_cerradura
        }

        self._mostrar_datos_handlers = {
            LuzInteligente: self._mostrar_datos_luz,
            Termostato: self._mostrar_datos_termostato,
            CamaraSeguridad: self._mostrar_datos_camara,
            CerraduraInteligente: self._mostrar_datos_cerradura
        }

    # ============================================================
    # Métodos públicos (dispatch polimórfico)
    # ============================================================

    def encender(self, dispositivo: 'Dispositivo') -> None:
        """
        Enciende dispositivo (dispatch polimórfico).
        
        Args:
            dispositivo: Dispositivo a encender
            
        Raises:
            ValueError: Si tipo de dispositivo desconocido
        """
        tipo = type(dispositivo)
        if tipo not in self._encender_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._encender_handlers[tipo](dispositivo)

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos de dispositivo (dispatch polimórfico).
        
        Args:
            dispositivo: Dispositivo a mostrar
            
        Raises:
            ValueError: Si tipo de dispositivo desconocido
        """
        tipo = type(dispositivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](dispositivo)

    # ============================================================
    # Handlers privados (NO usar lambdas)
    # ============================================================

    def _encender_luz(self, dispositivo: 'LuzInteligente') -> None:
        self._luz_service.encender(dispositivo)

    def _encender_termostato(self, dispositivo: 'Termostato') -> None:
        self._termostato_service.encender(dispositivo)

    def _encender_camara(self, dispositivo: 'CamaraSeguridad') -> None:
        self._camara_service.encender(dispositivo)

    def _encender_cerradura(self, dispositivo: 'CerraduraInteligente') -> None:
        self._cerradura_service.bloquear(dispositivo)

    def _mostrar_datos_luz(self, dispositivo: 'LuzInteligente') -> None:
        self._luz_service.mostrar_datos(dispositivo)

    def _mostrar_datos_termostato(self, dispositivo: 'Termostato') -> None:
        self._termostato_service.mostrar_datos(dispositivo)

    def _mostrar_datos_camara(self, dispositivo: 'CamaraSeguridad') -> None:
        self._camara_service.mostrar_datos(dispositivo)

    def _mostrar_datos_cerradura(self, dispositivo: 'CerraduraInteligente') -> None:
        self._cerradura_service.mostrar_datos(dispositivo)


# ================================================================================
# ARCHIVO 6/7: luz_inteligente_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\luz_inteligente_service.py
# ================================================================================

"""Servicio para gestionar luces inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.iluminacion_strategy import IluminacionStrategy


class LuzInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre luces inteligentes.
    
    Usa estrategia de iluminación para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de iluminación."""
        super().__init__(IluminacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, luz: 'LuzInteligente') -> None:
        """
        Muestra datos de una luz inteligente.
        
        Args:
            luz: Luz a mostrar
        """
        super().mostrar_datos(luz)  # Datos comunes (ID, estado, tipo)
        print(f"Intensidad: {luz.get_intensidad()}%")
        r, g, b = luz.get_color_rgb()
        print(f"Color RGB: ({r}, {g}, {b})")

    def encender(self, luz: 'LuzInteligente') -> None:
        """
        Enciende luz con intensidad máxima.
        
        Args:
            luz: Luz a encender
        """
        luz.set_encendido(True)
        luz.set_intensidad(100)

    def apagar(self, luz: 'LuzInteligente') -> None:
        """
        Apaga luz.
        
        Args:
            luz: Luz a apagar
        """
        luz.set_encendido(False)
        luz.set_intensidad(0)

    def ajustar_intensidad(self, luz: 'LuzInteligente', intensidad: int) -> None:
        """
        Ajusta intensidad de la luz.
        
        Args:
            luz: Luz a ajustar
            intensidad: Nueva intensidad (0-100%)
        """
        luz.set_intensidad(intensidad)

    def cambiar_color(self, luz: 'LuzInteligente', color: tuple) -> None:
        """
        Cambia color de la luz.
        
        Args:
            luz: Luz a ajustar
            color: Tupla RGB (R, G, B)
        """
        luz.set_color_rgb(color)

# ================================================================================
# ARCHIVO 7/7: termostato_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\termostato_service.py
# ================================================================================

"""Servicio para gestionar termostatos."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.climatizacion_strategy import ClimatizacionStrategy


class TermostatoService(DispositivoService):
    """
    Servicio para operaciones sobre termostatos.
    
    Usa estrategia de climatización para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de climatización."""
        super().__init__(ClimatizacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, termostato: 'Termostato') -> None:
        """
        Muestra datos de un termostato.
        
        Args:
            termostato: Termostato a mostrar
        """
        super().mostrar_datos(termostato)  # Datos comunes (ID, estado, tipo)
        print(f"Temperatura Objetivo: {termostato.get_temperatura_objetivo()}°C")

    def encender(self, termostato: 'Termostato') -> None:
        """
        Enciende el termostato.
        
        Args:
            termostato: Termostato a encender
        """
        termostato.set_encendido(True)

    def apagar(self, termostato: 'Termostato') -> None:
        """
        Apaga el termostato.
        
        Args:
            termostato: Termostato a apagar
        """
        termostato.set_encendido(False)

