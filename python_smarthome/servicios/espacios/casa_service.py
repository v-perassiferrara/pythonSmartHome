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
