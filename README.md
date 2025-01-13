# Proyecto de Automatización con Selenium

Bienvenido al proyecto de automatización, examen para la vacante de Automatizacion de Pruebas. La prueba consiste en hacer una busqueda en "www.mercadolibre.com", seleccionar el pais de México y realizar una serie de filtros para imprimir los primeros 5 resultados en la consola.

Este README proporciona las instrucciones necesarias para configurar el entorno, instalar dependencias, y empezar a trabajar con el proyecto.

## Requisitos Previos

- **Python 3.6+** necesita estar instalado en tu sistema.
- **pip** (gestor de paquetes de Python) debe estar disponible.
- **Google Chrome - latest version** navegador necesario para realizar el scrapping

## Configuración del Entorno Virtual

Es altamente recomendable utilizar un entorno virtual para aislar las dependencias del proyecto y evitar conflictos con otras librerías instaladas globalmente.

### Paso 1: Crear el Entorno Virtual

#### En Windows:
```bash
python -m venv .venv
```

#### En MacOS/Linux:
```bash
python3 -m venv .venv
```

> [!IMPORTANT]
> Este comando crea un directorio `.venv` en el proyecto.

### Paso 2: Activar el Entorno Virtual

#### En Windows:

```bash
.\.venv\Scripts\activate
```

#### En MacOS/Linux:
```bash
source .venv/bin/activate
```

> [!NOTE]
> Siempre activa tu entorno virtual antes de instalar nuevas librerías o ejecutar scripts de Python para asegurarte de que estás trabajando en el entorno correcto.

## Instalación de Dependencias

Una vez que tu entorno virtual esté activo, instala las dependencias listadas en `requirements.txt`.

```bash
pip install -r requirements.txt
```

> [!WARNING]
> Asegúrate de que el archivo `requirements.txt` esté actualizado y contenga todas las dependencias necesarias para el proyecto.

## Ejecución del Proyecto

Después de configurar y activar el entorno virtual, y de instalar todas las dependencias, puedes ejecutar el script:

```bash
python main.py
```