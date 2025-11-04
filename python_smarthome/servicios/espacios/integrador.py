"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: casa_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\casa_service.py
# ================================================================================

"""Servicio para gestionar casas."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.casa import Casa

from python_smarthome.entidades.espacios.casa import Casa
from python_smarthome.entidades.espacios.habitacion import Habitacion


class CasaService:
    """
    Servicio para operaciones de alto nivel sobre casas.
    """

    def crear_casa_con_habitaciones(
        self,
        direccion: str,
        superficie: float,
        propietario: str,
        nombres_habitaciones: List[str]
    ) -> 'Casa':
        """
        Crea una casa y le asigna habitaciones.
        
        Args:
            direccion: Dirección de la casa
            superficie: Superficie en m²
            propietario: Nombre del propietario
            nombres_habitaciones: Lista de nombres para las habitaciones
            
        Returns:
            La casa creada con sus habitaciones
        """
        casa = Casa(direccion, superficie, propietario)
        habitaciones = [Habitacion(nombre) for nombre in nombres_habitaciones]
        casa.set_habitaciones(habitaciones)
        return casa


# ================================================================================
# ARCHIVO 3/4: configuracion_casa_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\configuracion_casa_service.py
# ================================================================================

"""Servicio para gestionar la configuración de la casa."""

import os
import pickle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa

from python_smarthome.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_smarthome.excepciones.persistencia_exception import PersistenciaException


class ConfiguracionCasaService:
    """
    Servicio para persistir y leer la configuración de la casa.
    """

    def persistir(self, config: 'ConfiguracionCasa') -> None:
        """
        Guarda la configuración en un archivo .dat usando pickle.
        
        Args:
            config: La configuración a guardar
            
        Raises:
            PersistenciaException: Si hay un error de escritura
        """
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
        
        nombre_archivo = f"{config.get_propietario()}{EXTENSION_DATA}"
        ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(config, f)
            print(f"Configuración de {config.get_propietario()} guardada en {ruta_archivo}")
        except IOError as e:
            raise PersistenciaException(
                mensaje_usuario=f"No se pudo guardar la configuración de {config.get_propietario()}",
                mensaje_tecnico=f"Error al escribir en {ruta_archivo}: {e}"
            )

    @staticmethod
    def leer_configuracion(propietario: str) -> 'ConfiguracionCasa':
        """
        Lee la configuración desde un archivo .dat.
        
        Args:
            propietario: Nombre del propietario para encontrar el archivo
            
        Returns:
            La configuración leída
            
        Raises:
            PersistenciaException: Si el archivo no existe o está corrupto
        """
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            raise PersistenciaException(
                mensaje_usuario=f"No se encontró la configuración de {propietario}",
                mensaje_tecnico=f"El archivo {ruta_archivo} no existe"
            )
        
        try:
            with open(ruta_archivo, 'rb') as f:
                config = pickle.load(f)
            print(f"Configuración de {propietario} leída desde {ruta_archivo}")
            return config
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                mensaje_usuario=f"No se pudo leer la configuración de {propietario}",
                mensaje_tecnico=f"Error al leer o deserializar {ruta_archivo}: {e}"
            )

    def mostrar_datos(self, config: 'ConfiguracionCasa') -> None:
        """
        Muestra los datos de una configuración de casa.
        
        Args:
            config: La configuración a mostrar
        """
        casa = config.get_casa()
        print("\n--- CONFIGURACIÓN DE LA CASA ---")
        print(f"Propietario: {config.get_propietario()}")
        print(f"Dirección: {casa.get_direccion()}")
        print(f"Superficie: {casa.get_superficie()} m²")
        print(f"Fecha de Instalación: {config.get_fecha_instalacion()}")
        print(f"Habitaciones: {len(casa.get_habitaciones())}")
        
        total_dispositivos = sum(len(h.get_dispositivos()) for h in casa.get_habitaciones())
        print(f"Total de Dispositivos: {total_dispositivos}")
        print("---------------------------------")


# ================================================================================
# ARCHIVO 4/4: habitacion_service.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\habitacion_service.py
# ================================================================================

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

