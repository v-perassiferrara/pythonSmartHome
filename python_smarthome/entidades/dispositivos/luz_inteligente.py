"""Entidad LuzInteligente - Dispositivo de iluminación."""

from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    INTENSIDAD_MIN,
    INTENSIDAD_MAX,
    COLOR_INICIAL
)


class LuzInteligente(Dispositivo):
    """
    Luz inteligente con control de intensidad y color.
    
    Attributes:
        _intensidad: Intensidad de la luz (0-100%)
        _color_rgb: Color RGB como tupla (R, G, B)
    """

    def __init__(self):
        """Inicializa luz inteligente con valores por defecto."""
        super().__init__()
        self._intensidad: int = INTENSIDAD_MAX
        self._color_rgb: Tuple[int, int, int] = COLOR_INICIAL

    def get_intensidad(self) -> int:
        """
        Obtiene intensidad de la luz.
        
        Returns:
            Intensidad (0-100%)
        """
        return self._intensidad

    def set_intensidad(self, intensidad: int) -> None:
        """
        Establece intensidad de la luz.
        
        Args:
            intensidad: Intensidad (0-100%)
            
        Raises:
            ValueError: Si intensidad fuera de rango
        """
        if not (INTENSIDAD_MIN <= intensidad <= INTENSIDAD_MAX):
            raise ValueError(
                f"Intensidad debe estar entre {INTENSIDAD_MIN} y {INTENSIDAD_MAX}"
            )
        self._intensidad = intensidad

    def get_color_rgb(self) -> Tuple[int, int, int]:
        """
        Obtiene color RGB.
        
        Returns:
            Tupla (R, G, B)
        """
        return self._color_rgb

    def set_color_rgb(self, color: Tuple[int, int, int]) -> None:
        """
        Establece color RGB.
        
        Args:
            color: Tupla (R, G, B) donde cada componente es 0-255
            
        Raises:
            ValueError: Si valores fuera de rango
        """
        r, g, b = color
        if not all(0 <= c <= 255 for c in [r, g, b]):
            raise ValueError("RGB components must be between 0 and 255")
        self._color_rgb = color
