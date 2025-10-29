# CLAUDE.md - Guía Técnica Completa para IA

**Proyecto**: PythonSmartHome
**Versión**: 1.0.0
**Fecha**: Octubre 2025
**Propósito**: Guía definitiva para que una IA construya el sistema completo

---

## Índice

1. [Contexto y Objetivo](#contexto-y-objetivo)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Estructura de Directorios](#estructura-de-directorios)
4. [Constantes del Sistema](#constantes-del-sistema)
5. [Entidades (DTOs)](#entidades-dtos)
6. [Servicios de Negocio](#servicios-de-negocio)
7. [Patrones de Diseño](#patrones-de-diseño)
8. [Sistema de Sensores (Threading)](#sistema-de-sensores-threading)
9. [Excepciones Personalizadas](#excepciones-personalizadas)
10. [Main.py - Demostración Completa](#mainpy---demostración-completa)
11. [Checklist de Implementación](#checklist-de-implementación)
12. [Convenciones Obligatorias](#convenciones-obligatorias)

---

## Contexto y Objetivo

### ¿Qué construir?

Un sistema de **domótica (smart home)** completo en Python 3.13 que demuestre los siguientes patrones de diseño:

1. **SINGLETON** - DispositivoServiceRegistry (instancia única compartida)
2. **FACTORY METHOD** - DispositivoFactory (creación de dispositivos)
3. **OBSERVER** - Sensores y automatización en tiempo real
4. **STRATEGY** - Algoritmos de automatización intercambiables
5. **REGISTRY** - Dispatch polimórfico (bonus)

### ¿Por qué domótica?

Es el equivalente perfecto del sistema forestal:
- **Cultivos** → **Dispositivos** (LuzInteligente, Termostato, etc.)
- **Plantación** → **Habitación** (contiene dispositivos)
- **Tierra** → **Casa** (contiene habitaciones)
- **Sistema de Riego** → **Sistema de Automatización**
- **Sensores ambientales** → **Sensores IoT** (movimiento, temperatura)

---

## Arquitectura del Sistema

### Principios SOLID

```
SINGLE RESPONSIBILITY
- Entidades: Solo datos (getters/setters)
- Servicios: Solo lógica de negocio
- Patrones: Implementaciones aisladas

OPEN/CLOSED
- Agregar nuevos dispositivos sin modificar factory
- Agregar estrategias sin cambiar servicios

LISKOV SUBSTITUTION
- Todos los dispositivos son Dispositivo
- Todas las estrategias son AutomationStrategy

INTERFACE SEGREGATION
- Observer[T]: Genérico para eventos
- AutomationStrategy: Específico para automatización

DEPENDENCY INVERSION
- Servicios dependen de Strategy (abstracción)
- Factory retorna Dispositivo (interfaz)
```

### Flujo de Datos

```
main.py (presentación)
    |
    v
CasaService (negocio alto nivel)
    |
    v
HabitacionService (dominio)
    |
    v
DispositivoServiceRegistry (singleton + registry)
    |
    v
LuzInteligenteService (servicio específico)
    |
    v
IluminacionStrategy (estrategia inyectada)
    |
    v
LuzInteligente (entidad - solo datos)
```

---

## Estructura de Directorios

```
python_smarthome/
|
+-- __init__.py
+-- constantes.py              # TODAS las constantes aquí
|
+-- entidades/
|   +-- __init__.py
|   +-- dispositivos/
|   |   +-- __init__.py
|   |   +-- dispositivo.py           # ABC base
|   |   +-- luz_inteligente.py
|   |   +-- termostato.py
|   |   +-- camara_seguridad.py
|   |   +-- cerradura_inteligente.py
|   +-- espacios/
|   |   +-- __init__.py
|   |   +-- casa.py
|   |   +-- habitacion.py
|   |   +-- configuracion_casa.py
|   +-- usuarios/
|       +-- __init__.py
|       +-- usuario.py
|       +-- escena.py
|       +-- nivel_acceso.py      # Enum
|
+-- servicios/
|   +-- __init__.py
|   +-- dispositivos/
|   |   +-- __init__.py
|   |   +-- dispositivo_service.py                  # ABC base
|   |   +-- luz_inteligente_service.py
|   |   +-- termostato_service.py
|   |   +-- camara_seguridad_service.py
|   |   +-- cerradura_inteligente_service.py
|   |   +-- dispositivo_service_registry.py         # SINGLETON + REGISTRY
|   +-- espacios/
|   |   +-- __init__.py
|   |   +-- casa_service.py
|   |   +-- habitacion_service.py
|   |   +-- configuracion_casa_service.py
|   +-- usuarios/
|   |   +-- __init__.py
|   |   +-- usuario_service.py
|   +-- negocio/
|       +-- __init__.py
|       +-- casa_service.py
|       +-- grupo_dispositivos.py    # Generic[T]
|       +-- modo_sistema.py          # Enum
|
+-- patrones/
|   +-- __init__.py
|   +-- singleton/
|   |   +-- __init__.py
|   +-- factory/
|   |   +-- __init__.py
|   |   +-- dispositivo_factory.py
|   +-- observer/
|   |   +-- __init__.py
|   |   +-- observable.py            # Generic[T]
|   |   +-- observer.py              # Generic[T]
|   |   +-- eventos/
|   |       +-- __init__.py
|   |       +-- evento_sensor.py
|   +-- strategy/
|       +-- __init__.py
|       +-- automation_strategy.py   # ABC
|       +-- impl/
|           +-- __init__.py
|           +-- iluminacion_strategy.py
|           +-- climatizacion_strategy.py
|           +-- seguridad_strategy.py
|
+-- sensores/
|   +-- __init__.py
|   +-- sensor_movimiento_task.py    # Observable[bool]
|   +-- sensor_temperatura_task.py   # Observable[float]
|   +-- sensor_apertura_task.py      # Observable[bool]
|
+-- control/
|   +-- __init__.py
|   +-- automation_control_task.py   # Observer[bool] + Observer[float]
|
+-- excepciones/
    +-- __init__.py
    +-- smarthome_exception.py
    +-- capacidad_insuficiente_exception.py
    +-- permiso_denegado_exception.py
    +-- persistencia_exception.py
    +-- mensajes_exception.py
```

---

## Constantes del Sistema

**Archivo**: `python_smarthome/constantes.py`

```python
"""
Constantes centralizadas del sistema de domótica.

REGLA: NUNCA hardcodear valores mágicos en el código.
TODO debe estar definido aquí.
"""

# ============================================================
# DISPOSITIVOS - Luces Inteligentes
# ============================================================
INTENSIDAD_MIN = 0  # %
INTENSIDAD_MAX = 100  # %
COLOR_INICIAL = (255, 255, 255)  # RGB - Blanco

# ============================================================
# DISPOSITIVOS - Termostatos
# ============================================================
TEMP_MIN = 10  # °C
TEMP_MAX = 30  # °C
TEMP_OBJETIVO_INICIAL = 22  # °C

# ============================================================
# DISPOSITIVOS - Cámaras de Seguridad
# ============================================================
RESOLUCION_INICIAL = "1080p"
DETECCION_MOVIMIENTO_INICIAL = True

# ============================================================
# DISPOSITIVOS - Cerraduras Inteligentes
# ============================================================
BATERIA_INICIAL = 100  # %
METODO_ACCESO_INICIAL = "PIN"

# ============================================================
# SENSORES - Intervalos de lectura
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
# AUTOMATIZACIÓN - Condiciones
# ============================================================
HORA_INICIO_NOCHE = 20  # 20:00
HORA_FIN_NOCHE = 7  # 07:00
TEMP_CONFORT_MIN = 18  # °C
TEMP_CONFORT_MAX = 24  # °C
TEMP_CONFORT_OBJETIVO = 22  # °C
INTERVALO_CONTROL_AUTOMATION = 2.5  # segundos

# ============================================================
# HABITACIONES - Capacidad
# ============================================================
MAX_DISPOSITIVOS_HABITACION = 20

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
# MENSAJES DE EXCEPCION
# ============================================================
# (Se definen en mensajes_exception.py)
```

---

## Entidades (DTOs)

### Regla de Oro para Entidades

```
ENTIDADES:
- Solo contienen DATOS
- Getters y setters SIMPLES
- NO contienen lógica de negocio
- Campos privados (prefijo _)
- Validaciones SOLO en setters (ej. temperatura >= 10)
- Usar TYPE_CHECKING para imports circulares
```

### Ejemplo: LuzInteligente

**Archivo**: `python_smarthome/entidades/dispositivos/luz_inteligente.py`

```python
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
```

### Ejemplo: Dispositivo (Base ABC)

**Archivo**: `python_smarthome/entidades/dispositivos/dispositivo.py`

```python
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
```

---

## Servicios de Negocio

### Regla de Oro para Servicios

```
SERVICIOS:
- Contienen LÓGICA DE NEGOCIO
- NO tienen estado (stateless cuando sea posible)
- Reciben entidades como parámetros
- Retornan valores o modifican entidades
- Inyectan dependencias en __init__
- Usan constantes de constantes.py
```

### Ejemplo: LuzInteligenteService

**Archivo**: `python_smarthome/servicios/dispositivos/luz_inteligente_service.py`

```python
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
        super().mostrar_datos(luz)  # Datos comunes (ID, estado)
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
```

---

## Patrones de Diseño

### 1. SINGLETON - DispositivoServiceRegistry

**Archivo**: `python_smarthome/servicios/dispositivos/dispositivo_service_registry.py`

```python
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
```

### 2. FACTORY METHOD - DispositivoFactory

**Archivo**: `python_smarthome/patrones/factory/dispositivo_factory.py`

```python
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
```

### 3. OBSERVER - Observable[T] y Observer[T]

**Archivo**: `python_smarthome/patrones/observer/observable.py`

```python
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
```

**Archivo**: `python_smarthome/patrones/observer/observer.py`

```python
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
```

### 4. STRATEGY - AutomationStrategy

**Archivo**: `python_smarthome/patrones/strategy/automation_strategy.py`

```python
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
```

**Archivo**: `python_smarthome/patrones/strategy/impl/iluminacion_strategy.py`

```python
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
```

---

## Sistema de Sensores (Threading)

### Sensor de Movimiento

**Archivo**: `python_smarthome/sensores/sensor_movimiento_task.py`

```python
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
```

### Control de Automatización

**Archivo**: `python_smarthome/control/automation_control_task.py`

```python
"""Controlador de automatización - Thread + OBSERVER pattern."""

import threading
import time
from typing import TYPE_CHECKING
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


class AutomationControlTask(threading.Thread, Observer[bool], Observer[float]):
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

    def actualizar(self, evento) -> None:
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
```

---

## Excepciones Personalizadas

### Excepción Base

**Archivo**: `python_smarthome/excepciones/smarthome_exception.py`

```python
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
```

### Excepción Específica: CapacidadInsuficienteException

**Archivo**: `python_smarthome/excepciones/capacidad_insuficiente_exception.py`

```python
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
```

### Mensajes Centralizados

**Archivo**: `python_smarthome/excepciones/mensajes_exception.py`

```python
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
```

---

## Main.py - Demostración Completa

**Archivo**: `main.py`

```python
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
```

---

## Checklist de Implementación

### Fase 1: Estructura Base
- [ ] Crear estructura de directorios completa
- [ ] Crear `constantes.py` con todas las constantes
- [ ] Crear todos los `__init__.py`

### Fase 2: Patrones (Fundamento)
- [ ] Implementar `Observable[T]` y `Observer[T]` (OBSERVER)
- [ ] Implementar `AutomationStrategy` y estrategias (STRATEGY)
- [ ] Implementar `DispositivoFactory` (FACTORY METHOD)
- [ ] Implementar `DispositivoServiceRegistry` (SINGLETON + REGISTRY)

### Fase 3: Entidades
- [ ] `Dispositivo` (base ABC)
- [ ] `LuzInteligente`
- [ ] `Termostato`
- [ ] `CamaraSeguridad`
- [ ] `CerraduraInteligente`
- [ ] `Casa`, `Habitacion`, `ConfiguracionCasa`
- [ ] `Usuario`, `Escena`, `NivelAcceso`

### Fase 4: Servicios
- [ ] `DispositivoService` (base ABC)
- [ ] `LuzInteligenteService` (inyecta IluminacionStrategy)
- [ ] `TermostatoService` (inyecta ClimatizacionStrategy)
- [ ] `CamaraSeguridadService` (inyecta SeguridadStrategy)
- [ ] `CerraduraInteligenteService` (inyecta SeguridadStrategy)
- [ ] `CasaService`, `HabitacionService`, `ConfiguracionCasaService`
- [ ] `UsuarioService`
- [ ] `CasaService` (negocio), `GrupoDispositivos[T]`

### Fase 5: Sensores (Threading)
- [ ] `SensorMovimientoTask` (Observable[bool])
- [ ] `SensorTemperaturaTask` (Observable[float])
- [ ] `AutomationControlTask` (Observer[bool] + Observer[float])

### Fase 6: Excepciones
- [ ] `SmartHomeException` (base)
- [ ] `CapacidadInsuficienteException`
- [ ] `PermisoDenegadoException`
- [ ] `PersistenciaException`
- [ ] `MensajesException` (centralizados)

### Fase 7: Main y Testing
- [ ] Implementar `main.py` completo
- [ ] Ejecutar y verificar salida
- [ ] Verificar archivo `data/Juan Perez.dat` creado
- [ ] Verificar threads se detienen correctamente

---

## Convenciones Obligatorias

### Código
```python
# 1. Nombres en inglés (variables, métodos, clases)
# 2. Comentarios en español
# 3. Docstrings en español (Google Style)
# 4. Constantes en constantes.py
# 5. NO usar lambdas
# 6. NO usar emojis en print
# 7. PEP 8 compliance 100%
```

### Type Hints
```python
# Siempre usar TYPE_CHECKING para imports circulares
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modulo import Clase

def metodo(self, param: 'Clase') -> None:
    pass
```

### Excepciones
```python
# Mensajes en inglés para código
raise ValueError("Temperature out of range")

# Mensajes en español para usuario
return "La temperatura esta fuera de rango"
```

### Threading
```python
# Threads SIEMPRE daemon
threading.Thread.__init__(self, daemon=True)

# Graceful shutdown con Event
self._detenido = threading.Event()

# Usar THREAD_JOIN_TIMEOUT de constantes
thread.join(timeout=THREAD_JOIN_TIMEOUT)
```

---

**ESTA GUÍA CONTIENE TODO LO NECESARIO PARA CONSTRUIR EL SISTEMA COMPLETO**

Sigue el orden del checklist y respeta las convenciones obligatorias.