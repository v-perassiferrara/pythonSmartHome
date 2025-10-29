"""Excepción de persistencia."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class PersistenciaException(SmartHomeException):
    """
    Excepción lanzada cuando hay un error de lectura o escritura en disco.
    """

    def __init__(self, mensaje_usuario: str, mensaje_tecnico: str):
        super().__init__(mensaje_usuario, mensaje_tecnico)
