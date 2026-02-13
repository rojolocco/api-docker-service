# API Docker Service

![GitHub release (latest by date)](https://img.shields.io/github/v/release/rojolocco/api-docker-service)
![Python Version](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1%2B-green)

Un servicio API basado en FastAPI optimizado para despliegue en Docker y orquestado con Docker Compose.

## Características

- **FastAPI**: API rápida y moderna con documentación automática
- **Docker Multi-stage**: Optimizado para tamaño reducido y seguridad
- **UV Package Manager**: Gestión de dependencias rápida y eficiente
- **Pruebas Unitarias**: Pruebas automatizadas con pytest
- **CI/CD Ready**: Preparado para integración y despliegue continuo
- **Configuración por Entorno**: Diferentes configuraciones para desarrollo y producción

## Requisitos

- Python 3.13+
- Docker y Docker Compose
- uv (opcional para desarrollo local)

## Estructura del Proyecto

```text
api-docker-service/
├── app/                    # Código fuente de la aplicación
│   ├── __init__.py
│   ├── main.py             # Punto de entrada de la API
│   ├── core/               # Núcleo de la aplicación
│   │   ├── __init__.py
│   │   ├── config.py       # Configuraciones
│   │   ├── middleware.py   # Middlewares
│   │   └── utils.py        # Utilidades
│   ├── db/                 # Configuración de base de datos
│   │   └── __init__.py
│   ├── models/             # Modelos de datos
│   │   └── __init__.py
│   ├── services/           # Lógica de negocio y servicios
│   │   └── __init__.py
│   ├── utils/              # Utilidades de la aplicación
│   │   └── __init__.py
│   └── api/                # Módulos de API
│       └── v1/             # Versión 1 de API
│           ├── __init__.py
│           ├── agents/     # Funcionalidad para agentes
│           │   ├── __init__.py
│           │   ├── routes.py
│           │   └── schemas.py
│           ├── automation/ # Funcionalidad para automatización
│           │   ├── __init__.py
│           │   ├── routes.py
│           │   └── schemas.py
│           ├── frontend/   # Endpoints para frontend
│           │   ├── __init__.py
│           │   ├── routes.py
│           │   └── schemas.py
│           └── storage/    # Funcionalidad para almacenamiento
│               ├── __init__.py
│               ├── routes.py
│               └── schemas.py
├── test/                   # Pruebas unitarias
│   ├── __init__.py
│   ├── conftest.py         # Configuración de pytest
│   ├── test_main.py        # Pruebas principales
│   └── api/                # Pruebas específicas de API
│       ├── __init__.py
│       └── test_client.py  # Pruebas de cliente API
├── docker-compose.dev.yaml # Configuración para desarrollo
├── docker-compose.yaml     # Configuración para producción
├── Dockerfile              # Definición multi-stage para Docker
├── pyproject.toml          # Dependencias y configuración del proyecto
└── LICENSE                 # Licencia del proyecto
```

## Instalación y Ejecución

### Desarrollo Local

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/rojolocco/api-docker-service.git
   cd api-docker-service
   ```

2. Instalar dependencias con uv:

   ```bash
   uv pip install -e .
   ```

3. Ejecutar en modo desarrollo:

   ```bash
   uvicorn app.main:app --reload
   ```

### Con Docker (Desarrollo)

1. Crear archivo `.env.dev` con las variables de entorno necesarias
2. Ejecutar:

   ```bash
   docker-compose -f docker-compose.dev.yaml up --build
   ```

### Producción

1. Crear archivo `.env` con las variables de entorno de producción
2. Ejecutar:

   ```bash
   docker-compose up -d
   ```

## Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

## API Endpoints

- `GET /`: Endpoint principal que devuelve un mensaje de bienvenida
- Documentación API (sólo en desarrollo):
  - Swagger UI: `/docs`
  - ReDoc: `/redoc`
  - OpenAPI JSON: `/openapi.json`

## Variables de Entorno

- `API_ENV`: Entorno de ejecución (`development` o `production`)
- Otras variables definidas en `.env` o `.env.dev`

## Seguridad

El Dockerfile implementa las mejores prácticas de seguridad:

- Usuario no-root para la ejecución
- Imágenes base mínimas
- Verificación de salud

## Licencia

Ver archivo [LICENSE](LICENSE) para más detalles.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abra un issue o un pull request para sugerencias o correcciones.
