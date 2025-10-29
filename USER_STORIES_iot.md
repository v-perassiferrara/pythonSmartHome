# Historias de Usuario - Sistema de Domótica (Smart Home)

**Proyecto**: PythonSmartHome
**Versión**: 1.0.0
**Fecha**: Octubre 2025
**Metodología**: User Story Mapping

---

## Índice

1. [Epic 1: Gestión de Casa y Habitaciones](#epic-1-gestión-de-casa-y-habitaciones)
2. [Epic 2: Gestión de Dispositivos](#epic-2-gestión-de-dispositivos)
3. [Epic 3: Sistema de Sensores y Automatización](#epic-3-sistema-de-sensores-y-automatización)
4. [Epic 4: Gestión de Usuarios](#epic-4-gestión-de-usuarios)
5. [Epic 5: Operaciones de Negocio (Escenas y Modos)](#epic-5-operaciones-de-negocio-escenas-y-modos)
6. [Epic 6: Persistencia y Configuración](#epic-6-persistencia-y-configuración)
7. [Historias Técnicas (Patrones de Diseño)](#historias-técnicas-patrones-de-diseño)

---

## Epic 1: Gestión de Casa y Habitaciones

### US-001: Registrar Casa Inteligente

**Como** propietario de una casa
**Quiero** registrar mi propiedad con su dirección y superficie
**Para** tener un control oficial de mi hogar inteligente

#### Criterios de Aceptación

- [x] El sistema debe permitir crear una casa con:
  - Dirección única (cadena de texto)
  - Superficie en metros cuadrados (número positivo)
  - Nombre del propietario (cadena de texto)
- [x] La superficie debe ser mayor a 0, si no lanzar `ValueError`
- [x] La casa debe poder modificarse posteriormente
- [x] El sistema debe validar que los datos sean consistentes

#### Detalles Técnicos

**Clase**: `Casa` (`python_smarthome/entidades/espacios/casa.py`)
**Servicio**: `CasaService` (`python_smarthome/servicios/espacios/casa_service.py`)

**Código de ejemplo**:
```python
from python_smarthome.servicios.espacios.casa_service import CasaService

casa_service = CasaService()
casa = casa_service.crear_casa_con_habitaciones(
    direccion="Calle Falsa 123",
    superficie=150.0,
    propietario="Juan Perez",
    nombres_habitaciones=["Living", "Cocina", "Dormitorio"]
)
```

**Validaciones**:
```python
# Superficie válida
casa.set_superficie(180.0)  # OK

# Superficie inválida
casa.set_superficie(-50.0)  # ValueError: superficie debe ser mayor a cero
casa.set_superficie(0)  # ValueError: superficie debe ser mayor a cero
```

**Trazabilidad**: `main.py` líneas 111-116

---

### US-002: Crear Habitaciones en Casa

**Como** administrador de casa inteligente
**Quiero** crear habitaciones asociadas a mi casa
**Para** organizar los dispositivos en espacios identificables

#### Criterios de Aceptación

- [x] Una habitación debe tener:
  - Nombre identificatorio único
  - Superficie máxima (parte de la casa)
  - Lista de dispositivos (vacía al inicio)
  - Lista de sensores (vacía al inicio)
- [x] La habitación debe estar asociada a una casa válida
- [x] El sistema debe controlar la cantidad de dispositivos
- [x] Las habitaciones deben crearse como lista

#### Detalles Técnicos

**Clase**: `Habitacion` (`python_smarthome/entidades/espacios/habitacion.py`)
**Servicio**: `HabitacionService` (`python_smarthome/servicios/espacios/habitacion_service.py`)

**Código de ejemplo**:
```python
from python_smarthome.entidades.espacios.habitacion import Habitacion

habitacion = Habitacion(
    nombre="Living",
    superficie=30.0
)

# Obtener desde casa
habitaciones = casa.get_habitaciones()
living = habitaciones[0]
```

**Validaciones**:
```python
# Dispositivos válidos
habitacion.agregar_dispositivo(luz)  # OK

# Máximo de dispositivos
if len(habitacion.get_dispositivos()) >= MAX_DISPOSITIVOS_HABITACION:
    raise CapacidadInsuficienteException()
```

**Trazabilidad**: `main.py` línea 117, `casa_service.py` líneas 21-54

---

### US-003: Crear Configuración de Casa Completa

**Como** auditor de sistemas de seguridad
**Quiero** crear una configuración que vincule casa, habitaciones y fecha de instalación
**Para** tener documentación oficial completa

#### Criterios de Aceptación

- [x] Una configuración de casa debe contener:
  - ID de configuración (número único)
  - Referencia a Casa
  - Lista de habitaciones
  - Nombre del propietario
  - Fecha de instalación (fecha)
- [x] Todos los campos son obligatorios
- [x] La configuración debe poder persistirse y recuperarse
- [x] La configuración debe poder mostrarse en consola con formato

#### Detalles Técnicos

**Clase**: `ConfiguracionCasa` (`python_smarthome/entidades/espacios/configuracion_casa.py`)
**Servicio**: `ConfiguracionCasaService` (`python_smarthome/servicios/espacios/configuracion_casa_service.py`)

**Código de ejemplo**:
```python
from python_smarthome.entidades.espacios.configuracion_casa import ConfiguracionCasa
from datetime import date

config = ConfiguracionCasa(
    id_config=1,
    casa=casa,
    fecha_instalacion=date.today(),
    propietario="Juan Perez"
)
```

**Salida de mostración**:
```
CONFIGURACION DE CASA
=====================
ID Config:   1
Propietario: Juan Perez
Direccion:   Calle Falsa 123
Superficie:  150.0 m2
Fecha:       2025-10-29
Cantidad de habitaciones: 3
Cantidad total de dispositivos: 15
```

**Trazabilidad**: `main.py` líneas 123-129

---

## Epic 2: Gestión de Dispositivos

### US-004: Instalar Luces Inteligentes en Habitación

**Como** usuario de casa inteligente
**Quiero** instalar luces inteligentes en una habitación
**Para** controlar la iluminación de forma automatizada

#### Criterios de Aceptación

- [x] Debe poder instalar múltiples luces simultáneamente
- [x] Cada luz debe tener:
  - Estado: encendida/apagada (bool)
  - Intensidad: 0-100% (int)
  - Color RGB: tupla (R, G, B)
  - ID único de dispositivo
- [x] El sistema debe verificar capacidad de la habitación
- [x] Si no hay capacidad, lanzar `CapacidadInsuficienteException`
- [x] Las luces deben crearse vía Factory Method (no instanciación directa)

#### Detalles Técnicos

**Clase**: `LuzInteligente` (`python_smarthome/entidades/dispositivos/luz_inteligente.py`)
**Servicio**: `LuzInteligenteService` (`python_smarthome/servicios/dispositivos/luz_inteligente_service.py`)
**Factory**: `DispositivoFactory` (`python_smarthome/patrones/factory/dispositivo_factory.py`)

**Código de ejemplo**:
```python
from python_smarthome.servicios.espacios.habitacion_service import HabitacionService

habitacion_service = HabitacionService()

# Instalar 3 luces (usa Factory Method internamente)
habitacion_service.instalar(habitacion, "LuzInteligente", 3)
```

**Constantes utilizadas**:
```python
INTENSIDAD_MIN = 0  # %
INTENSIDAD_MAX = 100  # %
COLOR_INICIAL = (255, 255, 255)  # Blanco
```

**Trazabilidad**: `main.py` línea 141

---

### US-005: Instalar Termostatos para Climatización

**Como** usuario preocupado por la eficiencia energética
**Quiero** instalar termostatos inteligentes
**Para** controlar la temperatura de forma automatizada

#### Criterios de Aceptación

- [x] Debe poder instalar múltiples termostatos simultáneamente
- [x] Cada termostato debe tener:
  - Estado: encendido/apagado (bool)
  - Temperatura objetivo: 10-30°C (float)
  - Temperatura actual: lectura del sensor (float)
  - Modo: calor/frío/auto (enum)
- [x] El sistema debe verificar capacidad de la habitación
- [x] Los termostatos deben crearse vía Factory Method

#### Detalles Técnicos

**Clase**: `Termostato` (`python_smarthome/entidades/dispositivos/termostato.py`)
**Servicio**: `TermostatoService` (`python_smarthome/servicios/dispositivos/termostato_service.py`)

**Código de ejemplo**:
```python
# Instalar 1 termostato
habitacion_service.instalar(habitacion, "Termostato", 1)
```

**Constantes utilizadas**:
```python
TEMP_MIN = 10  # °C
TEMP_MAX = 30  # °C
TEMP_OBJETIVO_INICIAL = 22  # °C
```

**Trazabilidad**: `main.py` línea 142

---

### US-006: Instalar Cámaras de Seguridad

**Como** propietario preocupado por la seguridad
**Quiero** instalar cámaras de seguridad inteligentes
**Para** monitorear mi hogar en tiempo real

#### Criterios de Aceptación

- [x] Debe poder instalar múltiples cámaras simultáneamente
- [x] Cada cámara debe tener:
  - Estado: encendida/apagada (bool)
  - Modo grabación: activado/desactivado (bool)
  - Detección de movimiento: activada/desactivada (bool)
  - Resolución: 720p/1080p/4K (string)
- [x] Las cámaras ocupan capacidad en la habitación
- [x] El sistema debe verificar capacidad disponible

#### Detalles Técnicos

**Clase**: `CamaraSeguridad` (`python_smarthome/entidades/dispositivos/camara_seguridad.py`)
**Servicio**: `CamaraSeguridadService` (`python_smarthome/servicios/dispositivos/camara_seguridad_service.py`)

**Código de ejemplo**:
```python
# Instalar 2 cámaras
habitacion_service.instalar(habitacion, "CamaraSeguridad", 2)
```

**Constantes utilizadas**:
```python
RESOLUCION_INICIAL = "1080p"
DETECCION_MOVIMIENTO_INICIAL = True
```

**Trazabilidad**: `main.py` línea 143

---

### US-007: Instalar Cerraduras Inteligentes

**Como** usuario preocupado por la seguridad física
**Quiero** instalar cerraduras inteligentes
**Para** controlar el acceso a mi hogar de forma remota

#### Criterios de Aceptación

- [x] Debe poder instalar múltiples cerraduras simultáneamente
- [x] Cada cerradura debe tener:
  - Estado: bloqueada/desbloqueada (bool)
  - Método de acceso: PIN/huella/tarjeta (enum)
  - Log de accesos (lista de eventos)
  - Batería: 0-100% (int)
- [x] Las cerraduras no requieren mucha capacidad
- [x] El sistema debe verificar capacidad disponible

#### Detalles Técnicos

**Clase**: `CerraduraInteligente` (`python_smarthome/entidades/dispositivos/cerradura_inteligente.py`)
**Servicio**: `CerraduraInteligenteService` (`python_smarthome/servicios/dispositivos/cerradura_inteligente_service.py`)

**Código de ejemplo**:
```python
# Instalar 2 cerraduras
habitacion_service.instalar(habitacion, "CerraduraInteligente", 2)
```

**Constantes utilizadas**:
```python
BATERIA_INICIAL = 100  # %
METODO_ACCESO_INICIAL = "PIN"
```

**Verificar estado**:
```python
cerradura = dispositivos[0]
if cerradura.is_bloqueada():
    print("Cerradura bloqueada")
else:
    print("Cerradura desbloqueada")
```

**Trazabilidad**: `main.py` línea 144

---

### US-008: Encender/Apagar Todos los Dispositivos de una Habitación

**Como** usuario del sistema
**Quiero** encender o apagar todos los dispositivos de una habitación
**Para** controlar el estado de forma centralizada

#### Criterios de Aceptación

- [x] El control debe:
  - Cambiar estado de todos los dispositivos
  - Aplicar estrategia específica por tipo
  - Luces: ajustar intensidad y color
  - Termostatos: ajustar temperatura objetivo
  - Cámaras: activar/desactivar grabación
  - Cerraduras: bloquear/desbloquear
- [x] El sistema debe usar el patrón Strategy para control
- [x] Cada dispositivo debe responder según su estrategia

#### Detalles Técnicos

**Servicio**: `HabitacionService.encender_todos()` / `apagar_todos()`
**Estrategias**:
- `IluminacionStrategy` (luces)
- `ClimatizacionStrategy` (termostatos)
- `SeguridadStrategy` (cámaras, cerraduras)

**Código de ejemplo**:
```python
# Encender todos los dispositivos
habitacion_service.encender_todos(habitacion)

# Apagar todos los dispositivos
habitacion_service.apagar_todos(habitacion)
```

**Ejecución por tipo**:
```python
# LuzInteligente (iluminación)
# - Encender: intensidad 100%, color blanco

# Termostato (climatización)
# - Encender: temperatura objetivo 22°C

# CamaraSeguridad (seguridad)
# - Encender: activar grabación

# CerraduraInteligente (seguridad)
# - Encender: bloquear
```

**Trazabilidad**: `habitacion_service.py` líneas 82-129

---

### US-009: Mostrar Datos de Dispositivos por Tipo

**Como** administrador de casa inteligente
**Quiero** ver los datos de cada dispositivo de forma específica
**Para** conocer el estado actual de mis dispositivos

#### Criterios de Aceptación

- [x] El sistema debe mostrar datos específicos por tipo:
  - **LuzInteligente**: Dispositivo, Estado, Intensidad, Color RGB
  - **Termostato**: Dispositivo, Estado, Temp Objetivo, Temp Actual
  - **CamaraSeguridad**: Dispositivo, Estado, Grabación, Detección
  - **CerraduraInteligente**: Dispositivo, Estado, Bloqueada, Batería
- [x] Usar el patrón Registry para dispatch polimórfico
- [x] NO usar cascadas de isinstance()

#### Detalles Técnicos

**Registry**: `DispositivoServiceRegistry.mostrar_datos()`

**Código de ejemplo**:
```python
from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry

registry = DispositivoServiceRegistry.get_instance()

for dispositivo in habitacion.get_dispositivos():
    registry.mostrar_datos(dispositivo)
    # Despacho automático al servicio correcto
```

**Salida ejemplo (LuzInteligente)**:
```
Dispositivo: LuzInteligente
ID: 1
Estado: encendida
Intensidad: 75%
Color RGB: (255, 200, 150)
```

**Trazabilidad**: `dispositivo_service_registry.py` líneas 78-89

---

## Epic 3: Sistema de Sensores y Automatización

### US-010: Monitorear Movimiento en Tiempo Real

**Como** sistema de automatización
**Quiero** detectar movimiento cada 2 segundos
**Para** tomar decisiones de automatización basadas en presencia

#### Criterios de Aceptación

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Detectar movimiento cada 2 segundos (configurable)
  - Generar detecciones aleatorias (True/False)
  - Notificar a observadores cada vez que detecta
  - Soportar detención graceful con timeout
- [x] Implementar patrón Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[bool]`

#### Detalles Técnicos

**Clase**: `SensorMovimientoTask` (`python_smarthome/sensores/sensor_movimiento_task.py`)
**Patrón**: Observer (Observable[bool])

**Código de ejemplo**:
```python
from python_smarthome.sensores.sensor_movimiento_task import SensorMovimientoTask

# Crear sensor (thread daemon)
sensor_mov = SensorMovimientoTask()

# Iniciar detección continua
sensor_mov.start()

# Detener cuando sea necesario
sensor_mov.detener()
sensor_mov.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_MOVIMIENTO = 2.0  # segundos
```

**Eventos generados**:
```python
# Cada detección notifica valor bool a observadores
movimiento: bool = True  # Movimiento detectado
self.notificar_observadores(movimiento)
```

**Trazabilidad**: `main.py` líneas 158-166

---

### US-011: Monitorear Temperatura Ambiental en Tiempo Real

**Como** sistema de automatización
**Quiero** leer la temperatura ambiental cada 3 segundos
**Para** complementar datos en decisiones de climatización

#### Criterios de Aceptación

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer temperatura cada 3 segundos (configurable)
  - Generar lecturas aleatorias entre -10°C y 40°C
  - Notificar a observadores cada vez que lee
  - Soportar detención graceful con timeout
- [x] Implementar patrón Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Técnicos

**Clase**: `SensorTemperaturaTask` (`python_smarthome/sensores/sensor_temperatura_task.py`)
**Patrón**: Observer (Observable[float])

**Código de ejemplo**:
```python
from python_smarthome.sensores.sensor_temperatura_task import SensorTemperaturaTask

# Crear sensor (thread daemon)
sensor_temp = SensorTemperaturaTask()

# Iniciar lectura continua
sensor_temp.start()

# Detener cuando sea necesario
sensor_temp.detener()
sensor_temp.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_TEMPERATURA = 3.0  # segundos
TEMP_AMBIENTE_MIN = -10  # °C
TEMP_AMBIENTE_MAX = 40  # °C
```

**Trazabilidad**: `main.py` líneas 158-166

---

### US-012: Control Automático Basado en Sensores

**Como** sistema de automatización
**Quiero** ejecutar acciones automáticamente cuando se cumplan condiciones
**Para** optimizar el uso de dispositivos según necesidades reales

#### Criterios de Aceptación

- [x] El controlador debe:
  - Ejecutarse en un thread daemon separado
  - Evaluar condiciones cada 2.5 segundos
  - Observar sensores de movimiento y temperatura
  - Ejecutar acciones cuando:
    - Movimiento detectado en modo noche (20:00-07:00), O
    - Temperatura fuera de rango confort (18-24°C)
  - NO ejecutar si condiciones no se cumplen
  - Manejar excepción si no hay permisos
- [x] Implementar patrón Observer (Observer[bool] y Observer[float])
- [x] Recibir sensores vía inyección de dependencias

#### Detalles Técnicos

**Clase**: `AutomationControlTask` (`python_smarthome/control/automation_control_task.py`)
**Patrón**: Observer (observa sensores)

**Código de ejemplo**:
```python
from python_smarthome.control.automation_control_task import AutomationControlTask

# Inyectar dependencias
automation_control = AutomationControlTask(
    sensor_movimiento=sensor_mov,
    sensor_temperatura=sensor_temp,
    habitacion=habitacion,
    habitacion_service=habitacion_service
)

# Iniciar control automático
automation_control.start()

# Detener cuando sea necesario
automation_control.detener()
automation_control.join(timeout=2.0)
```

**Lógica de decisión**:
```python
hora_actual = datetime.now().hour
es_modo_noche = (HORA_INICIO_NOCHE <= hora_actual) or (hora_actual <= HORA_FIN_NOCHE)

if movimiento_detectado and es_modo_noche:
    # ENCENDER LUCES con intensidad reducida
    habitacion_service.ejecutar_escena(habitacion, "ModoNoche")
elif temperatura < TEMP_CONFORT_MIN or temperatura > TEMP_CONFORT_MAX:
    # AJUSTAR TERMOSTATO
    habitacion_service.ajustar_climatizacion(habitacion, TEMP_CONFORT_OBJETIVO)
```

**Constantes de automatización**:
```python
HORA_INICIO_NOCHE = 20  # 20:00
HORA_FIN_NOCHE = 7  # 07:00
TEMP_CONFORT_MIN = 18  # °C
TEMP_CONFORT_MAX = 24  # °C
TEMP_CONFORT_OBJETIVO = 22  # °C
INTERVALO_CONTROL_AUTOMATION = 2.5  # segundos
```

**Trazabilidad**: `main.py` líneas 160-166, `automation_control_task.py` líneas 67-91

---

### US-013: Detener Sistema de Automatización de Forma Segura

**Como** administrador del sistema
**Quiero** detener el sistema de automatización de forma controlada
**Para** evitar corrupción de datos o procesos incompletos

#### Criterios de Aceptación

- [x] El sistema debe:
  - Detener todos los threads con `threading.Event`
  - Esperar finalización con timeout configurable (2s)
  - NO forzar terminación abrupta
  - Permitir que threads completen operación actual
- [x] Threads deben ser daemon (finalizan con main)
- [x] Usar timeout de `constantes.py`

#### Detalles Técnicos

**Código de ejemplo**:
```python
from python_smarthome.constantes import THREAD_JOIN_TIMEOUT

# Detener sensores y control
sensor_mov.detener()
sensor_temp.detener()
automation_control.detener()

# Esperar finalización con timeout
sensor_mov.join(timeout=THREAD_JOIN_TIMEOUT)  # 2s
sensor_temp.join(timeout=THREAD_JOIN_TIMEOUT)
automation_control.join(timeout=THREAD_JOIN_TIMEOUT)

# Si timeout expira, threads daemon finalizan automáticamente
```

**Constantes**:
```python
THREAD_JOIN_TIMEOUT = 2.0  # segundos
```

**Trazabilidad**: `main.py` líneas 256-263

---

## Epic 4: Gestión de Usuarios

### US-014: Registrar Usuario con Escenas Asignadas

**Como** administrador de casa inteligente
**Quiero** registrar usuarios con sus escenas personalizadas
**Para** organizar el acceso y personalización del sistema

#### Criterios de Aceptación

- [x] Un usuario debe tener:
  - ID único (número entero)
  - Nombre completo
  - Nivel de acceso (1-5: invitado, familiar, propietario, admin, super)
  - Lista de escenas asignadas (puede estar vacía)
- [x] Las escenas deben tener:
  - ID único
  - Nombre de la escena
  - Descripción
  - Lista de acciones (dispositivos a controlar)
- [x] Un usuario puede tener múltiples escenas
- [x] Lista de escenas es inmutable (defensive copy)

#### Detalles Técnicos

**Clases**:
- `Usuario` (`python_smarthome/entidades/usuarios/usuario.py`)
- `Escena` (`python_smarthome/entidades/usuarios/escena.py`)
- `NivelAcceso` (`python_smarthome/entidades/usuarios/nivel_acceso.py`)

**Código de ejemplo**:
```python
from python_smarthome.entidades.usuarios.usuario import Usuario
from python_smarthome.entidades.usuarios.escena import Escena
from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso

# Crear escenas
escenas = [
    Escena(1, "Modo Noche", "Luces tenues, termostato bajo"),
    Escena(2, "Modo Cine", "Luces apagadas, TV encendida"),
    Escena(3, "Modo Vacaciones", "Todo apagado, cámaras activas")
]

# Crear usuario
usuario = Usuario(
    id_usuario=1,
    nombre="Juan Perez",
    nivel_acceso=NivelAcceso.PROPIETARIO,
    escenas=escenas
)
```

**Trazabilidad**: `main.py` líneas 176-185

---

### US-015: Asignar Nivel de Acceso a Usuario

**Como** propietario de casa
**Quiero** asignar niveles de acceso a usuarios
**Para** controlar qué dispositivos y escenas pueden usar

#### Criterios de Aceptación

- [x] Un nivel de acceso debe tener:
  - Valor numérico (1-5)
  - Descripción del nivel
  - Permisos asociados
- [x] El sistema debe verificar nivel antes de ejecutar acciones
- [x] Si no tiene nivel suficiente, no puede ejecutar escena
- [x] El servicio debe permitir asignar/actualizar nivel

#### Detalles Técnicos

**Enum**: `NivelAcceso` (`python_smarthome/entidades/usuarios/nivel_acceso.py`)
**Servicio**: `UsuarioService.asignar_nivel_acceso()`

**Código de ejemplo**:
```python
from python_smarthome.servicios.usuarios.usuario_service import UsuarioService
from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso

usuario_service = UsuarioService()

# Asignar nivel de acceso
usuario_service.asignar_nivel_acceso(
    usuario=usuario,
    nivel=NivelAcceso.PROPIETARIO
)

# Verificar nivel
if usuario.get_nivel_acceso().value >= NivelAcceso.FAMILIAR.value:
    print("Usuario tiene permisos suficientes")
else:
    print("Usuario NO tiene permisos")
```

**Niveles de acceso**:
```python
class NivelAcceso(Enum):
    INVITADO = 1      # Solo consultar
    FAMILIAR = 2      # Ejecutar escenas básicas
    PROPIETARIO = 3   # Ejecutar todas las escenas
    ADMIN = 4         # Configurar dispositivos
    SUPER = 5         # Configurar sistema completo
```

**Trazabilidad**: `main.py` líneas 191-196

---

### US-016: Ejecutar Escenas Asignadas a Usuario

**Como** usuario del sistema
**Quiero** ejecutar las escenas que me fueron asignadas
**Para** personalizar mi experiencia en la casa

#### Criterios de Aceptación

- [x] El usuario debe:
  - Tener nivel de acceso suficiente
  - Ejecutar solo escenas asignadas
  - Aplicar acciones a dispositivos específicos
  - Ver confirmación de ejecución
- [x] Las escenas deben ejecutarse en orden de prioridad
- [x] Si no tiene nivel de acceso, retornar False (no ejecuta)
- [x] Si tiene nivel de acceso, retornar True (ejecuta)

#### Detalles Técnicos

**Servicio**: `UsuarioService.ejecutar_escena()`

**Código de ejemplo**:
```python
# Ejecutar escena
resultado = usuario_service.ejecutar_escena(
    usuario=usuario,
    escena_id=1,  # Modo Noche
    habitacion=habitacion
)

if resultado:
    print("Escena ejecutada exitosamente")
else:
    print("No puede ejecutar - permisos insuficientes")
```

**Salida esperada**:
```
Ejecutando escena: Modo Noche
Accion: Ajustando luces a 30% de intensidad
Accion: Ajustando termostato a 20 C
Accion: Desactivando camaras
Escena ejecutada exitosamente
```

**Ordenamiento**:
```python
# Escenas se ordenan por prioridad
# Usa método estático _obtener_prioridad_escena() en lugar de lambda
```

**Trazabilidad**: `main.py` líneas 199-204, `usuario_service.py` líneas 34-72

---

### US-017: Asignar Usuarios a Casa

**Como** propietario de casa
**Quiero** asignar usuarios a mi casa inteligente
**Para** organizar el acceso por propiedad

#### Criterios de Aceptación

- [x] Una casa debe poder tener múltiples usuarios
- [x] La lista de usuarios debe ser inmutable (defensive copy)
- [x] Debe poder obtener lista de usuarios
- [x] Debe poder reemplazar lista completa de usuarios

#### Detalles Técnicos

**Clase**: `Casa.set_usuarios()`

**Código de ejemplo**:
```python
usuarios = [
    Usuario(1, "Juan Perez", NivelAcceso.PROPIETARIO, escenas.copy()),
    Usuario(2, "Maria Lopez", NivelAcceso.FAMILIAR, escenas.copy())
]

# Asignar usuarios a casa
casa.set_usuarios(usuarios)

# Obtener usuarios (copia inmutable)
lista_usuarios = casa.get_usuarios()
```

**Trazabilidad**: `main.py` línea 187

---

## Epic 5: Operaciones de Negocio (Escenas y Modos)

### US-018: Gestionar Múltiples Casas

**Como** propietario de múltiples propiedades
**Quiero** gestionar varias casas desde un servicio centralizado
**Para** tener control unificado de todas mis propiedades

#### Criterios de Aceptación

- [x] El servicio debe permitir:
  - Agregar casas (ConfiguracionCasa)
  - Buscar casa por dirección
  - Activar modo específico en una casa
  - Ejecutar escenas globales
- [x] Debe manejar múltiples casas simultáneamente
- [x] Debe usar diccionario interno para almacenar casas

#### Detalles Técnicos

**Servicio**: `CasaService` (`python_smarthome/servicios/negocio/casa_service.py`)

**Código de ejemplo**:
```python
from python_smarthome.servicios.negocio.casa_service import CasaService

casa_service = CasaService()

# Agregar casa
casa_service.add_casa(config)

# Buscar casa por dirección
casa = casa_service.buscar_casa("Calle Falsa 123")
```

**Trazabilidad**: `main.py` línea 225

---

### US-019: Activar Modo del Sistema

**Como** usuario del sistema
**Quiero** activar modos predefinidos del sistema (Noche, Vacaciones, Fiesta)
**Para** configurar múltiples dispositivos con un solo comando

#### Criterios de Aceptación

- [x] Debe permitir especificar:
  - Dirección de la casa
  - Modo a activar (ModoNoche, ModoVacaciones, ModoFiesta, ModoCine)
- [x] Debe configurar todos los dispositivos según el modo
- [x] Debe mostrar mensaje de confirmación
- [x] Si casa no existe, manejar error apropiadamente

#### Detalles Técnicos

**Servicio**: `CasaService.activar_modo()`
**Enum**: `ModoSistema` (`python_smarthome/servicios/negocio/modo_sistema.py`)

**Código de ejemplo**:
```python
from python_smarthome.servicios.negocio.modo_sistema import ModoSistema

# Activar modo noche
casa_service.activar_modo(
    direccion="Calle Falsa 123",
    modo=ModoSistema.NOCHE
)
```

**Modos disponibles**:
```python
class ModoSistema(Enum):
    NOCHE = "noche"           # Luces 30%, temp 20°C, cámaras ON
    VACACIONES = "vacaciones" # Todo OFF, cámaras ON, cerraduras ON
    FIESTA = "fiesta"         # Luces 100% colores, música ON
    CINE = "cine"             # Luces OFF, TV ON, sonido surround
```

**Salida esperada**:
```
Activando modo: NOCHE
Configurando dispositivos...
Modo NOCHE activado exitosamente
```

**Trazabilidad**: `main.py` línea 228

---

### US-020: Agrupar Dispositivos por Tipo

**Como** administrador del sistema
**Quiero** agrupar todos los dispositivos de un tipo específico
**Para** realizar operaciones masivas sobre ellos

#### Criterios de Aceptación

- [x] Debe permitir agrupar por tipo de dispositivo (Class type)
- [x] Debe:
  - Buscar todos los dispositivos del tipo especificado
  - Agruparlos en todas las habitaciones
  - Empaquetarlos en un contenedor genérico tipo-seguro
  - Mostrar cantidad agrupada
- [x] Usar Generics para tipo-seguridad: `GrupoDispositivos[T]`
- [x] Permitir mostrar contenido del grupo

#### Detalles Técnicos

**Servicio**: `CasaService.agrupar_por_tipo()`
**Clase**: `GrupoDispositivos[T]` (`python_smarthome/servicios/negocio/grupo_dispositivos.py`)

**Código de ejemplo**:
```python
from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
from python_smarthome.entidades.dispositivos.termostato import Termostato

# Agrupar todas las luces
grupo_luces = casa_service.agrupar_por_tipo(LuzInteligente)
grupo_luces.mostrar_contenido_grupo()

# Agrupar todos los termostatos
grupo_termostatos = casa_service.agrupar_por_tipo(Termostato)
grupo_termostatos.mostrar_contenido_grupo()
```

**Salida esperada**:
```
AGRUPANDO 8 unidades de <class 'python_smarthome.entidades.dispositivos.luz_inteligente.LuzInteligente'>

Contenido del grupo:
  Tipo: LuzInteligente
  Cantidad: 8
  ID Grupo: 1

AGRUPANDO 3 unidades de <class 'python_smarthome.entidades.dispositivos.termostato.Termostato'>

Contenido del grupo:
  Tipo: Termostato
  Cantidad: 3
  ID Grupo: 2
```

**Tipo-seguridad**:
```python
# GrupoDispositivos es genérico tipo-seguro
grupo_luces: GrupoDispositivos[LuzInteligente] = ...
grupo_termostatos: GrupoDispositivos[Termostato] = ...
```

**Trazabilidad**: `main.py` líneas 232-236

---

## Epic 6: Persistencia y Configuración

### US-021: Persistir Configuración de Casa en Disco

**Como** administrador del sistema
**Quiero** guardar configuraciones de casa en disco
**Para** mantener datos permanentes entre ejecuciones

#### Criterios de Aceptación

- [x] El sistema debe:
  - Serializar ConfiguracionCasa completa con Pickle
  - Guardar en directorio `data/`
  - Nombre de archivo: `{propietario}.dat`
  - Crear directorio si no existe
  - Mostrar mensaje de confirmación
- [x] Si ocurre error, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Técnicos

**Servicio**: `ConfiguracionCasaService.persistir()`

**Código de ejemplo**:
```python
from python_smarthome.servicios.espacios.configuracion_casa_service import ConfiguracionCasaService

config_service = ConfiguracionCasaService()

# Persistir configuración
config_service.persistir(config)
# Crea: data/Juan Perez.dat
```

**Salida esperada**:
```
Configuracion de Juan Perez persistida exitosamente en data/Juan Perez.dat
```

**Constantes**:
```python
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
```

**Manejo de errores**:
```python
try:
    config_service.persistir(config)
except PersistenciaException as e:
    print(e.get_user_message())
    print(f"Archivo: {e.get_nombre_archivo()}")
    print(f"Operacion: {e.get_tipo_operacion().value}")
```

**Trazabilidad**: `main.py` línea 242, `configuracion_casa_service.py` líneas 62-112

---

### US-022: Recuperar Configuración de Casa desde Disco

**Como** auditor
**Quiero** recuperar configuraciones guardadas previamente
**Para** consultar históricos y realizar auditorías

#### Criterios de Aceptación

- [x] El sistema debe:
  - Deserializar archivo `.dat` con Pickle
  - Buscar en directorio `data/`
  - Validar que propietario no sea nulo/vacío
  - Retornar ConfiguracionCasa completa
  - Mostrar mensaje de confirmación
- [x] Si archivo no existe, lanzar `PersistenciaException`
- [x] Si archivo corrupto, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Técnicos

**Servicio**: `ConfiguracionCasaService.leer_configuracion()` (método estático)

**Código de ejemplo**:
```python
# Leer configuración persistida
config_leida = ConfiguracionCasaService.leer_configuracion("Juan Perez")

# Mostrar datos recuperados
config_service.mostrar_datos(config_leida)
```

**Salida esperada**:
```
Configuracion de Juan Perez recuperada exitosamente desde data/Juan Perez.dat

CONFIGURACION DE CASA
=====================
ID Config:   1
Propietario: Juan Perez
Direccion:   Calle Falsa 123
...
```

**Validaciones**:
```python
# Propietario vacío
try:
    ConfiguracionCasaService.leer_configuracion("")
except ValueError as e:
    print("El nombre del propietario no puede ser nulo o vacio")

# Archivo no existe
try:
    ConfiguracionCasaService.leer_configuracion("NoExiste")
except PersistenciaException as e:
    print(f"Archivo no encontrado: {e.get_nombre_archivo()}")
```

**Trazabilidad**: `main.py` líneas 246-247, `configuracion_casa_service.py` líneas 114-171

---

### US-023: Mostrar Datos Completos de Configuración de Casa

**Como** auditor
**Quiero** ver todos los datos de una configuración en formato legible
**Para** analizar la información completa de una casa inteligente

#### Criterios de Aceptación

- [x] El sistema debe mostrar:
  - Encabezado "CONFIGURACION DE CASA"
  - ID de configuración
  - Propietario
  - Dirección de la casa
  - Superficie de la casa
  - Fecha de instalación
  - Cantidad de habitaciones
  - Cantidad total de dispositivos
  - Listado detallado de cada dispositivo
- [x] Cada dispositivo debe mostrarse con datos específicos de su tipo
- [x] Usar Registry para dispatch polimórfico

#### Detalles Técnicos

**Servicio**: `ConfiguracionCasaService.mostrar_datos()`

**Código de ejemplo**:
```python
# Mostrar configuración completa
config_service.mostrar_datos(config)
```

**Salida esperada**:
```
CONFIGURACION DE CASA
=====================
ID Config:   1
Propietario: Juan Perez
Direccion:   Calle Falsa 123
Superficie:  150.0 m2
Fecha:       2025-10-29
Cantidad de habitaciones: 3
Cantidad total de dispositivos: 15
Listado de Dispositivos
____________________________

Dispositivo: LuzInteligente
ID: 1
Estado: encendida
Intensidad: 75%
Color RGB: (255, 200, 150)

Dispositivo: Termostato
ID: 2
Estado: encendido
Temp Objetivo: 22.0 C
Temp Actual: 21.5 C

...
```

**Trazabilidad**: `main.py` línea 247, `configuracion_casa_service.py` líneas 28-60

---

## Historias Técnicas (Patrones de Diseño)

### US-TECH-001: Implementar Singleton para DispositivoServiceRegistry

**Como** arquitecto de software
**Quiero** garantizar una única instancia del registro de servicios
**Para** compartir estado consistente entre todos los servicios

#### Criterios de Aceptación

- [x] Implementar patrón Singleton thread-safe
- [x] Usar double-checked locking con Lock
- [x] Inicialización perezosa (lazy initialization)
- [x] Método `get_instance()` para acceso
- [x] Constructor `__new__` para controlar instanciación
- [x] NO permitir múltiples instancias

#### Detalles Técnicos

**Clase**: `DispositivoServiceRegistry`
**Patrón**: Singleton

**Implementación**:
```python
from threading import Lock

class DispositivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked
                    cls._instance = super().__new__(cls)
                    # Inicializar servicios una sola vez
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
```

**Uso**:
```python
# Opción 1: Instanciación directa
registry = DispositivoServiceRegistry()

# Opción 2: Método get_instance()
registry = DispositivoServiceRegistry.get_instance()

# Ambas retornan la MISMA instancia
assert registry is DispositivoServiceRegistry.get_instance()
```

**Trazabilidad**: `dispositivo_service_registry.py` líneas 20-46

---

### US-TECH-002: Implementar Factory Method para Creación de Dispositivos

**Como** arquitecto de software
**Quiero** centralizar creación de dispositivos mediante Factory Method
**Para** desacoplar cliente de clases concretas

#### Criterios de Aceptación

- [x] Crear clase `DispositivoFactory` con método estático
- [x] Soportar creación de: LuzInteligente, Termostato, CamaraSeguridad, CerraduraInteligente
- [x] Usar diccionario de factories (no if/elif cascades)
- [x] Lanzar `ValueError` si tipo desconocido
- [x] Retornar tipo base `Dispositivo` (no tipos concretos)
- [x] NO usar lambdas - usar métodos estáticos dedicados

#### Detalles Técnicos

**Clase**: `DispositivoFactory`
**Patrón**: Factory Method

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

    @staticmethod
    def _crear_luz() -> LuzInteligente:
        from python_smarthome.entidades.dispositivos.luz_inteligente import LuzInteligente
        return LuzInteligente()

    # ... otros métodos _crear_*
```

**Uso**:
```python
from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory

# Cliente NO conoce clases concretas
dispositivo = DispositivoFactory.crear_dispositivo("LuzInteligente")
# Retorna Dispositivo (interfaz), no LuzInteligente (concreto)
```

**Trazabilidad**: `dispositivo_factory.py` líneas 8-67

---

### US-TECH-003: Implementar Observer Pattern para Sensores

**Como** arquitecto de software
**Quiero** implementar patrón Observer con Generics
**Para** notificar cambios de sensores de forma tipo-segura

#### Criterios de Aceptación

- [x] Crear clase `Observable[T]` genérica
- [x] Crear interfaz `Observer[T]` genérica
- [x] Soportar múltiples observadores
- [x] Métodos: `agregar_observador()`, `eliminar_observador()`, `notificar_observadores()`
- [x] Sensores heredan de `Observable[bool]` o `Observable[float]`
- [x] Controlador hereda de `Observer[bool]` y `Observer[float]`
- [x] Thread-safe en notificaciones

#### Detalles Técnicos

**Clases**: `Observable[T]`, `Observer[T]`
**Patrón**: Observer

**Implementación**:
```python
from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso**:
```python
# Sensor es Observable[bool]
class SensorMovimientoTask(threading.Thread, Observable[bool]):
    def run(self):
        while not self._detenido.is_set():
            mov = self._detectar_movimiento()
            self.notificar_observadores(mov)  # Notifica bool

# Controlador es Observer[bool]
class AutomationControlTask(Observer[bool]):
    def actualizar(self, evento: bool) -> None:
        self._ultimo_movimiento = evento  # Recibe bool
```

**Trazabilidad**: `observable.py`, `observer.py`

---

### US-TECH-004: Implementar Strategy Pattern para Automatización

**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de automatización
**Para** permitir diferentes estrategias según tipo de dispositivo

#### Criterios de Aceptación

- [x] Crear interfaz `AutomationStrategy` abstracta
- [x] Implementar `IluminacionStrategy` (luces)
- [x] Implementar `ClimatizacionStrategy` (termostatos)
- [x] Implementar `SeguridadStrategy` (cámaras, cerraduras)
- [x] Inyectar estrategia en constructor de servicios
- [x] Servicios delegan ejecución a estrategia
- [x] Estrategias usan constantes de `constantes.py`

#### Detalles Técnicos

**Interfaz**: `AutomationStrategy`
**Implementaciones**: `IluminacionStrategy`, `ClimatizacionStrategy`, `SeguridadStrategy`
**Patrón**: Strategy

**Implementación**:
```python
# Interfaz
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
            dispositivo.set_intensidad(30)  # 30% en modo noche
        else:
            dispositivo.set_intensidad(100)  # 100% de día

# Estrategia 2: Climatización
class ClimatizacionStrategy(AutomationStrategy):
    def __init__(self, temp_objetivo: float):
        self._temp_objetivo = temp_objetivo

    def ejecutar_accion(self, fecha, dispositivo, evento):
        dispositivo.set_temperatura_objetivo(self._temp_objetivo)
```

**Inyección**:
```python
class LuzInteligenteService(DispositivoService):
    def __init__(self):
        super().__init__(IluminacionStrategy())  # Inyección

class TermostatoService(DispositivoService):
    def __init__(self):
        super().__init__(ClimatizacionStrategy(22.0))  # Inyección
```

**Delegación**:
```python
class DispositivoService(ABC):
    def ejecutar_automatizacion(self, dispositivo: 'Dispositivo', evento: Any) -> None:
        # Delegar a estrategia
        self._estrategia_automation.ejecutar_accion(
            datetime.now(), dispositivo, evento
        )
```

**Trazabilidad**: `iluminacion_strategy.py`, `climatizacion_strategy.py`, `dispositivo_service.py` líneas 35-59

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimórfico

**Como** arquitecto de software
**Quiero** eliminar cascadas de isinstance()
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptación

- [x] Crear diccionarios de handlers por tipo
- [x] Registrar handler para cada tipo de dispositivo
- [x] Método `encender()` usa dispatch automático
- [x] Método `mostrar_datos()` usa dispatch automático
- [x] Lanzar error si tipo no registrado
- [x] NO usar lambdas - usar métodos de instancia dedicados

#### Detalles Técnicos

**Clase**: `DispositivoServiceRegistry`
**Patrón**: Registry

**Implementación**:
```python
class DispositivoServiceRegistry:
    def __init__(self):
        # Diccionarios de handlers
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

    def encender(self, dispositivo: Dispositivo) -> None:
        tipo = type(dispositivo)
        if tipo not in self._encender_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._encender_handlers[tipo](dispositivo)

    # Handlers dedicados (NO lambdas)
    def _encender_luz(self, dispositivo):
        return self._luz_service.encender(dispositivo)
```

**Ventajas**:
- Sin `isinstance()` cascades
- Fácil agregar nuevos tipos
- Mejor rendimiento (O(1) lookup)
- Más testeable

**Trazabilidad**: `dispositivo_service_registry.py` líneas 48-89

---

## Resumen de Cobertura Funcional

### Totales por Epic

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: Casa y Habitaciones | 3 | 3 | 100% |
| Epic 2: Gestión de Dispositivos | 6 | 6 | 100% |
| Epic 3: Sensores y Automatización | 4 | 4 | 100% |
| Epic 4: Gestión de Usuarios | 4 | 4 | 100% |
| Epic 5: Operaciones de Negocio | 3 | 3 | 100% |
| Epic 6: Persistencia y Configuración | 3 | 3 | 100% |
| Historias Técnicas (Patrones) | 5 | 5 | 100% |
| **TOTAL** | **28** | **28** | **100%** |

### Patrones de Diseño Cubiertos

- [x] SINGLETON - DispositivoServiceRegistry
- [x] FACTORY METHOD - DispositivoFactory
- [x] OBSERVER - Sensores y eventos
- [x] STRATEGY - Automatización
- [x] REGISTRY - Dispatch polimórfico (bonus)

### Funcionalidades Completas

- [x] Gestión de 4 tipos de dispositivos
- [x] Sistema de sensores con 3 threads
- [x] Gestión de usuarios con niveles de acceso
- [x] Persistencia con Pickle
- [x] Operaciones de negocio de alto nivel
- [x] Manejo de excepciones específicas
- [x] PEP 8 compliance 100%
- [x] Type hints con TYPE_CHECKING
- [x] Constantes centralizadas
- [x] Código limpio sin lambdas

---

**Última actualización**: Octubre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%