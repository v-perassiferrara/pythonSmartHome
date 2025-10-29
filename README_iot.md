# Sistema de Domótica (Smart Home)

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de automatización del hogar que demuestra la implementación de múltiples patrones de diseño de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#características-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseño-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Módulos del Sistema](#módulos-del-sistema)
- [Documentación Técnica](#documentación-técnica)
- [Testing y Validación](#testing-y-validación)
- [Contribución](#contribución)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **PythonSmartHome** aborda los desafíos de la automatización moderna del hogar, un dominio que requiere:

1. **Gestión de Múltiples Tipos de Dispositivos**
   - Dispositivos de iluminación (Luces inteligentes, Tiras LED)
   - Dispositivos de climatización (Termostatos, Aire acondicionado)
   - Dispositivos de seguridad (Cámaras, Cerraduras inteligentes)
   - Cada tipo con características y protocolos de comunicación particulares

2. **Monitoreo Ambiental en Tiempo Real**
   - Sensores de movimiento, temperatura y apertura operando continuamente
   - Sistema de automatización basado en condiciones ambientales
   - Respuesta dinámica a eventos del hogar

3. **Gestión de Usuarios y Permisos**
   - Control de usuarios con niveles de acceso
   - Asignación y seguimiento de escenas personalizadas
   - Dispositivos con certificaciones de seguridad

4. **Planificación Espacial**
   - Optimización del uso de habitaciones
   - Registro de ubicación de dispositivos
   - Control de distribución espacial

5. **Persistencia y Trazabilidad**
   - Almacenamiento permanente de configuraciones
   - Recuperación de históricos para análisis
   - Registro de eventos de seguridad

### Actores del Sistema

- **Propietario de Casa**: Gestiona la configuración general, supervisa operaciones
- **Usuario Familiar**: Ejecuta escenas, controla dispositivos básicos
- **Sistema de Automatización**: Opera de forma autónoma basado en sensores
- **Auditor/Inspector**: Consulta registros persistidos para verificación de seguridad

### Flujo de Operaciones Típico

```
1. CONFIGURACIÓN --> Se crea una casa con habitaciones y dispositivos
2. INSTALACIÓN --> Se instalan dispositivos según habitación
3. MONITOREO --> Sensores detectan movimiento, temperatura y apertura continuamente
4. AUTOMATIZACIÓN --> Sistema ejecuta acciones cuando se cumplen condiciones
5. REACCIÓN --> Dispositivos responden según estrategias específicas
6. ESCENAS --> Usuarios ejecutan rutinas personalizadas
7. EVENTOS --> Se registran eventos de seguridad
8. PERSISTENCIA --> Datos se guardan para auditoría futura
```

---

## Características Principales

### Funcionalidades del Sistema

#### 1. Gestión de Dispositivos

- **Creación dinámica** de 4 tipos de dispositivos mediante Factory Pattern
  - **LuzInteligente**: Dispositivo de iluminación con intensidad y color
  - **Termostato**: Dispositivo de climatización con temperatura objetivo
  - **CamaraSeguridad**: Dispositivo de seguridad con detección de movimiento
  - **CerraduraInteligente**: Dispositivo de seguridad con control de acceso

- **Estado diferenciado** por tipo
  - Iluminación: Estado on/off, intensidad (0-100%), color RGB
  - Climatización: Estado on/off, temperatura objetivo (10-30°C)
  - Seguridad: Estado on/off, modo grabación, alertas

- **Control automático**
  - Luces: Ajuste de intensidad y color
  - Termostato: Ajuste de temperatura objetivo
  - Cámaras: Activación/desactivación de grabación

#### 2. Sistema de Sensores Inteligente

- **Sensores en tiempo real** (patrón Observer)
  - Sensor de movimiento: lecturas cada 2 segundos
  - Sensor de temperatura: lecturas cada 3 segundos
  - Sensor de apertura: detección instantánea
  - Rangos: -10C a 40C, detección binaria de movimiento/apertura

- **Automatización condicional**
  - Se activa cuando:
    - Movimiento detectado en modo noche, O
    - Temperatura fuera de rango, O
    - Apertura detectada en modo seguridad
  - Control cada 2.5 segundos

- **Notificaciones de eventos**
  - Eventos de sensores a observadores suscritos
  - Sistema tipo-seguro con Generics (Observable[bool], Observable[float])

#### 3. Gestión de Usuarios

- **Usuarios con nivel de acceso**
  - Nivel requerido para ejecutar acciones
  - Validación automática antes de ejecutar escenas
  - Fecha de registro y permisos

- **Sistema de escenas**
  - Asignación múltiple de escenas por usuario
  - Ejecución ordenada por prioridad
  - Estado de escenas (activa/inactiva)
  - Hora programada para cada escena

- **Dispositivos autorizados**
  - ID único, nombre y certificación
  - Asignación a usuarios con permisos

#### 4. Gestión Espacial

- **Casa**
  - Dirección única
  - Superficie en metros cuadrados
  - Propietario

- **Habitación**
  - Nombre identificatorio
  - Control de dispositivos instalados
  - Lista de dispositivos activos
  - Sensores asignados

- **Configuración de Casa**
  - Vincula casa con habitaciones
  - Propietario y fecha de instalación
  - Persistible en disco

#### 5. Operaciones de Negocio

- **Instalación automática**
  - Cálculo de dispositivos por habitación
  - Validación de compatibilidad
  - Creación vía Factory Method

- **Ejecución de escenas**
  - Activa múltiples dispositivos coordinadamente
  - Verifica permisos antes de ejecutar
  - Excepción si permisos insuficientes

- **Modos del sistema**
  - Modo específico por tipo de situación
  - Empaquetado en grupos genéricos tipo-seguros
  - Mostración de estado de modos

- **Registro de eventos**
  - Aplicación de log a todo el sistema
  - Registro de tipo de evento registrado

#### 6. Persistencia de Datos

- **Serialización con Pickle**
  - Guardado completo de ConfiguracionCasa
  - Directorio configurable (default: `data/`)
  - Nombre de archivo: `{propietario}.dat`

- **Recuperación de datos**
  - Lectura de configuraciones persistidas
  - Validación de integridad
  - Manejo de excepciones específicas

---

## Arquitectura del Sistema

### Principios Arquitectónicos

El sistema está diseñado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una única razón para cambiar
  - Entidades: Solo contienen datos (DTOs)
  - Servicios: Solo contienen lógica de negocio
  - Patrones: Implementaciones aisladas y reutilizables

- **Open/Closed**: Abierto a extensión, cerrado a modificación
  - Nuevos dispositivos: Agregar sin modificar factory existente
  - Nuevas estrategias: Implementar interfaz sin cambiar servicios

- **Liskov Substitution**: Subtipos intercambiables
  - Todos los dispositivos son Dispositivo
  - Todas las estrategias implementan AutomationStrategy

- **Interface Segregation**: Interfaces específicas
  - Observer[T]: Genérico para cualquier tipo de evento
  - AutomationStrategy: Específico para automatización

- **Dependency Inversion**: Dependencias de abstracciones
  - Servicios dependen de Strategy (abstracción), no implementaciones
  - Factory retorna Dispositivo (interfaz), no tipos concretos

### Separación de Capas

```
+----------------------------------+
|        PRESENTACIÓN              |
|  (main.py - Demostración CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (CasaService, ModoSistema)      |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (HabitacionService, etc.)       |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Dispositivo, Casa, Usuario)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

### Inyección de Dependencias

El sistema utiliza inyección manual de dependencias:

```python
# Estrategia inyectada en constructor
class LuzInteligenteService(DispositivoService):
    def __init__(self):
        super().__init__(IluminacionStrategy())

# Sensores inyectados en controlador
automation_control = AutomationControlTask(
    sensor_movimiento,      # Dependencia inyectada
    sensor_temperatura,     # Dependencia inyectada
    habitacion,
    habitacion_service
)
```

---

## Patrones de Diseño Implementados

### 1. SINGLETON Pattern

**Ubicación**: `python_smarthome/servicios/dispositivos/dispositivo_service_registry.py`

**Problema que resuelve**:
- Garantizar una única instancia del registro de servicios
- Compartir estado entre todos los servicios del sistema
- Evitar múltiples registros inconsistentes

**Implementación**:
```python
class DispositivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Uso en el sistema**:
- Todos los servicios de dispositivos comparten el mismo registry
- Elimina cadenas de `isinstance()` mediante dispatch polimórfico
- Acceso: `DispositivoServiceRegistry.get_instance()`

---

### 2. FACTORY METHOD Pattern

**Ubicación**: `python_smarthome/patrones/factory/dispositivo_factory.py`

**Problema que resuelve**:
- Creación de dispositivos sin conocer clases concretas
- Encapsulación de lógica de construcción compleja
- Extensibilidad para nuevos tipos de dispositivos

**Implementación**:
```python
class DispositivoFactory:
    @staticmethod
    def crear_dispositivo(tipo: str) -> Dispositivo:
        factories = {
            "LuzInteligente": DispositivoFactory._crear_luz,
            "Termostato": DispositivoFactory._crear_termostato,
            "CamaraSeguridad": DispositivoFactory._crear_camara,
            "CerraduraInteligente": DispositivoFactory._crear_cerradura
        }

        if tipo not in factories:
            raise ValueError(f"Tipo desconocido: {tipo}")

        return factories[tipo]()
```

**Uso en el sistema**:
```python
# HabitacionService usa factory internamente
habitacion_service.instalar(habitacion, "LuzInteligente", 3)
# Crea 3 Luces sin conocer constructor
```

---

### 3. OBSERVER Pattern

**Ubicación**: `python_smarthome/patrones/observer/`

**Problema que resuelve**:
- Notificación automática a múltiples observadores
- Desacoplamiento entre sensores y consumidores
- Sistema de eventos tipo-seguro

**Implementación**:
```python
class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso en el sistema**:
```python
# Sensor es Observable
class SensorMovimientoTask(threading.Thread, Observable[bool]):
    def run(self):
        while not self._detenido.is_set():
            movimiento = self._detectar_movimiento()
            # Notifica a todos los observadores
            self.notificar_observadores(movimiento)
            time.sleep(INTERVALO_SENSOR_MOVIMIENTO)

# AutomationControlTask es Observer
class AutomationControlTask(Observer[bool]):
    def actualizar(self, evento: bool) -> None:
        # Recibe notificación automáticamente
        self._ultimo_movimiento = evento
```

---

### 4. STRATEGY Pattern

**Ubicación**: `python_smarthome/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de automatización intercambiables
- Eliminar condicionales tipo if/else
- Permitir cambios en tiempo de ejecución

**Implementación**:
```python
class AutomationStrategy(ABC):
    @abstractmethod
    def ejecutar_accion(
        self,
        fecha: datetime,
        dispositivo: 'Dispositivo',
        evento: Any
    ) -> None:
        pass

# Estrategia 1: Iluminación
class IluminacionStrategy(AutomationStrategy):
    def ejecutar_accion(self, fecha, dispositivo, evento):
        hora = fecha.hour
        if HORA_INICIO_NOCHE <= hora or hora <= HORA_FIN_NOCHE:
            dispositivo.set_intensidad(50)  # 50% en modo noche
        else:
            dispositivo.set_intensidad(100)  # 100% de día

# Estrategia 2: Climatización
class ClimatizacionStrategy(AutomationStrategy):
    def __init__(self, temp_objetivo: float):
        self._temp_objetivo = temp_objetivo

    def ejecutar_accion(self, fecha, dispositivo, evento):
        dispositivo.set_temperatura_objetivo(self._temp_objetivo)
```

**Uso en el sistema**:
```python
# Inyección de estrategia en servicio
class LuzInteligenteService(DispositivoService):
    def __init__(self):
        super().__init__(IluminacionStrategy())  # Iluminación

class TermostatoService(DispositivoService):
    def __init__(self):
        super().__init__(ClimatizacionStrategy(22.0))  # Climatización
```

---

### 5. REGISTRY Pattern (Bonus)

**Ubicación**: `python_smarthome/servicios/dispositivos/dispositivo_service_registry.py`

**Problema que resuelve**:
- Eliminar cascadas de `isinstance()`
- Dispatch polimórfico basado en tipo
- Punto único de registro de servicios

**Implementación**:
```python
class DispositivoServiceRegistry:
    def __init__(self):
        # Registro de handlers por tipo
        self._encender_handlers = {
            LuzInteligente: self._encender_luz,
            Termostato: self._encender_termostato,
            CamaraSeguridad: self._encender_camara,
            CerraduraInteligente: self._encender_cerradura
        }

    def encender(self, dispositivo: Dispositivo) -> None:
        tipo = type(dispositivo)
        if tipo not in self._encender_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")

        # Dispatch polimórfico
        self._encender_handlers[tipo](dispositivo)
```

---

## Requisitos del Sistema

### Requisitos de Software

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Módulos Estándar**: Solo biblioteca estándar de Python (sin dependencias externas)

### Requisitos de Hardware

- **RAM**: Mínimo 512 MB
- **Disco**: 50 MB libres
- **Procesador**: Cualquier procesador moderno (1 GHz+)

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/python-smarthome.git
cd python-smarthome
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Verificar Instalación

```bash
python --version
# Debe mostrar Python 3.13 o superior
```

### 4. Ejecutar Sistema

```bash
python main.py
```

**Salida esperada**:
```
======================================================================
         SISTEMA DE DOMÓTICA - PATRONES DE DISEÑO
======================================================================

----------------------------------------------------------------------
  PATRÓN SINGLETON: Inicializando servicios
----------------------------------------------------------------------
[OK] Todos los servicios comparten la misma instancia del Registry

1. Creando casa con habitaciones...
...
======================================================================
              EJEMPLO COMPLETADO EXITOSAMENTE
======================================================================
  [OK] SINGLETON   - DispositivoServiceRegistry (instancia única)
  [OK] FACTORY     - Creación de dispositivos
  [OK] OBSERVER    - Sistema de sensores y eventos
  [OK] STRATEGY    - Algoritmos de automatización
======================================================================
```

---

## Uso del Sistema

### Ejemplo Básico

```python
from python_smarthome.servicios.espacios.casa_service import CasaService
from python_smarthome.servicios.espacios.habitacion_service import HabitacionService

# 1. Crear casa con habitaciones
casa_service = CasaService()
casa = casa_service.crear_casa_con_habitaciones(
    direccion="Calle Falsa 123",
    superficie=150.0,  # m2
    propietario="Juan Perez",
    nombres_habitaciones=["Living", "Cocina", "Dormitorio"]
)

# 2. Obtener habitación
habitacion = casa.get_habitaciones()[0]

# 3. Instalar dispositivos (usa Factory Method internamente)
habitacion_service = HabitacionService()
habitacion_service.instalar(habitacion, "LuzInteligente", 3)
habitacion_service.instalar(habitacion, "Termostato", 1)

# 4. Ejecutar escena (usa Strategy Pattern internamente)
habitacion_service.ejecutar_escena(habitacion, "ModoNoche")
```

### Sistema de Automatización

```python
from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask
from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask
from python_smarthome.control.automation_control_task import AutomationControlTask

# Crear sensores (Observable)
sensor_mov = SensorMovimientoTask()
sensor_temp = SensorTemperaturaTask()

# Crear controlador (Observer)
automation_control = AutomationControlTask(
    sensor_mov,
    sensor_temp,
    habitacion,
    habitacion_service
)

# Iniciar threads daemon
sensor_mov.start()
sensor_temp.start()
automation_control.start()

# Sistema funciona automáticamente
time.sleep(20)  # Dejarlo funcionar 20 segundos

# Detener sistema
sensor_mov.detener()
sensor_temp.detener()
automation_control.detener()
```

### Persistencia de Datos

```python
from python_smarthome.servicios.espacios.configuracion_casa_service import ConfiguracionCasaService
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa

# Crear configuración
config = ConfiguracionCasa(
    id_config=1,
    casa=casa,
    fecha_instalacion=date.today(),
    propietario="Juan Perez"
)

# Persistir
config_service = ConfiguracionCasaService()
config_service.persistir(config)
# Crea archivo: data/Juan Perez.dat

# Recuperar
config_leida = ConfiguracionCasaService.leer_configuracion("Juan Perez")
config_service.mostrar_datos(config_leida)
```

---

## Estructura del Proyecto

```
PythonSmartHome/
|
+-- main.py                          # Punto de entrada del sistema
+-- CLAUDE_iot.md                    # Guía para Claude Code
+-- README_iot.md                    # Este archivo
+-- USER_STORIES_iot.md              # Historias de usuario detalladas
+-- RUBRICA_EVALUACION_iot.md        # Rúbrica de evaluación técnica
|
+-- .venv/                           # Entorno virtual Python
|
+-- data/                            # Datos persistidos (archivos .dat)
|
+-- python_smarthome/                # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes centralizadas del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- __init__.py
    |   |
    |   +-- dispositivos/            # Dispositivos del sistema
    |   |   +-- __init__.py
    |   |   +-- dispositivo.py       # Interfaz base
    |   |   +-- luz_inteligente.py   # Dispositivo de iluminación
    |   |   +-- termostato.py        # Dispositivo de climatización
    |   |   +-- camara_seguridad.py  # Dispositivo de seguridad
    |   |   +-- cerradura_inteligente.py  # Control de acceso
    |   |
    |   +-- espacios/                # Gestión espacial
    |   |   +-- __init__.py
    |   |   +-- casa.py              # Casa completa
    |   |   +-- habitacion.py        # Habitación individual
    |   |   +-- configuracion_casa.py # Configuración completa
    |   |
    |   +-- usuarios/                # Gestión de usuarios
    |       +-- __init__.py
    |       +-- usuario.py           # Usuario del sistema
    |       +-- escena.py            # Escena personalizada
    |       +-- nivel_acceso.py      # Nivel de permisos
    |
    +-- servicios/                   # Lógica de negocio
    |   +-- __init__.py
    |   |
    |   +-- dispositivos/            # Servicios de dispositivos
    |   |   +-- __init__.py
    |   |   +-- dispositivo_service.py              # Servicio base
    |   |   +-- luz_inteligente_service.py          # Servicio Luz
    |   |   +-- termostato_service.py               # Servicio Termostato
    |   |   +-- camara_seguridad_service.py         # Servicio Cámara
    |   |   +-- cerradura_inteligente_service.py    # Servicio Cerradura
    |   |   +-- dispositivo_service_registry.py     # Registry + Singleton
    |   |
    |   +-- espacios/                # Servicios espaciales
    |   |   +-- __init__.py
    |   |   +-- casa_service.py                     # Servicio Casa
    |   |   +-- habitacion_service.py               # Servicio Habitación
    |   |   +-- configuracion_casa_service.py       # Servicio Configuración
    |   |
    |   +-- usuarios/                # Servicios de usuarios
    |   |   +-- __init__.py
    |   |   +-- usuario_service.py                  # Servicio Usuario
    |   |
    |   +-- negocio/                 # Servicios de alto nivel
    |       +-- __init__.py
    |       +-- casa_service.py                     # Operaciones casas
    |       +-- modo_sistema.py                     # Modos del sistema
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- __init__.py
    |   |
    |   +-- singleton/               # Patrón Singleton
    |   |   +-- __init__.py
    |   |
    |   +-- factory/                 # Patrón Factory Method
    |   |   +-- __init__.py
    |   |   +-- dispositivo_factory.py              # Factory de dispositivos
    |   |
    |   +-- observer/                # Patrón Observer
    |   |   +-- __init__.py
    |   |   +-- observable.py                       # Clase Observable[T]
    |   |   +-- observer.py                         # Interfaz Observer[T]
    |   |   +-- eventos/
    |   |       +-- __init__.py
    |   |       +-- evento_sensor.py                # Evento de sensores
    |   |       +-- evento_automatizacion.py        # Evento de automatización
    |   |
    |   +-- strategy/                # Patrón Strategy
    |       +-- __init__.py
    |       +-- automation_strategy.py              # Interfaz Strategy
    |       +-- impl/
    |           +-- __init__.py
    |           +-- iluminacion_strategy.py         # Iluminación
    |           +-- climatizacion_strategy.py       # Climatización
    |
    +-- sensores/                    # Sistema de sensores
    |   +-- __init__.py
    |   +-- sensor_movimiento_task.py               # Sensor movimiento
    |   +-- sensor_temperatura_task.py              # Sensor temperatura
    |   +-- sensor_apertura_task.py                 # Sensor apertura
    |
    +-- control/                     # Control de automatización
    |   +-- __init__.py
    |   +-- automation_control_task.py              # Controlador
    |
    +-- excepciones/                 # Excepciones personalizadas
        +-- __init__.py
        +-- smarthome_exception.py                  # Excepción base
        +-- capacidad_insuficiente_exception.py
        +-- permiso_denegado_exception.py
        +-- persistencia_exception.py
        +-- mensajes_exception.py                   # Mensajes centralizados
```

---

## Módulos del Sistema

### Módulo: `entidades`

**Responsabilidad**: Objetos de dominio puros (DTOs - Data Transfer Objects)

**Características**:
- Solo contienen datos y getters/setters
- NO contienen lógica de negocio
- Campos privados con encapsulación

**Clases principales**:
- `Dispositivo`: Interfaz base para todos los dispositivos
- `LuzInteligente`: Dispositivo de iluminación con intensidad y color
- `Termostato`: Dispositivo de climatización con temperatura
- `Casa`: Propiedad completa con habitaciones
- `Habitacion`: Espacio con dispositivos instalados
- `Usuario`: Persona con escenas asignadas

---

## Documentación Técnica

### Convenciones de Código

#### PEP 8 Compliance (100%)

- **Nombres de variables**: `snake_case`
- **Nombres de clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE` en `constantes.py`
- **Privados**: Prefijo `_nombre`

#### Docstrings (Google Style)

```python
def metodo(self, parametro: str) -> int:
    """
    Descripción breve del método.

    Args:
        parametro: Descripción del parámetro

    Returns:
        Descripción del valor de retorno

    Raises:
        ValueError: Cuando ocurre validación
    """
```

#### Type Hints

```python
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from modulo import Clase  # Evita imports circulares

def metodo(self, lista: List[int]) -> Optional[str]:
    pass
```

### Configuración de Constantes

Todas las constantes en `constantes.py`:

```python
# Dispositivos
INTENSIDAD_MIN = 0
INTENSIDAD_MAX = 100
TEMP_MIN = 10
TEMP_MAX = 30

# Sensores
INTERVALO_SENSOR_MOVIMIENTO = 2.0
INTERVALO_SENSOR_TEMPERATURA = 3.0
TEMP_AMBIENTE_MIN = -10
TEMP_AMBIENTE_MAX = 40

# Automatización
HORA_INICIO_NOCHE = 20
HORA_FIN_NOCHE = 7
```

**Regla**: NUNCA hardcodear valores mágicos en el código.

---

## Testing y Validación

### Ejecución del Sistema Completo

El archivo `main.py` contiene un test de integración completo que valida:

1. [x] Patrón Singleton - Instancia única compartida
2. [x] Patrón Factory - Creación de 4 tipos de dispositivos
3. [x] Patrón Observer - Sensores y notificaciones
4. [x] Patrón Strategy - Automatización diferenciada
5. [x] Instalación y control de dispositivos
6. [x] Sistema de automatización
7. [x] Gestión de usuarios con permisos
8. [x] Ejecución de escenas
9. [x] Persistencia y recuperación
10. [x] Threading y graceful shutdown

---

## Contribución

### Cómo Agregar un Nuevo Tipo de Dispositivo

#### Paso 1: Definir Constantes

En `constantes.py`:
```python
# Constantes del nuevo dispositivo
VOLTAJE_ENCHUFE = 220
CORRIENTE_MAX_ENCHUFE = 10
```

#### Paso 2: Crear Entidad

En `entidades/dispositivos/enchufe_inteligente.py`:
```python
from python_smarthome.entidades.dispositivos.dispositivo import Dispositivo
from python_smarthome.constantes import (
    VOLTAJE_ENCHUFE,
    CORRIENTE_MAX_ENCHUFE
)

class EnchufeInteligente(Dispositivo):
    """Entidad EnchufeInteligente - solo datos."""

    def __init__(self):
        super().__init__()
        self._voltaje = VOLTAJE_ENCHUFE
        self._corriente_maxima = CORRIENTE_MAX_ENCHUFE
        self._consumo_actual = 0.0

    def get_voltaje(self) -> int:
        return self._voltaje

    def get_corriente_maxima(self) -> int:
        return self._corriente_maxima

    def get_consumo_actual(self) -> float:
        return self._consumo_actual

    def set_consumo_actual(self, consumo: float) -> None:
        if consumo < 0:
            raise ValueError("Consumo cannot be negative")
        self._consumo_actual = consumo
```

#### Paso 3: Crear Servicio

En `servicios/dispositivos/enchufe_inteligente_service.py`:
```python
from python_smarthome.servicios.dispositivos.dispositivo_service import DispositivoService
from python_smarthome.patrones.strategy.impl.consumo_strategy import ConsumoStrategy

class EnchufeInteligenteService(DispositivoService):
    """Servicio para EnchufeInteligente."""

    def __init__(self):
        super().__init__(ConsumoStrategy())

    def mostrar_datos(self, dispositivo: 'EnchufeInteligente') -> None:
        super().mostrar_datos(dispositivo)
        print(f"Voltaje: {dispositivo.get_voltaje()}V")
        print(f"Consumo actual: {dispositivo.get_consumo_actual()}W")
```

#### Paso 4: Registrar en Registry

En `dispositivo_service_registry.py`:
```python
from python_smarthome.entidades.dispositivos.enchufe_inteligente import EnchufeInteligente
from python_smarthome.servicios.dispositivos.enchufe_inteligente_service import EnchufeInteligenteService

class DispositivoServiceRegistry:
    def __init__(self):
        self._enchufe_service = EnchufeInteligenteService()

        self._encender_handlers[EnchufeInteligente] = self._encender_enchufe
        self._mostrar_datos_handlers[EnchufeInteligente] = self._mostrar_datos_enchufe

    def _encender_enchufe(self, dispositivo):
        return self._enchufe_service.encender(dispositivo)

    def _mostrar_datos_enchufe(self, dispositivo):
        return self._enchufe_service.mostrar_datos(dispositivo)
```

#### Paso 5: Registrar en Factory

En `dispositivo_factory.py`:
```python
@staticmethod
def _crear_enchufe() -> EnchufeInteligente:
    from python_smarthome.entidades.dispositivos.enchufe_inteligente import EnchufeInteligente
    return EnchufeInteligente()

@staticmethod
def crear_dispositivo(tipo: str) -> Dispositivo:
    factories = {
        # ... existentes
        "EnchufeInteligente": DispositivoFactory._crear_enchufe
    }
```

#### Paso 6: Usar el Nuevo Dispositivo

```python
habitacion_service.instalar(habitacion, "EnchufeInteligente", 2)
```

---

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## Contacto y Soporte

- **Documentación**: Ver `CLAUDE_iot.md` para guía técnica detallada
- **Historias de Usuario**: Ver `USER_STORIES_iot.md` para casos de uso
- **Rúbrica de Evaluación**: Ver `RUBRICA_EVALUACION_iot.md`

---

## Notas Adicionales

### Compatibilidad con Windows

El sistema fue desarrollado y probado en Windows. Consideraciones:

- **NO usar emojis** en print (problema de encoding)
- **NO usar caracteres Unicode especiales** en consola
- Usar solo ASCII estándar: `[OK]`, `[!]`, `[INFO]`

### Rendimiento

- Sistema optimizado para operaciones locales
- Threads livianos para sensores
- Persistencia con Pickle (rápida pero NO para producción)

### Limitaciones Conocidas

1. Pickle NO es seguro para datos no confiables
2. Sistema single-process (no distribuido)
3. Sin base de datos relacional
4. Sin interfaz gráfica (solo CLI)

**Este es un proyecto EDUCATIVO** enfocado en patrones de diseño, NO en producción real.

---

**Última actualización**: Octubre 2025
**Versión del sistema**: 1.0.0
**Python requerido**: 3.13+