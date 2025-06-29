# DNED Backend

Este proyecto es una API desarrollada en **FastAPI** con persistencia de datos en **MySQL**, orientada a proporcionar servicios backend para un sistema modular. Su diseño sigue una arquitectura basada en capas, que facilita la escalabilidad y el mantenimiento del código.

---

## Tecnologías utilizadas

- **FastAPI**: Framework moderno y rápido para construir APIs con Python 3.7+ basado en *type hints*.
- **MySQL**: Sistema de gestión de bases de datos relacional utilizado como almacenamiento persistente.
- **Uvicorn**: Servidor ASGI utilizado para ejecutar la aplicación FastAPI.
- **Docker (opcional)**: Para levantar el entorno completo con contenedores de forma sencilla.

---

## Requisitos

- Python 3.11 o superior
- MySQL 8.0 o superior (si se ejecuta en local)
- PowerShell o terminal compatible para entornos virtuales

---

## Configuración local (ambiente virtual)

1. **Crear el entorno virtual**

   ```bash
   python -m venv .venv
   ```

2. **Activar el entorno virtual**

   En PowerShell (Windows):

   ```bash
   .venv\Scripts\Activate.ps1
   ```

   En Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

3. **Instalar los requerimientos**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Opcional) Crear o actualizar archivo de requerimientos**

   ```bash
   pip freeze > requirements.txt
   ```

---

## 🐳 Uso con Docker

1. **Levantar el entorno completo**

   ```bash
   docker compose up --build
   ```

2. Acceder a la API:  
   [http://localhost:8000](http://localhost:8000)

3. Documentación Swagger:  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧱 Arquitectura del proyecto

El proyecto sigue una arquitectura en capas:

```
/app
├── configuration/     # Configuración del entorno y base de datos
├── controllers/       # Endpoints de la API (FastAPI routers)
├── domain/            # Modelos y estructuras de datos (DTOs, entidades)
├── repository/        # Acceso y lógica de persistencia de datos
├── service/           # Reglas de negocio y procesamiento principal
├── main.py            # Punto de entrada de la aplicación
└── requirements.txt   # Dependencias del proyecto
```

Este enfoque modular facilita el mantenimiento, testing y escalabilidad del sistema.

---

## 📦 Dependencias destacadas

```text
fastapi==0.115.14
uvicorn==0.35.0
pydantic==2.11.7
httpx==0.28.1
python-dotenv==1.1.1
email-validator==2.2.0
rich==14.0.0
```

---

## 📬 Contacto

Si tienes preguntas, sugerencias o deseas contribuir, no dudes en abrir un issue o pull request.

---

## Documentacion :
### SqlAlchemy :
- https://docs.sqlalchemy.org/en/20/tutorial/engine.html

