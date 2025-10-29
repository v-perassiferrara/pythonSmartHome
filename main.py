"""
Sistema de Domótica (Smart Home) - Demostración Completa

Este archivo demuestra el funcionamiento de todos los patrones de diseño:
- SINGLETON: DispositivoServiceRegistry
- FACTORY METHOD: DispositivoFactory
- OBSERVER: Sensores y automatización
- STRATEGY: Algoritmos de automatización
- REGISTRY: Dispatch polimórfico

Autor: [Tu nombre]
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
    
    # ================================================================
    # 1. PATRON SINGLETON: Verificar instancia única
    # ================================================================
    print_section("PATRON SINGLETON: Inicializando servicios")
    
    registry1 = DispositivoServiceRegistry()
    registry2 = DispositivoServiceRegistry.get_instance()
    
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
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
    print(f"Habitaciones: {len(casa.get_habitaciones())}")
    
    # ================================================================
    # 3. PATRON FACTORY: Instalar dispositivos
    # ================================================================
    print_section("2. PATRON FACTORY: Instalando dispositivos")
    
    habitacion_service = HabitacionService()
    habitaciones = casa.get_habitaciones()
    living = habitaciones[0]
    
    # Factory Method se usa internamente en instalar()
    habitacion_service.instalar(living, "LuzInteligente", 3)
    habitacion_service.instalar(living, "Termostato", 1)
    habitacion_service.instalar(living, "CamaraSeguridad", 1)
    habitacion_service.instalar(living, "CerraduraInteligente", 1)
    
    print(f"Dispositivos instalados en {living.get_nombre()}: {len(living.get_dispositivos())}")
    
    # ================================================================
    # 4. Mostrar datos de dispositivos (Registry)
    # ================================================================
    print_section("3. PATRON REGISTRY: Mostrando datos de dispositivos")
    
    for dispositivo in living.get_dispositivos()[:2]:  # Mostrar primeros 2
        registry1.mostrar_datos(dispositivo)
        print()
    
    # ================================================================
    # 5. Crear usuarios con escenas
    # ================================================================
    print_section("4. Creando usuarios con escenas")
    
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
    print(f"Nivel de acceso: {usuario.get_nivel_acceso().name}")
    print(f"Escenas: {len(usuario.get_escenas())}")
    
    # ================================================================
    # 6. PATRON OBSERVER: Sistema de sensores
    # ================================================================
    print_section("5. PATRON OBSERVER: Iniciando sistema de sensores")
    
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
    
    # Iniciar threads daemon
    sensor_mov.start()
    sensor_temp.start()
    automation_control.start()
    
    print("Sistema de sensores iniciado (3 threads daemon)")
    print("Sensores notifican automaticamente al controlador (OBSERVER)")
    print("Esperando 10 segundos para observar automatizacion...")
    
    time.sleep(10)
    
    # ================================================================
    # 7. Detener sistema de sensores
    # ================================================================
    print_section("6. Deteniendo sistema de sensores")
    
    sensor_mov.detener()
    sensor_temp.detener()
    automation_control.detener()
    
    sensor_mov.join(timeout=THREAD_JOIN_TIMEOUT)
    sensor_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    automation_control.join(timeout=THREAD_JOIN_TIMEOUT)
    
    print("Sistema de sensores detenido correctamente (graceful shutdown)")
    
    # ================================================================
    # 8. Persistencia
    # ================================================================
    print_section("7. Persistiendo configuracion en disco")
    
    config = ConfiguracionCasa(
        id_config=1,
        casa=casa,
        fecha_instalacion=date.today(),
        propietario="Juan Perez"
    )
    
    config_service = ConfiguracionCasaService()
    
    try:
        config_service.persistir(config)
    except SmartHomeException as e:
        print(f"[ERROR] {e.get_user_message()}")
    
    # ================================================================
    # 9. Recuperar configuración
    # ================================================================
    print_section("8. Recuperando configuracion desde disco")
    
    try:
        config_leida = ConfiguracionCasaService.leer_configuracion("Juan Perez")
        config_service.mostrar_datos(config_leida)
    except SmartHomeException as e:
        print(f"[ERROR] {e.get_user_message()}")
    
    # ================================================================
    # 10. Agrupar dispositivos por tipo
    # ================================================================
    print_section("9. Agrupando dispositivos por tipo")
    
    casa_negocio_service = CasaNegocioService()
    casa_negocio_service.add_casa(config)
    
    # Agrupar todas las luces
    grupo_luces = casa_negocio_service.agrupar_por_tipo(LuzInteligente)
    grupo_luces.mostrar_contenido_grupo()
    
    # Agrupar todos los termostatos
    grupo_termostatos = casa_negocio_service.agrupar_por_tipo(Termostato)
    grupo_termostatos.mostrar_contenido_grupo()
    
    # ================================================================
    # Resumen final
    # ================================================================
    print_header("EJEMPLO COMPLETADO EXITOSAMENTE")
    
    print("  [OK] SINGLETON   - DispositivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de dispositivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de automatizacion")
    print("  [OK] REGISTRY    - Dispatch polimorfico")
    
    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
