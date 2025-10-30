"""Servicio para gestionar habitaciones."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion

from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory
from python_smarthome.constantes import (
    MAX_DISPOSITIVOS_HABITACION,
    INTENSIDAD_MODO_NOCHE,
    TEMP_CONFORT_OBJETIVO
)
from python_smarthome.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException


class HabitacionService:
    """
    Servicio para operaciones sobre habitaciones.
    
    Demuestra uso del patrón FACTORY METHOD para crear dispositivos.
    """

    def instalar(self, habitacion: 'Habitacion', tipo_dispositivo: str, cantidad: int) -> None:
        """
        Instala dispositivos en una habitación usando FACTORY METHOD pattern.
        
        Demuestra:
        - Cliente (HabitacionService) NO conoce clases concretas
        - Factory encapsula lógica de creación
        - Fácil extensión para nuevos tipos
        
        Args:
            habitacion: La habitación donde instalar
            tipo_dispositivo: El tipo de dispositivo a instalar
            cantidad: Cuántos dispositivos instalar
            
        Raises:
            CapacidadInsuficienteException: Si no hay espacio
            ValueError: Si tipo de dispositivo desconocido
        """
        # Validar cantidad
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        
        # Verificar capacidad
        capacidad_actual = len(habitacion.get_dispositivos())
        capacidad_disponible = MAX_DISPOSITIVOS_HABITACION - capacidad_actual
        
        if cantidad > capacidad_disponible:
            raise CapacidadInsuficienteException(
                capacidad_requerida=cantidad,
                capacidad_disponible=capacidad_disponible
            )
        
        # Crear dispositivos usando FACTORY METHOD
        print(f"Instalando {cantidad} dispositivos de tipo {tipo_dispositivo}...")
        for i in range(cantidad):
            # FACTORY METHOD: cliente NO instancia clases concretas
            dispositivo = DispositivoFactory.crear_dispositivo(tipo_dispositivo)
            habitacion.agregar_dispositivo(dispositivo)
            print(f"  - Dispositivo {i+1}/{cantidad} instalado (ID: {dispositivo.get_id_dispositivo()})")
        
        print(f"Instalacion completada. Total dispositivos: {len(habitacion.get_dispositivos())}")

    def ajustar_luces_modo_noche(self, habitacion: 'Habitacion') -> None:
        """
        Ajusta las luces de la habitación a modo noche.
        
        Aplica intensidad reducida (INTENSIDAD_MODO_NOCHE) a todas las luces.
        
        Args:
            habitacion: Habitación a ajustar
        """
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        
        contador = 0
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.set_encendido(True)
                dispositivo.set_intensidad(INTENSIDAD_MODO_NOCHE)
                contador += 1
        
        if contador > 0:
            print(f"Ajustadas {contador} luces a modo noche ({INTENSIDAD_MODO_NOCHE}%)")

    def ajustar_climatizacion(self, habitacion: 'Habitacion') -> None:
        """
        Ajusta la climatización de la habitación a temperatura de confort.
        
        Args:
            habitacion: Habitación a ajustar
        """
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        
        contador = 0
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, Termostato):
                dispositivo.set_encendido(True)
                dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)
                contador += 1
        
        if contador > 0:
            print(f"Ajustados {contador} termostatos a {TEMP_CONFORT_OBJETIVO}°C")

    def encender_todos(self, habitacion: 'Habitacion') -> None:
        """
        Enciende todos los dispositivos de una habitación.
        
        Args:
            habitacion: Habitación a controlar
        """
        from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
        
        registry = DispositivoServiceRegistry.get_instance()
        print(f"\nEncendiendo todos los dispositivos de {habitacion.get_nombre()}...")
        
        for dispositivo in habitacion.get_dispositivos():
            registry.encender(dispositivo)
            print(f"  - Dispositivo ID {dispositivo.get_id_dispositivo()} encendido")

    def apagar_todos(self, habitacion: 'Habitacion') -> None:
        """
        Apaga todos los dispositivos de una habitación.
        
        Args:
            habitacion: Habitación a controlar
        """
        print(f"\nApagando todos los dispositivos de {habitacion.get_nombre()}...")
        
        for dispositivo in habitacion.get_dispositivos():
            dispositivo.set_encendido(False)
            print(f"  - Dispositivo ID {dispositivo.get_id_dispositivo()} apagado")

    def mostrar_todos(self, habitacion: 'Habitacion') -> None:
        """
        Muestra datos de todos los dispositivos usando REGISTRY pattern.
        
        Args:
            habitacion: Habitación a mostrar
        """
        from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
        
        registry = DispositivoServiceRegistry.get_instance()
        print(f"\n=== DISPOSITIVOS EN {habitacion.get_nombre().upper()} ===")
        
        if not habitacion.get_dispositivos():
            print("(Sin dispositivos instalados)")
        else:
            for i, dispositivo in enumerate(habitacion.get_dispositivos(), 1):
                print(f"\n--- Dispositivo {i} ---")
                registry.mostrar_datos(dispositivo)
        
        print("=" * 50)