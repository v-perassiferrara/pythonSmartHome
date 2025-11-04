"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\factory
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: dispositivo_factory.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\factory\dispositivo_factory.py
# ================================================================================

"""Factory para crear dispositivos - FACTORY METHOD pattern."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class DispositivoFactory:
    """
    Factory para crear dispositivos sin conocer clases concretas.
    
    Implementa FACTORY METHOD pattern.
    """

    @staticmethod
    def crear_dispositivo(tipo: str) -> 'Dispositivo':
        """
        Crea dispositivo según tipo especificado.
        
        Args:
            tipo: Tipo de dispositivo ("LuzInteligente", "Termostato", etc.)
            
        Returns:
            Instancia de Dispositivo
            
        Raises:
            ValueError: Si tipo desconocido
        """
        # Diccionario de factories (NO if/elif cascades)
        factories = {
            "LuzInteligente": DispositivoFactory._crear_luz,
            "Termostato": DispositivoFactory._crear_termostato,
            "CamaraSeguridad": DispositivoFactory._crear_camara,
            "CerraduraInteligente": DispositivoFactory._crear_cerradura
        }

        if tipo not in factories:
            raise ValueError(f"Tipo desconocido: {tipo}")

        return factories[tipo]()

    @staticmethod
    def _crear_luz() -> 'Dispositivo':
        """Crea luz inteligente."""
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        return LuzInteligente()

    @staticmethod
    def _crear_termostato() -> 'Dispositivo':
        """Crea termostato."""
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        return Termostato()

    @staticmethod
    def _crear_camara() -> 'Dispositivo':
        """Crea cámara de seguridad."""
        from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
        return CamaraSeguridad()

    @staticmethod
    def _crear_cerradura() -> 'Dispositivo':
        """Crea cerradura inteligente."""
        from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente
        return CerraduraInteligente()


