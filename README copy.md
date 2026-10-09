# Trabajo grupal: Pipeline de análisis de datos con Python

## Programación Aplicada a la IA --- Grupo 01: Marvel Comics

> **Propósito de este documento:** servir como guía de referencia del
> proyecto para cualquier integrante del grupo, colaborador o persona
> que revise el repositorio. Describe el objetivo, el flujo de trabajo,
> la arquitectura propuesta, los requisitos técnicos, los análisis
> posibles, las pruebas y los entregables.
>
> **Dataset asignado:** `grupo01_marvel_comics.csv` --- personajes de
> Marvel Comics (16.376 filas, según el enunciado).

------------------------------------------------------------------------

## 1. Resumen del proyecto

El trabajo consiste en diseñar y construir en grupo un pequeño
*pipeline* de análisis de datos orientado a objetos. El programa debe
partir de un archivo CSV en bruto, comprobar que los datos tienen un
formato razonable, limpiarlos, analizarlos y generar visualizaciones que
permitan comunicar los resultados.

El proyecto debe demostrar el uso justificado de:

-   Python y programación orientada a objetos (POO).
-   NumPy.
-   Pandas.
-   Matplotlib.
-   Funciones auxiliares reutilizables.
-   Herencia y `super()`.
-   Encapsulación.
-   Excepciones personalizadas y control de errores.

La arquitectura concreta ---número de clases, nombres, atributos,
métodos y relaciones--- la decide el grupo. Lo importante es que las
responsabilidades estén claramente separadas y que el código se pueda
ejecutar de principio a fin.

### Resultado esperado

Al finalizar, el repositorio debe contener:

1.  Código Python organizado en varios módulos `.py`.
2.  Un pipeline ejecutable desde un punto de entrada.
3.  Un dataset limpio exportado a CSV.
4.  Al menos tres gráficos distintos, con título y ejes, guardados en
    una carpeta de resultados.
5.  Un PowerPoint que explique el desarrollo, los resultados y las
    conclusiones.
6.  Un único archivo `.zip` o un enlace a un repositorio con los
    materiales del grupo.

No se solicita una memoria extensa ni un informe escrito independiente:
el código, los resultados y el PowerPoint constituyen la entrega.

------------------------------------------------------------------------

## 2. Objetivos

El pipeline debe ser capaz de:

-   **Cargar** el CSV de Marvel Comics.
-   **Validar** que el archivo existe, se puede leer y contiene una
    estructura adecuada.
-   **Limpiar** los datos, tratando valores nulos, duplicados, tipos y
    texto.
-   **Analizar** los datos mediante estadísticas descriptivas, filtros y
    agrupaciones.
-   **Visualizar** los resultados con gráficos claros.
-   **Exportar** el dataset limpio y los gráficos a la carpeta de
    resultados.
-   **Gestionar errores esperables** mediante excepciones y mensajes
    comprensibles.
-   **Aplicar POO** con una arquitectura propia, modular y fácil de
    entender.

------------------------------------------------------------------------

## 3. Dataset: Marvel Comics

El grupo 01 tiene asignado el archivo `grupo01_marvel_comics.csv`,
descrito en el enunciado como un conjunto de datos reales sobre
personajes de Marvel Comics, con 16.376 filas.

Entre los campos contemplados en el dataset se encuentran los
siguientes:

  -----------------------------------------------------------------------
  Campo                               Descripción general
  ----------------------------------- -----------------------------------
  `page_id`                           Identificador asociado al registro
                                      o página del personaje.

  `name`                              Nombre del personaje.

  `ID`                                Información de identidad del
                                      personaje, según las categorías del
                                      dataset.

  `ALIGN`                             Alineamiento del personaje, por
                                      ejemplo, bueno, malo o neutral,
                                      según los valores presentes.

  `EYE`                               Color de ojos.

  `HAIR`                              Color de pelo.

  `SEX`                               Categoría de sexo o género tal como
                                      está codificada en el dataset.

  `GSM`                               Campo de diversidad sexual o de
                                      género, de acuerdo con las
                                      categorías originales.

  `ALIVE`                             Estado vital del personaje, según
                                      la codificación original.

  `APPEARANCES`                       Número de apariciones registrado.

  `FIRST APPEARANCE`                  Información de la primera
                                      aparición.

  `Year`                              Año asociado a la primera
                                      aparición.
  -----------------------------------------------------------------------

**Importante:** antes de programar las validaciones o los análisis, el
grupo debe comprobar los nombres, tipos, categorías y valores reales del
CSV entregado. La tabla anterior es una orientación para entender el
conjunto de datos; el archivo es la referencia definitiva. No se deben
inventar categorías ni asumir que todos los campos están completos.

### Preguntas que pueden guiar el análisis

El grupo puede elegir preguntas que sean respondibles con las columnas y
la calidad real de los datos. Algunas ideas:

-   ¿Cómo se distribuyen los personajes por alineamiento?
-   ¿Cuántos personajes aparecen en cada categoría de estado vital?
-   ¿Qué categorías de sexo o género aparecen en el dataset?
-   ¿En qué años debutaron más personajes?
-   ¿Qué décadas concentran más primeras apariciones?
-   ¿Cuáles son los personajes con más apariciones registradas?
-   ¿Cómo se distribuyen los personajes según el número de apariciones?
-   ¿Se observan diferencias en el número de apariciones entre
    categorías de alineamiento?
-   ¿Qué campos contienen más valores ausentes y cómo afecta eso al
    análisis?

Estas preguntas son propuestas, no resultados anticipados. Las
conclusiones deben obtenerse ejecutando el análisis sobre el CSV real.

------------------------------------------------------------------------

## 4. Flujo de trabajo obligatorio

El pipeline debe seguir, conceptualmente, estas cuatro etapas:

``` text
CSV original
    |
    v
Carga y validación
    |
    v
Limpieza y transformación
    |
    v
Análisis
    |
    v
Visualización y exportación
    |
    v
Resultados + conclusiones
```

### 4.1. Carga y validación

La carga consiste en leer el CSV con Pandas y comprobar que puede
utilizarse.

Tareas recomendadas:

1.  Comprobar que la ruta del archivo es correcta.
2.  Comprobar que el archivo existe y es accesible.
3.  Leer el CSV con `pandas`.
4.  Comprobar que el resultado es un DataFrame válido y que contiene
    registros.
5.  Comprobar la presencia de las columnas necesarias para el pipeline.
6.  Comprobar, cuando proceda, que las columnas utilizadas en los
    análisis tienen tipos adecuados o pueden convertirse.
7.  Si la estructura no es válida, lanzar una excepción apropiada en
    lugar de continuar con datos incorrectos.

La validación debe ser coherente con los análisis elegidos. No es
necesario exigir columnas que el programa no vaya a utilizar, salvo que
el grupo defina expresamente un esquema obligatorio.

### 4.2. Limpieza y transformación

La limpieza debe realizarse de forma explícita y reproducible. Como
mínimo, se deben estudiar y tratar estos aspectos:

-   **Valores nulos:** detectar los ausentes y decidir cómo tratarlos
    según la columna y el análisis.
-   **Duplicados:** identificar filas duplicadas y decidir si deben
    eliminarse. No se debe asumir que dos personajes con nombres iguales
    son necesariamente el mismo registro.
-   **Tipos de datos:** revisar los tipos de las columnas y convertirlos
    cuando sea apropiado.
-   **Texto:** normalizar espacios, formatos o diferencias de escritura
    cuando ello evite categorías artificialmente separadas.
-   **Valores anómalos:** detectar valores imposibles o inesperados
    cuando se conozcan las reglas del campo.
-   **Trazabilidad:** conservar el CSV original sin sobrescribirlo y
    exportar el resultado limpio a otro archivo.

#### Criterios para tratar valores nulos

No se deben borrar automáticamente todas las filas que contengan algún
valor ausente. Por ejemplo, un personaje puede tener nombre y
alineamiento conocidos, pero no tener información de color de ojos. Ese
registro puede seguir siendo útil para analizar el alineamiento.

Posibles estrategias, según el campo:

-   Mantener el nulo si el análisis puede excluirlo de forma controlada.
-   Sustituir un nulo categórico por una etiqueta como `Desconocido`, si
    mejora la interpretación y se documenta.
-   Mantener los valores numéricos ausentes como `NaN` cuando sea lo
    adecuado.
-   Excluir registros únicamente en el análisis que requiera el campo
    ausente, explicando el criterio.

No se deben asignar valores ficticios que puedan distorsionar las
estadísticas. Las decisiones de limpieza deben quedar explicadas en el
código o en el PowerPoint.

#### Revisión de calidad

Antes y después de limpiar, es útil registrar:

-   Número de filas y columnas.
-   Número de duplicados detectados y eliminados.
-   Número de valores nulos por columna.
-   Tipos de datos.
-   Número de registros finales.
-   Transformaciones aplicadas.

Esto permite explicar qué ha cambiado entre el CSV original y el limpio.

### 4.3. Análisis

El análisis debe usar los datos ya preparados y producir resultados que
respondan a las preguntas del grupo.

Puede incluir:

-   Estadísticas descriptivas con Pandas y NumPy.
-   Recuentos y porcentajes de categorías.
-   Filtros por alineamiento, año, estado vital u otras columnas
    disponibles.
-   Agrupaciones mediante `groupby`.
-   Ordenaciones y selección de los valores más altos o más bajos.
-   Comparaciones entre grupos.
-   Detección de valores ausentes o distribuciones muy desiguales.

Cada análisis debe tener un propósito comprensible. Es preferible
realizar unos pocos análisis bien explicados a producir muchas cifras
sin interpretación.

### 4.4. Visualización y exportación

La visualización se realizará con Matplotlib. El enunciado exige **un
mínimo de tres gráficos distintos**, cada uno con título y ejes,
guardados en una carpeta de resultados.

Cada gráfico debe:

-   Representar una pregunta o resultado del análisis.
-   Tener un título descriptivo.
-   Etiquetar los ejes cuando corresponda.
-   Mostrar categorías y escalas legibles.
-   Evitar saturación visual.
-   Guardarse como archivo dentro de `resultados/`.

También se debe exportar el dataset limpio a CSV dentro de esa carpeta.

------------------------------------------------------------------------

## 5. Arquitectura del proyecto

La arquitectura es una decisión del grupo. La siguiente estructura es
una propuesta para separar responsabilidades y facilitar la integración.
Se puede modificar si el grupo justifica otra organización.

``` text
marvel-dataset-analyzer/
├── main.py
├── cargador.py
├── limpiador.py
├── analizador.py
├── visualizador.py
├── excepciones.py
├── utilidades.py
├── grupo01_marvel_comics.csv
├── resultados/
│   ├── marvel_limpio.csv
│   ├── alineamiento.png
│   ├── personajes_por_anio.png
│   └── top_personajes_apariciones.png
└── README.md
```

### `main.py` --- punto de entrada

Responsabilidades:

-   Definir o recibir la ruta del dataset.
-   Crear los objetos necesarios.
-   Coordinar el orden de ejecución del pipeline.
-   Controlar los errores del flujo principal.
-   Mostrar mensajes de estado comprensibles.
-   Garantizar que la ejecución termina de forma controlada.

`main.py` debe coordinar, no contener toda la lógica de carga, limpieza,
análisis y dibujo.

### `cargador.py` --- lectura y validación

Puede contener una clase como `CargadorDatos`, encargada de:

-   Recibir la ruta del CSV.
-   Leer los datos con Pandas.
-   Validar el archivo y las columnas necesarias.
-   Devolver el DataFrame cargado.
-   Lanzar errores específicos cuando no pueda continuar.

### `limpiador.py` --- limpieza

Puede contener una clase como `LimpiadorDatos`, encargada de:

-   Recibir el DataFrame.
-   Aplicar las reglas de limpieza.
-   Evitar modificar accidentalmente el original si no es la intención.
-   Devolver un DataFrame limpio.
-   Mantener las transformaciones agrupadas en métodos claros.

### `analizador.py` --- análisis

Puede contener una clase como `AnalizadorMarvel`, encargada de:

-   Recibir el DataFrame limpio.
-   Calcular estadísticas.
-   Aplicar filtros.
-   Agrupar y ordenar resultados.
-   Devolver resultados en estructuras que pueda utilizar el
    visualizador.

### `visualizador.py` --- gráficos

Puede contener una clase como `VisualizadorMarvel`, encargada de:

-   Recibir los resultados del análisis.
-   Crear los gráficos con Matplotlib.
-   Añadir títulos y etiquetas.
-   Guardar las imágenes en `resultados/`.
-   Cerrar las figuras después de guardarlas cuando corresponda, para
    evitar acumularlas durante la ejecución.

### `excepciones.py` --- errores propios

Debe contener al menos dos clases de excepción personalizadas que
hereden de `Exception` y que se utilicen realmente en el pipeline.

Ejemplos de nombres posibles:

-   `DatasetInvalidoError`: para una estructura o contenido que no
    cumpla las condiciones necesarias.
-   `ColumnaInexistenteError`: para un análisis que solicite una columna
    que no está disponible.

Los nombres son orientativos. Las excepciones deben representar errores
concretos y utilizarse en los puntos apropiados.

### `utilidades.py` --- funciones auxiliares

Debe reunir funciones independientes de las clases cuando sean
reutilizables. Por ejemplo:

-   Normalizar una cadena de texto.
-   Comprobar o preparar una carpeta de resultados.
-   Formatear una salida estadística.
-   Validar un parámetro común.

No es necesario trasladar a este módulo funciones que solo tengan
sentido dentro de una clase.

------------------------------------------------------------------------

## 6. Requisitos técnicos obligatorios

El enunciado exige que aparezcan en el código, de forma justificada y no
forzada, todos los siguientes elementos:

  ------------------------------------------------------------------------
  Requisito                           Mínimo exigido Qué debe demostrarse
  --------------------- ---------------------------- ---------------------
  Herencia                           1 relación real Una clase hija hereda
                                                     de una clase padre y
                                                     amplía o especializa
                                                     su comportamiento.

  `super()`                             Uso correcto La clase hija llama
                                                     al comportamiento
                                                     correspondiente de la
                                                     clase padre, por
                                                     ejemplo, al
                                                     constructor.

  Encapsulación               Atributos protegidos o Se controla el acceso
                                            privados mediante `@property`
                                                     o getters/setters.

  Argumentos variables       1 función con `*args` o Los argumentos
                                          `**kwargs` variables se utilizan
                                                     con una finalidad
                                                     real.

  Valor por defecto                      1 parámetro Una función o método
                                                     tiene un parámetro
                                                     con valor
                                                     predeterminado.

  Excepciones                             Al menos 2 Heredan de
  personalizadas                                     `Exception` y se
                                                     lanzan o gestionan en
                                                     el programa.

  Control de errores        `try`, `except`, `else`, Los cuatro forman
                                           `finally` parte del flujo
                                                     principal.

  Gráficos                      Al menos 3 distintos Tienen título y ejes
                                                     y se guardan en la
                                                     carpeta de
                                                     resultados.

  Modularidad                           Varios `.py` El proyecto no está
                                                     resuelto en un único
                                                     fichero ni en un
                                                     notebook.

  Librerías                      Solo las permitidas Pandas, NumPy,
                                                     Matplotlib y
                                                     biblioteca estándar
                                                     de Python.
  ------------------------------------------------------------------------

### Orientación sobre herencia

La herencia debe modelar una relación razonable. Por ejemplo, un
cargador especializado para Marvel podría heredar de un cargador
genérico y añadir validaciones específicas del dataset.

No se recomienda crear una clase hija que no añada ni especialice ningún
comportamiento solo para cumplir el requisito.

### Orientación sobre encapsulación

Un atributo como `_ruta` o `_datos` puede ser protegido y exponerse
mediante una propiedad. El grupo debe decidir qué atributos necesitan
control de acceso y qué operaciones deben permitirse.

### Orientación sobre `*args` y `**kwargs`

Los argumentos variables deben resolver una necesidad del proyecto. Por
ejemplo, permitir que una función de análisis reciba varias columnas o
que una operación acepte opciones configurables. Debe quedar claro cómo
se interpretan esos argumentos.

### Orientación sobre excepciones

Las excepciones personalizadas no deben quedarse declaradas sin uso.
Deben lanzarse cuando ocurra el error que representan y gestionarse en
el lugar apropiado. No conviene capturar cualquier excepción de forma
indiscriminada si eso oculta errores de programación.

### Orientación sobre `try / except / else / finally`

-   `try`: contiene las operaciones que pueden fallar.
-   `except`: gestiona los errores que el programa sabe tratar.
-   `else`: se ejecuta si el bloque `try` termina sin excepciones.
-   `finally`: se ejecuta tanto si hubo una excepción como si no, y
    sirve para acciones de cierre o mensajes finales.

------------------------------------------------------------------------

## 7. Ejemplo de coordinación del pipeline

El siguiente ejemplo es únicamente una referencia para entender cómo se
conectan los módulos. No es una plantilla obligatoria ni sustituye la
implementación de las clases.

``` python
from cargador import CargadorDatos
from limpiador import LimpiadorDatos
from analizador import AnalizadorMarvel
from visualizador import VisualizadorMarvel
from excepciones import DatasetInvalidoError, ColumnaInexistenteError


def main():
    try:
        cargador = CargadorDatos("grupo01_marvel_comics.csv")
        datos = cargador.cargar()

        limpiador = LimpiadorDatos()
        datos_limpios = limpiador.limpiar(datos)

        analizador = AnalizadorMarvel(datos_limpios)
        resultados = analizador.analizar()

        visualizador = VisualizadorMarvel(resultados)
        visualizador.generar_graficos()

        datos_limpios.to_csv(
            "resultados/marvel_limpio.csv",
            index=False
        )

    except (FileNotFoundError, DatasetInvalidoError) as error:
        print(f"Error en la carga o validación: {error}")

    except ColumnaInexistenteError as error:
        print(f"Error durante el análisis: {error}")

    else:
        print("Pipeline ejecutado correctamente.")

    finally:
        print("Fin de la ejecución.")


if __name__ == "__main__":
    main()
```

Para que el ejemplo funcione, las clases y métodos importados deben
existir y respetar las interfaces acordadas por el grupo. También debe
prepararse la carpeta `resultados/` antes de guardar los archivos.

------------------------------------------------------------------------

## 8. Propuesta de análisis y gráficos

Los análisis definitivos deben seleccionarse después de inspeccionar el
dataset y comprobar la calidad de las columnas.

### Análisis A: alineamiento

**Pregunta:** ¿Cómo se distribuyen los personajes por alineamiento?

Operaciones posibles:

-   Contar los personajes de cada categoría.
-   Calcular el porcentaje de cada categoría sobre los registros con
    alineamiento conocido.
-   Ordenar las categorías por frecuencia.
-   Decidir cómo mostrar los valores ausentes.

**Visualización sugerida:** gráfico de barras con categorías en el eje X
y número de personajes en el eje Y.

### Análisis B: primeras apariciones

**Pregunta:** ¿Cómo varía el número de primeras apariciones registradas
a lo largo del tiempo?

Operaciones posibles:

-   Revisar y convertir el campo de año.
-   Excluir del análisis temporal los registros sin año válido,
    contabilizándolos aparte.
-   Agrupar los personajes por año o por década.
-   Contar los registros de cada periodo.

**Visualización sugerida:** gráfico de líneas para años o gráfico de
barras para décadas. Debe tener sentido con el rango temporal y la
cantidad de valores disponibles.

### Análisis C: personajes con más apariciones

**Pregunta:** ¿Qué personajes tienen más apariciones registradas?

Operaciones posibles:

-   Convertir `APPEARANCES` a formato numérico.
-   Tratar los valores ausentes sin convertirlos en apariciones
    ficticias.
-   Ordenar de mayor a menor.
-   Seleccionar los diez primeros, o una cantidad configurable.

**Visualización sugerida:** gráfico de barras horizontales con el nombre
del personaje y el número de apariciones.

### Posibles análisis adicionales

-   Distribución del estado vital.
-   Distribución de color de ojos o pelo, teniendo en cuenta los nulos.
-   Comparación del número de apariciones por alineamiento.
-   Histograma del número de apariciones.
-   Comparación de la frecuencia de aparición por década y alineamiento.

El grupo debe evitar conclusiones causales si los datos solo permiten
observar asociaciones o distribuciones.

------------------------------------------------------------------------

## 9. Pruebas y validación del programa

Antes de preparar la entrega, se debe comprobar el funcionamiento de
cada etapa por separado y del pipeline completo.

### Pruebas de carga

-   El archivo correcto se carga sin errores.
-   Una ruta inexistente produce un error controlado.
-   Un archivo vacío o con una estructura no válida se detecta.
-   Las columnas requeridas se validan correctamente.

### Pruebas de limpieza

-   Los valores nulos se tratan conforme a las reglas definidas.
-   Los duplicados se identifican según un criterio explícito.
-   Las conversiones de tipos no destruyen datos válidos.
-   El DataFrame original no se modifica accidentalmente.
-   El resultado limpio conserva las columnas necesarias para el
    análisis.

### Pruebas de análisis

-   Las estadísticas se calculan sobre la columna correcta.
-   Los filtros devuelven los registros esperados.
-   Las agrupaciones y ordenaciones son coherentes.
-   Las columnas inexistentes generan la excepción correspondiente.
-   Los valores ausentes no producen resultados engañosos.

### Pruebas de visualización y exportación

-   Se generan al menos tres tipos de gráficos distintos.
-   Todos los gráficos tienen título y ejes etiquetados cuando
    corresponda.
-   Los archivos se guardan en `resultados/`.
-   El CSV limpio se exporta correctamente.
-   Las imágenes generadas pueden abrirse y contienen información
    legible.

### Prueba de ejecución completa

Ejecutar el programa desde el punto de entrada y comprobar que:

1.  Se carga el CSV.
2.  Se valida y limpia.
3.  Se realizan los análisis.
4.  Se generan los gráficos.
5.  Se exportan los resultados.
6.  Se muestra un mensaje de ejecución correcta si todo termina bien.
7.  Los errores esperables se gestionan sin interrumpir el programa con
    trazas no controladas.

------------------------------------------------------------------------

## 10. Organización del trabajo en equipo

El enunciado indica que hay diez grupos de tres personas y recomienda
acordar la arquitectura antes de repartir el trabajo. Para este grupo se
puede utilizar el siguiente reparto orientativo:

  -----------------------------------------------------------------------
  Área                                Responsabilidades principales
  ----------------------------------- -----------------------------------
  Integrante 1: carga y limpieza      `cargador.py`, `limpiador.py`,
                                      validación y tratamiento de datos.

  Integrante 2: análisis y errores    `analizador.py`, `excepciones.py`,
                                      estadísticas, filtros y
                                      agrupaciones.

  Integrante 3: visualización e       `visualizador.py`, coordinación de
  integración                         `main.py`, exportación y gráficos.

  Todo el grupo                       Arquitectura, revisión de
                                      requisitos, pruebas integrales,
                                      conclusiones y PowerPoint.
  -----------------------------------------------------------------------

El reparto puede cambiar según los conocimientos y la disponibilidad de
cada persona. No obstante, todos los integrantes deben comprender la
arquitectura y poder explicar cómo funciona el pipeline.

### Acuerdos que deben cerrarse antes de programar

-   Nombre y responsabilidad de cada clase.
-   Qué recibe y qué devuelve cada método.
-   Qué excepciones puede lanzar cada módulo.
-   Qué columnas se consideran necesarias.
-   Qué reglas de limpieza se van a aplicar.
-   Qué preguntas de análisis se van a responder.
-   Qué resultados necesita recibir el visualizador.
-   Cómo se ejecuta el proyecto desde `main.py`.

Es recomendable utilizar control de versiones y realizar una revisión
conjunta antes de integrar cambios.

------------------------------------------------------------------------

## 11. PowerPoint de presentación

El PowerPoint debe mostrar cómo se ha desarrollado la solución, sus
resultados y las conclusiones. No se pide una memoria extensa.

Una posible estructura de presentación es:

1.  **Portada:** título del trabajo, asignatura e integrantes.
2.  **Objetivo:** qué problema resuelve el pipeline y qué se pretende
    analizar.
3.  **Dataset:** procedencia indicada en el material, dimensiones y
    descripción de los campos utilizados.
4.  **Arquitectura:** módulos, clases y relación entre ellas.
5.  **Carga y validación:** comprobaciones realizadas y errores que se
    gestionan.
6.  **Limpieza:** problemas detectados, decisiones tomadas y cambios
    realizados.
7.  **Análisis:** preguntas planteadas, estadísticas y agrupaciones.
8.  **Visualizaciones:** gráficos principales y explicación de lo que
    muestran.
9.  **Conclusiones:** respuestas a las preguntas iniciales, limitaciones
    y posibles mejoras.
10. **Demostración o ejecución:** resumen del funcionamiento completo
    del programa.

Las conclusiones deben derivarse de los resultados obtenidos, no de
suposiciones previas.

------------------------------------------------------------------------

## 12. Reglas y restricciones del enunciado

-   Se permite utilizar únicamente las librerías vistas en clase:
    **Pandas, NumPy, Matplotlib y la biblioteca estándar de Python**.
-   No se permite resolver el trabajo en un único fichero.
-   No se permite entregar el trabajo resuelto exclusivamente en un
    notebook.
-   La separación en clases y ficheros forma parte de la evaluación.
-   Cada grupo trabaja con un dataset distinto.
-   Las entregas no deberían parecerse en resultados ni en arquitectura.
-   Se valorará negativamente una arquitectura calcada de la de otro
    grupo, aunque el dataset sea diferente.
-   El código debe ejecutarse de principio a fin sin errores no
    controlados.

Por tanto, las decisiones de arquitectura, limpieza y análisis deben
responder a las características concretas del dataset de Marvel Comics.

------------------------------------------------------------------------

## 13. Entrega final

La entrega debe consistir en **un único archivo `.zip` o un enlace a un
repositorio** por grupo que incluya:

-   Los módulos `.py`, organizados por responsabilidad.
-   La carpeta `resultados/`.
-   Los gráficos generados.
-   El dataset limpio exportado a CSV.
-   El PowerPoint con el desarrollo, los resultados y las conclusiones.

Ejemplo de estructura final:

``` text
grupo01_marvel_comics/
├── main.py
├── cargador.py
├── limpiador.py
├── analizador.py
├── visualizador.py
├── excepciones.py
├── utilidades.py
├── grupo01_marvel_comics.csv
├── README.md
├── resultados/
│   ├── marvel_limpio.csv
│   ├── alineamiento.png
│   ├── personajes_por_anio.png
│   └── top_personajes_apariciones.png
└── presentacion/
    └── presentacion_final.pptx
```

El nombre y la organización interna pueden variar, siempre que los
materiales requeridos estén incluidos y sean fáciles de localizar.

------------------------------------------------------------------------

## 14. Lista de comprobación final

Antes de entregar, revisad todos los puntos:

-   [ ] El CSV original está incluido y no se sobrescribe.
-   [ ] El proyecto está dividido en varios módulos `.py`.
-   [ ] Las clases tienen responsabilidades claras.
-   [ ] El CSV se carga y valida.
-   [ ] Los nulos, duplicados, tipos y textos se han estudiado y
    tratado.
-   [ ] El dataset limpio se exporta a la carpeta `resultados/`.
-   [ ] Se realizan estadísticas, filtros y agrupaciones.
-   [ ] Hay al menos una relación de herencia real.
-   [ ] Se utiliza `super()` correctamente.
-   [ ] Hay encapsulación con atributos protegidos o privados y
    propiedades o getters/setters.
-   [ ] Hay una función con `*args` o `**kwargs`.
-   [ ] Hay otra función o método con un parámetro por defecto.
-   [ ] Hay al menos dos excepciones personalizadas, utilizadas en el
    programa.
-   [ ] El flujo principal utiliza `try`, `except`, `else` y `finally`.
-   [ ] Se generan al menos tres gráficos distintos.
-   [ ] Los gráficos tienen título y ejes.
-   [ ] Los gráficos se guardan en `resultados/`.
-   [ ] Se utilizan únicamente las librerías permitidas.
-   [ ] El programa se ejecuta de principio a fin sin errores no
    controlados.
-   [ ] El PowerPoint presenta el desarrollo, los resultados y las
    conclusiones.
-   [ ] La entrega está organizada en un ZIP o repositorio único.

------------------------------------------------------------------------

## 15. Criterio general de calidad

Un trabajo completo no consiste únicamente en cumplir cada requisito de
forma aislada. La solución debe tener coherencia: las clases deben
colaborar entre sí, las excepciones deben responder a errores reales,
las funciones auxiliares deben ser reutilizables y los gráficos deben
representar resultados del análisis.

La arquitectura propuesta en este documento es una guía de organización,
no una estructura impuesta por el profesor. El grupo debe tomar sus
propias decisiones y poder justificarlas.

**La meta final es entregar un pipeline modular, comprensible,
reproducible y ejecutable, que convierta el CSV original de Marvel
Comics en un conjunto de datos limpio, análisis y visualizaciones, y que
demuestre correctamente los conceptos de programación exigidos en el
trabajo.**

------------------------------------------------------------------------

## Referencia

Documento base: *Programación Aplicada a la IA --- Trabajo Grupal:
Pipeline de Análisis de Datos con Python*, Ibon Soto Alsua, Mondragon
Unibertsitatea, 11 páginas.

Este README combina los requisitos del enunciado con una propuesta
práctica de organización y desarrollo para el dataset del grupo 01. Las
decisiones de implementación y los resultados definitivos corresponden
al grupo.
