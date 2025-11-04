"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: capacidad_insuficiente_exception.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\capacidad_insuficiente_exception.py
# ================================================================================

"""Excepción de capacidad insuficiente."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class CapacidadInsuficienteException(SmartHomeException):
    """
    Excepción lanzada cuando no hay capacidad para instalar dispositivos.
    
    Attributes:
        _capacidad_requerida: Dispositivos requeridos
        _capacidad_disponible: Dispositivos disponibles
    """

    def __init__(
        self,
        capacidad_requerida: int,
        capacidad_disponible: int
    ):
        """
        Inicializa excepción.
        
        Args:
            capacidad_requerida: Dispositivos que se intentaron instalar
            capacidad_disponible: Dispositivos que caben
        """
        self._capacidad_requerida = capacidad_requerida
        self._capacidad_disponible = capacidad_disponible
        
        mensaje_usuario = MensajesException.CAPACIDAD_INSUFICIENTE_USUARIO.format(
            requerida=capacidad_requerida,
            disponible=capacidad_disponible
        )
        
        mensaje_tecnico = MensajesException.CAPACIDAD_INSUFICIENTE_TECNICO.format(
            requerida=capacidad_requerida,
            disponible=capacidad_disponible
        )
        
        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_capacidad_requerida(self) -> int:
        """Obtiene capacidad requerida."""
        return self._capacidad_requerida

    def get_capacidad_disponible(self) -> int:
        """Obtiene capacidad disponible."""
        return self._capacidad_disponible


# ================================================================================
# ARCHIVO 3/6: mensajes_exception.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\mensajes_exception.py
# ================================================================================

"""Mensajes de excepción centralizados."""


class MensajesException:
    """Mensajes de excepción (inglés para código, español para usuario)."""

    # Capacidad insuficiente
    CAPACIDAD_INSUFICIENTE_USUARIO = (
        "No hay capacidad suficiente en la habitacion. "
        "Se requiere capacidad para {requerida} dispositivos, "
        "pero solo hay {disponible} disponible."
    )
    CAPACIDAD_INSUFICIENTE_TECNICO = (
        "Insufficient capacity: required={requerida}, available={disponible}"
    )

    # Permiso denegado
    PERMISO_DENEGADO_USUARIO = (
        "El usuario {nombre} no tiene permisos suficientes. "
        "Nivel requerido: {requerido}, Nivel actual: {actual}"
    )
    PERMISO_DENEGADO_TECNICO = (
        "Permission denied for user={nombre}: required_level={requerido}, actual_level={actual}"
    )

    # Persistencia
    PERSISTENCIA_ESCRITURA_USUARIO = (
        "No se pudo guardar la configuracion de {propietario}. "
        "Verifique permisos del directorio."
    )
    PERSISTENCIA_ESCRITURA_TECNICO = (
        "Write error for file={archivo}: {detalle}"
    )

    PERSISTENCIA_LECTURA_USUARIO = (
        "No se pudo leer la configuracion de {propietario}. "
        "El archivo puede no existir o estar corrupto."
    )
    PERSISTENCIA_LECTURA_TECNICO = (
        "Read error for file={archivo}: {detalle}"
    )


# ================================================================================
# ARCHIVO 4/6: permiso_denegado_exception.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\permiso_denegado_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\persistencia_exception.py
# ================================================================================

"""Excepción de persistencia."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class PersistenciaException(SmartHomeException):
    """
    Excepción lanzada cuando hay un error de lectura o escritura en disco.
    """

    def __init__(self, mensaje_usuario: str, mensaje_tecnico: str):
        super().__init__(mensaje_usuario, mensaje_tecnico)


# ================================================================================
# ARCHIVO 6/6: smarthome_exception.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\smarthome_exception.py
# ================================================================================

"""Excepción base del sistema de domótica."""


class SmartHomeException(Exception):
    """
    Excepción base para errores del sistema de domótica.
    
    Attributes:
        _mensaje_usuario: Mensaje legible para usuario
        _mensaje_tecnico: Mensaje técnico con detalles
    """

    def __init__(self, mensaje_usuario: str, mensaje_tecnico: str):
        """
        Inicializa excepción.
        
        Args:
            mensaje_usuario: Mensaje para usuario final
            mensaje_tecnico: Mensaje para desarrollador/log
        """
        super().__init__(mensaje_tecnico)
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico

    def get_user_message(self) -> str:
        """
        Obtiene mensaje para usuario.
        
        Returns:
            Mensaje legible
        """
        return self._mensaje_usuario

    def get_technical_message(self) -> str:
        """
        Obtiene mensaje técnico.
        
        Returns:
            Mensaje con detalles técnicos
        """
        return self._mensaje_tecnico

    def get_full_message(self) -> str:
        """
        Obtiene mensaje completo.
        
        Returns:
            Ambos mensajes concatenados
        """
        return f"{self._mensaje_usuario}\nDetalle tecnico: {self._mensaje_tecnico}"

