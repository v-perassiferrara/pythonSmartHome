# RÚBRICA DE EVALUACIÓN - Sistema de Domótica (Smart Home)

**Proyecto**: PythonSmartHome
**Versión**: 1.0.0
**Fecha**: Octubre 2025
**Puntaje Total**: 100 puntos

---

## Tabla de Contenidos

1. [Criterios de Evaluación](#criterios-de-evaluación)
2. [Sección 1: Patrones de Diseño (40 puntos)](#sección-1-patrones-de-diseño-40-puntos)
3. [Sección 2: Arquitectura y Código (30 puntos)](#sección-2-arquitectura-y-código-30-puntos)
4. [Sección 3: Funcionalidades del Dominio (20 puntos)](#sección-3-funcionalidades-del-dominio-20-puntos)
5. [Sección 4: Documentación y Presentación (10 puntos)](#sección-4-documentación-y-presentación-10-puntos)
6. [Checklist de Verificación Automatizada](#checklist-de-verificación-automatizada)
7. [Criterios de Aprobación](#criterios-de-aprobación)

---

## Criterios de Evaluación

### Escala de Puntuación

- **Excelente (100%)**: Cumple perfectamente con todos los requisitos
- **Muy Bueno (80-99%)**: Cumple con la mayoría de requisitos, mínimos errores
- **Bueno (60-79%)**: Cumple requisitos básicos, algunos errores
- **Insuficiente (0-59%)**: No cumple requisitos mínimos

### Requisitos para Aprobar

- Puntaje mínimo: **60/100 puntos**
- Patrones obligatorios implementados: **4/5** (Singleton, Factory, Observer, Strategy)
- Sistema ejecutable sin errores críticos
- Código funcional y demostrable

---

## Sección 1: Patrones de Diseño (40 puntos)

### 1.1 Patrón SINGLETON (8 puntos)

**Implementación**: `python_smarthome/servicios/dispositivos/dispositivo_service_registry.py`

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Implementa `__new__` para controlar instanciación | 2 | ☐ |
| Usa double-checked locking con `Lock` (thread-safe) | 2 | ☐ |
| Método `get_instance()` funciona correctamente | 1 | ☐ |
| Todas las instancias son la misma (test `registry1 is registry2`) | 2 | ☐ |
| Inicialización perezosa (lazy initialization) | 1 | ☐ |

**Código de verificación**:
```python
registry1 = DispositivoServiceRegistry()
registry2 = DispositivoServiceRegistry.get_instance()
assert registry1 is registry2  # Debe ser True
```

---

### 1.2 Patrón FACTORY METHOD (8 puntos)

**Implementación**: `python_smarthome/patrones/factory/dispositivo_factory.py`

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Método estático `crear_dispositivo(tipo: str)` implementado | 2 | ☐ |
| Usa diccionario de factories (NO if/elif cascades) | 2 | ☐ |
| Crea 4 tipos: LuzInteligente, Termostato, Cámara, Cerradura | 2 | ☐ |
| Retorna tipo base `Dispositivo` (no tipos concretos) | 1 | ☐ |
| Lanza `ValueError` para tipos desconocidos | 1 | ☐ |

**Código de verificación**:
```python
luz = DispositivoFactory.crear_dispositivo("LuzInteligente")
assert isinstance(luz, Dispositivo)  # Tipo base
assert type(luz).__name__ == "LuzInteligente"  # Tipo concreto
```

---

### 1.3 Patrón OBSERVER (8 puntos)

**Implementación**: 
- `python_smarthome/patrones/observer/observable.py`
- `python_smarthome/patrones/observer/observer.py`
- `python_smarthome/sensores/*.py`

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| `Observable[T]` genérico con TypeVar | 2 | ☐ |
| `Observer[T]` genérico con método `actualizar(evento: T)` | 2 | ☐ |
| Sensores heredan de `Observable[bool]` o `Observable[float]` | 2 | ☐ |
| Controlador hereda de `Observer` y se suscribe a sensores | 1 | ☐ |
| Notificaciones funcionan correctamente (sensores → control) | 1 | ☐ |

**Código de verificación**:
```python
sensor = SensorMovimientoTask()
control = AutomationControlTask(sensor, ...)
sensor.agregar_observador(control)
# Al ejecutar sensor, control recibe notificaciones
```

---

### 1.4 Patrón STRATEGY (8 puntos)

**Implementación**: 
- `python_smarthome/patrones/strategy/automation_strategy.py`
- `python_smarthome/patrones/strategy/impl/*.py`

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Interfaz `AutomationStrategy` abstracta con método `ejecutar_accion` | 2 | ☐ |
| Implementa `IluminacionStrategy` (ajuste de luces) | 2 | ☐ |
| Implementa `ClimatizacionStrategy` (ajuste de temperatura) | 2 | ☐ |
| Estrategias inyectadas en constructores de servicios | 1 | ☐ |
| Servicios delegan ejecución a estrategia | 1 | ☐ |

**Código de verificación**:
```python
luz_service = LuzInteligenteService()
# Internamente usa IluminacionStrategy()
luz_service.ejecutar_automatizacion(luz, evento)
```

---

### 1.5 Patrón REGISTRY (Bonus) (8 puntos)

**Implementación**: `python_smarthome/servicios/dispositivos/dispositivo_service_registry.py`

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Diccionarios de handlers por tipo (`_encender_handlers`, etc.) | 2 | ☐ |
| NO usa cascadas de `isinstance()` | 2 | ☐ |
| Dispatch polimórfico con lookup O(1) | 2 | ☐ |
| Usa métodos dedicados (NO lambdas) | 1 | ☐ |
| Lanza error para tipos no registrados | 1 | ☐ |

**Código de verificación**:
```python
registry = DispositivoServiceRegistry.get_instance()
# NO debe haber if isinstance(dispositivo, LuzInteligente)
registry.encender(luz)  # Dispatch automático
```

---

## Sección 2: Arquitectura y Código (30 puntos)

### 2.1 Estructura de Proyecto (6 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Estructura de directorios completa según especificación | 2 | ☐ |
| Todos los `__init__.py` presentes | 1 | ☐ |
| Separación correcta: entidades/servicios/patrones/sensores | 2 | ☐ |
| Archivo `constantes.py` centralizado | 1 | ☐ |

---

### 2.2 Principios SOLID (8 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| **Single Responsibility**: Entidades solo datos, servicios solo lógica | 2 | ☐ |
| **Open/Closed**: Factory permite agregar dispositivos sin modificar | 2 | ☐ |
| **Liskov Substitution**: Dispositivos intercambiables | 1 | ☐ |
| **Interface Segregation**: Interfaces específicas (Observer[T], Strategy) | 2 | ☐ |
| **Dependency Inversion**: Servicios dependen de abstracciones | 1 | ☐ |

---

### 2.3 Convenciones de Código (8 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| PEP 8 compliance (nombres, espaciado, líneas) | 2 | ☐ |
| Type hints en todos los métodos públicos | 2 | ☐ |
| Docstrings (Google Style) en clases y métodos principales | 2 | ☐ |
| Uso de `TYPE_CHECKING` para imports circulares | 1 | ☐ |
| NO usa lambdas (métodos dedicados) | 1 | ☐ |

---

### 2.4 Manejo de Excepciones (4 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Implementa `SmartHomeException` como base | 1 | ☐ |
| Al menos 2 excepciones específicas (Capacidad, Permiso, Persistencia) | 2 | ☐ |
| Mensajes usuario/técnico separados | 1 | ☐ |

---

### 2.5 Threading (4 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Threads daemon (finalizan con main) | 1 | ☐ |
| Graceful shutdown con `threading.Event` | 2 | ☐ |
| Uso de `THREAD_JOIN_TIMEOUT` de constantes | 1 | ☐ |

---

## Sección 3: Funcionalidades del Dominio (20 puntos)

### 3.1 Entidades Completas (8 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| 4 tipos de dispositivos implementados (Luz, Termostato, Cámara, Cerradura) | 4 | ☐ |
| Casa, Habitación, ConfiguraciónCasa implementadas | 2 | ☐ |
| Usuario, Escena, NivelAcceso implementados | 2 | ☐ |

---

### 3.2 Servicios de Negocio (6 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| HabitacionService con método `instalar()` usando Factory | 2 | ☐ |
| Métodos `encender_todos()`, `apagar_todos()` implementados | 2 | ☐ |
| CasaService con método `agrupar_por_tipo()` genérico | 2 | ☐ |

---

### 3.3 Sistema de Sensores (6 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| SensorMovimientoTask (Observable[bool]) funcional | 2 | ☐ |
| SensorTemperaturaTask (Observable[float]) funcional | 2 | ☐ |
| AutomationControlTask observa sensores y ejecuta acciones | 2 | ☐ |

---

## Sección 4: Documentación y Presentación (10 puntos)

### 4.1 Archivo main.py (5 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Demuestra los 5 patrones de diseño | 3 | ☐ |
| Se ejecuta sin errores | 1 | ☐ |
| Salida clara y formateada | 1 | ☐ |

---

### 4.2 Persistencia (3 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Serialización con Pickle funcional | 1 | ☐ |
| Crea archivo `data/{propietario}.dat` | 1 | ☐ |
| Recuperación de datos funcional | 1 | ☐ |

---

### 4.3 Documentación Técnica (2 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| README.md claro y completo | 1 | ☐ |
| Comentarios relevantes en código complejo | 1 | ☐ |

---

## Checklist de Verificación Automatizada

### Verificaciones Básicas

```python
# 1. Importaciones exitosas
try:
    from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
    from python_smarthome.patrones.factory.dispositivo_factory import DispositivoFactory
    print("[OK] Importaciones exitosas")
except ImportError as e:
    print(f"[ERROR] Fallo en importaciones: {e}")
```

### Test de Patrones

```python
# 2. Test SINGLETON
registry1 = DispositivoServiceRegistry()
registry2 = DispositivoServiceRegistry.get_instance()
assert registry1 is registry2, "SINGLETON no funciona"
print("[OK] SINGLETON funciona correctamente")

# 3. Test FACTORY
luz = DispositivoFactory.crear_dispositivo("LuzInteligente")
termostato = DispositivoFactory.crear_dispositivo("Termostato")
assert type(luz).__name__ == "LuzInteligente"
assert type(termostato).__name__ == "Termostato"
print("[OK] FACTORY funciona correctamente")

# 4. Test OBSERVER
sensor = SensorMovimientoTask()
control = AutomationControlTask(sensor, None, None, None)
sensor.agregar_observador(control)
assert len(sensor._observadores) > 0
print("[OK] OBSERVER funciona correctamente")

# 5. Test STRATEGY
luz_service = LuzInteligenteService()
assert hasattr(luz_service, '_estrategia_automation')
print("[OK] STRATEGY funciona correctamente")

# 6. Test REGISTRY
registry = DispositivoServiceRegistry.get_instance()
assert hasattr(registry, '_encender_handlers')
assert len(registry._encender_handlers) >= 4
print("[OK] REGISTRY funciona correctamente")
```

### Test de Ejecución

```python
# 7. Test main.py
import subprocess
resultado = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
assert resultado.returncode == 0, "main.py falló"
assert "EJEMPLO COMPLETADO EXITOSAMENTE" in resultado.stdout
print("[OK] main.py ejecuta correctamente")
```

### Test de Persistencia

```python
# 8. Test persistencia
import os
assert os.path.exists("data/Juan Perez.dat"), "Archivo de datos no creado"
print("[OK] Persistencia funciona correctamente")
```

---

## Criterios de Aprobación

### Aprobación Mínima (60 puntos)

Para aprobar el proyecto se requiere:

1. **Patrones obligatorios (mínimo 24/40 puntos)**:
   - SINGLETON: 6/8 puntos mínimo
   - FACTORY: 6/8 puntos mínimo
   - OBSERVER: 6/8 puntos mínimo
   - STRATEGY: 6/8 puntos mínimo

2. **Arquitectura (mínimo 18/30 puntos)**:
   - Estructura correcta
   - SOLID básico aplicado
   - Código ejecutable

3. **Funcionalidades (mínimo 12/20 puntos)**:
   - Al menos 3 tipos de dispositivos
   - Servicios básicos funcionales

4. **Documentación (mínimo 6/10 puntos)**:
   - main.py funcional
   - Persistencia básica

### Aprobación Excelente (90+ puntos)

Para obtener calificación excelente:

- Todos los patrones implementados correctamente (38/40 puntos)
- Arquitectura completa y limpia (28/30 puntos)
- Todas las funcionalidades (18/20 puntos)
- Documentación completa (9/10 puntos)
- Código sin warnings de PEP 8
- Threading sin race conditions
- Excepciones bien manejadas

---

## Resumen de Puntos por Sección

| Sección | Puntos Máximos | Puntos Mínimos para Aprobar |
|---------|----------------|------------------------------|
| 1. Patrones de Diseño | 40 | 24 |
| 2. Arquitectura y Código | 30 | 18 |
| 3. Funcionalidades del Dominio | 20 | 12 |
| 4. Documentación y Presentación | 10 | 6 |
| **TOTAL** | **100** | **60** |

---

## Notas Finales

### Penalizaciones

- **-5 puntos**: Código no ejecutable (errores de sintaxis)
- **-3 puntos**: Imports circulares no resueltos
- **-2 puntos**: Warnings de PEP 8 graves (más de 10)
- **-2 puntos**: Uso de lambdas en lugar de métodos dedicados
- **-1 punto**: Valores mágicos hardcodeados (no en constantes.py)

### Bonus

- **+3 puntos**: Implementación completa del patrón REGISTRY
- **+2 puntos**: Tests unitarios con pytest
- **+2 puntos**: Type hints en el 100% del código
- **+1 punto**: Documentación excepcional con diagramas

**Puntaje máximo con bonus**: 108 puntos (se limita a 100)

---

**Fecha de última actualización**: Octubre 2025
**Versión de rúbrica**: 1.0.0