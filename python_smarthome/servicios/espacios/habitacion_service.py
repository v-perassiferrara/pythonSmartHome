"""Servicio para gestionar habitaciones."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion

from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory
from python_smarthome.constantes import MAX_DISPOSITIVOS_HABITACION
from python_smarthome.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException


class HabitacionService:
    """
    Servicio para operaciones sobre habitaciones.
    """

    def instalar(self, habitacion: 'Habitacion', tipo_dispositivo: str, cantidad: int) -> None:
        """
        Instala dispositivos en una habitación usando una factory.
        
        Args:
            habitacion: La habitación donde instalar
            tipo_dispositivo: El tipo de dispositivo a instalar
            cantidad: Cuántos dispositivos instalar
            
        Raises:
            CapacidadInsuficienteException: Si no hay espacio
        """
        capacidad_actual = len(habitacion.get_dispositivos())
        if capacidad_actual + cantidad > MAX_DISPOSITIVOS_HABITACION:
            raise CapacidadInsuficienteException(
                capacidad_requerida=cantidad,
                capacidad_disponible=MAX_DISPOSITIVOS_HABITACION - capacidad_actual
            )
        
        for _ in range(cantidad):
            dispositivo = DispositivoFactory.crear_dispositivo(tipo_dispositivo)
            habitacion.agregar_dispositivo(dispositivo)

    def ajustar_luces_modo_noche(self, habitacion: 'Habitacion') -> None:
        """Ajusta las luces de la habitación a modo noche."""
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.set_intensidad(30)

    def ajustar_climatizacion(self, habitacion: 'Habitacion') -> None:
        """Ajusta la climatización de la habitación."""
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        from python_smarthome.constantes import TEMP_CONFORT_OBJETIVO
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, Termostato):
                dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)
