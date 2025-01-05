# Django Books API

Este proyecto es una prueba técnica para Seek y es una API para gestionar libros, construida con Django, Django REST Framework y MongoDB (PyMongo). Incluye Docker y Docker Compose.

## Características

- Gestión de libros: creación, lectura, actualización y eliminación.
- Autenticación basada en tokens.
- Documentación automática de la API con Swagger y ReDoc.
- Comandos personalizados para cargar datos iniciales y crear usuarios de prueba.

## Requisitos

- Docker
- Docker Compose
- Python 3.12

## Instalación

### Usando Docker y Docker Compose

Clona este repositorio:

```bash
git clone <repositorio-url>
cd <directorio-del-proyecto>
```

Construye e inicia los contenedores:

```bash
docker-compose up --build
```

## Comandos personalizados

Después de tener docker compose inicializado y puedes empezar a hacer los siguientes comandos para cargar los libros iniciales y además algunos usuarios que te permitirán autenticarte en la aplicación usando el endpoint: [http://localhost:8000/api-token-auth](http://localhost:800/api-token-auth)

1. **Cargar datos iniciales**

    Cargar un conjunto de libros iniciales en la base de datos:

    ```bash
    docker-compose exec web python manage.py initial_data
    ```

2. **Crear usuarios de prueba**

    Crear usuarios de prueba con credenciales predefinidas:

    ```bash
    docker-compose exec web python manage.py create_test_users
    ```

    Usuarios de prueba serán:
    user1 - password1
    user2 - password2

La API estará disponible en [http://localhost:8000/api/](http://localhost:8000/api/).

## Documentación de la API

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
