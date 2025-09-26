# Learning Flask - Proyecto Completo

Este repositorio contiene una colección de ejemplos y proyectos desarrollados para aprender Flask, el micro-framework de Python para desarrollo web. Todo el contenido está basado en el tutorial de YouTube "Flask Tutorial for Beginners" de LesmeFranco.

## Tabla de Contenidos

- [Introducción a Flask](#introducción-a-flask)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejemplos y Módulos](#ejemplos-y-módulos)
  - [Blueprints](#blueprints)
  - [Bases de Datos & SQLAlchemy](#bases-de-datos--sqlalchemy)
  - [Formularios, POST y Archivos](#formularios-post-y-archivos)
  - [Rutas y URLs](#rutas-y-urls)
  - [Sesiones y Cookies](#sesiones-y-cookies)
  - [Archivos Estáticos & Bootstrap](#archivos-estáticos--bootstrap)
  - [Templates & HTML](#templates--html)
  - [Autenticación de Usuarios](#autenticación-de-usuarios)
- [Migraciones con Alembic](#migraciones-con-alembic)
- [Licencia](#licencia)

---

## Introducción a Flask

Flask es un micro-framework para Python que permite crear aplicaciones web de manera sencilla y flexible. Es ideal para aprender los conceptos básicos de desarrollo web, manejo de rutas, plantillas, bases de datos y autenticación.

## Estructura del Proyecto

```bash
LICENSE
README.md
Blueprints/
  run.py
  blueprintapp/
    __init__.py
    app.py
    blueprints/
      core/
        __init_.py
        routes.py
        templates/
      people/
        __init__.py
        models.py
        routes.py
        templates/
      todos/
        __init__.py
        models.py
        routes.py
        templates/
    migrations/
      ...
    templates/
      base.html
    instance/
      blueprints.db
Databases&SQLAlchemy/
  dbapplication/
    app.py
    models.py
    routes.py
    run.py
    migrations/
      ...
    templates/
      base.html
      details.html
      index.html
    instance/
      testdb.db
Forms-Post-Files/
  app.py
  downloads/
  files/
  templates/
Hello-flask/
  app.py
Routes&URLs/
  app.py
Session&Cookies/
  app.py
  templates/
StaticFiles&Bootstrap/
  app.py
  static/
  templates/
Templates&HTML/
  app.py
  templates/
UserAuthetication/
  dbapplication/
    app.py
    delete.py
    models.py
    routes.py
    run.py
    migrations/
      ...
    templates/
      base.html
      details.html
      index.html
      login.html
      signup.html
      users.html
```

## Instalación y Configuración

1. Clona el repositorio:

   ```pwsh
   git clone https://github.com/LesmeFranco/learning-flask.git
   ```

2. Crea un entorno virtual para cada ejercicio:

   ```pwsh
   python3 -m venv .venv
   ```

3. Inicia el entorno virtual e instala las dependencias

   ```pwsh
   # En Windows:
   .venv\Scripts\activate
   # Dentro del entorno
   pip install flask flask_sqlalchemy flask_bcrypt flask_migrate flask_login
   ```

4. Ejecuta los ejemplos de la carpeta correspondiente:
   ```pwsh
   # Ejemplo
   cd Blueprints
   python run.py
   ```

# Ejemplos y Módulos

## Blueprints

Organiza la aplicación en módulos reutilizables. Cada blueprint tiene su propio conjunto de rutas, modelos y plantillas.

- **core/**: Rutas principales y templates base.
- **people/**: Gestión de personas, modelos y rutas.
- **todos/**: Gestión de tareas, modelos y rutas.
- **run.py**: Punto de entrada para la app con blueprints.

---

## Bases de Datos & SQLAlchemy

Ejemplo de integración de bases de datos usando SQLAlchemy y migraciones con Alembic.

- **dbapplication/**: App con modelos, rutas y migraciones.
- **models.py**: Definición de modelos de base de datos.
- **routes.py**: Rutas para interactuar con los modelos.
- **migrations/**: Archivos de migración generados por Alembic.
- **instance/**: Bases de datos SQLite.

---

## Formularios, POST y Archivos

Manejo de formularios HTML, envío de datos por POST y subida/descarga de archivos.

- **app.py**: Lógica para procesar formularios y archivos.
- **downloads/**, **files/**: Ejemplos de archivos subidos y descargados.
- **templates/**: Plantillas para mostrar formularios y descargas.

---

## Rutas y URLs

Ejemplo básico de definición de rutas y manejo de parámetros en Flask.

- **app.py**: Rutas simples y dinámicas.

---

## Sesiones y Cookies

Gestión de sesiones de usuario y almacenamiento de datos en cookies.

- **app.py**: Ejemplo de login y manejo de sesión.
- **templates/**: Plantillas para login y visualización de datos de sesión.

---

## Archivos Estáticos & Bootstrap

Uso de archivos estáticos (CSS, JS, imágenes) y Bootstrap para mejorar la apariencia de la app.

- **static/**: Archivos CSS, JS e imágenes.
- **app.py**: Configuración para servir archivos estáticos.
- **templates/**: Uso de Bootstrap en las plantillas.

---

## Templates & HTML

Uso de Jinja2 para renderizar HTML dinámico y filtros personalizados.

- **templates/**: Plantillas HTML con variables y filtros.
- **app.py**: Ejemplo de renderización y uso de filtros.

---

## Autenticación de Usuarios

Sistema de registro, login y gestión de usuarios con base de datos.

- **dbapplication/**: App con autenticación.
- **models.py**: Modelo de usuario.
- **routes.py**: Rutas para login, registro y gestión de usuarios.
- **templates/**: Plantillas para login, registro y listado de usuarios.

---

## Migraciones con Alembic

La carpeta **migrations/** en cada módulo con base de datos contiene los archivos necesarios para gestionar cambios en los modelos usando Alembic.

- **alembic.ini**: Configuración de Alembic.
- **env.py**: Script principal de migración.
- **versions/**: Migraciones generadas.

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo LICENSE para más detalles.

---

## Créditos

Basado en el tutorial de YouTube: _Flask Tutorial for Beginners_  
**Autor del repositorio**: LesmeFranco
