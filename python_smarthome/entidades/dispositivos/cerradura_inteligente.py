"""Entidad CerraduraInteligente - Dispositivo de acceso."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    BATERIA_INICIAL,
    METODO_ACCESO_INICIAL
)


class CerraduraInteligente(Dispositivo):
    """
    Cerradura inteligente con control de acceso y batería.
    
    Attributes:
        _bloqueada: Estado de la cerradura (bloqueada/desbloqueada)
        _bateria: Nivel de batería (0-100%)
        _metodo_acceso: Método de acceso actual
    """

    def __init__(self):
        """Inicializa cerradura con valores por defecto."""
        super().__init__()
        self._bloqueada: bool = True
        self._bateria: int = BATERIA_INICIAL
        self._metodo_acceso: str = METODO_ACCESO_INICIAL

    def is_bloqueada(self) -> bool:
        """Verifica si la cerradura está bloqueada."""
        return self._bloqueada

    def bloquear(self) -> None:
        """Bloquea la cerradura."""
        self._bloqueada = True

    def desbloquear(self) -> None:
        """Desbloquea la cerradura."""
        self._bloqueada = False

    def get_bateria(self) -> int:
        """Obtiene el nivel de batería."""
        return self._bateria

    def get_metodo_acceso(self) -> str:
        """Obtiene el método de acceso."""
        return self._metodo_acceso

    def set_metodo_acceso(self, metodo: str) -> None:
        """Establece el método de acceso."""
        self._metodo_acceso = metodo
