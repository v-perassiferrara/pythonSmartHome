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
