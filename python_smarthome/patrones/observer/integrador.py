"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\observable.py
# ================================================================================

"""Clase base Observable - OBSERVER pattern."""

from typing import Generic, TypeVar, List, TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from python_smarthome.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase base para objetos observables.
    
    Implementa OBSERVER pattern con tipo-seguridad mediante Generics.
    
    Type Parameters:
        T: Tipo de evento que emite (ej. float para temperatura)
    """

    def __init__(self):
        """Inicializa lista de observadores."""
        self._observadores: List['Observer[T]'] = []

    def agregar_observador(self, observador: 'Observer[T]') -> None:
        """
        Agrega un observador a la lista.
        
        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        """
        Elimina un observador de la lista.
        
        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores.
        
        Args:
            evento: Evento a notificar (tipo T)
        """
        for observador in self._observadores:
            observador.actualizar(evento)


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\observer.py
# ================================================================================

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


