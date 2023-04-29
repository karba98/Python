<p align="center">
  <img width="800" height="300" src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png">
</p>

# Ejercicios de Programación en Python

Este proyecto contiene varios pequeños ejercicios para probar y practicar temas sencillos y probar algunas librerías interesantes en Python.

## Cómo usar este proyecto

Para usar este proyecto, simplemente clona este repositorio en tu computadora local:

git clone [https://github.com/karba98/Python.git](https://github.com/karba98/Python.git)

Si usa el IDE VS Code. configure en launch.json y settings.json tanto la ejecución de pruebas de pytest como la depuración de cada ejercicio

## Estructura de ejercicio

📁  ->  Carpeta<br>
📄  ->  Archivo


📁 <b>py_*</b><br>
`├─`  📁 <b>app</b>: Carpeta donde se encuentra el ejercicio principal.<br>
`├─`  📁 <b>tests</b>: Carpeta donde se encuentran los tests del ejercicio.<br>
`├─`  📁 <b>.vscode</b>: Carpeta donde se encuentran los archivos de configuración para VS Code.<br>
`└─`  📄 <b>requirements.txt</b>: Archivo que contiene las librerías necesarias para ejecutar el ejercicio.<br>

## ¿Qué es Python?

Python es un lenguaje de programación potente y fácil de aprender. Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos. La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en diversas áreas y sobre la mayoría de las plataformas.

Python es un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, la programación imperativa y, en menor medida, la programación funcional. Es un lenguaje interpretado, usa tipado dinámico y es multiplataforma.

Python es desarrollado por la Python Software Foundation (PSF), una organización sin ánimo de lucro que promueve, protege y avanza el lenguaje Python, y que también apoya y facilita el crecimiento de una comunidad diversa e internacional de programadores de Python.

## ¿Cómo instalar Python?

Para instalar Python en tu sistema operativo, puedes descargarlo desde la página oficial [https://www.python.org/downloads/](https://www.python.org/downloads/), donde encontrarás las versiones más recientes y las notas de lanzamiento.

También puedes usar el intérprete interactivo de Python desde tu navegador web, accediendo a [https://www.python.org/shell/](https://www.python.org/shell/), donde podrás ejecutar código Python sin necesidad de instalar nada.

## ¿Cómo ejecutar los ejercicios?

Para ejecutar los ejercicios de este proyecto, debes tener instalado Python en tu ordenador y abrir una terminal o consola. Luego, navega hasta la carpeta donde se encuentran los archivos .py y ejecuta el comando `python nombre_del_archivo.py`, donde `nombre_del_archivo.py` es el nombre del ejercicio que quieres probar.

Por ejemplo, si quieres ejecutar el ejercicio `hello_world.py`, debes escribir `(python | py) hello_world.py` y presionar Enter.

## Uso de Python en Visual Studio Code
<br>
<br>
<p align="center">
  <img width="800" height="300" src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg">
</p>
<br>
<br>

## Cómo usar y configurar Python en Visual Studio Code

Visual Studio Code (VS Code) es un editor de código fuente gratuito y multiplataforma que ofrece soporte para múltiples lenguajes de programación, entre ellos Python. VS Code tiene muchas ventajas para programar en Python, como:

- Una interfaz sencilla y personalizable.
- Un sistema de extensiones que permite añadir funcionalidades extra al editor.
- Un depurador integrado que facilita la detección y corrección de errores.
- Un terminal integrado que permite ejecutar comandos de Python y otras herramientas.
- Un sistema de IntelliSense que ofrece sugerencias de código, autocompletado, resaltado de sintaxis y documentación.
- Un sistema de control de versiones integrado que permite trabajar con Git y otros sistemas.

Para usar y configurar Python en VS Code, debes seguir los siguientes pasos:

### 1. Instalar Python y la extensión de Python para VS Code

Para poder ejecutar código Python en VS Code, debes tener instalado un intérprete de Python en tu sistema operativo. Puedes descargarlo desde la página oficial [https://www.python.org/downloads/](https://www.python.org/downloads/), donde encontrarás las versiones más recientes y las notas de lanzamiento.

También debes instalar la extensión de Python para VS Code, que te proporcionará las herramientas necesarias para trabajar con este lenguaje en el editor. Para ello, haz clic en el menú de extensiones a la izquierda y busca "Python". Selecciona la extensión de Microsoft y haz clic en "Instalar".


### 2. Seleccionar el intérprete de Python (general)

Una vez instalada la extensión de Python, debes seleccionar el intérprete de Python que quieres usar para ejecutar tu código. Para ello, abre un archivo .py o crea uno nuevo y haz clic en la barra de estado inferior izquierda, donde aparece "Seleccionar intérprete de Python".


Se abrirá una lista con los intérpretes disponibles en tu sistema. Elige el que quieras usar o instala uno nuevo si no tienes ninguno.

### 3. Escribir y ejecutar código Python

Ahora ya puedes escribir y ejecutar código Python en VS Code. Para escribir código, puedes usar el editor normal o la ventana interactiva de REPL (Read-Eval-Print Loop), que te permite ejecutar código línea por línea e interactuar con el intérprete.

Para ejecutar código, puedes usar el terminal integrado o el depurador integrado. El terminal te permite ejecutar comandos de Python y otras herramientas desde el editor. El depurador te permite ejecutar tu código paso a paso, establecer puntos de interrupción, inspeccionar variables y ver la salida.

Para abrir el terminal integrado, puedes usar el atajo Ctrl+` o hacer clic en "Terminal" > "Nueva terminal" en el menú superior. Para ejecutar tu código desde el terminal, puedes usar el comando `python nombre_del_archivo.py`, donde `nombre_del_archivo.py` es el nombre del archivo que quieres ejecutar.

### 4. Ejecutar código desde el terminal

Para abrir el depurador integrado, puedes hacer clic en "Ejecutar" > "Iniciar depuración" en el menú superior o usar el atajo F5. Para ejecutar tu código desde el depurador, debes tener un archivo launch.json que especifique la configuración de depuración. Puedes crear uno automáticamente haciendo clic en "Crear archivo launch.json" cuando se te solicite o manualmente haciendo clic en "Ejecutar" > "Agregar configuración" y eligiendo "Python".

### 5. Crear archivo launch.json

El archivo launch.json contiene una serie de opciones que determinan cómo se ejecuta y depura tu código. Puedes modificarlo según tus necesidades o dejarlo con los valores por defecto. Algunas de las opciones más importantes son:

- `name`: El nombre de la configuración que aparece en el menú desplegable de depuración.
- `type`: El tipo de depurador que se usa. Debe ser "python" para este caso.
- `request`: El tipo de solicitud que se hace al depurador. Debe ser "launch" para ejecutar un archivo o "attach" para conectarse a un proceso existente.
- `program`: La ruta del archivo que se quiere ejecutar o depurar.
- `args`: Una lista de argumentos que se pasan al programa al ejecutarlo.
- `console`: El tipo de consola que se usa para mostrar la salida del programa. Puede ser "internalConsole", "integratedTerminal" o "externalTerminal".
- `stopOnEntry`: Un valor booleano que indica si el depurador debe detenerse en la primera línea del programa o no.

Puedes consultar el resto de opciones disponibles en la [documentación oficial](https://code.visualstudio.com/docs/python/debugging#_launchjson-attributes).

Una vez que tienes tu archivo launch.json configurado, puedes iniciar la depuración haciendo clic en el botón verde con el icono de reproducir o presionando F5. Verás que se abre una barra de herramientas con los controles de depuración y una ventana lateral con las variables, los puntos de interrupción, la pila de llamadas y la salida.

### 5. Depurar código con VS Code

Puedes usar los botones de la barra de herramientas para controlar la ejecución del programa:

- Continuar (F5): Continúa la ejecución hasta el siguiente punto de interrupción o hasta el final del programa.
- Interrumpir (Shift+F5): Detiene la ejecución del programa y muestra el estado actual.
- Paso siguiente (F10): Ejecuta la siguiente línea de código y se detiene.
- Paso dentro (F11): Entra en la función o método que se está llamando y se detiene en la primera línea.
- Paso fuera (Shift+F11): Sale de la función o método actual y se detiene en la línea donde se hizo la llamada.
- Reiniciar (Ctrl+Shift+F5): Reinicia la ejecución del programa desde el principio.
- Detener (Shift+F5): Termina la sesión de depuración y cierra el programa.

Puedes establecer puntos de interrupción haciendo clic en el margen izquierdo del editor, junto al número de línea. Los puntos de interrupción son lugares donde quieres que el depurador se detenga para examinar el estado del programa. Puedes activar o desactivar los puntos de interrupción haciendo clic en ellos o eliminarlos arrastrándolos fuera del margen.

### 6. Establecer puntos de interrupción

Puedes inspeccionar las variables que están en el ámbito actual usando la ventana lateral de variables. Puedes expandir o contraer las variables para ver sus atributos o elementos. También puedes modificar los valores de las variables haciendo doble clic en ellos y escribiendo el nuevo valor

## Cómo crear el entorno de Python en VS Code

Un entorno de Python es un espacio aislado donde puedes instalar y usar una versión específica de Python y los paquetes que necesites para tu proyecto. Los entornos te permiten tener diferentes configuraciones para diferentes proyectos sin que interfieran entre sí.

Para crear el entorno de Python en VS Code, puedes usar el módulo venv estándar de Python o la herramienta conda si usas Anaconda. En este caso, vamos a usar venv como ejemplo.

### 1. Crear el entorno virtual con venv

Para crear el entorno virtual con venv, debes abrir el terminal integrado de VS Code y ejecutar el siguiente comando:

`python -m venv .venv`

Este comando crea una carpeta llamada .venv en la raíz de tu proyecto, donde se guardará el intérprete de Python y los paquetes que instales. Puedes cambiar el nombre de la carpeta si quieres, pero se recomienda usar .venv por convención.

### 2. Activar el entorno virtual

Para activar el entorno virtual, debes seleccionarlo como el intérprete de Python que quieres usar para tu proyecto. Para ello, haz clic en la barra de estado inferior izquierda, donde aparece "Seleccionar intérprete de Python".


Se abrirá una lista con los intérpretes disponibles en tu sistema. Elige el que corresponda al entorno virtual que acabas de crear. Debería tener un formato similar a este:

`Python 3.x.x 64-bit ('.venv': venv)`

Al seleccionar el intérprete, VS Code activará automáticamente el entorno virtual cada vez que abras un terminal integrado. Verás que aparece el nombre del entorno entre paréntesis al principio del prompt:

`(.venv) PS C:\Users\user\project>`

Esto indica que estás usando el intérprete y los paquetes del entorno virtual y no los del sistema.

### 3. Instalar los paquetes necesarios

Para instalar los paquetes necesarios para tu proyecto, puedes usar el comando pip desde el terminal integrado. Por ejemplo, si quieres instalar la librería requests, puedes ejecutar:

`pip install requests`

Esto instalará la librería requests y sus dependencias en la carpeta .venv del proyecto. Puedes comprobar los paquetes instalados usando el comando:

`pip list`

También puedes crear un archivo requirements.txt donde especifiques los nombres y las versiones de los paquetes que quieres instalar. Por ejemplo:

requests==2.26.0 pandas==1.3.4 matplotlib==3.5.0


Luego, puedes instalar todos los paquetes del archivo usando el comando:

`pip install -r requirements.txt`

Esto te facilitará la gestión de las dependencias de tu proyecto y te permitirá compartirlo con otros desarrolladores.

### 4. Desactivar o eliminar el entorno virtual

Para desactivar el entorno virtual, puedes cambiar el intérprete de Python por otro o cerrar el terminal integrado.

Para eliminar el entorno virtual, simplemente borra la carpeta .venv del proyecto.
Mensaje recibido. Ya he creado una sección en el readme.md de

## Comandos útiles de Python

### Manejo de paquetes

* `pip install <nombre_paquete>`: instala un paquete.
* `pip uninstall <nombre_paquete>`: desinstala un paquete.
* `pip freeze > requirements.txt`: guarda una lista de paquetes instalados y sus versiones en un archivo `requirements.txt`.
* `pip install -r requirements.txt`: instala paquetes listados en un archivo `requirements.txt`.
* `python setup.py install`: instala un paquete desde su código fuente.

### Manejo de archivos

* `with open("<nombre_archivo>", "r") as f`: abre un archivo para lectura.
* `with open("<nombre_archivo>", "w") as f`: abre un archivo para escritura.
* `os.path.exists("<ruta_archivo>")`: verifica si un archivo existe.
* `os.mkdir("<nombre_directorio>")`: crea un nuevo directorio.
* `os.listdir("<ruta_directorio>")`: lista los archivos en un directorio.
* `shutil.copy("<archivo_origen>", "<archivo_destino>")`: copia un archivo.

### Lectura y escritura de archivos

* `with open("<nombre_archivo>", "r") as f`: abre un archivo para lectura.
* `with open("<nombre_archivo>", "w") as f`: abre un archivo para escritura.
* `with open("<nombre_archivo>", "a") as f`: abre un archivo para añadir información al final.
* `f.read()`: lee todo el contenido de un archivo y lo devuelve como una cadena de texto.
* `f.readline()`: lee una sola línea de un archivo y la devuelve como una cadena de texto.
* `f.readlines()`: lee todas las líneas de un archivo y las devuelve como una lista de cadenas de texto.
* `f.write("<cadena>")`: escribe una cadena de texto en un archivo.
* `f.writelines(<lista_de_cadenas>)`: escribe una lista de cadenas de texto en un archivo.

### Manipulación de archivos

* `os.path.exists("<ruta_archivo>")`: verifica si un archivo existe.
* `os.path.abspath("<ruta_archivo>")`: devuelve la ruta absoluta de un archivo.
* `os.path.dirname("<ruta_archivo>")`: devuelve el directorio que contiene un archivo.
* `os.path.basename("<ruta_archivo>")`: devuelve el nombre base de un archivo.
* `os.path.splitext("<ruta_archivo>")`: divide una ruta de archivo en la ruta y la extensión.
* `os.rename("<ruta_archivo_antiguo>", "<ruta_archivo_nuevo>")`: renombra un archivo.
* `os.remove("<ruta_archivo>")`: elimina un archivo.

### Manipulación de directorios


* `os.mkdir("<nombre_directorio>")`: crea un nuevo directorio.
* `os.makedirs("<ruta_directorio>")`: crea un nuevo directorio y todos sus subdirectorios.
* `os.rmdir("<nombre_directorio>")`: elimina un directorio vacío.
* `shutil.copy("<archivo_origen>", "<archivo_destino>")`: copia un archivo.
* `shutil.copytree("<directorio_origen>", "<directorio_destino>")`: copia un directorio y todos sus subdirectorios.
* `shutil.rmtree("<directorio>")`: elimina un directorio y todos sus contenidos.

### Manejo de archivos comprimidos

* `zipfile.ZipFile("<nombre_archivo_zip>", "w")`: crea un archivo zip.
* `zipfile.ZipFile("<nombre_archivo_zip>", "r")`: abre un archivo zip.
* `zipfile.ZipFile("<nombre_archivo_zip>", "a")`: añade archivos a un archivo zip existente.
* `zipfile.ZipFile("<nombre_archivo_zip>").extractall("<ruta_destino>")`: extrae todos los archivos de un archivo zip.
* `zipfile.ZipFile("<nombre_archivo_zip>").extract("<nombre_archivo>", "<ruta_destino>")`: extrae un archivo específico de un archivo zip.

### Testing

* `pytest` : ejecuta tests.
* `pytest -v`: muestra un detalle completo de los tests.
* `pytest --cov`: muestra un reporte de cobertura de los tests.
* `pytest --cov=<nombre_paquete>`: muestra un reporte de cobertura específico para el paquete indicado.
* `pytest --cov-report=html`: genera un reporte HTML de cobertura.
* `pytest --cov-report=xml`: genera un reporte XML de cobertura.
* `pytest --cov-report=term-missing`: muestra la cobertura de código faltante en el reporte.
* `pytest --cov-fail-under=<porcentaje>`: falla el test si la cobertura de código está por debajo del porcentaje indicado.
* `pytest --disable-warnings`: deshabilita la emisión de advertencias durante los tests.
* `pytest --pdb`: inicia el debugger PDB en caso de que falle un test.
* `pytest --maxfail=<n>`: detiene los tests después del n-ésimo fallo.
* `pytest --flake8`: ejecuta la herramienta de linter Flake8 en el código de los tests.
* `pytest --mypy`: ejecuta la herramienta de tipado estático Mypy en el código de los tests.

### Ejecución y depuración de aplicaciones

* `python <nombre_archivo>.py`: ejecuta un archivo Python.
* `python -m <nombre_paquete>`: ejecuta una aplicación Python desde el paquete indicado.
* `uvicorn <nombre_main_app>:app --reload`: ejecuta una aplicación FastAPI en modo de desarrollo.

## ¿Dónde puedo aprender más sobre Python?

Si quieres aprender más sobre Python, puedes consultar los siguientes recursos:

- El tutorial oficial de Python: [https://docs.python.org/es/3/tutorial/index.html](https://docs.python.org/es/3/tutorial/index.html), donde encontrarás una introducción al lenguaje y sus características[^2^][5].
- La documentación oficial de Python: [https://docs.python.org/es/3/index.html](https://docs.python.org/es/3/index.html), donde encontrarás la referencia
