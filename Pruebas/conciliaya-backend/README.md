# ConciliaYa Backend - Aplicación Full Stack para Gestión de Conflictos Vecinales

## 📋 Descripción del Proyecto

**ConciliaYa** es una aplicación web full stack para la gestión integral de conflictos vecinales. Permite reportar, clasificar, registrar y mediar conflictos entre vecinos de manera organizada y eficiente.

### Tecnologías Utilizadas

- **Backend**: Spring Boot 3.1.5 (Java 17)
- **Frontend**: React (próxima fase)
- **Base de Datos**: PostgreSQL / MySQL
- **Microservicio**: FastAPI (Python 3.9+)
- **API REST**: RESTful con JSON

---

## 🏗️ Arquitectura

### Arquitectura Hexagonal (Ports and Adapters)

La aplicación sigue el patrón de arquitectura hexagonal para lograr máxima separación de responsabilidades:

```
┌─────────────────────────────────────────────────────────┐
│                       PRESENTACIÓN                       │
│                   (Controllers REST)                      │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────┐
│                   APLICACIÓN                             │
│         (Services, Use Cases, DTOs)                      │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────┐
│                     DOMINIO                              │
│  (Entidades, Puertos/Interfaces, Casos de Uso)          │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────┐
│                INFRAESTRUCTURA                           │
│ (Adaptadores: JPA, HTTP, Configuración)                │
└─────────────────────────────────────────────────────────┘
```

### Capas

#### 1. **Domain Layer** (Dominio)
Contiene la lógica de negocio pura, independiente de frameworks:
- `model/`: Entidades de dominio (Usuario, Conflicto, Mediacion, etc.)
- `ports/`: Interfaces que definen los contratos
- `usecase/`: Casos de uso con lógica de negocio

#### 2. **Application Layer** (Aplicación)
Orquesta el dominio:
- `service/`: Servicios de aplicación
- DTOs para entrada/salida

#### 3. **Infrastructure Layer** (Infraestructura)
Implementaciones técnicas:
- `adapter/input/`: Controllers REST
- `adapter/output/`: Repositories JPA, Cliente HTTP
- `config/`: Configuración de Spring
- `exception/`: Excepciones personalizadas

---

## 📦 Estructura de Paquetes

```
com.conciliaya
├── domain/
│   ├── model/              # Entidades de dominio (POJOs)
│   │   ├── Usuario.java
│   │   ├── Conflicto.java
│   │   ├── Mediacion.java
│   │   ├── TipoConflicto.java
│   │   ├── EstadoConflicto.java
│   │   └── Perfil.java
│   ├── ports/              # Interfaces/Contratos
│   │   ├── UsuarioRepositoryPort.java
│   │   ├── ConflictoRepositoryPort.java
│   │   ├── MediacionRepositoryPort.java
│   │   └── ClasificadorConflictoPort.java
│   └── usecase/            # Casos de Uso
│       ├── CrearConflictoUseCase.java
│       ├── ObtenerConflictosUseCase.java
│       ├── ActualizarEstadoConflictoUseCase.java
│       └── AsignarMediacionUseCase.java
├── application/
│   └── service/            # Servicios de aplicación
├── infrastructure/
│   ├── adapter/
│   │   ├── input/          # Controllers REST
│   │   │   ├── ConflictoController.java
│   │   │   ├── UsuarioController.java
│   │   │   ├── GlobalExceptionHandler.java
│   │   │   └── dto/        # Data Transfer Objects
│   │   └── output/         # Repositorios JPA, Clientes HTTP
│   │       ├── persistence/
│   │       │   ├── *Entity.java
│   │       │   ├── *JpaRepository.java
│   │       │   └── *RepositoryAdapter.java
│   │       └── http/
│   │           └── ClasificadorConflictoAdapter.java
│   ├── config/             # Configuración
│   │   ├── WebClientConfig.java
│   │   └── UseCaseConfig.java
│   └── exception/          # Excepciones personalizadas
└── ConciliaYaApplication.java   # Clase principal
```

---

## 🎯 Entidades de Dominio

### 1. **Usuario**
Representa a los usuarios del sistema.

**Atributos:**
- `id`: Identificador único
- `nombre`: Primer nombre
- `apellido`: Apellido
- `email`: Correo electrónico (único)
- `telefono`: Teléfono de contacto
- `direccion`: Dirección
- `numeroDocumento`: Número de documento (único)
- `perfil`: Perfil/rol del usuario
- `activo`: Estado activo/inactivo
- `fechaCreacion`, `fechaActualizacion`: Auditoría

### 2. **Conflicto**
Representa un conflicto vecinal reportado.

**Atributos:**
- `id`: Identificador único
- `titulo`: Título del conflicto
- `descripcion`: Descripción detallada (se clasifica automáticamente)
- `ubicacion`: Ubicación del conflicto
- `usuarioReportante`: Usuario que reporta
- `usuarioInvolucrado`: Otra parte involucrada
- `tipoConflicto`: Tipo clasificado automáticamente
- `estadoConflicto`: Estado actual (nuevo, en proceso, resuelto, etc.)
- `prioridad`: 1-5 (baja a alta)
- `observaciones`: Notas adicionales
- `fechaReporte`, `fechaActualizacion`: Auditoría

### 3. **Mediación**
Representa el proceso de resolución de un conflicto.

**Atributos:**
- `id`: Identificador único
- `conflicto`: Conflicto a mediar
- `mediador`: Usuario mediador
- `fechaInicio`: Inicio de mediación
- `fechaFinalizacion`: Fin de mediación
- `resultado`: Resultado de la mediación
- `acuerdos`: Acuerdos alcanzados
- `completada`: Si la mediación está completa
- `fechaCreacion`, `fechaActualizacion`: Auditoría

### 4. **TipoConflicto**
Categoría de conflicto (ruido, estacionamiento, mascota, etc.)

### 5. **EstadoConflicto**
Estado del conflicto (nuevo, en revisión, en mediación, resuelto, etc.)

### 6. **Perfil**
Rol del usuario (ciudadano, mediador, administrador, etc.)

---

## 🔌 Puertos (Interfaces)

Los puertos definen los contratos que los adaptadores deben implementar:

### UsuarioRepositoryPort
```java
public interface UsuarioRepositoryPort {
    Usuario save(Usuario usuario);
    Optional<Usuario> findById(Long id);
    List<Usuario> findAllActivos();
    Optional<Usuario> findByEmail(String email);
    // ... más métodos
}
```

### ConflictoRepositoryPort
```java
public interface ConflictoRepositoryPort {
    Conflicto save(Conflicto conflicto);
    Optional<Conflicto> findById(Long id);
    List<Conflicto> findAll();
    List<Conflicto> findByEstado(Long estadoId);
    // ... más métodos
}
```

### ClasificadorConflictoPort
Integración con microservicio FastAPI para clasificación automática:
```java
public interface ClasificadorConflictoPort {
    Long clasificarConflicto(String descripcion);
    ClassificacionResponse clasificarConflictoDetallado(String descripcion);
    boolean esServicioDisponible();
}
```

---

## 📝 Casos de Uso

### CrearConflictoUseCase
Crea un nuevo conflicto con validación y clasificación automática.

```java
Conflicto conflicto = crearConflictoUseCase.ejecutar(
    "Música fuerte a las 3 AM",
    "Mi vecino pone música a volumen muy alto...",
    "Avenida Principal 123",
    usuarioReportante
);
```

### ObtenerConflictosUseCase
Obtiene conflictos con opciones de filtrado.

```java
List<Conflicto> conflictos = obtenerConflictosUseCase.obtenerPorEstado(estadoId);
List<Conflicto> prioridad = obtenerConflictosUseCase.obtenerPorPrioridad();
```

### ActualizarEstadoConflictoUseCase
Actualiza el estado de un conflicto.

```java
Conflicto actualizado = actualizarEst adoptoUseCase.ejecutar(
    conflictoId,
    nuevoEstado,
    "Observación: mediación en progreso"
);
```

### AsignarMediacionUseCase
Asigna un mediador a un conflicto.

```java
Mediacion mediacion = asignarMediacionUseCase.ejecutar(conflicto, mediador);
```

---

## 🌐 Endpoints REST

### Conflictos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/conflictos` | Obtener todos los conflictos |
| GET | `/api/conflictos/{id}` | Obtener un conflicto específico |
| POST | `/api/conflictos` | Crear nuevo conflicto |
| PUT | `/api/conflictos/{id}` | Actualizar conflicto |
| DELETE | `/api/conflictos/{id}` | Eliminar conflicto |
| GET | `/api/conflictos/por-estado/{estadoId}` | Obtener por estado |
| GET | `/api/conflictos/por-prioridad` | Obtener ordenados por prioridad |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/usuarios` | Obtener todos los usuarios |
| GET | `/api/usuarios/{id}` | Obtener usuario específico |
| POST | `/api/usuarios` | Crear nuevo usuario |
| PUT | `/api/usuarios/{id}` | Actualizar usuario |
| DELETE | `/api/usuarios/{id}` | Eliminar usuario |
| GET | `/api/usuarios/email/{email}` | Buscar por email |

---

## 🗄️ Base de Datos

### Tablas

1. **usuarios**: Registra usuarios del sistema
2. **perfiles**: Define roles (ciudadano, mediador, administrador)
3. **conflictos**: Registro de conflictos reportados
4. **tipos_conflicto**: Categorías de conflictos
5. **estados_conflicto**: Estados posibles de conflictos
6. **mediaciones**: Proceso de resolución de conflictos

### Script SQL (PostgreSQL)

```sql
CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    numero_documento VARCHAR(20) UNIQUE NOT NULL,
    perfil_id BIGINT,
    fecha_creacion TIMESTAMP NOT NULL,
    fecha_actualizacion TIMESTAMP,
    activo BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE conflictos (
    id BIGSERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    usuario_reportante_id BIGINT NOT NULL,
    usuario_involucrado_id BIGINT,
    tipo_conflicto_id BIGINT,
    estado_conflicto_id BIGINT,
    fecha_reporte TIMESTAMP NOT NULL,
    fecha_actualizacion TIMESTAMP,
    observaciones TEXT,
    prioridad INTEGER NOT NULL,
    FOREIGN KEY (usuario_reportante_id) REFERENCES usuarios(id)
);

-- Ver archivo completo en src/main/resources/
```

---

## ⚙️ Configuración

### application.yml

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/conciliaya_db
    username: postgres
    password: password

fastapi:
  url: http://localhost:8000
  classifier-endpoint: /api/v1/classify-conflict
  timeout: 5000
```

---

## 🧪 Validaciones

### A nivel controllers (anotaciones)
- `@NotBlank`: Campo obligatorio no vacío
- `@Email`: Formato de email válido
- `@Size`: Tamaño mínimo y máximo
- `@Min`, `@Max`: Valores numéricos
- `@Valid`: Validación recursiva

### A nivel dominio (lógica de negocio)
- Validación de transiciones de estado
- Cálculo de prioridades
- Restricciones de negocio

---

## 🛡️ Manejo de Errores

### Excepciones Personalizadas

- `ConciliaYaException`: Base para todas las excepciones
- `RecursoNoEncontradoException`: Recurso no existe (404)
- `ErrorValidacionException`: Datos inválidos (400)
- `ViolacionReglaNegocios`: Violación de reglas (409)
- `IntegracionExternaException`: Error con servicio externo (503)

### GlobalExceptionHandler

Centraliza el manejo de excepciones y proporciona respuestas coherentes:

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    // Maneja todas las excepciones
}
```

---

## 💻 Cómo Ejecutar

### Requisitos
- Java 17+
- Maven 3.8+
- PostgreSQL 13+ o MySQL 8+

### Pasos

1. **Clonar repositorio**
```bash
git clone <url-repo>
cd conciliaya-backend
```

2. **Configurar base de datos**
```bash
# PostgreSQL
createdb conciliaya_db
psql -U postgres -d conciliaya_db < src/main/resources/schema.sql
```

3. **Instalar dependencias**
```bash
mvn clean install
```

4. **Ejecutar aplicación**
```bash
mvn spring-boot:run
```

5. **API disponible en**
```
http://localhost:8080/api/swagger-ui.html
```

---

## 📊 Flujo de Uso Típico

1. **Usuario reporta conflict**
   - POST `/api/conflictos`
   - Descripción se envía a clasificador Python
   - Tipo se asigna automáticamente

2. **Listar conflictos**
   - GET `/api/conflictos`
   - Filtrar por estado, tipo, prioridad

3. **Asignar mediador**
   - POST `/api/mediaciones`
   - Enlazar conflicto con mediador

4. **Actualizar estado**
   - PUT `/api/conflictos/{id}`
   - Cambiar estado del conflicto

5. **Registrar resultado**
   - PUT `/api/mediaciones/{id}`
   - Completar mediación con acuerdos

---

## 🔍 Principios SOLID Aplicados

- **S**ingle Responsibility: Cada clase tiene una sola responsabilidad
- **O**pen/Closed: Abierto para extensión, cerrado para modificación
- **L**iskov Substitution: Las subclases pueden substituir la clase base
- **I**nterface Segregation: Interfaces específicas, no genéricas
- **D**ependency Inversion: Depender de abstracciones, no de implementaciones

---

## 🎯 Principios de Clean Code

- Nombres claros y descriptivos
- Métodos pequeños enfocados
- Funciones puras sin efectos secundarios
- Comentarios JavaDoc en clases públicas
- Sin lógica de negocio en controllers

---

## 🚀 Próximos Pasos

- [ ] Autenticación y autorización (Spring Security)
- [ ] Paginación de resultados
- [ ] Búsqueda avanzada
- [ ] Reportes y estadísticas
- [ ] Notificaciones por email
- [ ] Frontend React
- [ ] Tests unitarios e integración
- [ ] Docker y deployment

---

## 📚 Referencias

- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

---

## 📞 Contacto

Para preguntas o sugerencias sobre el backend, contacte al equipo de desarrollo.

---

**Versión**: 1.0.0  
**Última actualización**: Marzo 2024  
**Autor**: ConciliaYa Team
