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
