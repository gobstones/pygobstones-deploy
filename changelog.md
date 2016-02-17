# 2016-02-10 - v1.5.4

- Solucionado el problema con los encodings.

# 2015-09-06 - v1.5.3

- Nuevo fix para el tema de los encodings. Ahora
  la GUI trabaja con UTF-8 y la implementación
  del lenguaje con ASCII. Esperemos esto solucione
  todo el asunto.
- Se arregló un bug por el cual se perdia informa-
  ción de una celda.


# 2015-08-30 - v1.5.2

- Fixes a los errores de encoding.
- Se arregló el error python cuando se introducia
  una variable donde se esperaba un comando. Ahora
  se informa adecuadamente el error.
- Se arregló el auto-completador que por algun motivo
  estaba robando mensajes destinados a la GUI y eso
  generaba inestabilidad en la aplicación. Ahora el
  auto-completador hace uso del lenguaje sin ejecutarlo
  en un proceso aparte.
- Se arregló un problema por el cual no se estaba 
  detectando correctamente la presencia de la definicion
  'program'.


# 2015-08-23 - v1.5.1

- Se arregló el problema con la codificación unicode
  que impedia ver la pantalla de BOOM
- Ahora los tableros aleatorios miden 3x3 como mínimo.
- Se arregló un problema con la codificación unicode
  que no permitia que se reporten los errores de
  sintaxis de la biblioteca.


# 2015-08-14 - v1.5.0

- Gran refactoring de código para poder convertir
  PyGobstones en un paquete 'pip' y posteriormente
  en un paquete 'deb'. Aún queda trabajo por hacer.
- Se arreglaron problemas con archivos y paths
  que contenian caracteres unicode.
- Se arregló el pequeño bug introducido de curses
  en Windows
- Se agregó el autocompletado. Esta herramienta es
  prototípica y habrá mejoras a medida que haya
  feedback sobre su uso.
- Se integraron los tests a PyUnit
- Para pygobstones-lang, se ejecutan los tests desde
  ./run_tests.sh
- Ahora se cuenta con un archivo de log de PyGobstones
  para facilmente contar con la traza de la aplicación.
  Este está disponible en:
    <CarpetaDeUsuario>/.pygobstones/pygobstones.log


# 2015-07-23 - v1.4.1

- Se arregló en Windows el problema relacionado
  con la libreria 'curses'


# 2015-06-16 - v1.4.0

Nuevas características:
- Se deshabilitó TODA la recursión. Para habilitarla se debe 
  pasar la opción "--recursion" a la implementación del 
  lenguaje.
- Ahora PyGobstones hace BOOM cuando se intenta ejecutar 
  repeticiones anidadas (también hay error en chequeo).
- Se agregaron todas las combinaciones de CTRL + Letra 

Bugfixes:
- Se arregló un error de PyGobstones que no dejaba realizar 
  chequeos (bug introducido tras un refactoring)
- Se arregló el problema por el cual todos los booleanos de 
  una lista de booleanos eran tomados como 'True'
- Se arregló la implementación del foreach para eliminar el 
  indice tras su utilización.
- Se arregló el módulo 'liveness'. Ahora es posible chequear 
  que las variables declaradas sean utilizadas al menos una 
  vez.


# 2015-06-13 v1.3.1

- Se incorporaron chequeo para los campos de la construccion 
  de registros:
- Todos los campos que define el tipo de registro deben ser 
  asignados durante la construcción
- No se admiten campos que no formen parte de la definición 
  de registro.


# 2015-06-08 v1.3.0

- Se corrigió el constructor que construye dado un registro 
  existente. Se chequea que el tipo del registro existente 
  coincida con el del constructor que se está creando, pero
  todavía no hay chequeo para los campos que se ingresan.
- Se separó la GUI de la implementación del lenguaje en 
  GITHUB, para fomentar la colaboración.
- Se unificaron las implementaciones. ¡Basta de mantener dos
  cosas a la vez! Ahora voy a poder meterme con los warning
  de anidación y otras yerbas.


# 2015-02-05 - v1.2.1

- Se arregló un error por el cual era posible crear un
  registro de un tipo dado basado en otro registro de un
  tipo distinto.



# 2014-11-21 - v1.2.0

Nuevo:
- Las ramas del modo interactivo son independientes (no se
  pueden cruzar variables).
- Se agregó la posibilidad de incluir una expresión de 
  registro dentro de la expresión constructora de un tipo
  registro. De este modo se crea un nuevo registro basado
  en esta expresion "sobreescribiendo" los valores de
  algunos campos de ese registro (minimo uno).
    Ej: Persona(p | nombre <- "pepe")
- Se renombró "isNil" a "isEmpty".
- Los Strings ahora son comparables mediante operadores
  relacionales (si, habia Strings y no lo dije).
- Se agregó una vestimenta que transoforma cada celda
  en un pixel.
- Se agregó la opción de guardar un tablero del editor
  como una imagen (alpha feature, must improve).
- Ahora se deshabilitan los arreglos y los registros 
  modificables (i.e. el operador punto) cuando se utiliza
  el tablero implícito.
- Se renombraron las instrucciones de bytecode "pushVar"
  a "pushFrom" y "assign" a "popTo".
- Se agregaron más tests.

Actualizaciones:
- Se actualizó el ejemplo de PixelArt

Fixes:
- Ahora la repetición (repeat) exige que la expresión
  que oficia de contador se encuentre delimitada por 
  paréntesis.
    Ej: repeat (3) { Skip }
- Se arregló el comportamiento del match-to
- Ahora en XGobstones utilizando el modo interactivo con 
  tablero explícito es posible nombrar al parámetro por
  referencia como se desee.
- Se removió de la sintaxis la vieja declaración de tipo
  para las variables.
  


# 2014-10-16 - v1.1.2

- Se arregló un error por el cual el foreach no terminaba
  cuando se iteraba sobre listas sin elementos.


# 2014-10-14 - v1.1.1

- Se arregló un error del foreach al utilizar secuencias
  enumerativas.


# 2014-10-14 - v1.1.0

- XGobstones permite utilizar el tablero implícito al estilo
  Gobstones omitiendo la variable de program/procedimiento "t.".
- El comando "if" permite utilizar la palabra clave "then"
  opcionalmente.
- Se arregló un bug en los rangos enumerativos de Gobstones.
- Se agregaron dos ejemplos del modo interactivo.


# 2014-06-25 - v1.0.18

- Ahora PyGobstones utiliza como directorio por defecto para
  guardar y cargar archivos el directorio %HOME%/gobstones
- A partir de esta versión PyGobstones está disponible en
  formato 'deb' para su instalación en distribuciones de
  Linux basadas en Debian.


# 2014-06-23 - v1.0.17

- Se arregló un bug interno introducido una mala gestion del
  repositorio de Gobstones por Mercurial que no permitia 
  continuar con la ejecución del programa.


# 2014-06-18 - v1.0.16

- Ahora se permite que existan variables, funciones o campos
  con nombres similares a las primitivas de Gobstones. ej:     

      function azul() {return(Azul)}

- Ahora es posible retornar expresiones en el program. Las
  mismas aparecerán en la ventana de resultados, solapa
  "Valores de retorno". Al no tener nombre, se las etiqueta
  como '#n' donde 'n' es la posición que la expresión ocupa
  en la tupla que se retorna. ej:

      program { 
          v := 2
          return(v, v+3, 4*4, Rojo)
      }

      v    =>   2
      #2   =>   5
      #3   =>   16
      #4   =>   Rojo

- Ahora el ejecutable principal es 'pygobstones.py' tanto para
  Linux como para Windows.


# 2014-06-18 - v1.0.15

- Se introdujeron fixes para el correcto funcionamiento de las 
  vestimentas.
- Se agregó una carpeta "docs" que contiene documentación sobre 
  PyGobstones.
- Se agregó el README.md.
- Se arregló el XGobstones el error por el cual los campos
  booleanos de los registros siempre denotaban True.
- Se quitó el procedimiento primitivo "IrAlOrigen" de Gobstones.


# 2014-06-08 - v1.0.14

- Se agregó una carpeta "examples" la cuál contiene ejemplos
  de programas en Gobstones


# 2014-06-01 - v1.0.13

- Se arregló un problema que no permitia anidar dos registros de
  diferente tipo los cuales poseen mismos nombres de campo.
- Se extendió el manejador de excepciones de PyGobstones para que
  maneje el error de ejecución cuando divergen el tipo actual de
  una variable y el nuevo tipo con el cual se pretende asignar.
- Ahora se importan de Biblioteca tanto un tipo de registro como
  sus funciones observadoras.


# 2014-05-27 - v1.0.12

- Ahora el operador punto "." no es aplicable a parámetros e indices.
- El operador "++" hace BOOM cuando se aplica sobre valores con tipo
  distinto al tipo lista.
- Se arregló el chequeo del rango de listas. Ahora se levanta una
  excepcion para expresiones del tipo [a,b,c..d] y cualquier otra
  expresión no definida por XGobstones.


# 2014-05-19 - v1.0.11

- Se mejoró el inspector de variables de retorno. Ahora se incluye
  un text area para visualizar datos de gran extensión y con mayor
  comodidad. Y se arregló un error que aparecia cuando no se
  retornaban variables.
- Se arregló la funcionalidad de chequeo.
- Ahora el operador '==' funciona para registros y listas.
- Se arregló la función 'init(xs)'.


# 2014-05-14 - v1.0.10

- Se agregó una solapa "Variables de retorno" en la visualizacion
  de los resultados de cada ejecución.
- Se corrigió un error en los rangos de XGobstones por los cuales
  el rango [1,1..10] generaba la sucesión de 1 a 10 cuando debería
  generar una lista vacía.
- Se modificó el comportamiento del editor de tableros para no
  abrir un editor nuevo cada vez que se presiona el botón editor de
  tableros. En vez, se hace un show() de esta ventana.


# 2014-05-08 - v1.0.9

- Se agregó una nueva preferencia para habilitar/deshabilitar
  la auto-indentación.
- Por defecto, la auto-indentación permanece deshabilitada
  (temporal hasta que esté 100% funcional).
- Se arregló el modo interactive para XGobstones.
- Se arregló un error en el cuál PyGobstones no capturaba
  las excepciones de XGobstones, por lo cuál quedaba esperando
  a la finalización de su ejecución infinitamente.


# 2014-05-06 - v1.0.8

- Ahora es posible indentar y desindentar  un conjunto de lineas 
  seleccionadas presionando las teclas <TAB> o <BACKTAB>.
- Las nuevas lineas creadas respetan la indentación de la linea
  anterior.


# 2014-04-21 - v1.0.7

- Se arregló el comando foreach para que funcione correctamente
  con los rangos.
- Se amplió el mecanismo de testing, agregando librerias de
  testing para Gobstones hechas en Gobstones.
- Se agregaron varios tests para garantizar el funcionamiento
  del comando foreach para los diferentes rangos (validos e
  invalidos).


# 2014-04-18 - v1.0.6

- Se agregó Syntax Highlighting para el archivo de biblioteca.
- Se habilitó el uso de XGobstones en PyGobstones.
- Se extendió el Syntax Highlighting para contemplar los elementos
  de XGobstones.
- Ahora los observadores de los campos de los registros son
  polimorficos, lo cual permite que haya varios tipos de registro
  con mismos nombres de campos.


# 2014-04-09 - v1.0.5

-Se arregló un bug del Syntax Highlighting que no permitia que
los numeros de un rango se coloreen completamente.
-Ahora se realizan chequeos de tipo y de liveness sobre el
codigo al utilizar el botón de chequeo.
-Se modificó el Syntax Highlighting para colorear las definiciones
(program, interactive program, function, procedure) con un color
diferente a los demás keywords.


# 2014-03-28 - v1.0.4

Se cambió el modo de chequeo de los interpretes a estricto. Al
chequear ahora se delatan aquellas invocaciones a procedimientos
o funciones que no respeten la definición.


# 2014-03-27 - v1.0.3

Se habilitó el Syntax Highlighting para resaltar la sintaxis de
Gobstones 3.0.0.


# 2014 - v1.0.0

Nueva versión de PyGobstones la cual posee una GUI completamente nueva.
Entre las características que podemos encontrar en el nuevo PyGobstones,
podemos observar:
    - Estética renovada.
    - Nuevo editor de tableros.
    - Mejorada la usabilidad.
    - Posibilidad de alternar entre los interpretes 
      Gobstones y XGobstones.
    - Incoporación de la Biblioteca al entorno de trabajo.
    - Incorporación de Vestimentas personalizadas para el
      tablero.

Equipo de desarrollo de PyGobstones:
    - Pablo Barenbaum
    - Ariel Morellato
    - Leonardo Orellana
    - Ary Pablo Batista
