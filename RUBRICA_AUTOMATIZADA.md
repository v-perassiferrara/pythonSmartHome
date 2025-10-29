\# Rubrica de Evaluacion Automatizada - Compatible con n8n



\*\*Proyecto\*\*: PythonForestal

\*\*Version\*\*: 1.0.0

\*\*Fecha\*\*: Octubre 2025

\*\*Proposito\*\*: Automatizacion de correccion de proyectos en n8n



---



\## Introduccion



Este documento define criterios de evaluacion automatizables mediante n8n para proyectos de software que implementen patrones de diseno. Cada criterio incluye:



1\. \*\*ID unico\*\*: Para referencia en workflows de n8n

2\. \*\*Tipo de verificacion\*\*: Estatica (codigo) o Dinamica (ejecucion)

3\. \*\*Metodo de deteccion\*\*: Como automatizar la verificacion

4\. \*\*Comando/Regex\*\*: Script o patron para ejecutar

5\. \*\*Puntaje\*\*: Puntos asignados al criterio

6\. \*\*Threshold\*\*: Umbral de aprobacion



---



\## Formato JSON para n8n



Cada criterio se puede representar en JSON para workflows de n8n:



```json

{

&nbsp; "criterio\_id": "SING-001",

&nbsp; "categoria": "Singleton",

&nbsp; "descripcion": "Verificar implementacion de Singleton",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -r '\_instance = None' --include='\*.py'",

&nbsp; "puntaje\_max": 5,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\## Seccion 1: Verificaciones Estaticas (Analisis de Codigo)



\### 1.1 Patron SINGLETON



\#### SING-001: Atributo de Instancia Unica

```json

{

&nbsp; "id": "SING-001",

&nbsp; "categoria": "Singleton",

&nbsp; "descripcion": "Verificar atributo \_instance en clase",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn '\_instance = None' --include='\*.py' .",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



\*\*Validacion esperada\*\*: Al menos 1 coincidencia en archivo `\*registry\*.py`



---



\#### SING-002: Metodo \_\_new\_\_ Implementado

```json

{

&nbsp; "id": "SING-002",

&nbsp; "categoria": "Singleton",

&nbsp; "descripcion": "Verificar metodo \_\_new\_\_ para control de instancia",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'def \_\_new\_\_' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### SING-003: Thread-Safety con Lock

```json

{

&nbsp; "id": "SING-003",

&nbsp; "categoria": "Singleton",

&nbsp; "descripcion": "Verificar uso de threading.Lock",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'threading.Lock\\\\|from threading import Lock' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\#### SING-004: Metodo get\_instance()

```json

{

&nbsp; "id": "SING-004",

&nbsp; "categoria": "Singleton",

&nbsp; "descripcion": "Verificar metodo get\_instance()",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'def get\_instance' --include='\*.py' .",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\### 1.2 Patron FACTORY METHOD



\#### FACT-001: Metodo Factory Estatico

```json

{

&nbsp; "id": "FACT-001",

&nbsp; "categoria": "Factory",

&nbsp; "descripcion": "Verificar metodo factory estatico",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn '@staticmethod' --include='\*factory\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 2,

&nbsp; "peso": "critico"

}

```



---



\#### FACT-002: Clase Factory Existe

```json

{

&nbsp; "id": "FACT-002",

&nbsp; "categoria": "Factory",

&nbsp; "descripcion": "Verificar existencia de clase Factory",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -name '\*factory\*.py' -type f",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### FACT-003: Metodo crear\_\* Implementado

```json

{

&nbsp; "id": "FACT-003",

&nbsp; "categoria": "Factory",

&nbsp; "descripcion": "Verificar metodos de creacion",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'def crear\_\\\\|def \_crear\_' --include='\*factory\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 4,

&nbsp; "peso": "alto"

}

```



---



\#### FACT-004: Diccionario de Factories

```json

{

&nbsp; "id": "FACT-004",

&nbsp; "categoria": "Factory",

&nbsp; "descripcion": "Verificar uso de diccionario para dispatch",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'factories = {' --include='\*factory\*.py' .",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\### 1.3 Patron OBSERVER



\#### OBSR-001: Clase Observable Existe

```json

{

&nbsp; "id": "OBSR-001",

&nbsp; "categoria": "Observer",

&nbsp; "descripcion": "Verificar clase Observable",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'class Observable' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### OBSR-002: Clase Observer Existe

```json

{

&nbsp; "id": "OBSR-002",

&nbsp; "categoria": "Observer",

&nbsp; "descripcion": "Verificar interfaz Observer",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'class Observer' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### OBSR-003: Uso de Generics

```json

{

&nbsp; "id": "OBSR-003",

&nbsp; "categoria": "Observer",

&nbsp; "descripcion": "Verificar uso de Generic\[T]",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'Generic\\\\\[T\\\\]\\\\|Observable\\\\\[' --include='\*.py' .",

&nbsp; "puntaje": 4,

&nbsp; "threshold": 2,

&nbsp; "peso": "alto"

}

```



---



\#### OBSR-004: Metodo notificar\_observadores

```json

{

&nbsp; "id": "OBSR-004",

&nbsp; "categoria": "Observer",

&nbsp; "descripcion": "Verificar metodo de notificacion",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'def notificar\_observadores' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\### 1.4 Patron STRATEGY



\#### STRT-001: Interfaz Strategy Abstracta

```json

{

&nbsp; "id": "STRT-001",

&nbsp; "categoria": "Strategy",

&nbsp; "descripcion": "Verificar interfaz Strategy abstracta",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'class.\*Strategy.\*ABC' --include='\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### STRT-002: Implementaciones de Strategy

```json

{

&nbsp; "id": "STRT-002",

&nbsp; "categoria": "Strategy",

&nbsp; "descripcion": "Verificar al menos 2 implementaciones",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'Strategy):' --include='\*.py' .",

&nbsp; "puntaje": 4,

&nbsp; "threshold": 2,

&nbsp; "peso": "critico"

}

```



---



\#### STRT-003: Inyeccion de Estrategia

```json

{

&nbsp; "id": "STRT-003",

&nbsp; "categoria": "Strategy",

&nbsp; "descripcion": "Verificar inyeccion via constructor",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'self.\_estrategia\\\\|estrategia:' --include='\*service\*.py' .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 2,

&nbsp; "peso": "alto"

}

```



---



\### 1.5 Calidad de Codigo



\#### QUAL-001: Constantes Centralizadas

```json

{

&nbsp; "id": "QUAL-001",

&nbsp; "categoria": "Calidad",

&nbsp; "descripcion": "Verificar archivo constantes.py existe",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -name 'constantes.py' -type f",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\#### QUAL-002: NO Lambdas

```json

{

&nbsp; "id": "QUAL-002",

&nbsp; "categoria": "Calidad",

&nbsp; "descripcion": "Verificar ausencia de lambdas",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'lambda ' --include='\*.py' . | wc -l",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 0,

&nbsp; "peso": "medio",

&nbsp; "inverted": true

}

```



\*\*Nota\*\*: `inverted: true` significa que 0 coincidencias es BUENO



---



\#### QUAL-003: Type Hints

```json

{

&nbsp; "id": "QUAL-003",

&nbsp; "categoria": "Calidad",

&nbsp; "descripcion": "Verificar uso de type hints",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'def.\*->\\\\|: str\\\\|: int\\\\|: float' --include='\*.py' . | wc -l",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 50,

&nbsp; "peso": "medio"

}

```



---



\#### QUAL-004: Docstrings Google Style

```json

{

&nbsp; "id": "QUAL-004",

&nbsp; "categoria": "Calidad",

&nbsp; "descripcion": "Verificar docstrings Google Style (Args:)",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn 'Args:' --include='\*.py' . | wc -l",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 20,

&nbsp; "peso": "bajo"

}

```



---



\#### QUAL-005: Organizacion de Imports

```json

{

&nbsp; "id": "QUAL-005",

&nbsp; "categoria": "Calidad",

&nbsp; "descripcion": "Verificar comentarios de seccion en imports",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "grep",

&nbsp; "comando": "grep -rn '# Standard library\\\\|# Local application' --include='\*.py' . | wc -l",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 10,

&nbsp; "peso": "bajo"

}

```



---



\### 1.6 Estructura del Proyecto



\#### STRC-001: Paquete entidades/

```json

{

&nbsp; "id": "STRC-001",

&nbsp; "categoria": "Estructura",

&nbsp; "descripcion": "Verificar paquete entidades existe",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -type d -name 'entidades'",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\#### STRC-002: Paquete servicios/

```json

{

&nbsp; "id": "STRC-002",

&nbsp; "categoria": "Estructura",

&nbsp; "descripcion": "Verificar paquete servicios existe",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -type d -name 'servicios'",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\#### STRC-003: Paquete patrones/

```json

{

&nbsp; "id": "STRC-003",

&nbsp; "categoria": "Estructura",

&nbsp; "descripcion": "Verificar paquete patrones existe",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -type d -name 'patrones'",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### STRC-004: Archivos \_\_init\_\_.py

```json

{

&nbsp; "id": "STRC-004",

&nbsp; "categoria": "Estructura",

&nbsp; "descripcion": "Verificar archivos \_\_init\_\_.py en paquetes",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -name '\_\_init\_\_.py' -type f | wc -l",

&nbsp; "puntaje": 2,

&nbsp; "threshold": 10,

&nbsp; "peso": "medio"

}

```



---



\## Seccion 2: Verificaciones Dinamicas (Ejecucion)



\### 2.1 Ejecucion Exitosa



\#### EXEC-001: Ejecutar main.py Sin Errores

```json

{

&nbsp; "id": "EXEC-001",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar que main.py ejecuta sin errores",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python",

&nbsp; "comando": "timeout 30 python main.py",

&nbsp; "puntaje": 10,

&nbsp; "threshold": 0,

&nbsp; "peso": "critico",

&nbsp; "validacion": "return\_code == 0"

}

```



---



\#### EXEC-002: Mensaje de Exito Final

```json

{

&nbsp; "id": "EXEC-002",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar mensaje EJEMPLO COMPLETADO EXITOSAMENTE",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep 'EJEMPLO COMPLETADO EXITOSAMENTE'",

&nbsp; "puntaje": 5,

&nbsp; "threshold": 1,

&nbsp; "peso": "critico"

}

```



---



\#### EXEC-003: No Excepciones No Manejadas

```json

{

&nbsp; "id": "EXEC-003",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar ausencia de tracebacks",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'traceback\\\\|error:' | wc -l",

&nbsp; "puntaje": 5,

&nbsp; "threshold": 0,

&nbsp; "peso": "alto",

&nbsp; "inverted": true

}

```



---



\### 2.2 Patrones en Accion



\#### EXEC-004: Patron Singleton Demostrado

```json

{

&nbsp; "id": "EXEC-004",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar mensaje de Singleton en output",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'singleton'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\#### EXEC-005: Patron Factory Demostrado

```json

{

&nbsp; "id": "EXEC-005",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar mensaje de Factory en output",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'factory'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\#### EXEC-006: Patron Observer Demostrado

```json

{

&nbsp; "id": "EXEC-006",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar mensaje de Observer en output",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'observer'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\#### EXEC-007: Patron Strategy Demostrado

```json

{

&nbsp; "id": "EXEC-007",

&nbsp; "categoria": "Ejecucion",

&nbsp; "descripcion": "Verificar mensaje de Strategy en output",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'strategy'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "medio"

}

```



---



\### 2.3 Funcionalidad



\#### EXEC-008: Plantacion Funcional

```json

{

&nbsp; "id": "EXEC-008",

&nbsp; "categoria": "Funcionalidad",

&nbsp; "descripcion": "Verificar mensaje de plantacion",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'plantar\\\\|cultivo'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 4,

&nbsp; "peso": "alto"

}

```



---



\#### EXEC-009: Riego Funcional

```json

{

&nbsp; "id": "EXEC-009",

&nbsp; "categoria": "Funcionalidad",

&nbsp; "descripcion": "Verificar mensaje de riego",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "python\_output",

&nbsp; "comando": "timeout 30 python main.py 2>\&1 | grep -i 'riego\\\\|agua'",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 2,

&nbsp; "peso": "alto"

}

```



---



\#### EXEC-010: Persistencia Funcional

```json

{

&nbsp; "id": "EXEC-010",

&nbsp; "categoria": "Funcionalidad",

&nbsp; "descripcion": "Verificar archivo persistido existe",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "filesystem",

&nbsp; "comando": "timeout 30 python main.py \&\& find ./data -name '\*.dat' -type f",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 1,

&nbsp; "peso": "alto"

}

```



---



\## Seccion 3: Metricas de Codigo



\### 3.1 Complejidad Ciclomatica



\#### METR-001: Complejidad Promedio Baja

```json

{

&nbsp; "id": "METR-001",

&nbsp; "categoria": "Metricas",

&nbsp; "descripcion": "Verificar complejidad ciclomatica promedio < 10",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "radon",

&nbsp; "comando": "radon cc . -a -s",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 10,

&nbsp; "peso": "bajo",

&nbsp; "requires\_tool": "radon"

}

```



\*\*Instalacion\*\*: `pip install radon`



---



\### 3.2 Lineas de Codigo



\#### METR-002: Total de Lineas de Codigo

```json

{

&nbsp; "id": "METR-002",

&nbsp; "categoria": "Metricas",

&nbsp; "descripcion": "Contar lineas de codigo Python",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "cloc",

&nbsp; "comando": "find . -name '\*.py' -not -path './.venv/\*' -exec wc -l {} + | tail -1",

&nbsp; "puntaje": 0,

&nbsp; "threshold": 500,

&nbsp; "peso": "informativo"

}

```



\*\*Nota\*\*: `puntaje: 0` indica que es solo informativo



---



\### 3.3 Duplicacion de Codigo



\#### METR-003: Codigo Duplicado

```json

{

&nbsp; "id": "METR-003",

&nbsp; "categoria": "Metricas",

&nbsp; "descripcion": "Detectar codigo duplicado con PMD CPD",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "cpd",

&nbsp; "comando": "pmd cpd --minimum-tokens 50 --language python --files .",

&nbsp; "puntaje": 3,

&nbsp; "threshold": 5,

&nbsp; "peso": "bajo",

&nbsp; "requires\_tool": "pmd",

&nbsp; "inverted": true

}

```



\*\*Instalacion\*\*: Descargar PMD desde https://pmd.github.io/



---



\## Seccion 4: Tests (Opcional)



\### 4.1 Tests Unitarios



\#### TEST-001: Tests Existen

```json

{

&nbsp; "id": "TEST-001",

&nbsp; "categoria": "Tests",

&nbsp; "descripcion": "Verificar archivos de tests",

&nbsp; "tipo": "estatica",

&nbsp; "metodo": "glob",

&nbsp; "comando": "find . -name 'test\_\*.py' -o -name '\*\_test.py' | wc -l",

&nbsp; "puntaje": 5,

&nbsp; "threshold": 1,

&nbsp; "peso": "bonus"

}

```



---



\#### TEST-002: Coverage > 70%

```json

{

&nbsp; "id": "TEST-002",

&nbsp; "categoria": "Tests",

&nbsp; "descripcion": "Verificar cobertura de tests",

&nbsp; "tipo": "dinamica",

&nbsp; "metodo": "pytest",

&nbsp; "comando": "pytest --cov=. --cov-report=term-missing | grep 'TOTAL' | awk '{print $4}'",

&nbsp; "puntaje": 10,

&nbsp; "threshold": 70,

&nbsp; "peso": "bonus",

&nbsp; "requires\_tool": "pytest-cov"

}

```



---



\## Workflow de n8n - Estructura Completa



\### Nodo 1: Inicializar Evaluacion



```json

{

&nbsp; "nodes": \[

&nbsp;   {

&nbsp;     "name": "Inicializar",

&nbsp;     "type": "n8n-nodes-base.set",

&nbsp;     "parameters": {

&nbsp;       "values": {

&nbsp;         "string": \[

&nbsp;           {

&nbsp;             "name": "proyecto\_path",

&nbsp;             "value": "/path/to/proyecto"

&nbsp;           },

&nbsp;           {

&nbsp;             "name": "puntaje\_total",

&nbsp;             "value": 0

&nbsp;           },

&nbsp;           {

&nbsp;             "name": "criterios\_pasados",

&nbsp;             "value": 0

&nbsp;           },

&nbsp;           {

&nbsp;             "name": "criterios\_fallados",

&nbsp;             "value": 0

&nbsp;           }

&nbsp;         ]

&nbsp;       }

&nbsp;     }

&nbsp;   }

&nbsp; ]

}

```



---



\### Nodo 2: Ejecutar Verificaciones Estaticas



```json

{

&nbsp; "name": "Verificaciones Estaticas",

&nbsp; "type": "n8n-nodes-base.executeCommand",

&nbsp; "parameters": {

&nbsp;   "command": "={{ $json.comando }}",

&nbsp;   "cwd": "={{ $json.proyecto\_path }}"

&nbsp; }

}

```



\*\*Input esperado\*\*: Array de criterios estaticos (SING-\*, FACT-\*, etc.)



---



\### Nodo 3: Ejecutar Verificaciones Dinamicas



```json

{

&nbsp; "name": "Verificaciones Dinamicas",

&nbsp; "type": "n8n-nodes-base.executeCommand",

&nbsp; "parameters": {

&nbsp;   "command": "python main.py",

&nbsp;   "cwd": "={{ $json.proyecto\_path }}",

&nbsp;   "timeout": 30000

&nbsp; }

}

```



---



\### Nodo 4: Evaluar Criterios



```json

{

&nbsp; "name": "Evaluar Criterio",

&nbsp; "type": "n8n-nodes-base.function",

&nbsp; "parameters": {

&nbsp;   "functionCode": "const output = $input.all();\\nconst criterio = $json;\\nconst resultado = output\[0].json.stdout;\\nconst coincidencias = (resultado.match(/\\\\n/g) || \[]).length;\\n\\nif (criterio.inverted) {\\n  criterio.pasado = coincidencias <= criterio.threshold;\\n} else {\\n  criterio.pasado = coincidencias >= criterio.threshold;\\n}\\n\\ncriterio.puntaje\_obtenido = criterio.pasado ? criterio.puntaje : 0;\\n\\nreturn criterio;"

&nbsp; }

}

```



---



\### Nodo 5: Calcular Puntaje Total



```json

{

&nbsp; "name": "Calcular Total",

&nbsp; "type": "n8n-nodes-base.aggregate",

&nbsp; "parameters": {

&nbsp;   "aggregate": "aggregateAllItemData",

&nbsp;   "fieldsToAggregate": {

&nbsp;     "fieldToAggregate": \[

&nbsp;       {

&nbsp;         "fieldToAggregate": "puntaje\_obtenido",

&nbsp;         "renameField": false,

&nbsp;         "operation": "sum",

&nbsp;         "outputFieldName": "puntaje\_total"

&nbsp;       }

&nbsp;     ]

&nbsp;   }

&nbsp; }

}

```



---



\### Nodo 6: Generar Reporte



```json

{

&nbsp; "name": "Generar Reporte",

&nbsp; "type": "n8n-nodes-base.function",

&nbsp; "parameters": {

&nbsp;   "functionCode": "const puntaje = $json.puntaje\_total;\\nconst criterios = $input.all();\\n\\nconst pasados = criterios.filter(c => c.json.pasado).length;\\nconst fallados = criterios.filter(c => !c.json.pasado).length;\\n\\nconst porcentaje = (puntaje / 260) \* 100;\\n\\nlet calificacion = 'Insuficiente';\\nif (porcentaje >= 90) calificacion = 'Excelente';\\nelse if (porcentaje >= 80) calificacion = 'Muy Bueno';\\nelse if (porcentaje >= 70) calificacion = 'Bueno';\\nelse if (porcentaje >= 60) calificacion = 'Suficiente';\\n\\nreturn {\\n  puntaje\_total: puntaje,\\n  puntaje\_maximo: 260,\\n  porcentaje: porcentaje.toFixed(2),\\n  calificacion: calificacion,\\n  criterios\_pasados: pasados,\\n  criterios\_fallados: fallados,\\n  aprobado: porcentaje >= 70\\n};"

&nbsp; }

}

```



---



\### Nodo 7: Enviar Notificacion



```json

{

&nbsp; "name": "Enviar Email",

&nbsp; "type": "n8n-nodes-base.emailSend",

&nbsp; "parameters": {

&nbsp;   "fromEmail": "evaluacion@sistema.com",

&nbsp;   "toEmail": "={{ $json.estudiante\_email }}",

&nbsp;   "subject": "Resultado Evaluacion - {{ $json.calificacion }}",

&nbsp;   "text": "Puntaje: {{ $json.puntaje\_total }}/260 ({{ $json.porcentaje }}%)\\nCalificacion: {{ $json.calificacion }}\\nCriterios pasados: {{ $json.criterios\_pasados }}\\nCriterios fallados: {{ $json.criterios\_fallados }}"

&nbsp; }

}

```



---



\## Archivo de Configuracion Completa (JSON)



```json

{

&nbsp; "evaluacion": {

&nbsp;   "version": "1.0.0",

&nbsp;   "puntaje\_maximo": 260,

&nbsp;   "umbral\_aprobacion": 182,

&nbsp;   "criterios": \[

&nbsp;     {

&nbsp;       "id": "SING-001",

&nbsp;       "categoria": "Singleton",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "grep -rn '\_instance = None' --include='\*.py' .",

&nbsp;       "puntaje": 2,

&nbsp;       "threshold": 1,

&nbsp;       "peso": "alto"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "SING-002",

&nbsp;       "categoria": "Singleton",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "grep -rn 'def \_\_new\_\_' --include='\*.py' .",

&nbsp;       "puntaje": 3,

&nbsp;       "threshold": 1,

&nbsp;       "peso": "critico"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "FACT-001",

&nbsp;       "categoria": "Factory",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "grep -rn '@staticmethod' --include='\*factory\*.py' .",

&nbsp;       "puntaje": 3,

&nbsp;       "threshold": 2,

&nbsp;       "peso": "critico"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "OBSR-001",

&nbsp;       "categoria": "Observer",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "grep -rn 'class Observable' --include='\*.py' .",

&nbsp;       "puntaje": 3,

&nbsp;       "threshold": 1,

&nbsp;       "peso": "critico"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "STRT-001",

&nbsp;       "categoria": "Strategy",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "grep -rn 'class.\*Strategy.\*ABC' --include='\*.py' .",

&nbsp;       "puntaje": 3,

&nbsp;       "threshold": 1,

&nbsp;       "peso": "critico"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "EXEC-001",

&nbsp;       "categoria": "Ejecucion",

&nbsp;       "tipo": "dinamica",

&nbsp;       "comando": "timeout 30 python main.py",

&nbsp;       "puntaje": 10,

&nbsp;       "threshold": 0,

&nbsp;       "peso": "critico",

&nbsp;       "validacion": "return\_code == 0"

&nbsp;     },

&nbsp;     {

&nbsp;       "id": "QUAL-001",

&nbsp;       "categoria": "Calidad",

&nbsp;       "tipo": "estatica",

&nbsp;       "comando": "find . -name 'constantes.py' -type f",

&nbsp;       "puntaje": 3,

&nbsp;       "threshold": 1,

&nbsp;       "peso": "alto"

&nbsp;     }

&nbsp;   ]

&nbsp; }

}

```



---



\## Script Python Helper para n8n



\### evaluador\_automatico.py



```python

\#!/usr/bin/env python3

"""

Script helper para evaluacion automatizada.

Uso: python evaluador\_automatico.py --proyecto /path/to/proyecto --config config.json

"""



import json

import subprocess

import sys

from pathlib import Path

from typing import Dict, List, Any



class EvaluadorAutomatico:

&nbsp;   def \_\_init\_\_(self, proyecto\_path: str, config\_path: str):

&nbsp;       self.proyecto\_path = Path(proyecto\_path)

&nbsp;       self.config = self.\_cargar\_config(config\_path)

&nbsp;       self.resultados = \[]



&nbsp;   def \_cargar\_config(self, config\_path: str) -> Dict:

&nbsp;       with open(config\_path, 'r') as f:

&nbsp;           return json.load(f)



&nbsp;   def ejecutar\_comando(self, comando: str) -> Dict\[str, Any]:

&nbsp;       """Ejecuta comando y retorna resultado."""

&nbsp;       try:

&nbsp;           resultado = subprocess.run(

&nbsp;               comando,

&nbsp;               shell=True,

&nbsp;               cwd=self.proyecto\_path,

&nbsp;               capture\_output=True,

&nbsp;               text=True,

&nbsp;               timeout=30

&nbsp;           )

&nbsp;           return {

&nbsp;               'exitcode': resultado.returncode,

&nbsp;               'stdout': resultado.stdout,

&nbsp;               'stderr': resultado.stderr,

&nbsp;               'exito': resultado.returncode == 0

&nbsp;           }

&nbsp;       except subprocess.TimeoutExpired:

&nbsp;           return {

&nbsp;               'exitcode': -1,

&nbsp;               'stdout': '',

&nbsp;               'stderr': 'Timeout',

&nbsp;               'exito': False

&nbsp;           }



&nbsp;   def evaluar\_criterio(self, criterio: Dict) -> Dict:

&nbsp;       """Evalua un criterio individual."""

&nbsp;       resultado\_cmd = self.ejecutar\_comando(criterio\['comando'])



&nbsp;       # Contar coincidencias

&nbsp;       coincidencias = resultado\_cmd\['stdout'].count('\\n')



&nbsp;       # Evaluar segun threshold

&nbsp;       inverted = criterio.get('inverted', False)

&nbsp;       if inverted:

&nbsp;           pasado = coincidencias <= criterio\['threshold']

&nbsp;       else:

&nbsp;           pasado = coincidencias >= criterio\['threshold']



&nbsp;       return {

&nbsp;           'id': criterio\['id'],

&nbsp;           'categoria': criterio\['categoria'],

&nbsp;           'pasado': pasado,

&nbsp;           'coincidencias': coincidencias,

&nbsp;           'threshold': criterio\['threshold'],

&nbsp;           'puntaje\_max': criterio\['puntaje'],

&nbsp;           'puntaje\_obtenido': criterio\['puntaje'] if pasado else 0,

&nbsp;           'peso': criterio\['peso'],

&nbsp;           'output': resultado\_cmd\['stdout']\[:500]  # Primeros 500 chars

&nbsp;       }



&nbsp;   def evaluar\_todos(self) -> Dict:

&nbsp;       """Evalua todos los criterios."""

&nbsp;       for criterio in self.config\['evaluacion']\['criterios']:

&nbsp;           resultado = self.evaluar\_criterio(criterio)

&nbsp;           self.resultados.append(resultado)



&nbsp;       # Calcular totales

&nbsp;       puntaje\_total = sum(r\['puntaje\_obtenido'] for r in self.resultados)

&nbsp;       puntaje\_maximo = self.config\['evaluacion']\['puntaje\_maximo']

&nbsp;       porcentaje = (puntaje\_total / puntaje\_maximo) \* 100



&nbsp;       # Determinar calificacion

&nbsp;       if porcentaje >= 90:

&nbsp;           calificacion = 'Excelente'

&nbsp;       elif porcentaje >= 80:

&nbsp;           calificacion = 'Muy Bueno'

&nbsp;       elif porcentaje >= 70:

&nbsp;           calificacion = 'Bueno'

&nbsp;       elif porcentaje >= 60:

&nbsp;           calificacion = 'Suficiente'

&nbsp;       else:

&nbsp;           calificacion = 'Insuficiente'



&nbsp;       return {

&nbsp;           'puntaje\_total': puntaje\_total,

&nbsp;           'puntaje\_maximo': puntaje\_maximo,

&nbsp;           'porcentaje': round(porcentaje, 2),

&nbsp;           'calificacion': calificacion,

&nbsp;           'aprobado': porcentaje >= 70,

&nbsp;           'criterios\_pasados': sum(1 for r in self.resultados if r\['pasado']),

&nbsp;           'criterios\_fallados': sum(1 for r in self.resultados if not r\['pasado']),

&nbsp;           'resultados': self.resultados

&nbsp;       }



&nbsp;   def generar\_reporte\_json(self, output\_path: str):

&nbsp;       """Genera reporte en formato JSON."""

&nbsp;       resumen = self.evaluar\_todos()

&nbsp;       with open(output\_path, 'w') as f:

&nbsp;           json.dump(resumen, f, indent=2)



&nbsp;   def generar\_reporte\_markdown(self, output\_path: str):

&nbsp;       """Genera reporte en formato Markdown."""

&nbsp;       resumen = self.evaluar\_todos()



&nbsp;       markdown = f"""# Reporte de Evaluacion Automatizada



\*\*Proyecto\*\*: {self.proyecto\_path.name}

\*\*Fecha\*\*: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}



\## Resumen



\- \*\*Puntaje Total\*\*: {resumen\['puntaje\_total']}/{resumen\['puntaje\_maximo']}

\- \*\*Porcentaje\*\*: {resumen\['porcentaje']}%

\- \*\*Calificacion\*\*: {resumen\['calificacion']}

\- \*\*Estado\*\*: {'APROBADO' if resumen\['aprobado'] else 'NO APROBADO'}



\## Detalles



| Criterio | Categoria | Pasado | Puntaje | Peso |

|----------|-----------|--------|---------|------|

"""

&nbsp;       for r in self.resultados:

&nbsp;           estado = '✓' if r\['pasado'] else '✗'

&nbsp;           markdown += f"| {r\['id']} | {r\['categoria']} | {estado} | {r\['puntaje\_obtenido']}/{r\['puntaje\_max']} | {r\['peso']} |\\n"



&nbsp;       with open(output\_path, 'w') as f:

&nbsp;           f.write(markdown)





if \_\_name\_\_ == '\_\_main\_\_':

&nbsp;   import argparse

&nbsp;   from datetime import datetime



&nbsp;   parser = argparse.ArgumentParser(description='Evaluador automatico de proyectos')

&nbsp;   parser.add\_argument('--proyecto', required=True, help='Path al proyecto')

&nbsp;   parser.add\_argument('--config', required=True, help='Path al archivo de configuracion')

&nbsp;   parser.add\_argument('--output-json', help='Path para reporte JSON')

&nbsp;   parser.add\_argument('--output-md', help='Path para reporte Markdown')



&nbsp;   args = parser.parse\_args()



&nbsp;   evaluador = EvaluadorAutomatico(args.proyecto, args.config)



&nbsp;   if args.output\_json:

&nbsp;       evaluador.generar\_reporte\_json(args.output\_json)

&nbsp;       print(f"Reporte JSON generado: {args.output\_json}")



&nbsp;   if args.output\_md:

&nbsp;       evaluador.generar\_reporte\_markdown(args.output\_md)

&nbsp;       print(f"Reporte Markdown generado: {args.output\_md}")



&nbsp;   # Imprimir resumen en consola

&nbsp;   resumen = evaluador.evaluar\_todos()

&nbsp;   print(f"\\n=== RESUMEN ===")

&nbsp;   print(f"Puntaje: {resumen\['puntaje\_total']}/{resumen\['puntaje\_maximo']} ({resumen\['porcentaje']}%)")

&nbsp;   print(f"Calificacion: {resumen\['calificacion']}")

&nbsp;   print(f"Estado: {'APROBADO' if resumen\['aprobado'] else 'NO APROBADO'}")



&nbsp;   sys.exit(0 if resumen\['aprobado'] else 1)

```



---



\## Uso del Sistema de Evaluacion



\### 1. Preparar Configuracion



Crear `config.json` con criterios deseados (usar JSON de seccion anterior).



\### 2. Ejecutar Evaluacion Local



```bash

python evaluador\_automatico.py \\

&nbsp; --proyecto /path/to/PythonForestal \\

&nbsp; --config config.json \\

&nbsp; --output-json resultado.json \\

&nbsp; --output-md resultado.md

```



\### 3. Integrar con n8n



1\. Importar workflow de n8n (JSON proporcionado)

2\. Configurar nodos con paths correctos

3\. Conectar con sistema de notificaciones (email, Slack, etc.)

4\. Ejecutar workflow manualmente o mediante webhook



\### 4. Automatizar con Git Hooks



```bash

\#!/bin/bash

\# .git/hooks/pre-push



echo "Ejecutando evaluacion automatica..."

python evaluador\_automatico.py \\

&nbsp; --proyecto . \\

&nbsp; --config .rubrica/config.json \\

&nbsp; --output-json .rubrica/ultimo\_resultado.json



if \[ $? -eq 0 ]; then

&nbsp; echo "Evaluacion APROBADA - Permitiendo push"

&nbsp; exit 0

else

&nbsp; echo "Evaluacion FALLIDA - Bloqueando push"

&nbsp; exit 1

fi

```



---



\## Pesos de Criterios



| Peso | Valor Numerico | Uso |

|------|----------------|-----|

| \*\*critico\*\* | 1.5x | Criterios fundamentales (patrones principales) |

| \*\*alto\*\* | 1.2x | Criterios importantes (calidad, estructura) |

| \*\*medio\*\* | 1.0x | Criterios deseables (documentacion, type hints) |

| \*\*bajo\*\* | 0.8x | Criterios opcionales (metricas, extras) |

| \*\*bonus\*\* | 0.5x | Criterios adicionales (tests, CI/CD) |



---



\## Conclusiones



Este sistema de evaluacion automatizada permite:



1\. \*\*Evaluacion objetiva\*\*: Criterios verificables automaticamente

2\. \*\*Escalabilidad\*\*: Evaluar multiples proyectos simultaneamente

3\. \*\*Consistencia\*\*: Mismos criterios para todos los proyectos

4\. \*\*Rapidez\*\*: Evaluacion completa en < 1 minuto

5\. \*\*Trazabilidad\*\*: Reportes detallados en JSON/Markdown

6\. \*\*Integracion\*\*: Compatible con n8n, CI/CD, Git hooks



---



\*\*Version\*\*: 1.0.0

\*\*Ultima Actualizacion\*\*: Octubre 2025

\*\*Compatible con\*\*: n8n v1.0+, Python 3.13+

