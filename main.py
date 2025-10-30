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