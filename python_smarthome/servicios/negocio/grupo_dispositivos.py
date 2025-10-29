"""Contenedor genérico para agrupar dispositivos."""

from typing import Generic, List, Type, TypeVar

T = TypeVar('T')


class GrupoDispositivos(Generic[T]):
    """
    Clase genérica para agrupar dispositivos de un mismo tipo.
    """

    def __init__(self, tipo: Type[T], dispositivos: List[T]):
        self._tipo = tipo
        self._dispositivos = dispositivos

    def mostrar_contenido_grupo(self) -> None:
        """Muestra el contenido del grupo."""
        print(f"\n--- GRUPO DE DISPOSITIVOS: {self._tipo.__name__} ---")
        print(f"Cantidad: {len(self._dispositivos)}")
        for dispositivo in self._dispositivos:
            print(f"  - ID: {dispositivo.get_id_dispositivo()}")
        print("---------------------------------")
