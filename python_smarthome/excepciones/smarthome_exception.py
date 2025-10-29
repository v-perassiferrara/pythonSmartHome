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