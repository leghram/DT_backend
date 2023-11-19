# API BACKEND

API para la aplicacion de CRUD de usuarios

## Requisitos Previos

- Python 3.10 o superior
- tener Docker instalado

## Instalación

## Clona este repositorio:

crea un carpeta de proyecto

```bash
mkdir proyecto
cd proyecto
```

luego ejecuta el siguiente comando para clonar el repositorio en la carpeta actual

```bash
git clone https://github.com/leghram/DT_backend.git .
```

## Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

## Activa el entorno virtual:

- En Windows:

  ```bash
  venv\Scripts\activate
  ```

- En macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

## Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Opcion 1: Levantar la API y crear una base de datos

Levanta la API usando el sigiuente comando
Adicionalmente se tiene que crear una base de datos en postgres.

Para crear la tabla en bases de datos tener como referencia los archivos de la carpeta /sql

```bash
uvicorn app.main:app --reload
```

## Opcion 2 : Levantar El Proyecto usando containers

Para seguir estos pasos es necesario contar con Docker

### Inicia los contenedores

Ejecutar el siguiente comando para levantar la API con la base de datos

```bash
docker-compose up -d
```

### Frontend de la aplicacion

visita el siguiente repositorio para clonarlo y ejecutarlo

url : https://github.com/leghram/DT_frontend
