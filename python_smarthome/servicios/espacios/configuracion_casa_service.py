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
