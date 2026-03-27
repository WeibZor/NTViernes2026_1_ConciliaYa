# 📋 ConciliaYa - Documentación General del Proyecto

Bienvenido a **ConciliaYa**, una solución integral para la gestión y mediación de conflictos vecinales. Este documento proporciona una visión general del proyecto completo y guías para su instalación, configuración y despliegue.

## 📑 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Arquitectura General](#arquitectura-general)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Requisitos del Sistema](#requisitos-del-sistema)
5. [Instalación Completa](#instalación-completa)
6. [Configuración](#configuración)
7. [Ejecución de la Aplicación](#ejecución-de-la-aplicación)
8. [Documentación de Componentes](#documentación-de-componentes)
9. [Flujo de Trabajo](#flujo-de-trabajo)
10. [Mejoras Futuras](#mejoras-futuras)

---

## Visión General

**ConciliaYa** es una plataforma web completa diseñada para:

- ✅ **Registrar conflictos** vecinales con descripción detallada
- ✅ **Clasificar automáticamente** conflictos usando IA (Python FastAPI)
- ✅ **Gestionar usuarios** y perfiles de mediadores
- ✅ **Asignar mediaciones** automáticas basadas en disponibilidad
- ✅ **Rastrear estados** de resolución en tiempo real
- ✅ **Escalable y mantenible** con arquitectura hexagonal

### Casos de Uso Principales

1. **Usuario Reportero**: Registra un nuevo conflicto en la plataforma
2. **Clasificador Inteligente**: Sistema automático analiza y clasifica el conflicto
3. **Asignación de Mediador**: El sistema asigna un mediador disponible
4. **Seguimiento**: Estado del conflicto se actualiza en tiempo real
5. **Resolución**: Mediador finaliza la mediación con observaciones

---

## Arquitectura General

ConciliaYa utiliza una **arquitectura de tres capas** con **hexágonos independientes**:

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                         │
│              Interfaz de Usuario Web                        │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP REST
┌────────────────────▼────────────────────────────────────────┐
│              BACKEND (Spring Boot)                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Domain Layer (Lógica de Negocio Pura)              │  │
│  │  - Entidades de dominio                             │  │
│  │  - Puertos (Interfaces)                             │  │
│  │  - Casos de Uso                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Application Layer (Controladores)                   │  │
│  │  - REST Controllers                                 │  │
│  │  - DTOs y Validación                                │  │
│  │  - Global Exception Handler                         │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Infrastructure Layer (Adaptadores)                  │  │
│  │  - Persistencia (JPA/Hibernate)                      │  │
│  │  - Integración HTTP externa                         │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬──────────────────────────┬────────────────────┘
             │ JDBC              │ HTTP
             │                        │
┌────────────▼──────────┐    ┌────────▼────────────────────┐
│  DATABASE             │    │ MICROSERVICE (FastAPI)      │
│  (PostgreSQL/MySQL)   │    │ Clasificador de Conflictos  │
│  - 6 Tablas           │    │ - IA de Clasificación       │
│  - Relaciones         │    │ - Análisis de Texto         │
└───────────────────────┘    └─────────────────────────────┘
```

### Principios Arquitectónicos

- **Hexagonal (Ports & Adapters)**: Separación clara de dominios
- **Clean Code**: Código limpio y comprensible
- **SOLID**: 5 principios de diseño aplicados
- **Functional Programming**: Uso de Streams, Optional, Funciones Puras

---

## Estructura del Proyecto

```
Proyecto integrador/
├── conciliaya-backend/           # Spring Boot Application
│   ├── src/main/java/
│   │   └── com/conciliaya/
│   │       ├── domain/           # Capa de Dominio
│   │       │   ├── entity/       # Entidades de negocio
│   │       │   ├── ports/        # Interfaces (Puertos)
│   │       │   └── usecase/      # Casos de Uso
│   │       ├── application/      # Capa de Aplicación
│   │       │   ├── dto/          # Data Transfer Objects
│   │       │   ├── exception/    # Excepciones personalizadas
│   │       │   └── controller/   # REST Controllers
│   │       ├── infrastructure/   # Capa de Infraestructura
│   │       │   └── adapter/
│   │       │       ├── output/   # Adaptadores de persistencia
│   │       │       └── input/    # Adaptadores HTTP
│   │       └── config/           # Configuración Spring
│   ├── pom.xml                   # Dependencias Maven
│   └── README.md                 # Documentación backend
│
├── conciliaya-frontend/          # React Application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/           # Componentes React
│   │   ├── pages/                # Páginas
│   │   ├── services/             # Servicios API
│   │   ├── styles/               # Archivos CSS
│   │   ├── App.js                # Componente raíz
│   │   └── index.js              # Entrada
│   ├── package.json              # Dependencias NPM
│   ├── .env.example              # Variables de entorno
│   └── README.md                 # Documentación frontend
│
└── conciliaya-classifier/        # FastAPI Microservice
    ├── main.py                   # Aplicación principal
    ├── requirements.txt          # Dependencias Python
    └── README.md                 # Documentación API
```

---

## Requisitos del Sistema

### Backend (Spring Boot)

- **Java**: JDK 17 o superior
- **Maven**: 4.0.0 o superior
- **Bases de Datos**: PostgreSQL 14+ o MySQL 8.0+
- **Puerto**: 8080 (configurable)

### Frontend (React)

- **Node.js**: 16+ o superior
- **npm**: 8+ o npm
- **Puerto**: 3000 (configurable)

### Microservice (FastAPI)

- **Python**: 3.9 o superior
- **pip**: Gestor de paquetes de Python
- **Puerto**: 8000 (configurable)

### Sistema Operativo

- Windows 10+ con PowerShell o CMD
- Linux (Ubuntu 20.04+ recomendado)
- macOS 10.15+

---

## Instalación Completa

### 1️⃣ Instalación del Backend (Spring Boot)

```bash
# Navegar al directorio del backend
cd "Proyecto integrador/conciliaya-backend"

# Instalar dependencias con Maven
mvn clean install

# (Opcional) Crear base de datos
# PostgreSQL:
# CREATE DATABASE conciliaya;

# MySQL:
# CREATE DATABASE conciliaya CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Archivos de configuración necesarios:**
- ✅ `pom.xml` - Configurado ✓
- ✅ `application.yml` - Configurable
- ✅ `WebClientConfig` - Para HTTP
- ✅ `UseCaseConfig` - Para inyección de dependencias

### 2️⃣ Instalación del Frontend (React)

```bash
# Navegar al directorio del frontend
cd "Proyecto integrador/conciliaya-frontend"

# Instalar dependencias
npm install

# Crear archivo .env (desde .env.example)
# cp .env.example .env
# Editar .env con URL del backend: REACT_APP_API_URL=http://localhost:8080
```

**Dependencias principales:**
- ✅ React 18.2.0
- ✅ React Router DOM 6.16.0
- ✅ Axios 1.5.0
- ✅ React Toastify 9.1.3

### 3️⃣ Instalación del Microservice (FastAPI)

```bash
# Navegar al directorio del microservice
cd "Proyecto integrador/conciliaya-classifier"

# Crear entorno virtual (Recomendado)
python -m venv env
# En Windows:
env\Scripts\activate
# En Linux/Mac:
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

**Dependencias principales:**
- ✅ FastAPI 0.104.1
- ✅ Uvicorn 0.24.0
- ✅ Pydantic 2.4.2

---

## Configuración

### Backend - `application.yml`

```yaml
spring:
  application:
    name: conciliaya-backend
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: false
  datasource:
    url: jdbc:postgresql://localhost:5432/conciliaya
    username: postgres
    password: tu_contraseña
    driver-class-name: org.postgresql.Driver

# Microservice Integration
microservice:
  clasificador:
    url: http://localhost:8000
    endpoint: /api/v1/classify-conflict
    timeout-ms: 5000

server:
  port: 8080
  servlet:
    context-path: /api

logging:
  level:
    com.conciliaya: INFO
    org.springframework.web: WARN
```

### Frontend - `.env`

```env
REACT_APP_API_URL=http://localhost:8080/api
REACT_APP_ENV=development
```

### Microservice - Variables de Entorno

```bash
# En el archivo .env del microservice (opcional)
UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
LOG_LEVEL=INFO
```

---

## Ejecución de la Aplicación

### Opción 1: Ejecución Individual (Desarrollo)

#### Backend

```bash
cd conciliaya-backend
# Compilar y ejecutar
mvn spring-boot:run

# La aplicación estará disponible en:
# http://localhost:8080/api
```

#### Frontend

```bash
cd conciliaya-frontend
# Instalar dependencias (primera vez)
npm install

# Iniciar servidor de desarrollo
npm start

# La aplicación abrirá en:
# http://localhost:3000
```

#### Microservice

```bash
cd conciliaya-classifier
# Activar entorno virtual (si aplica)
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ejecutar con Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# API disponible en:
# http://localhost:8000
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Opción 2: Orden de Inicio Recomendado

```
1. Iniciar Base de Datos (PostgreSQL/MySQL)
   ↓
2. Iniciar Microservice (FastAPI) en puerto 8000
   ↓
3. Iniciar Backend (Spring Boot) en puerto 8080
   ↓
4. Iniciar Frontend (React) en puerto 3000
```

---

## Documentación de Componentes

Cada componente tiene su propia documentación detallada:

### 📖 Backend - Spring Boot
**Ubicación**: [conciliaya-backend/README.md](conciliaya-backend/README.md)

**Contiene**:
- Descripción detallada de la arquitectura hexagonal
- Especificación de 6 entidades de dominio
- 4 puertos y sus responsabilidades
- 4 casos de uso con flujos de trabajo
- 13 endpoints REST de la API
- Estrategia de validación y manejo excepciones
- Principios SOLID y Clean Code aplicados

### 📖 Frontend - React
**Ubicación**: [conciliaya-frontend/README.md](conciliaya-frontend/README.md)

**Contiene**:
- Estructura de componentes y páginas
- Servicios de API (ConflictoService, UsuarioService)
- Sistema de enrutamiento con React Router
- Sistema de notificaciones (toast)
- Guía de estilos y diseño responsive
- Pasos para ejecutar en desarrollo/producción

### 📖 Microservice - FastAPI
**Ubicación**: [conciliaya-classifier/README.md](conciliaya-classifier/README.md)

**Contiene**:
- Arquitectura de clasificación con IA
- 8 tipos de conflictos soportados
- 4 endpoints REST con ejemplos
- Lógica pura de clasificación
- Testing con cURL/Python
- Documentación Swagger automática

---

## Flujo de Trabajo

### Flujo de Creación de Conflicto

```
1. Usuario accede a /crear-conflicto (Frontend)
   ↓
2. Llena formulario con descripción y detalles
   ↓
3. Frontend valida datos localmente
   ↓
4. Envía POST a /api/conflictos (Backend)
   ↓
5. Backend valida con DTO (validaciones)
   ↓
6. Crea caso de uso: CrearConflictoUseCase
   ↓
7. Backend llama a Microservice (clasificación)
   ↓
8. FastAPI categoriza conflicto automáticamente
   ↓
9. Backend guarda en base de datos
   ↓
10. Obtiene primer mediador disponible
   ↓
11. Crea mediación automática
   ↓
12. Retorna respuesta JSON al frontend
   ↓
13. Frontend muestra confirmación con toast
   ↓
14. Redirige a página de conflictos
```

### Flujo de Actualización de Estado

```
Usuario → [Homepage] → [Ver conflicto]
             ↓
        [Actualizar Estado]
             ↓
    PUT /api/conflictos/{id}
             ↓
ActualizarEstadoConflictoUseCase
             ↓
Validar transición de estado
             ↓
Guardar en base de datos
             ↓
Retornar respuesta
             ↓
Frontend actualiza UI
```

---

## Mejoras Futuras

### Fase 2: Seguridad y Autenticación
- [ ] Implementar Spring Security con JWT
- [ ] Autenticación de usuarios
- [ ] Autorizaciones basadas en roles
- [ ] Control de acceso (RBAC)

### Fase 3: Testing Completo
- [ ] Unit tests para dominios (JUnit 5)
- [ ] Tests de controladores (MockMvc)
- [ ] Tests de use cases con Mockito
- [ ] Tests de frontend (Jest + React Testing Library)
- [ ] Integration Tests con TestContainers

### Fase 4: Características Avanzadas
- [ ] Notificaciones en tiempo real (WebSockets)
- [ ] Paginación de resultados
- [ ] Búsqueda avanzada con filtros
- [ ] Exportar reportes (PDF/CSV)
- [ ] Dashboard analítico
- [ ] Gráficos de estadísticas

### Fase 5: Infraestructura
- [ ] Docker y Docker Compose
- [ ] CI/CD con GitHub Actions
- [ ] Deployment a Kubernetes
- [ ] Monitoreo con Prometheus/Grafana
- [ ] Logging centralizado (ELK Stack)

### Fase 6: Base de Datos
- [ ] Scripts SQL para inicialización
- [ ] Flyway/Liquibase para migraciones
- [ ] Vistas auxiliares
- [ ] Índices optimizados

---

## Soporte y Contacto

Para preguntas, problemas o sugerencias:

1. **Revisar Documentación**: Consultar README de cada componente
2. **Verificar Logs**: Revisar archivos de log de Spring Boot y FastAPI
3. **Base de Datos**: Asegurar que la BD está accesible
4. **Puertos**: Verificar que 8080, 3000, 8000 no estén en uso

---

## Licencia

Este proyecto es de código abierto. Todos los derechos reservados © 2024.

---

## Estructura Técnica Resumida

| Componente | Tecnología | Puerto | Estado |
|-----------|-----------|--------|--------|
| **Backend** | Spring Boot 3.1.5 + Java 17 | 8080 | ✅ Completado |
| **Frontend** | React 18.2.0 + Axios | 3000 | ✅ Completado |
| **Microservice** | FastAPI 0.104.1 + Python 3.9 | 8000 | ✅ Completado |
| **Database** | PostgreSQL 14 / MySQL 8.0 | 5432/3306 | 🔧 Configurable |
| **API REST** | Endpoints especificados | 8080 | ✅ 13 Endpoints |

---

**Última actualización**: Diciembre 2024
**Versión**: 1.0.0
**Autores**: Equipo de Desarrollo ConciliaYa
