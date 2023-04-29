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

📁  ->  Carpeta
📄  ->  Archivo


📁 py_*<br>
`├─`  📁 app: Carpeta donde se encuentra el ejercicio principal.<br>
`├─`  📁 tests: Carpeta donde se encuentran los tests del ejercicio.<br>
`├─`  📁 .vscode: Carpeta donde se encuentran los archivos de configuración para VS Code.<br>
`└─`  📄 requirements.txt: Archivo que contiene las librerías necesarias para ejecutar el ejercicio.<br>

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
