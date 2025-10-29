"""Excepción de permiso denegado."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class PermisoDenegadoException(SmartHomeException):
    """
    Excepción lanzada cuando un usuario no tiene permisos suficientes.
    """

    def __init__(self, nombre_usuario: str, nivel_requerido: str, nivel_actual: str):
        mensaje_usuario = MensajesException.PERMISO_DENEGADO_USUARIO.format(
            nombre=nombre_usuario,
            requerido=nivel_requerido,
            actual=nivel_actual
        )
        
        mensaje_tecnico = MensajesException.PERMISO_DENEGADO_TECNICO.format(
            nombre=nombre_usuario,
            requerido=nivel_requerido,
            actual=nivel_actual
        )
        
        super().__init__(mensaje_usuario, mensaje_tecnico)
