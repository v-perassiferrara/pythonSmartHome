"""Interfaz Observer - OBSERVER pattern."""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz para observadores.
    
    Type Parameters:
        T: Tipo de evento que recibe (ej. bool para movimiento)
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica.
        
        Args:
            evento: Evento recibido (tipo T)
        """
        pass
