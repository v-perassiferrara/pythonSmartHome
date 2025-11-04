"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome
Fecha de generacion: 2025-11-04 15:57:25
Total de archivos integrados: 62
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: ..
#   1.main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: control
#   4. __init__.py
#   5. automation_control_task.py
#
# DIRECTORIO: entidades
#   6. __init__.py
#
# DIRECTORIO: entidades\dispositivos
#   7. __init__.py
#   8. camara_seguridad.py
#   9. cerradura_inteligente.py
#   10. dispositivo.py
#   11. luz_inteligente.py
#   12. termostato.py
#
# DIRECTORIO: entidades\espacios
#   13. __init__.py
#   14. casa.py
#   15. configuracion_casa.py
#   16. habitacion.py
#
# DIRECTORIO: entidades\usuarios
#   17. __init__.py
#   18. escena.py
#   19. nivel_acceso.py
#   20. usuario.py
#
# DIRECTORIO: excepciones
#   21. __init__.py
#   22. capacidad_insuficiente_exception.py
#   23. mensajes_exception.py
#   24. permiso_denegado_exception.py
#   25. persistencia_exception.py
#   26. smarthome_exception.py
#
# DIRECTORIO: patrones
#   27. __init__.py
#
# DIRECTORIO: patrones\factory
#   28. __init__.py
#   29. dispositivo_factory.py
#
# DIRECTORIO: patrones\observer
#   30. __init__.py
#   31. observable.py
#   32. observer.py
#
# DIRECTORIO: patrones\observer\eventos
#   33. __init__.py
#
# DIRECTORIO: patrones\singleton
#   34. __init__.py
#
# DIRECTORIO: patrones\strategy
#   35. __init__.py
#   36. automation_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   37. __init__.py
#   38. climatizacion_strategy.py
#   39. iluminacion_strategy.py
#   40. seguridad_strategy.py
#
# DIRECTORIO: sensores
#   41. __init__.py
#   42. sensor_apertura_task.py
#   43. sensor_movimiento_task.py
#   44. sensor_temperatura_task.py
#
# DIRECTORIO: servicios
#   45. __init__.py
#
# DIRECTORIO: servicios\dispositivos
#   46. __init__.py
#   47. camara_seguridad_service.py
#   48. cerradura_inteligente_service.py
#   49. dispositivo_service.py
#   50. dispositivo_service_registry.py
#   51. luz_inteligente_service.py
#   52. termostato_service.py
#
# DIRECTORIO: servicios\espacios
#   53. __init__.py
#   54. casa_service.py
#   55. configuracion_casa_service.py
#   56. habitacion_service.py
#
# DIRECTORIO: servicios\negocio
#   57. __init__.py
#   58. casa_service.py
#   59. grupo_dispositivos.py
#   60. modo_sistema.py
#
# DIRECTORIO: servicios\usuarios
#   61. __init__.py
#   62. usuario_service.py
#



################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 1/62: main.py
# Directorio: ..
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\main.py
# ==============================================================================

"""
Sistema de Domótica (Smart Home) - Demostración Completa

Este archivo demuestra el funcionamiento de todos los patrones de diseño:
- SINGLETON: DispositivoServiceRegistry (instancia única)
- FACTORY METHOD: DispositivoFactory (creación sin conocer clases concretas)
- OBSERVER: Sensores y automatización (notificaciones push)
- STRATEGY: Algoritmos de automatización (intercambiables en runtime)
- REGISTRY: Dispatch polimórfico (sin isinstance cascades)

Autor: Valentino Perassi Ferrara
Fecha: Octubre 2025
"""

import time
from datetime import date

from python_smarthome.constantes import THREAD_JOIN_TIMEOUT

# Servicios
from python_smarthome.servicios.espacios.casa_service import CasaService
from python_smarthome.servicios.espacios.habitacion_service import HabitacionService
from python_smarthome.servicios.espacios.configuracion_casa_service import ConfiguracionCasaService
from python_smarthome.servicios.usuarios.usuario_service import UsuarioService
from python_smarthome.servicios.negocio.casa_service import CasaService as CasaNegocioService
from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry

# Entidades
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
from python_smarthome.entidades.usuarios.usuario import Usuario
from python_smarthome.entidades.usuarios.escena import Escena
from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato

# Sensores y control
from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
from python_smarthome.control.automation_control_task import AutomationControlTask

# Excepciones
from python_smarthome.excepciones.smarthome_exception import SmartHomeException


def print_header(titulo: str) -> None:
    """Imprime encabezado formateado."""
    print()
    print("=" * 70)
    print(f"  {titulo}")
    print("=" * 70)
    print()


def print_section(titulo: str) -> None:
    """Imprime sección formateada."""
    print()
    print("-" * 70)
    print(f"  {titulo}")
    print("-" * 70)


def main():
    """Función principal de demostración."""
    
    print_header("SISTEMA DE DOMOTICA - PATRONES DE DISENO")
    print("Este sistema demuestra 5 patrones de diseño:")
    print("  1. SINGLETON   - Una sola instancia compartida")
    print("  2. FACTORY     - Creacion sin conocer clases concretas")
    print("  3. OBSERVER    - Notificaciones automaticas")
    print("  4. STRATEGY    - Algoritmos intercambiables")
    print("  5. REGISTRY    - Dispatch polimorfico sin isinstance")
    
    # ================================================================
    # 1. PATRON SINGLETON: Verificar instancia única
    # ================================================================
    print_section("PATRON SINGLETON: Verificando instancia unica")
    
    print("Creando dos referencias al registry...")
    registry1 = DispositivoServiceRegistry()
    registry2 = DispositivoServiceRegistry.get_instance()
    
    print(f"registry1 ID: {id(registry1)}")
    print(f"registry2 ID: {id(registry2)}")
    
    if registry1 is registry2:
        print("[OK] SINGLETON FUNCIONA: Ambas referencias apuntan a la MISMA instancia")
        print("     Thread-safe con double-checked locking")
    else:
        print("[ERROR] Singleton no funciona correctamente")
        return
    
    # ================================================================
    # 2. Crear casa con habitaciones
    # ================================================================
    print_section("1. Creando casa con habitaciones")
    
    casa_service = CasaService()
    casa = casa_service.crear_casa_con_habitaciones(
        direccion="Calle Falsa 123",
        superficie=150.0,
        propietario="Juan Perez",
        nombres_habitaciones=["Living", "Cocina", "Dormitorio"]
    )
    
    print(f"Casa creada: {casa.get_direccion()}")
    print(f"Superficie: {casa.get_superficie()} m2")
    print(f"Propietario: {casa.get_propietario()}")
    print(f"Habitaciones: {len(casa.get_habitaciones())}")
    for hab in casa.get_habitaciones():
        print(f"  - {hab.get_nombre()}")
    
    # ================================================================
    # 3. PATRON FACTORY: Instalar dispositivos
    # ================================================================
    print_section("2. PATRON FACTORY: Instalando dispositivos")
    print("DEMOSTRACION: El cliente NO conoce clases concretas")
    print("              Solo pide tipo (string) y Factory crea la instancia")
    
    habitacion_service = HabitacionService()
    habitaciones = casa.get_habitaciones()
    living = habitaciones[0]
    
    print(f"\nInstalando en: {living.get_nombre()}")
    print("-" * 40)
    
    # Factory Method se usa internamente en instalar()
    habitacion_service.instalar(living, "LuzInteligente", 3)
    print()
    habitacion_service.instalar(living, "Termostato", 1)
    print()
    habitacion_service.instalar(living, "CamaraSeguridad", 1)
    print()
    habitacion_service.instalar(living, "CerraduraInteligente", 1)
    
    print(f"\n[OK] Dispositivos instalados: {len(living.get_dispositivos())}")
    print("     FACTORY METHOD permite agregar nuevos tipos sin modificar codigo")
    
    # ================================================================
    # 4. PATRON REGISTRY: Mostrar datos de dispositivos
    # ================================================================
    print_section("3. PATRON REGISTRY: Dispatch polimorfico")
    print("DEMOSTRACION: Registry despacha al servicio correcto SIN isinstance()")
    
    print("\nMostrando primeros 3 dispositivos:")
    for i, dispositivo in enumerate(living.get_dispositivos()[:3], 1):
        print(f"\n--- Dispositivo {i} ---")
        # Registry hace dispatch automático según tipo
        registry1.mostrar_datos(dispositivo)
    
    print("\n[OK] REGISTRY funciona: Lookup O(1) sin cascadas de isinstance()")
    
    # ================================================================
    # 5. PATRON STRATEGY: Demostración explícita
    # ================================================================
    print_section("4. PATRON STRATEGY: Algoritmos intercambiables")
    print("DEMOSTRACION: Servicios usan estrategias inyectadas para automatizacion")
    
    from python_smarthome.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
    from python_smarthome.servicios.dispositivos.termostato_service import TermostatoService
    
    luz_service = LuzInteligenteService()
    termostato_service = TermostatoService()
    
    print(f"\nLuzInteligenteService usa: {type(luz_service.get_estrategia()).__name__}")
    print(f"TermostatoService usa: {type(termostato_service.get_estrategia()).__name__}")
    
    print("\nEjecutando automatizacion en primera luz...")
    luz = living.get_dispositivos()[0]
    luz_service.ejecutar_automatizacion(luz, None)
    print(f"Intensidad ajustada a: {luz.get_intensidad()}% (segun estrategia)")
    
    print("\n[OK] STRATEGY funciona: Algoritmos intercambiables sin modificar servicios")
    
    # ================================================================
    # 6. Crear usuarios con escenas
    # ================================================================
    print_section("5. Creando usuarios con escenas")
    
    escenas = [
        Escena(1, "Modo Noche", "Luces tenues, termostato bajo"),
        Escena(2, "Modo Cine", "Luces apagadas"),
        Escena(3, "Modo Vacaciones", "Todo apagado, camaras activas")
    ]
    
    usuario = Usuario(
        id_usuario=1,
        nombre="Juan Perez",
        nivel_acceso=NivelAcceso.PROPIETARIO,
        escenas=escenas
    )
    
    print(f"Usuario creado: {usuario.get_nombre()}")
    print(f"Nivel de acceso: {usuario.get_nivel_acceso().name} (valor: {usuario.get_nivel_acceso().value})")
    print(f"Escenas asignadas: {len(usuario.get_escenas())}")
    for escena in usuario.get_escenas():
        print(f"  - {escena.get_nombre()}: {escena.get_descripcion()}")
    
    # ================================================================
    # 7. PATRON OBSERVER: Sistema de sensores
    # ================================================================
    print_section("6. PATRON OBSERVER: Sistema de sensores")
    print("DEMOSTRACION: Sensores notifican automaticamente al controlador")
    
    # Crear sensores (Observable)
    sensor_mov = SensorMovimientoTask()
    sensor_temp = SensorTemperaturaTask()
    
    # Crear controlador (Observer)
    automation_control = AutomationControlTask(
        sensor_mov,
        sensor_temp,
        living,
        habitacion_service
    )
    
    print("\nArquitectura OBSERVER:")
    print("  SensorMovimientoTask (Observable[bool])")
    print("  SensorTemperaturaTask (Observable[float])")
    print("  AutomationControlTask (Observer[bool] y Observer[float])")
    
    # Iniciar threads daemon
    sensor_mov.start()
    sensor_temp.start()
    automation_control.start()
    
    print("\n[OK] Sistema de sensores iniciado (3 threads daemon)")
    print("     Sensores notifican AUTOMATICAMENTE al controlador")
    print("     Esperando 10 segundos para observar automatizacion...")
    
    time.sleep(10)
    
    # ================================================================
    # 8. Detener sistema de sensores
    # ================================================================
    print_section("7. Deteniendo sistema de sensores")
    
    print("Enviando señal de detencion (graceful shutdown)...")
    sensor_mov.detener()
    sensor_temp.detener()
    automation_control.detener()
    
    print("Esperando finalizacion de threads...")
    sensor_mov.join(timeout=THREAD_JOIN_TIMEOUT)
    sensor_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    automation_control.join(timeout=THREAD_JOIN_TIMEOUT)
    
    print("[OK] Sistema de sensores detenido correctamente")
    print("     Graceful shutdown con threading.Event")
    
    # ================================================================
    # 9. Persistencia
    # ================================================================
    print_section("8. Persistiendo configuracion en disco")
    
    config = ConfiguracionCasa(
        id_config=1,
        casa=casa,
        fecha_instalacion=date.today(),
        propietario="Juan Perez"
    )
    
    config_service = ConfiguracionCasaService()
    
    try:
        config_service.persistir(config)
        print("[OK] Configuracion guardada en data/Juan Perez.dat")
    except SmartHomeException as e:
        print(f"[ERROR] {e.get_user_message()}")
    
    # ================================================================
    # 10. Recuperar configuración
    # ================================================================
    print_section("9. Recuperando configuracion desde disco")
    
    try:
        config_leida = ConfiguracionCasaService.leer_configuracion("Juan Perez")
        config_service.mostrar_datos(config_leida)
        print("[OK] Configuracion recuperada exitosamente")
    except SmartHomeException as e:
        print(f"[ERROR] {e.get_user_message()}")
    
    # ================================================================
    # 11. Agrupar dispositivos por tipo (Generics)
    # ================================================================
    print_section("10. Agrupando dispositivos por tipo (Generics)")
    
    casa_negocio_service = CasaNegocioService()
    casa_negocio_service.add_casa(config)
    
    print("\nAgrupando con type-safety (Generic[T])...")
    
    # Agrupar todas las luces
    grupo_luces = casa_negocio_service.agrupar_por_tipo(LuzInteligente)
    grupo_luces.mostrar_contenido_grupo()
    
    # Agrupar todos los termostatos
    grupo_termostatos = casa_negocio_service.agrupar_por_tipo(Termostato)
    grupo_termostatos.mostrar_contenido_grupo()
    
    print("[OK] Agrupacion generica tipo-segura completada")
    
    # ================================================================
    # Resumen final
    # ================================================================
    print_header("DEMOSTRACION COMPLETADA EXITOSAMENTE")
    
    print("PATRONES DE DISEÑO IMPLEMENTADOS:")
    print()
    print("  [OK] SINGLETON   - DispositivoServiceRegistry")
    print("       * Instancia unica compartida (thread-safe)")
    print("       * Double-checked locking con Lock")
    print()
    print("  [OK] FACTORY     - DispositivoFactory")
    print("       * Creacion sin conocer clases concretas")
    print("       * Facil extension (Open/Closed)")
    print()
    print("  [OK] OBSERVER    - Sistema de sensores")
    print("       * Notificaciones push automaticas")
    print("       * Tipo-seguro con Generics (Observable[T])")
    print()
    print("  [OK] STRATEGY    - Algoritmos de automatizacion")
    print("       * Estrategias inyectadas en constructores")
    print("       * Intercambiables en runtime")
    print()
    print("  [OK] REGISTRY    - Dispatch polimorfico")
    print("       * Sin cascadas de isinstance()")
    print("       * Lookup O(1) con diccionarios")
    
    print()
    print("PRINCIPIOS SOLID APLICADOS:")
    print("  * Single Responsibility: Entidades vs Servicios")
    print("  * Open/Closed: Factory permite extension")
    print("  * Liskov Substitution: Dispositivos intercambiables")
    print("  * Interface Segregation: Observer[T], Strategy ABC")
    print("  * Dependency Inversion: Servicios dependen de abstracciones")
    
    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()

################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 2/62: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/62: constantes.py
# Directorio: .
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\constantes.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: control
################################################################################

# ==============================================================================
# ARCHIVO 4/62: __init__.py
# Directorio: control
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/62: automation_control_task.py
# Directorio: control
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\control\automation_control_task.py
# ==============================================================================

"""Controlador de automatización - Thread + OBSERVER pattern."""

import threading
import time
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
    from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
    from python_smarthome.entidades.espacios.habitacion import Habitacion
    from python_smarthome.servicios.espacios.habitacion_service import HabitacionService

from python_smarthome.patrones.observer.observer import Observer
from python_smarthome.constantes import (
    INTERVALO_CONTROL_AUTOMATION,
    HORA_INICIO_NOCHE,
    HORA_FIN_NOCHE,
    TEMP_CONFORT_MIN,
    TEMP_CONFORT_MAX
)


class AutomationControlTask(threading.Thread, Observer):
    """
    Controlador de automatización.
    
    Thread daemon que observa sensores y ejecuta acciones automáticas.
    Implementa OBSERVER pattern (observa movimiento y temperatura).
    """

    def __init__(
        self,
        sensor_movimiento: 'SensorMovimientoTask',
        sensor_temperatura: 'SensorTemperaturaTask',
        habitacion: 'Habitacion',
        habitacion_service: 'HabitacionService'
    ):
        """
        Inicializa controlador.
        
        Args:
            sensor_movimiento: Sensor de movimiento (Observable[bool])
            sensor_temperatura: Sensor de temperatura (Observable[float])
            habitacion: Habitación a controlar
            habitacion_service: Servicio de habitación
        """
        threading.Thread.__init__(self, daemon=True)
        
        # Inyección de dependencias
        self._sensor_movimiento = sensor_movimiento
        self._sensor_temperatura = sensor_temperatura
        self._habitacion = habitacion
        self._habitacion_service = habitacion_service
        
        # Estado interno
        self._ultimo_movimiento: bool = False
        self._ultima_temperatura: float = 22.0
        self._detenido = threading.Event()
        
        # Suscribirse a sensores (OBSERVER)
        self._sensor_movimiento.agregar_observador(self)
        self._sensor_temperatura.agregar_observador(self)

    def actualizar(self, evento: Any) -> None:
        """
        Recibe notificaciones de sensores (OBSERVER).
        
        Args:
            evento: bool (movimiento) o float (temperatura)
        """
        if isinstance(evento, bool):
            # Movimiento
            self._ultimo_movimiento = evento
        elif isinstance(evento, float):
            # Temperatura
            self._ultima_temperatura = evento

    def run(self) -> None:
        """Loop principal del controlador."""
        print("[CONTROL] Controlador de automatizacion iniciado")
        
        while not self._detenido.is_set():
            self._evaluar_y_ejecutar()
            time.sleep(INTERVALO_CONTROL_AUTOMATION)
        
        print("[CONTROL] Controlador de automatizacion detenido")

    def _evaluar_y_ejecutar(self) -> None:
        """Evalúa condiciones y ejecuta acciones."""
        hora_actual = datetime.now().hour
        es_modo_noche = (HORA_INICIO_NOCHE <= hora_actual) or (hora_actual <= HORA_FIN_NOCHE)
        
        # Condición 1: Movimiento detectado en modo noche
        if self._ultimo_movimiento and es_modo_noche:
            print(f"[CONTROL] Movimiento en modo noche - Ajustando luces")
            self._habitacion_service.ajustar_luces_modo_noche(self._habitacion)
        
        # Condición 2: Temperatura fuera de rango confort
        if not (TEMP_CONFORT_MIN <= self._ultima_temperatura <= TEMP_CONFORT_MAX):
            print(f"[CONTROL] Temp fuera de confort ({self._ultima_temperatura}C) - Ajustando")
            self._habitacion_service.ajustar_climatizacion(self._habitacion)

    def detener(self) -> None:
        """Detiene el controlador de forma graceful."""
        self._detenido.set()


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 6/62: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\dispositivos
################################################################################

# ==============================================================================
# ARCHIVO 7/62: __init__.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 8/62: camara_seguridad.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\camara_seguridad.py
# ==============================================================================

"""Entidad CamaraSeguridad - Dispositivo de vigilancia."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    RESOLUCION_INICIAL,
    DETECCION_MOVIMIENTO_INICIAL
)


class CamaraSeguridad(Dispositivo):
    """
    Cámara de seguridad con detección de movimiento.
    
    Attributes:
        _resolucion: Resolución de video (e.g., "1080p")
        _deteccion_movimiento: Estado de la detección de movimiento
        _grabacion: Estado de la grabación
    """

    def __init__(self):
        """Inicializa cámara con valores por defecto."""
        super().__init__()
        self._resolucion: str = RESOLUCION_INICIAL
        self._deteccion_movimiento: bool = DETECCION_MOVIMIENTO_INICIAL
        self._grabacion: bool = False

    def get_resolucion(self) -> str:
        """Obtiene la resolución de video."""
        return self._resolucion

    def set_resolucion(self, resolucion: str) -> None:
        """Establece la resolución de video."""
        self._resolucion = resolucion

    def is_deteccion_movimiento_activa(self) -> bool:
        """Verifica si la detección de movimiento está activa."""
        return self._deteccion_movimiento

    def set_deteccion_movimiento(self, activa: bool) -> None:
        """Activa o desactiva la detección de movimiento."""
        self._deteccion_movimiento = activa

    def is_grabando(self) -> bool:
        """Verifica si la cámara está grabando."""
        return self._grabacion

    def set_grabacion(self, grabando: bool) -> None:
        """Inicia o detiene la grabación."""
        self._grabacion = grabando


# ==============================================================================
# ARCHIVO 9/62: cerradura_inteligente.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\cerradura_inteligente.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 10/62: dispositivo.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\dispositivo.py
# ==============================================================================

"""Interfaz base para todos los dispositivos."""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Dispositivo(ABC):
    """
    Clase base abstracta para dispositivos IoT.
    
    Attributes:
        _id_dispositivo: ID único del dispositivo
        _encendido: Estado on/off del dispositivo
    """

    _contador_id: int = 0

    def __init__(self):
        """Inicializa dispositivo con ID único."""
        Dispositivo._contador_id += 1
        self._id_dispositivo: int = Dispositivo._contador_id
        self._encendido: bool = False

    def get_id_dispositivo(self) -> int:
        """
        Obtiene ID del dispositivo.
        
        Returns:
            ID único
        """
        return self._id_dispositivo

    def is_encendido(self) -> bool:
        """
        Verifica si dispositivo está encendido.
        
        Returns:
            True si está encendido
        """
        return self._encendido

    def set_encendido(self, encendido: bool) -> None:
        """
        Establece estado del dispositivo.
        
        Args:
            encendido: True para encender, False para apagar
        """
        self._encendido = encendido


# ==============================================================================
# ARCHIVO 11/62: luz_inteligente.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\luz_inteligente.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 12/62: termostato.py
# Directorio: entidades\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\dispositivos\termostato.py
# ==============================================================================

"""Entidad Termostato - Dispositivo de climatización."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    TEMP_MIN,
    TEMP_MAX,
    TEMP_OBJETIVO_INICIAL
)


class Termostato(Dispositivo):
    """
    Termostato inteligente con control de temperatura.
    
    Attributes:
        _temperatura_objetivo: Temperatura deseada (°C)
    """

    def __init__(self):
        """Inicializa termostato con valores por defecto."""
        super().__init__()
        self._temperatura_objetivo: float = TEMP_OBJETIVO_INICIAL

    def get_temperatura_objetivo(self) -> float:
        """
        Obtiene temperatura objetivo.
        
        Returns:
            Temperatura objetivo (°C)
        """
        return self._temperatura_objetivo

    def set_temperatura_objetivo(self, temperatura: float) -> None:
        """
        Establece temperatura objetivo.
        
        Args:
            temperatura: Temperatura objetivo (°C)
            
        Raises:
            ValueError: Si temperatura fuera de rango
        """
        if not (TEMP_MIN <= temperatura <= TEMP_MAX):
            raise ValueError(
                f"Temperatura debe estar entre {TEMP_MIN} y {TEMP_MAX}"
            )
        self._temperatura_objetivo = temperatura



################################################################################
# DIRECTORIO: entidades\espacios
################################################################################

# ==============================================================================
# ARCHIVO 13/62: __init__.py
# Directorio: entidades\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/62: casa.py
# Directorio: entidades\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\casa.py
# ==============================================================================

"""Entidad Casa - Representa una propiedad."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion
    from python_smarthome.entidades.usuarios.usuario import Usuario


class Casa:
    """
    Representa una casa con dirección, superficie y habitaciones.
    
    Attributes:
        _direccion: Dirección de la casa
        _superficie: Superficie en m²
        _propietario: Nombre del propietario
        _habitaciones: Lista de habitaciones en la casa
        _usuarios: Lista de usuarios autorizados
    """

    def __init__(self, direccion: str, superficie: float, propietario: str):
        self._direccion = direccion
        self._superficie = superficie
        self._propietario = propietario
        self._habitaciones: List['Habitacion'] = []
        self._usuarios: List['Usuario'] = []

    def get_direccion(self) -> str:
        return self._direccion

    def get_superficie(self) -> float:
        return self._superficie

    def get_propietario(self) -> str:
        return self._propietario

    def get_habitaciones(self) -> List['Habitacion']:
        return self._habitaciones.copy()  # Defensive copy

    def set_habitaciones(self, habitaciones: List['Habitacion']) -> None:
        self._habitaciones = habitaciones

    def get_usuarios(self) -> List['Usuario']:
        return self._usuarios.copy()  # Defensive copy

    def set_usuarios(self, usuarios: List['Usuario']) -> None:
        self._usuarios = usuarios


# ==============================================================================
# ARCHIVO 15/62: configuracion_casa.py
# Directorio: entidades\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\configuracion_casa.py
# ==============================================================================

"""Entidad ConfiguracionCasa - Agrupa toda la configuración de una casa."""

from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.casa import Casa


class ConfiguracionCasa:
    """
    Agrupa la configuración completa de una casa inteligente.
    
    Attributes:
        _id_config: ID de la configuración
        _casa: La casa configurada
        _fecha_instalacion: Fecha de instalación
        _propietario: Propietario de la configuración
    """

    def __init__(self, id_config: int, casa: 'Casa', fecha_instalacion: date, propietario: str):
        self._id_config = id_config
        self._casa = casa
        self._fecha_instalacion = fecha_instalacion
        self._propietario = propietario

    def get_id_config(self) -> int:
        return self._id_config

    def get_casa(self) -> 'Casa':
        return self._casa

    def get_fecha_instalacion(self) -> date:
        return self._fecha_instalacion

    def get_propietario(self) -> str:
        return self._propietario


# ==============================================================================
# ARCHIVO 16/62: habitacion.py
# Directorio: entidades\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\espacios\habitacion.py
# ==============================================================================

"""Entidad Habitacion - Representa un espacio dentro de una casa."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class Habitacion:
    """
    Representa una habitación con un nombre y dispositivos.
    
    Attributes:
        _nombre: Nombre de la habitación
        _dispositivos: Lista de dispositivos en la habitación
    """

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List['Dispositivo'] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List['Dispositivo']:
        return self._dispositivos.copy()  # Defensive copy

    def agregar_dispositivo(self, dispositivo: 'Dispositivo') -> None:
        self._dispositivos.append(dispositivo)

    def agregar_dispositivos(self, dispositivos: List['Dispositivo']) -> None:
        self._dispositivos.extend(dispositivos)



################################################################################
# DIRECTORIO: entidades\usuarios
################################################################################

# ==============================================================================
# ARCHIVO 17/62: __init__.py
# Directorio: entidades\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/62: escena.py
# Directorio: entidades\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\escena.py
# ==============================================================================

"""Entidad Escena - Representa una rutina o configuración guardada."""


class Escena:
    """
    Representa una escena que agrupa una serie de acciones.
    
    Attributes:
        _id_escena: ID de la escena
        _nombre: Nombre de la escena
        _descripcion: Descripción de la escena
    """

    def __init__(self, id_escena: int, nombre: str, descripcion: str):
        self._id_escena = id_escena
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id_escena(self) -> int:
        return self._id_escena

    def get_nombre(self) -> str:
        return self._nombre

    def get_descripcion(self) -> str:
        return self._descripcion


# ==============================================================================
# ARCHIVO 19/62: nivel_acceso.py
# Directorio: entidades\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\nivel_acceso.py
# ==============================================================================

"""Enum NivelAcceso - Define los niveles de permiso en el sistema."""

from enum import Enum


class NivelAcceso(Enum):
    """
    Enumeración para los niveles de acceso de usuario.
    """
    INVITADO = 1
    FAMILIAR = 2
    PROPIETARIO = 3
    ADMIN = 4
    SUPER = 5


# ==============================================================================
# ARCHIVO 20/62: usuario.py
# Directorio: entidades\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\entidades\usuarios\usuario.py
# ==============================================================================

"""Entidad Usuario - Representa un usuario del sistema."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.usuarios.escena import Escena
    from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso


class Usuario:
    """
    Representa un usuario del sistema con su nivel de acceso y escenas.
    
    Attributes:
        _id_usuario: ID del usuario
        _nombre: Nombre del usuario
        _nivel_acceso: Nivel de acceso del usuario
        _escenas: Lista de escenas asignadas al usuario
    """

    def __init__(self, id_usuario: int, nombre: str, nivel_acceso: 'NivelAcceso', escenas: List['Escena']):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._nivel_acceso = nivel_acceso
        self._escenas = escenas

    def get_id_usuario(self) -> int:
        return self._id_usuario

    def get_nombre(self) -> str:
        return self._nombre

    def get_nivel_acceso(self) -> 'NivelAcceso':
        return self._nivel_acceso

    def get_escenas(self) -> List['Escena']:
        return self._escenas.copy()  # Defensive copy



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 21/62: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/62: capacidad_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\capacidad_insuficiente_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 23/62: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\mensajes_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 24/62: permiso_denegado_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\permiso_denegado_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 25/62: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\persistencia_exception.py
# ==============================================================================

"""Excepción de persistencia."""

from python_smarthome.excepciones.smarthome_exception import SmartHomeException
from python_smarthome.excepciones.mensajes_exception import MensajesException


class PersistenciaException(SmartHomeException):
    """
    Excepción lanzada cuando hay un error de lectura o escritura en disco.
    """

    def __init__(self, mensaje_usuario: str, mensaje_tecnico: str):
        super().__init__(mensaje_usuario, mensaje_tecnico)


# ==============================================================================
# ARCHIVO 26/62: smarthome_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\excepciones\smarthome_exception.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 27/62: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 28/62: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/62: dispositivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\factory\dispositivo_factory.py
# ==============================================================================

"""Factory para crear dispositivos - FACTORY METHOD pattern."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class DispositivoFactory:
    """
    Factory para crear dispositivos sin conocer clases concretas.
    
    Implementa FACTORY METHOD pattern.
    """

    @staticmethod
    def crear_dispositivo(tipo: str) -> 'Dispositivo':
        """
        Crea dispositivo según tipo especificado.
        
        Args:
            tipo: Tipo de dispositivo ("LuzInteligente", "Termostato", etc.)
            
        Returns:
            Instancia de Dispositivo
            
        Raises:
            ValueError: Si tipo desconocido
        """
        # Diccionario de factories (NO if/elif cascades)
        factories = {
            "LuzInteligente": DispositivoFactory._crear_luz,
            "Termostato": DispositivoFactory._crear_termostato,
            "CamaraSeguridad": DispositivoFactory._crear_camara,
            "CerraduraInteligente": DispositivoFactory._crear_cerradura
        }

        if tipo not in factories:
            raise ValueError(f"Tipo desconocido: {tipo}")

        return factories[tipo]()

    @staticmethod
    def _crear_luz() -> 'Dispositivo':
        """Crea luz inteligente."""
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        return LuzInteligente()

    @staticmethod
    def _crear_termostato() -> 'Dispositivo':
        """Crea termostato."""
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        return Termostato()

    @staticmethod
    def _crear_camara() -> 'Dispositivo':
        """Crea cámara de seguridad."""
        from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
        return CamaraSeguridad()

    @staticmethod
    def _crear_cerradura() -> 'Dispositivo':
        """Crea cerradura inteligente."""
        from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente
        return CerraduraInteligente()



################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 30/62: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/62: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\observable.py
# ==============================================================================

"""Clase base Observable - OBSERVER pattern."""

from typing import Generic, TypeVar, List, TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from python_smarthome.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase base para objetos observables.
    
    Implementa OBSERVER pattern con tipo-seguridad mediante Generics.
    
    Type Parameters:
        T: Tipo de evento que emite (ej. float para temperatura)
    """

    def __init__(self):
        """Inicializa lista de observadores."""
        self._observadores: List['Observer[T]'] = []

    def agregar_observador(self, observador: 'Observer[T]') -> None:
        """
        Agrega un observador a la lista.
        
        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        """
        Elimina un observador de la lista.
        
        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores.
        
        Args:
            evento: Evento a notificar (tipo T)
        """
        for observador in self._observadores:
            observador.actualizar(evento)


# ==============================================================================
# ARCHIVO 32/62: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\observer.py
# ==============================================================================

"""Interfaz Observer - OBSERVER pattern."""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz para observadores.
    
    Type Parameters:
        T: Tipo de evento que recibe (ej. bool para movimiento)
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica.
        
        Args:
            evento: Evento recibido (tipo T)
        """
        pass



################################################################################
# DIRECTORIO: patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 33/62: __init__.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\observer\eventos\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 34/62: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 35/62: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/62: automation_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\automation_strategy.py
# ==============================================================================

"""Interfaz Strategy para automatización - STRATEGY pattern."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo


class AutomationStrategy(ABC):
    """
    Interfaz para estrategias de automatización.
    
    Implementa STRATEGY pattern.
    """

    @abstractmethod
    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Dispositivo', 
        evento: Any
    ) -> None:
        """
        Ejecuta acción de automatización.
        
        Args:
            fecha: Fecha/hora actual
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        pass



################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 37/62: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 38/62: climatizacion_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\climatizacion_strategy.py
# ==============================================================================

"""Estrategia de climatización - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import TEMP_CONFORT_OBJETIVO


class ClimatizacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para termostatos.
    
    Ajusta la temperatura a un valor de confort.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Termostato',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de climatización.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Termostato a controlar
            evento: Evento disparador (ignorado)
        """
        dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)


# ==============================================================================
# ARCHIVO 39/62: iluminacion_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\iluminacion_strategy.py
# ==============================================================================

"""Estrategia de iluminación - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy
from python_smarthome.constantes import (
    HORA_INICIO_NOCHE,
    HORA_FIN_NOCHE
)


class IluminacionStrategy(AutomationStrategy):
    """
    Estrategia de automatización para luces inteligentes.
    
    Ajusta intensidad según hora del día.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'LuzInteligente',
        evento: Any
    ) -> None:
        """
        Ejecuta acción de iluminación.
        
        Modo noche (20:00-07:00): Intensidad 30%
        Modo día: Intensidad 100%
        
        Args:
            fecha: Fecha/hora actual
            dispositivo: Luz a controlar
            evento: Evento disparador (ignorado)
        """
        hora = fecha.hour
        
        # Verificar si es modo noche
        es_modo_noche = (HORA_INICIO_NOCHE <= hora) or (hora <= HORA_FIN_NOCHE)
        
        if es_modo_noche:
            dispositivo.set_intensidad(30)  # 30% en modo noche
        else:
            dispositivo.set_intensidad(100)  # 100% de día


# ==============================================================================
# ARCHIVO 40/62: seguridad_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\patrones\strategy\impl\seguridad_strategy.py
# ==============================================================================

"""Estrategia de seguridad - STRATEGY pattern."""

from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class SeguridadStrategy(AutomationStrategy):
    """
    Estrategia de automatización para dispositivos de seguridad.
    """

    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: Any,
        evento: Any
    ) -> None:
        """
        Ejecuta acción de seguridad.
        
        Args:
            fecha: Fecha/hora actual (ignorado)
            dispositivo: Dispositivo a controlar
            evento: Evento disparador (ignorado)
        """
        # Para cámaras, enciende la grabación
        if hasattr(dispositivo, 'set_grabacion'):
            dispositivo.set_grabacion(True)
        
        # Para cerraduras, las bloquea
        if hasattr(dispositivo, 'bloquear'):
            dispositivo.bloquear()



################################################################################
# DIRECTORIO: sensores
################################################################################

# ==============================================================================
# ARCHIVO 41/62: __init__.py
# Directorio: sensores
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/62: sensor_apertura_task.py
# Directorio: sensores
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_apertura_task.py
# ==============================================================================

"""Sensor de apertura - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import INTERVALO_SENSOR_APERTURA


class SensorAperturaTask(threading.Thread, Observable[bool]):
    """
    Sensor de apertura que detecta si una puerta o ventana está abierta.
    
    Thread daemon que notifica detecciones cada INTERVALO_SENSOR_APERTURA segundos.
    Implementa OBSERVER pattern como Observable[bool].
    """

    def __init__(self):
        """Inicializa sensor de apertura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de apertura iniciado")
        
        while not self._detenido.is_set():
            # Detectar apertura (aleatorio para simulación)
            apertura = self._detectar_apertura()
            
            # Notificar a observadores
            self.notificar_observadores(apertura)
            
            if apertura:
                print(f"[SENSOR] Apertura detectada: {apertura}")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_APERTURA)
        
        print("[SENSOR] Sensor de apertura detenido")

    def _detectar_apertura(self) -> bool:
        """
        Detecta apertura (simulación).
        
        Returns:
            True si hay apertura, False si no
        """
        return random.choice([True, False])

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()


# ==============================================================================
# ARCHIVO 43/62: sensor_movimiento_task.py
# Directorio: sensores
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_movimiento_task.py
# ==============================================================================

"""Sensor de movimiento - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import INTERVALO_SENSOR_MOVIMIENTO


class SensorMovimientoTask(threading.Thread, Observable[bool]):
    """
    Sensor de movimiento que detecta presencia.
    
    Thread daemon que notifica detecciones cada INTERVALO_SENSOR_MOVIMIENTO segundos.
    Implementa OBSERVER pattern como Observable[bool].
    """

    def __init__(self):
        """Inicializa sensor de movimiento."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de movimiento iniciado")
        
        while not self._detenido.is_set():
            # Detectar movimiento (aleatorio para simulación)
            movimiento = self._detectar_movimiento()
            
            # Notificar a observadores
            self.notificar_observadores(movimiento)
            
            if movimiento:
                print(f"[SENSOR] Movimiento detectado: {movimiento}")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_MOVIMIENTO)
        
        print("[SENSOR] Sensor de movimiento detenido")

    def _detectar_movimiento(self) -> bool:
        """
        Detecta movimiento (simulación).
        
        Returns:
            True si hay movimiento, False si no
        """
        return random.choice([True, False])

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()


# ==============================================================================
# ARCHIVO 44/62: sensor_temperatura_task.py
# Directorio: sensores
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\sensores\sensor_temperatura_task.py
# ==============================================================================

"""Sensor de temperatura - Thread + OBSERVER pattern."""

import threading
import time
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from python_smarthome.patrones.observer.observable import Observable
from python_smarthome.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_AMBIENTE_MIN,
    TEMP_AMBIENTE_MAX
)


class SensorTemperaturaTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura que mide la temperatura ambiente.
    
    Thread daemon que notifica mediciones cada INTERVALO_SENSOR_TEMPERATURA segundos.
    Implementa OBSERVER pattern como Observable[float].
    """

    def __init__(self):
        """Inicializa sensor de temperatura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        print("[SENSOR] Sensor de temperatura iniciado")
        
        while not self._detenido.is_set():
            # Medir temperatura (aleatorio para simulación)
            temperatura = self._medir_temperatura()
            
            # Notificar a observadores
            self.notificar_observadores(temperatura)
            
            print(f"[SENSOR] Temperatura medida: {temperatura:.2f}°C")
            
            # Esperar intervalo
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
        
        print("[SENSOR] Sensor de temperatura detenido")

    def _medir_temperatura(self) -> float:
        """
        Mide la temperatura (simulación).
        
        Returns:
            Temperatura en °C
        """
        return random.uniform(TEMP_AMBIENTE_MIN, TEMP_AMBIENTE_MAX)

    def detener(self) -> None:
        """Detiene el sensor de forma graceful."""
        self._detenido.set()



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 45/62: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\dispositivos
################################################################################

# ==============================================================================
# ARCHIVO 46/62: __init__.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/62: camara_seguridad_service.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\camara_seguridad_service.py
# ==============================================================================

"""Servicio para gestionar cámaras de seguridad."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CamaraSeguridadService(DispositivoService):
    """
    Servicio para operaciones sobre cámaras de seguridad.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, camara: 'CamaraSeguridad') -> None:
        """
        Muestra datos de una cámara de seguridad.
        
        Args:
            camara: Cámara a mostrar
        """
        super().mostrar_datos(camara)  # Datos comunes (ID, estado, tipo)
        print(f"Resolución: {camara.get_resolucion()}")
        print(f"Detección de Movimiento: {'activa' if camara.is_deteccion_movimiento_activa() else 'inactiva'}")
        print(f"Grabando: {'sí' if camara.is_grabando() else 'no'}")

    def encender(self, camara: 'CamaraSeguridad') -> None:
        """
        Enciende la cámara y la grabación.
        
        Args:
            camara: Cámara a encender
        """
        camara.set_encendido(True)
        camara.set_grabacion(True)

    def apagar(self, camara: 'CamaraSeguridad') -> None:
        """
        Apaga la cámara y la grabación.
        
        Args:
            camara: Cámara a apagar
        """
        camara.set_encendido(False)
        camara.set_grabacion(False)

# ==============================================================================
# ARCHIVO 48/62: cerradura_inteligente_service.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\cerradura_inteligente_service.py
# ==============================================================================

"""Servicio para gestionar cerraduras inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.seguridad_strategy import SeguridadStrategy


class CerraduraInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre cerraduras inteligentes.
    
    Usa estrategia de seguridad para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de seguridad."""
        super().__init__(SeguridadStrategy())  # Inyección de dependencia

    def mostrar_datos(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Muestra datos de una cerradura inteligente.
        
        Args:
            cerradura: Cerradura a mostrar
        """
        super().mostrar_datos(cerradura)  # Datos comunes (ID, estado, tipo)
        print(f"Batería: {cerradura.get_bateria()}%")
        print(f"Estado: {'bloqueada' if cerradura.is_bloqueada() else 'desbloqueada'}")

    def bloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Bloquea la cerradura.
        
        Args:
            cerradura: Cerradura a bloquear
        """
        cerradura.bloquear()

    def desbloquear(self, cerradura: 'CerraduraInteligente') -> None:
        """
        Desbloquea la cerradura.
        
        Args:
            cerradura: Cerradura a desbloquear
        """
        cerradura.desbloquear()

# ==============================================================================
# ARCHIVO 49/62: dispositivo_service.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\dispositivo_service.py
# ==============================================================================

"""Servicio base para todos los dispositivos."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from datetime import datetime

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
    from python_smarthome.patrones.strategy.automation_strategy import AutomationStrategy


class DispositivoService(ABC):
    """
    Clase base abstracta para servicios de dispositivos.
    
    Inyecta una estrategia de automatización (STRATEGY PATTERN).
    """

    def __init__(self, strategy: 'AutomationStrategy'):
        """
        Inicializa servicio con estrategia de automatización.
        
        Args:
            strategy: Estrategia de automatización a usar
        """
        self._estrategia_automation = strategy

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos comunes de un dispositivo.
        
        Args:
            dispositivo: Dispositivo a mostrar
        """
        tipo_dispositivo = type(dispositivo).__name__
        print(f"Dispositivo: {tipo_dispositivo}")
        print(f"ID: {dispositivo.get_id_dispositivo()}")
        print(f"Estado: {'encendido' if dispositivo.is_encendido() else 'apagado'}")

    def ejecutar_automatizacion(self, dispositivo: 'Dispositivo', evento: Any) -> None:
        """
        Delega la ejecución de la automatización a la estrategia (STRATEGY PATTERN).
        
        Este método demuestra el uso del patrón STRATEGY:
        - El servicio NO sabe cómo automatizar
        - Delega la decisión a la estrategia inyectada
        - Permite cambiar el algoritmo en tiempo de ejecución
        
        Args:
            dispositivo: Dispositivo a controlar
            evento: Evento que dispara la acción
        """
        self._estrategia_automation.ejecutar_accion(datetime.now(), dispositivo, evento)

    def get_estrategia(self) -> 'AutomationStrategy':
        """
        Obtiene la estrategia actual (útil para testing).
        
        Returns:
            Estrategia de automatización
        """
        return self._estrategia_automation

    def set_estrategia(self, strategy: 'AutomationStrategy') -> None:
        """
        Cambia la estrategia en tiempo de ejecución (demuestra flexibilidad del patrón).
        
        Args:
            strategy: Nueva estrategia a usar
        """
        self._estrategia_automation = strategy

# ==============================================================================
# ARCHIVO 50/62: dispositivo_service_registry.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\dispositivo_service_registry.py
# ==============================================================================

"""Registry de servicios - SINGLETON + REGISTRY patterns."""

from threading import Lock
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
    from python_smarthome.entidades.dispositivos.termostato import Termostato
    from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
    from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

# Imports reales (no circulares)
from python_smarthome.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from python_smarthome.servicios.dispositivos.termostato_service import TermostatoService
from python_smarthome.servicios.dispositivos.camara_seguridad_service import CamaraSeguridadService
from python_smarthome.servicios.dispositivos.cerradura_inteligente_service import CerraduraInteligenteService


class DispositivoServiceRegistry:
    """
    Registry de servicios de dispositivos.
    
    Implementa SINGLETON pattern (instancia única) y REGISTRY pattern (dispatch polimórfico).
    Thread-safe mediante double-checked locking.
    """

    _instance: 'DispositivoServiceRegistry' = None
    _lock = Lock()

    def __new__(cls):
        """
        Crea o retorna instancia única (SINGLETON).
        
        Returns:
            Instancia única del registry
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'DispositivoServiceRegistry':
        """
        Obtiene instancia única del registry.
        
        Returns:
            Instancia única
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """Inicializa servicios específicos (llamado una sola vez)."""
        # Importar clases de entidades
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        from python_smarthome.entidades.dispositivos.camara_seguridad import CamaraSeguridad
        from python_smarthome.entidades.dispositivos.cerradura_inteligente import CerraduraInteligente

        # Crear servicios
        self._luz_service = LuzInteligenteService()
        self._termostato_service = TermostatoService()
        self._camara_service = CamaraSeguridadService()
        self._cerradura_service = CerraduraInteligenteService()

        # Registry de handlers (REGISTRY PATTERN)
        self._encender_handlers = {
            LuzInteligente: self._encender_luz,
            Termostato: self._encender_termostato,
            CamaraSeguridad: self._encender_camara,
            CerraduraInteligente: self._encender_cerradura
        }

        self._mostrar_datos_handlers = {
            LuzInteligente: self._mostrar_datos_luz,
            Termostato: self._mostrar_datos_termostato,
            CamaraSeguridad: self._mostrar_datos_camara,
            CerraduraInteligente: self._mostrar_datos_cerradura
        }

    # ============================================================
    # Métodos públicos (dispatch polimórfico)
    # ============================================================

    def encender(self, dispositivo: 'Dispositivo') -> None:
        """
        Enciende dispositivo (dispatch polimórfico).
        
        Args:
            dispositivo: Dispositivo a encender
            
        Raises:
            ValueError: Si tipo de dispositivo desconocido
        """
        tipo = type(dispositivo)
        if tipo not in self._encender_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._encender_handlers[tipo](dispositivo)

    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        """
        Muestra datos de dispositivo (dispatch polimórfico).
        
        Args:
            dispositivo: Dispositivo a mostrar
            
        Raises:
            ValueError: Si tipo de dispositivo desconocido
        """
        tipo = type(dispositivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](dispositivo)

    # ============================================================
    # Handlers privados (NO usar lambdas)
    # ============================================================

    def _encender_luz(self, dispositivo: 'LuzInteligente') -> None:
        self._luz_service.encender(dispositivo)

    def _encender_termostato(self, dispositivo: 'Termostato') -> None:
        self._termostato_service.encender(dispositivo)

    def _encender_camara(self, dispositivo: 'CamaraSeguridad') -> None:
        self._camara_service.encender(dispositivo)

    def _encender_cerradura(self, dispositivo: 'CerraduraInteligente') -> None:
        self._cerradura_service.bloquear(dispositivo)

    def _mostrar_datos_luz(self, dispositivo: 'LuzInteligente') -> None:
        self._luz_service.mostrar_datos(dispositivo)

    def _mostrar_datos_termostato(self, dispositivo: 'Termostato') -> None:
        self._termostato_service.mostrar_datos(dispositivo)

    def _mostrar_datos_camara(self, dispositivo: 'CamaraSeguridad') -> None:
        self._camara_service.mostrar_datos(dispositivo)

    def _mostrar_datos_cerradura(self, dispositivo: 'CerraduraInteligente') -> None:
        self._cerradura_service.mostrar_datos(dispositivo)


# ==============================================================================
# ARCHIVO 51/62: luz_inteligente_service.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\luz_inteligente_service.py
# ==============================================================================

"""Servicio para gestionar luces inteligentes."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.iluminacion_strategy import IluminacionStrategy


class LuzInteligenteService(DispositivoService):
    """
    Servicio para operaciones sobre luces inteligentes.
    
    Usa estrategia de iluminación para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de iluminación."""
        super().__init__(IluminacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, luz: 'LuzInteligente') -> None:
        """
        Muestra datos de una luz inteligente.
        
        Args:
            luz: Luz a mostrar
        """
        super().mostrar_datos(luz)  # Datos comunes (ID, estado, tipo)
        print(f"Intensidad: {luz.get_intensidad()}%")
        r, g, b = luz.get_color_rgb()
        print(f"Color RGB: ({r}, {g}, {b})")

    def encender(self, luz: 'LuzInteligente') -> None:
        """
        Enciende luz con intensidad máxima.
        
        Args:
            luz: Luz a encender
        """
        luz.set_encendido(True)
        luz.set_intensidad(100)

    def apagar(self, luz: 'LuzInteligente') -> None:
        """
        Apaga luz.
        
        Args:
            luz: Luz a apagar
        """
        luz.set_encendido(False)
        luz.set_intensidad(0)

    def ajustar_intensidad(self, luz: 'LuzInteligente', intensidad: int) -> None:
        """
        Ajusta intensidad de la luz.
        
        Args:
            luz: Luz a ajustar
            intensidad: Nueva intensidad (0-100%)
        """
        luz.set_intensidad(intensidad)

    def cambiar_color(self, luz: 'LuzInteligente', color: tuple) -> None:
        """
        Cambia color de la luz.
        
        Args:
            luz: Luz a ajustar
            color: Tupla RGB (R, G, B)
        """
        luz.set_color_rgb(color)

# ==============================================================================
# ARCHIVO 52/62: termostato_service.py
# Directorio: servicios\dispositivos
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\dispositivos\termostato_service.py
# ==============================================================================

"""Servicio para gestionar termostatos."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.dispositivos.termostato import Termostato

from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.climatizacion_strategy import ClimatizacionStrategy


class TermostatoService(DispositivoService):
    """
    Servicio para operaciones sobre termostatos.
    
    Usa estrategia de climatización para automatización.
    """

    def __init__(self):
        """Inicializa servicio con estrategia de climatización."""
        super().__init__(ClimatizacionStrategy())  # Inyección de dependencia

    def mostrar_datos(self, termostato: 'Termostato') -> None:
        """
        Muestra datos de un termostato.
        
        Args:
            termostato: Termostato a mostrar
        """
        super().mostrar_datos(termostato)  # Datos comunes (ID, estado, tipo)
        print(f"Temperatura Objetivo: {termostato.get_temperatura_objetivo()}°C")

    def encender(self, termostato: 'Termostato') -> None:
        """
        Enciende el termostato.
        
        Args:
            termostato: Termostato a encender
        """
        termostato.set_encendido(True)

    def apagar(self, termostato: 'Termostato') -> None:
        """
        Apaga el termostato.
        
        Args:
            termostato: Termostato a apagar
        """
        termostato.set_encendido(False)


################################################################################
# DIRECTORIO: servicios\espacios
################################################################################

# ==============================================================================
# ARCHIVO 53/62: __init__.py
# Directorio: servicios\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 54/62: casa_service.py
# Directorio: servicios\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\casa_service.py
# ==============================================================================

"""Servicio para gestionar casas."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.casa import Casa

from python_smarthome.entidades.espacios.casa import Casa
from python_smarthome.entidades.espacios.habitacion import Habitacion


class CasaService:
    """
    Servicio para operaciones de alto nivel sobre casas.
    """

    def crear_casa_con_habitaciones(
        self,
        direccion: str,
        superficie: float,
        propietario: str,
        nombres_habitaciones: List[str]
    ) -> 'Casa':
        """
        Crea una casa y le asigna habitaciones.
        
        Args:
            direccion: Dirección de la casa
            superficie: Superficie en m²
            propietario: Nombre del propietario
            nombres_habitaciones: Lista de nombres para las habitaciones
            
        Returns:
            La casa creada con sus habitaciones
        """
        casa = Casa(direccion, superficie, propietario)
        habitaciones = [Habitacion(nombre) for nombre in nombres_habitaciones]
        casa.set_habitaciones(habitaciones)
        return casa


# ==============================================================================
# ARCHIVO 55/62: configuracion_casa_service.py
# Directorio: servicios\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\configuracion_casa_service.py
# ==============================================================================

"""Servicio para gestionar la configuración de la casa."""

import os
import pickle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa

from python_smarthome.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_smarthome.excepciones.persistencia_exception import PersistenciaException


class ConfiguracionCasaService:
    """
    Servicio para persistir y leer la configuración de la casa.
    """

    def persistir(self, config: 'ConfiguracionCasa') -> None:
        """
        Guarda la configuración en un archivo .dat usando pickle.
        
        Args:
            config: La configuración a guardar
            
        Raises:
            PersistenciaException: Si hay un error de escritura
        """
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
        
        nombre_archivo = f"{config.get_propietario()}{EXTENSION_DATA}"
        ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(config, f)
            print(f"Configuración de {config.get_propietario()} guardada en {ruta_archivo}")
        except IOError as e:
            raise PersistenciaException(
                mensaje_usuario=f"No se pudo guardar la configuración de {config.get_propietario()}",
                mensaje_tecnico=f"Error al escribir en {ruta_archivo}: {e}"
            )

    @staticmethod
    def leer_configuracion(propietario: str) -> 'ConfiguracionCasa':
        """
        Lee la configuración desde un archivo .dat.
        
        Args:
            propietario: Nombre del propietario para encontrar el archivo
            
        Returns:
            La configuración leída
            
        Raises:
            PersistenciaException: Si el archivo no existe o está corrupto
        """
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            raise PersistenciaException(
                mensaje_usuario=f"No se encontró la configuración de {propietario}",
                mensaje_tecnico=f"El archivo {ruta_archivo} no existe"
            )
        
        try:
            with open(ruta_archivo, 'rb') as f:
                config = pickle.load(f)
            print(f"Configuración de {propietario} leída desde {ruta_archivo}")
            return config
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                mensaje_usuario=f"No se pudo leer la configuración de {propietario}",
                mensaje_tecnico=f"Error al leer o deserializar {ruta_archivo}: {e}"
            )

    def mostrar_datos(self, config: 'ConfiguracionCasa') -> None:
        """
        Muestra los datos de una configuración de casa.
        
        Args:
            config: La configuración a mostrar
        """
        casa = config.get_casa()
        print("\n--- CONFIGURACIÓN DE LA CASA ---")
        print(f"Propietario: {config.get_propietario()}")
        print(f"Dirección: {casa.get_direccion()}")
        print(f"Superficie: {casa.get_superficie()} m²")
        print(f"Fecha de Instalación: {config.get_fecha_instalacion()}")
        print(f"Habitaciones: {len(casa.get_habitaciones())}")
        
        total_dispositivos = sum(len(h.get_dispositivos()) for h in casa.get_habitaciones())
        print(f"Total de Dispositivos: {total_dispositivos}")
        print("---------------------------------")


# ==============================================================================
# ARCHIVO 56/62: habitacion_service.py
# Directorio: servicios\espacios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\espacios\habitacion_service.py
# ==============================================================================

"""Servicio para gestionar habitaciones."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.habitacion import Habitacion

from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory
from python_smarthome.constantes import (
    MAX_DISPOSITIVOS_HABITACION,
    INTENSIDAD_MODO_NOCHE,
    TEMP_CONFORT_OBJETIVO
)
from python_smarthome.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException


class HabitacionService:
    """
    Servicio para operaciones sobre habitaciones.
    
    Demuestra uso del patrón FACTORY METHOD para crear dispositivos.
    """

    def instalar(self, habitacion: 'Habitacion', tipo_dispositivo: str, cantidad: int) -> None:
        """
        Instala dispositivos en una habitación usando FACTORY METHOD pattern.
        
        Demuestra:
        - Cliente (HabitacionService) NO conoce clases concretas
        - Factory encapsula lógica de creación
        - Fácil extensión para nuevos tipos
        
        Args:
            habitacion: La habitación donde instalar
            tipo_dispositivo: El tipo de dispositivo a instalar
            cantidad: Cuántos dispositivos instalar
            
        Raises:
            CapacidadInsuficienteException: Si no hay espacio
            ValueError: Si tipo de dispositivo desconocido
        """
        # Validar cantidad
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        
        # Verificar capacidad
        capacidad_actual = len(habitacion.get_dispositivos())
        capacidad_disponible = MAX_DISPOSITIVOS_HABITACION - capacidad_actual
        
        if cantidad > capacidad_disponible:
            raise CapacidadInsuficienteException(
                capacidad_requerida=cantidad,
                capacidad_disponible=capacidad_disponible
            )
        
        # Crear dispositivos usando FACTORY METHOD
        print(f"Instalando {cantidad} dispositivos de tipo {tipo_dispositivo}...")
        for i in range(cantidad):
            # FACTORY METHOD: cliente NO instancia clases concretas
            dispositivo = DispositivoFactory.crear_dispositivo(tipo_dispositivo)
            habitacion.agregar_dispositivo(dispositivo)
            print(f"  - Dispositivo {i+1}/{cantidad} instalado (ID: {dispositivo.get_id_dispositivo()})")
        
        print(f"Instalacion completada. Total dispositivos: {len(habitacion.get_dispositivos())}")

    def ajustar_luces_modo_noche(self, habitacion: 'Habitacion') -> None:
        """
        Ajusta las luces de la habitación a modo noche.
        
        Aplica intensidad reducida (INTENSIDAD_MODO_NOCHE) a todas las luces.
        
        Args:
            habitacion: Habitación a ajustar
        """
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        
        contador = 0
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.set_encendido(True)
                dispositivo.set_intensidad(INTENSIDAD_MODO_NOCHE)
                contador += 1
        
        if contador > 0:
            print(f"Ajustadas {contador} luces a modo noche ({INTENSIDAD_MODO_NOCHE}%)")

    def ajustar_climatizacion(self, habitacion: 'Habitacion') -> None:
        """
        Ajusta la climatización de la habitación a temperatura de confort.
        
        Args:
            habitacion: Habitación a ajustar
        """
        from python_smarthome.entidades.dispositivos.termostato import Termostato
        
        contador = 0
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, Termostato):
                dispositivo.set_encendido(True)
                dispositivo.set_temperatura_objetivo(TEMP_CONFORT_OBJETIVO)
                contador += 1
        
        if contador > 0:
            print(f"Ajustados {contador} termostatos a {TEMP_CONFORT_OBJETIVO}°C")

    def encender_todos(self, habitacion: 'Habitacion') -> None:
        """
        Enciende todos los dispositivos de una habitación.
        
        Args:
            habitacion: Habitación a controlar
        """
        from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
        
        registry = DispositivoServiceRegistry.get_instance()
        print(f"\nEncendiendo todos los dispositivos de {habitacion.get_nombre()}...")
        
        for dispositivo in habitacion.get_dispositivos():
            registry.encender(dispositivo)
            print(f"  - Dispositivo ID {dispositivo.get_id_dispositivo()} encendido")

    def apagar_todos(self, habitacion: 'Habitacion') -> None:
        """
        Apaga todos los dispositivos de una habitación.
        
        Args:
            habitacion: Habitación a controlar
        """
        print(f"\nApagando todos los dispositivos de {habitacion.get_nombre()}...")
        
        for dispositivo in habitacion.get_dispositivos():
            dispositivo.set_encendido(False)
            print(f"  - Dispositivo ID {dispositivo.get_id_dispositivo()} apagado")

    def mostrar_todos(self, habitacion: 'Habitacion') -> None:
        """
        Muestra datos de todos los dispositivos usando REGISTRY pattern.
        
        Args:
            habitacion: Habitación a mostrar
        """
        from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
        
        registry = DispositivoServiceRegistry.get_instance()
        print(f"\n=== DISPOSITIVOS EN {habitacion.get_nombre().upper()} ===")
        
        if not habitacion.get_dispositivos():
            print("(Sin dispositivos instalados)")
        else:
            for i, dispositivo in enumerate(habitacion.get_dispositivos(), 1):
                print(f"\n--- Dispositivo {i} ---")
                registry.mostrar_datos(dispositivo)
        
        print("=" * 50)


################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 57/62: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 58/62: casa_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\casa_service.py
# ==============================================================================

"""Servicio de negocio para gestionar múltiples casas."""

from typing import Dict, List, Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
    from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo

from python_smarthome.servicios.negocio.grupo_dispositivos import GrupoDispositivos

T = TypeVar('T', bound='Dispositivo')


class CasaService:
    """
    Servicio de negocio para operaciones sobre múltiples casas.
    """

    def __init__(self):
        self._casas: Dict[str, 'ConfiguracionCasa'] = {}

    def add_casa(self, config: 'ConfiguracionCasa') -> None:
        """Agrega una casa al servicio."""
        direccion = config.get_casa().get_direccion()
        self._casas[direccion] = config

    def agrupar_por_tipo(self, tipo: Type[T]) -> GrupoDispositivos[T]:
        """
        Agrupa todos los dispositivos de un tipo específico de todas las casas.
        """
        dispositivos_agrupados: List[T] = []
        for config in self._casas.values():
            for habitacion in config.get_casa().get_habitaciones():
                for dispositivo in habitacion.get_dispositivos():
                    if isinstance(dispositivo, tipo):
                        dispositivos_agrupados.append(dispositivo)
        return GrupoDispositivos(tipo, dispositivos_agrupados)


# ==============================================================================
# ARCHIVO 59/62: grupo_dispositivos.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\grupo_dispositivos.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 60/62: modo_sistema.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\negocio\modo_sistema.py
# ==============================================================================

"""Enum para los modos del sistema."""

from enum import Enum


class ModoSistema(Enum):
    """
    Enumeración para los diferentes modos del sistema.
    """
    NOCHE = "noche"
    VACACIONES = "vacaciones"
    FIESTA = "fiesta"
    CINE = "cine"



################################################################################
# DIRECTORIO: servicios\usuarios
################################################################################

# ==============================================================================
# ARCHIVO 61/62: __init__.py
# Directorio: servicios\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\usuarios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/62: usuario_service.py
# Directorio: servicios\usuarios
# Ruta completa: C:\Users\Valen\Desktop\pythonSmartHome\python_smarthome\servicios\usuarios\usuario_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 62
# Generado: 2025-11-04 15:57:25
################################################################################
