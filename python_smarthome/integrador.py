"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome
Fecha: 2025-11-04 15:57:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\constantes.py
# ================================================================================

"""
Constantes centralizadas del sistema de domótica (Smart Home).

Este módulo contiene TODAS las constantes del sistema.
REGLA: NUNCA hardcodear valores mágicos en el código.
TODO debe estar definido aquí.

Autor: Sistema de Domótica
Fecha: Octubre 2025
"""

# ============================================================
# DISPOSITIVOS - Luces Inteligentes
# ============================================================
INTENSIDAD_MIN = 0  # %
INTENSIDAD_MAX = 100  # %
COLOR_INICIAL = (255, 255, 255)  # RGB - Blanco
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_AMARILLO = (255, 255, 0)

# ============================================================
# DISPOSITIVOS - Termostatos
# ============================================================
TEMP_MIN = 10  # °C
TEMP_MAX = 30  # °C
TEMP_OBJETIVO_INICIAL = 22  # °C

# Modos de termostato
MODO_CALOR = "heat"
MODO_FRIO = "cool"
MODO_AUTO = "auto"

# ============================================================
# DISPOSITIVOS - Cámaras de Seguridad
# ============================================================
RESOLUCION_INICIAL = "1080p"
RESOLUCION_720P = "720p"
RESOLUCION_1080P = "1080p"
RESOLUCION_4K = "4K"

DETECCION_MOVIMIENTO_INICIAL = True
GRABACION_INICIAL = False

# ============================================================
# DISPOSITIVOS - Cerraduras Inteligentes
# ============================================================
BATERIA_INICIAL = 100  # %
BATERIA_MIN = 0  # %
BATERIA_MAX = 100  # %

METODO_ACCESO_PIN = "PIN"
METODO_ACCESO_HUELLA = "huella"
METODO_ACCESO_TARJETA = "tarjeta"
METODO_ACCESO_INICIAL = METODO_ACCESO_PIN

# ============================================================
# SENSORES - Intervalos de lectura (en segundos)
# ============================================================
INTERVALO_SENSOR_MOVIMIENTO = 2.0  # segundos
INTERVALO_SENSOR_TEMPERATURA = 3.0  # segundos
INTERVALO_SENSOR_APERTURA = 1.5  # segundos

# ============================================================
# SENSORES - Rangos de medición
# ============================================================
TEMP_AMBIENTE_MIN = -10  # °C
TEMP_AMBIENTE_MAX = 40  # °C

# ============================================================
# AUTOMATIZACIÓN - Condiciones temporales
# ============================================================
HORA_INICIO_NOCHE = 20  # 20:00 (8:00 PM)
HORA_FIN_NOCHE = 7  # 07:00 (7:00 AM)

HORA_INICIO_DIA = 8  # 08:00 (8:00 AM)
HORA_FIN_DIA = 19  # 19:00 (7:00 PM)

# ============================================================
# AUTOMATIZACIÓN - Temperaturas de confort
# ============================================================
TEMP_CONFORT_MIN = 18  # °C
TEMP_CONFORT_MAX = 24  # °C
TEMP_CONFORT_OBJETIVO = 22  # °C

# Temperaturas para modos
TEMP_MODO_NOCHE = 20  # °C
TEMP_MODO_AHORRO = 19  # °C
TEMP_MODO_VACACIONES = 15  # °C

# ============================================================
# AUTOMATIZACIÓN - Intervalos de control
# ============================================================
INTERVALO_CONTROL_AUTOMATION = 2.5  # segundos

# ============================================================
# AUTOMATIZACIÓN - Intensidades de luz
# ============================================================
INTENSIDAD_MODO_NOCHE = 30  # %
INTENSIDAD_MODO_DIA = 100  # %
INTENSIDAD_MODO_CINE = 0  # %
INTENSIDAD_MODO_LECTURA = 80  # %

# ============================================================
# HABITACIONES - Capacidad
# ============================================================
MAX_DISPOSITIVOS_HABITACION = 20
MIN_DISPOSITIVOS_HABITACION = 0

# ============================================================
# USUARIOS - Niveles de acceso
# ============================================================
NIVEL_INVITADO = 1
NIVEL_FAMILIAR = 2
NIVEL_PROPIETARIO = 3
NIVEL_ADMIN = 4
NIVEL_SUPER = 5

# ============================================================
# ESCENAS - Prioridades
# ============================================================
PRIORIDAD_BAJA = 1
PRIORIDAD_MEDIA = 2
PRIORIDAD_ALTA = 3
PRIORIDAD_URGENTE = 4

# ============================================================
# THREADING
# ============================================================
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ============================================================
# PERSISTENCIA
# ============================================================
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# ============================================================
# VALIDACIONES - Superficie
# ============================================================
SUPERFICIE_MIN = 0.0  # m²
SUPERFICIE_MAX = 10000.0  # m²

# ============================================================
# VALIDACIONES - Strings
# ============================================================
LONGITUD_MIN_NOMBRE = 1
LONGITUD_MAX_NOMBRE = 100
LONGITUD_MIN_DIRECCION = 5
LONGITUD_MAX_DIRECCION = 200

# ============================================================
# MODOS DEL SISTEMA
# ============================================================
MODO_NOCHE = "noche"
MODO_VACACIONES = "vacaciones"
MODO_FIESTA = "fiesta"
MODO_CINE = "cine"
MODO_AHORRO = "ahorro"
MODO_SEGURIDAD = "seguridad"

# ============================================================
# MENSAJES DE SISTEMA (para logs y prints)
# ============================================================
MSG_SENSOR_INICIADO = "[SENSOR] {tipo} iniciado"
MSG_SENSOR_DETENIDO = "[SENSOR] {tipo} detenido"
MSG_CONTROL_INICIADO = "[CONTROL] Controlador de automatizacion iniciado"
MSG_CONTROL_DETENIDO = "[CONTROL] Controlador de automatizacion detenido"
MSG_DISPOSITIVO_ENCENDIDO = "[DISPOSITIVO] {tipo} ID {id} encendido"
MSG_DISPOSITIVO_APAGADO = "[DISPOSITIVO] {tipo} ID {id} apagado"

# ============================================================
# CONFIGURACIÓN DE SIMULACIÓN
# ============================================================
# Probabilidad de eventos en simulación
PROBABILIDAD_MOVIMIENTO = 0.3  # 30% de probabilidad
PROBABILIDAD_APERTURA = 0.1  # 10% de probabilidad

# Variación de temperatura (en °C)
VARIACION_TEMP_MAX = 2.0  # ±2°C de variación


