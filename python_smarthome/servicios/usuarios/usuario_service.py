"""Servicio para gestionar usuarios."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.usuarios.usuario import Usuario
    from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso


class UsuarioService:
    """
    Servicio para operaciones sobre usuarios.
    """

    def asignar_nivel_acceso(self, usuario: 'Usuario', nivel: 'NivelAcceso') -> None:
        """
        Asigna un nivel de acceso a un usuario.
        
        Args:
            usuario: El usuario a modificar
            nivel: El nuevo nivel de acceso
        """
        # En una implementación real, esto modificaría el estado del usuario.
        # Por ahora, solo imprimimos la acción.
        print(f"Asignando nivel {nivel.name} a {usuario.get_nombre()}")
