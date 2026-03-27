# 🏗️ Arquitectura Detallada de ConciliaYa

Documento técnico que describe la arquitectura completa de ConciliaYa, sus patrones de diseño, y decisiones arquitectónicas.

---

## 📐 Diagrama de Arquitectura Hexagonal (Ports & Adapters)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          CAPA DE ENTRADA (Controllers)                  │
│  ┌─────────────────────┐  ┌──────────────────┐  ┌───────────────────┐   │
│  │ ConflictoController │  │ UsuarioController│  │ MediacionController│   │
│  └──────────┬──────────┘  └────────┬─────────┘  └────────┬──────────┘   │
└─────────────┼──────────────────────┼─────────────────────┼───────────────┘
              │                      │                     │
              │  Casos de Uso (Pure) │                     │
┌─────────────▼──────────────────────▼─────────────────────▼───────────────┐
│                           CAPA DE DOMINIO                                │
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │                     Business Logic (Pure)                        │    │
│  │  ┌────────────────────┐  ┌──────────────────┐  ┌─────────────┐  │    │
│  │  │CrearConflictoUseCase│ │ObtenerConflictos │ │ActualizarEst│  │    │
│  │  └────────────────────┘  │     UseCase      │ │adoUseCase   │  │    │
│  │                          └──────────────────┘  └─────────────┘  │    │
│  │  ┌────────────────────┐                                      │    │
│  │  │AsignarMediacionCase│                                      │    │
│  │  └────────────────────┘                                      │    │
│  │                                                              │    │
│  │  • Validation Business Rules                               │    │
│  │  • Domain Entities (Usuario, Conflicto, Mediacion, etc.)   │    │
│  │  • Port Interfaces (Contracts)                             │    │
│  └──────────────────────────────────────────────────────────────────┘    │
└─────────────┬──────────────────────┬─────────────┬─────────────────────────┘
              │                      │             │
        PUERTO REPO            PUERTO REPO   PUERTO EXTERNA
              │                      │             │
┌─────────────▼─────────────┬────────▼──────┬────┼──────────────────────────┐
│   CAPA DE INFRAESTRUCTURA  │               │    │                         │
│ ┌───────────────────────┐  │  ┌──────────┐│    │ ┌──────────────────┐   │
│ │ Adaptador de BD       │  │  │DTO       ││    │ │HttpClientAdapter │   │
│ │ (RepositoriesAdapters)│  │  │Validator ││    │ │(Clasificador)    │   │
│ │                       │  │  │          ││    │ │                  │   │
│ │ • JPA Entities        │  │  └──────────┘│    │ │ WebClient Config │   │
│ │ • Spring Repositories │  │              │    │ │                  │   │
│ │ • Hibernate           │  │              │    │ └────────┬─────────┘   │
│ └──────────┬────────────┘  │              │    │          │             │
└───────────┬┴──────────────┬─┘              │    └──────────┼─────────────┘
            │               │               │               │
            │               │               │               │
┌───────────▼───┐  ┌────────▼──────┐   ┌────────────────────▼─────┐
│  PostgreSQL/  │  │   Exception   │   │   FastAPI Microservice   │
│    MySQL DB   │  │    Handler    │   │   (Clasificador)         │
│               │  │               │   │                          │
│  6 Tables     │  │ • Global      │   │ • Pure Functions         │
│  (usuarios,   │  │   Exception   │   │ • 8 Conflict Types       │
│   conflictos, │  │   Handler     │   │ • Classification Logic   │
│   mediaciones)│  │ • HTTP Status │   │ • Swagger UI             │
└───────────────┘  │   Codes       │   └──────────────────────────┘
                   │ • JSON Format │
                   └───────────────┘
```

---

## 📦 Estructura de Paquetes

```
com.conciliaya/
│
├── domain/                           # ⭐ CAPA DE DOMINIO (Núcleo)
│   ├── entity/
│   │   ├── Usuario.java              # Entidad sin dependencias externas
│   │   ├── Conflicto.java            # Lógica de validación pura
│   │   ├── Mediacion.java            # Métodos de negocio
│   │   ├── TipoConflicto.java
│   │   ├── EstadoConflicto.java
│   │   └── Perfil.java
│   │
│   ├── ports/                        # 🔌 Puertos (Contracts)
│   │   ├── UsuarioRepositoryPort.java        # ContratoBD para Usuario
│   │   ├── ConflictoRepositoryPort.java      # ContratoBD para Conflicto
│   │   ├── MediacionRepositoryPort.java      # ContratoBD para Mediacion
│   │   └── ClasificadorConflictoPort.java    # ContratoAPI externa
│   │
│   └── usecase/                      # 💼 Casos de Uso (Lógica Principal)
│       ├── CrearConflictoUseCase.java        # Crear + Clasificar automático
│       ├── ObtenerConflictosUseCase.java     # Listar con filtros
│       ├── ActualizarEstadoConflictoUseCase.java # Cambiar estado
│       └── AsignarMediacionUseCase.java      # Asignar mediador
│
├── application/                      # 🌐 CAPA DE APLICACIÓN
│   ├── dto/                          # Data Transfer Objects
│   │   ├── UsuarioDTO.java           # Request validation
│   │   ├── ConflictoDTO.java         # Request validation
│   │   ├── MediacionDTO.java         # Request validation
│   │   ├── UsuarioResponseDTO.java   # Response format
│   │   ├── ConflictoResponseDTO.java # Response format
│   │   └── ApiResponse.java          # Respuesta genérica
│   │
│   ├── exception/                    # Excepciones Personalizadas
│   │   ├── ConciliaYaException.java           # Excepción base
│   │   ├── RecursoNoEncontradoException.java  # 404
│   │   ├── ErrorValidacionException.java      # 400
│   │   ├── ViolacionReglaNegocios.java        # 422
│   │   ├── IntegracionExternaException.java   # 503
│   │   └── GlobalExceptionHandler.java        # Capturador global
│   │
│   └── controller/                   # REST Controllers
│       ├── ConflictoController.java   # 7 endpoints
│       └── UsuarioController.java     # 6 endpoints
│
└── infrastructure/                   # 🔧 CAPA DE INFRAESTRUCTURA
    └── adapter/
        ├── output/
        │   ├── persistence/
        │   │   ├── jpa/
        │   │   │   ├── UsuarioEntity.java
        │   │   │   ├── ConflictoEntity.java
        │   │   │   ├── MediacionEntity.java
        │   │   │   ├── TipoConflictoEntity.java
        │   │   │   ├── EstadoConflictoEntity.java
        │   │   │   └── PerfilEntity.java
        │   │   │
        │   │   ├── repository/
        │   │   │   ├── UsuarioJpaRepository.java    # Spring Data
        │   │   │   ├── ConflictoJpaRepository.java  # Spring Data
        │   │   │   └── MediacionJpaRepository.java  # Spring Data
        │   │   │
        │   │   └── adapter/
        │   │       ├── UsuarioRepositoryAdapter.java    # 💻 Implementa puerto
        │   │       ├── ConflictoRepositoryAdapter.java  # 💻 Implementa puerto
        │   │       └── MediacionRepositoryAdapter.java  # 💻 Implementa puerto
        │   │
        │   └── http/
        │       ├── client/
        │       │   └── ClasificadorConflictoAdapter.java  # 💻 Implementa puerto
        │       │
        │       └── config/
        │           └── WebClientConfig.java    # Configuración HTTP
        │
        └── input/
            └── controller/  # → Ya cubierto arriba
```

---

## 🔄 Flujos de Datos Principales

### Flujo 1: Crear Conflicto (POST /api/conflictos)

```
Usuario Frontend
    ↓
  [React Form]
    ↓ (Validación HTML5)
    ↓ (Datos JSON)
    ↓
[ConflictoController]
    ↓ (HTTP POST)
    ↓ (DTOs con @Valid)
    ↓
[CrearConflictoUseCase.ejecutar()]
    ├─ Validar descripción (mín. 10 caracteres)
    ├─ Validar usuario reportante existe
    ├─ Crear entidad Conflicto (dominio)
    ├─ Llamar ClasificadorConflictoPort
    │  └─ [ClasificadorConflictoAdapter]
    │     └─ WebClient HTTP POST a FastAPI
    │        ↓
    │     [FastAPI Microservice]
    │        ├─ Normalizar texto
    │        ├─ Contar palabras clave
    │        ├─ Calcular confianza
    │        ├─ Generar justificación
    │        └─ Retornar clasificación
    │  ←─ [Respuesta clasificación]
    │
    ├─ Asignar tipo conflicto (automático)
    ├─ Asignar estado = CLASIFICADO
    ├─ Guardar en BD (ConflictoRepositoryPort)
    │  └─ [ConflictoRepositoryAdapter]
    │     └─ [ConflictoJpaRepository]
    │        └─ [JPA → Database]
    │
    ├─ Obtener mediador disponible
    ├─ Crear mediación automática
    └─ Retornar ConflictoResponseDTO

[GlobalExceptionHandler]
    (Captura excepciones)
    └─ Mapea a HTTP Status Code
    └─ Retorna error JSON

←─ [Frontend]
    ├─ Muestra Toast (éxito/error)
    └─ Redirige a /conflictos
```

### Flujo 2: Obtener Conflictos (GET /api/conflictos)

```
Usuario → [Homepage]
    ↓
[ConflictoController.obtenerTodos()]
    ↓
[ObtenerConflictosUseCase.ejecutar()]
    ├─ ConflictoRepositoryPort.findAll()
    │  └─ [ConflictoRepositoryAdapter]
    │     └─ [ConflictoJpaRepository.findAll()]
    │        └─ [JPA → Database]
    │           ← [List<ConflictoEntity>]
    │
    ├─ Convertir a List<Conflicto> (dominio)
    │  (Usar Streams: .map().collect())
    │
    ├─ Filtrar por criterios (opcional)
    │  ├─ Por estado (filter()
    │  ├─ Por tipo
    │  └─ Por prioridad
    │
    └─ Retornar List<ConflictoResponseDTO>

←─ [Frontend]
    ├─ Itera sobre list
    ├─ Mapea a ConflictoCard component
    └─ Renderiza en grid
```

### Flujo 3: Actualizar Estado (PUT /api/conflictos/{id})

```
Usuario → [Ver Conflicto] → [Cambiar Estado]
    ↓
[ConflictoController.actualizarConflicto()]
    ↓ (DTOs validados)
    ↓
[ActualizarEstadoConflictoUseCase.ejecutar()]
    ├─ Obtener conflicto por ID
    │  └─ ConflictoRepositoryPort.findById()
    │
    ├─ Validar transición de estado
    │  ├─ REPORTADO → CLASIFICADO ✓
    │  ├─ CLASIFICADO → EN_MEDIACION ✓
    │  ├─ EN_MEDIACION → RESUELTO ✓
    │  ├─ O → ESCALADO ✓
    │  └─ Otro → ERROR ✗
    │
    ├─ Actualizar estado
    ├─ Guardar observaciones (si aplica)
    ├─ Guardar en BD
    │  └─ ConflictoRepositoryPort.save()
    │
    └─ Retornar confirmación

←─ [Frontend]
    └─ Actualiza UI + Toast
```

---

## 🎯 Patrones de Diseño Utilizados

### 1. Hexagonal (Ports & Adapters)
**Ubicación**: Domain ↔ Infrastructure

```java
// PUERTO (Contrato - Domain)
public interface UsuarioRepositoryPort {
    Usuario save(Usuario usuario);
    Optional<Usuario> findById(Long id);
    // ...
}

// ADAPTADOR (Implementación - Infrastructure)
@Component
class UsuarioRepositoryAdapter implements UsuarioRepositoryPort {
    @Autowired
    private UsuarioJpaRepository jpaRepository;
    
    @Override
    public Usuario save(Usuario usuario) {
        UsuarioEntity entity = mapper.toEntity(usuario);
        UsuarioEntity saved = jpaRepository.save(entity);
        return mapper.toDomain(saved);
    }
}
```

### 2. Repository Pattern
**Ubicación**: Infrastructure/persistence

```java
// Spring Data JPA (Repositorio técnico)
public interface UsuarioJpaRepository extends JpaRepository<UsuarioEntity, Long> {
    List<UsuarioEntity> findByActivoTrue();
    Optional<UsuarioEntity> findByEmail(String email);
}

// Adaptador de Dominio (Repositorio de negocio)
class UsuarioRepositoryAdapter implements UsuarioRepositoryPort {
    // Implementa métodos de negocio
}
```

### 3. DTO Pattern (Data Transfer Objects)
**Ubicación**: Application/dto

```java
// INPUT DTO (Validación)
@Data
public class ConflictoDTO {
    @NotBlank(message = "La descripción es requerida")
    @Size(min = 10, message = "Mínimo 10 caracteres")
    private String descripcion;
    
    @Min(1) @Max(5)
    private Integer prioridad;
}

// OUTPUT DTO (Respuesta)
@Data
public class ConflictoResponseDTO {
    private Long id;
    private String descripcion;
    private TipoConflictoDTO tipo;
    private EstadoConflictoDTO estado;
    // ...
}
```

### 4. Use Case Pattern (Application Service)
**Ubicación**: Domain/usecase

```java
@Component
public class CrearConflictoUseCase {
    private final ConflictoRepositoryPort repository;
    private final ClasificadorConflictoPort clasificador;
    
    public Conflicto ejecutar(String descripcion, /* ... */) {
        // Lógica pura sin dependencias de Spring
        validar(descripcion);
        Conflicto conflicto = new Conflicto(/* ... */);
        ClasificacionResponse clasificacion = clasificador.clasificar(descripcion);
        conflicto.asignarTipo(clasificacion.getTipo());
        return repository.save(conflicto);
    }
}
```

### 5. Global Exception Handler (Centralized Error Handling)
**Ubicación**: Application/exception

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(RecursoNoEncontradoException.class)
    public ResponseEntity<ApiResponse<Void>> handleNotFound(RecursoNoEncontradoException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(ApiResponse.error(ex.getMessage()));
    }
    
    @ExceptionHandler(ErrorValidacionException.class)
    public ResponseEntity<ApiResponse<Map<String, Object>>> handleValidation(
        ErrorValidacionException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
            .body(ApiResponse.error(ex.getErrores()));
    }
}
```

---

## 🎨 Principios SOLID Aplicados

### S - Single Responsibility Principle
```java
// ❌ MAL: Una clase con múltiples responsabilidades
class ConflictoService {
    void crearConflicto() { }          // Crear
    void guardarEnBD() { }              // Persistencia
    void enviarEmail() { }              // Notificación
    void clasificar() { }               // Clasificación
}

// ✅ BIEN: Cada clase con una responsabilidad
class CrearConflictoUseCase { }        // Crear
class ConflictoRepositoryPort { }      // Persistencia
class EmailService { }                  // Notificación
class ClasificadorConflictoPort { }    // Clasificación
```

### O - Open/Closed Principle
```java
// ❌ MAL: Cerrado a extensión
if (tipoConflicto.equals("RUIDO")) {
    clasificacion = "Ruido";
} else if (tipoConflicto.equals("DAÑO")) {
    clasificacion = "Daño Propiedad";
}

// ✅ BIEN: Abierto a extensión
interface ClasificadorConflictoPort {
    ClasificacionResponse clasificar(String descripcion);
    // Nuevas implementaciones sin modificar código existente
}
```

### L - Liskov Substitution Principle
```java
// Todos los adaptadores pueden reemplazarse entre sí
RepositoryPort repo1 = new ConflictoRepositoryAdapter(jpaRepository);
RepositoryPort repo2 = new ConflictoRepositoryAdapterAlternative(mongoRepository);
// El código sigue funcionando sin cambios
```

### I - Interface Segregation Principle
```java
// ❌ MAL: Una interfaz para todo
interface RepositoryPort {
    save(T t);
    find(Long id);
    update(T t);
    delete(Long id);
    custom1();
    custom2();
}

// ✅ BIEN: Interfaces específicas
interface ReadRepository<T> {
    find(Long id);
}

interface WriteRepository<T> {
    save(T t);
    update(T t);
}
```

### D - Dependency Inversion Principle
```java
// ❌ MAL: Depende de implementación concreta
class ConflictoService {
    ConflictoJpaRepository repo = new ConflictoJpaRepository();
}

// ✅ BIEN: Depende de abstracción
class CrearConflictoUseCase {
    private final ConflictoRepositoryPort repository; // Abstracción
    
    public CrearConflictoUseCase(ConflictoRepositoryPort repository) {
        this.repository = repository; // Inyectado
    }
}
```

---

## 🧪 Principios Clean Code

### 1. Nombres Significativos
```java
// ❌ MAL
List<Usuario> u = getU();
Integer p = c.getP();

// ✅ BIEN
List<Usuario> usuariosActivos = obtenerUsuariosActivos();
Integer prioridadConflicto = conflicto.obtenerPrioridad();
```

### 2. Métodos Pequeños
```java
// ❌ MAL: Método muy largo
public void procesarConflicto() {
    // 50+ líneas de código
}

// ✅ BIEN: Métodos pequeños y enfocados
public void ejecutar() {
    validar();
    clasificar();
    guardar();
    notificar();
}
```

### 3. DRY (Don't Repeat Yourself)
```java
// ❌ MAL: Código repetido
if (conflicto.getDescripcion().length() < 10) throw new Exception();
if (usuario.getNombre().length() < 3) throw new Exception();

// ✅ BIEN: Método reutilizable
private void validarMinLength(String value, int min, String fieldName) {
    if (value.length() < min) 
        throw new ErrorValidacionException(fieldName + " muy corto");
}
```

### 4. Sin Efectos Secundarios
```java
// ❌ MAL: Función impura (modifica estado)
public boolean validar(Conflicto conflicto) {
    conflicto.setEstado(VALIDADO); // Efecto secundario
    return true;
}

// ✅ BIEN: Función pura (retorna resultado)
public boolean validar(Conflicto conflicto) {
    return conflicto.getDescripcion().length() >= 10;
}
```

---

## 🚀 Características Técnicas

| Aspecto | Implementación | Beneficio |
|--------|-----------------|-----------|
| **Arquitectura** | Hexagonal (Ports & Adapters) | Flexibilidad, Testabilidad |
| **ORM** | JPA/Hibernate | Portabilidad de BD |
| **API** | REST con JSON | Estándar industry, fácil integración |
| **Validación** | DTOs + Jakarta | Separación de concerns |
| **Persistencia** | Pattern Repository | Abstracción de acceso a datos |
| **Excepciones** | Jerarquía personalizada | Control granular de errores |
| **Logging** | SLF4J + Logback | Flexible, configurable |
| **HTTP Client** | Spring WebClient | No-bloqueante, moderno |
| **Testing** | Spring Boot Test | Fácil de testear |

---

## 📚 Layers Explanation

```
┌─────────────────────────────────────────────────────────┐
│ PRESENTATION (Controllers)                              │
│ Responsabilidad: Mapear HTTP requests/responses         │
│ Dependencias: DTO, Use Cases                            │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ DOMAIN (Use Cases, Entities, Ports)                    │
│ Responsabilidad: Lógica pura de negocio                │
│ Dependencias: NINGUNA a Spring o librerías externas    │
│ Nota: ⭐ NÚCLEO - No cambia por decisiones técnicas   │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ INFRASTRUCTURE (Adapters, Data Access)                  │
│ Responsabilidad: Implementar puertos, acceder BD/APIs  │
│ Dependencias: Spring, JPA, HTTP clients                │
│ Nota: Puede reemplazarse sin afectar dominio           │
└─────────────────────────────────────────────────────────┘
```

---

**Documento de Arquitectura v1.0**
Última actualización: Diciembre 2024
Autor: Equipo Técnico ConciliaYa
