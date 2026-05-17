# Simple Spring Boot + MySQL Database Design

Este proyecto contiene un diseño de base de datos sencillo para MySQL y una estructura básica de Spring Boot para manejar:

- `TipoConflicto`
- `Perfil`
- `Usuario`
- `EstadoConflicto`
- `Conflicto`
- `Mediacion`

## Objetivo

Crear un diseño simple y limpio, con relaciones bien definidas y un API REST CRUD fácil de mantener.

## Modelo relacional

Tablas principales:

- `tipo_conflicto`
- `perfil`
- `estado_conflicto`
- `usuario`
- `conflicto`
- `mediacion`

Relaciones clave:

- `usuario.perfil_id` → `perfil.id`
- `conflicto.usuario_demandante_id` → `usuario.id`
- `conflicto.usuario_demandado_id` → `usuario.id`
- `conflicto.tipo_conflicto_id` → `tipo_conflicto.id`
- `conflicto.estado_conflicto_id` → `estado_conflicto.id`
- `mediacion.conflicto_id` → `conflicto.id`
- `mediacion.usuario_mediador_id` → `usuario.id`
- `mediacion.estado_conflicto_id` → `estado_conflicto.id`

## Archivos importantes

- `schema.sql` → script SQL completo con tablas y datos de ejemplo.
- `pom.xml` → configuración mínima de Spring Boot.
- `src/main/java/com/example/demo/model/` → entidades JPA.
- `src/main/java/com/example/demo/repository/` → repositorios Spring Data.
- `src/main/java/com/example/demo/controller/` → controladores REST CRUD.

## Cómo usar

1. Crear la base de datos en MySQL con `schema.sql`.
2. Ajustar `src/main/resources/application.properties` con el usuario y contraseña de MySQL.
3. Ejecutar la aplicación Spring Boot.

## API REST de ejemplo

- `GET /api/usuarios`
- `GET /api/usuarios/{id}`
- `POST /api/usuarios`
- `PUT /api/usuarios/{id}`
- `DELETE /api/usuarios/{id}`

- `GET /api/conflictos`
- `GET /api/conflictos/{id}`
- `POST /api/conflictos`
- `PUT /api/conflictos/{id}`
- `DELETE /api/conflictos/{id}`

- `GET /api/mediaciones`
- `GET /api/mediaciones/{id}`
- `POST /api/mediaciones`
- `PUT /api/mediaciones/{id}`
- `DELETE /api/mediaciones/{id}`
