-- ============================================================================
-- Script de Base de Datos - ConciliaYa
-- ============================================================================
-- Descripción: Creación de tablas y datos iniciales para ConciliaYa
-- Compatible: PostgreSQL 14+ y MySQL 8.0+
-- Última actualización: Diciembre 2024
-- ============================================================================

-- ============================================================================
-- TABLA: perfiles
-- Descripción: Define los roles/perfiles disponibles en el sistema
-- ============================================================================
CREATE TABLE IF NOT EXISTS perfiles (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(500),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- TABLA: usuarios
-- Descripción: Almacena información de todos los usuarios del sistema
-- ============================================================================
CREATE TABLE IF NOT EXISTS usuarios (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    perfil_id BIGINT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (perfil_id) REFERENCES perfiles(id),
    INDEX idx_email (email),
    INDEX idx_documento (numero_documento),
    INDEX idx_activo (activo)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- TABLA: tipos_conflicto
-- Descripción: Categorías de conflictos disponibles
-- ============================================================================
CREATE TABLE IF NOT EXISTS tipos_conflicto (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(500),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_nombre (nombre),
    INDEX idx_activo (activo)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- TABLA: estados_conflicto
-- Descripción: Define los estados posibles de un conflicto
-- ============================================================================
CREATE TABLE IF NOT EXISTS estados_conflicto (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(500),
    orden INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_nombre (nombre),
    INDEX idx_orden (orden)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- TABLA: conflictos
-- Descripción: Registro de todos los conflictos reportados
-- ============================================================================
CREATE TABLE IF NOT EXISTS conflictos (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(2000) NOT NULL,
    ubicacion VARCHAR(500),
    prioridad INT DEFAULT 1 CHECK (prioridad >= 1 AND prioridad <= 5),
    usuario_reportante_id BIGINT NOT NULL,
    tipo_conflicto_id BIGINT NOT NULL,
    estado_conflicto_id BIGINT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_reportante_id) REFERENCES usuarios(id),
    FOREIGN KEY (tipo_conflicto_id) REFERENCES tipos_conflicto(id),
    FOREIGN KEY (estado_conflicto_id) REFERENCES estados_conflicto(id),
    INDEX idx_estado (estado_conflicto_id),
    INDEX idx_tipo (tipo_conflicto_id),
    INDEX idx_usuario (usuario_reportante_id),
    INDEX idx_prioridad (prioridad),
    INDEX idx_fecha_creacion (fecha_creacion)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- TABLA: mediaciones
-- Descripción: Registro de mediaciones asignadas a conflictos
-- ============================================================================
CREATE TABLE IF NOT EXISTS mediaciones (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    conflicto_id BIGINT NOT NULL,
    mediador_id BIGINT NOT NULL,
    observaciones VARCHAR(2000),
    completada BOOLEAN NOT NULL DEFAULT FALSE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (conflicto_id) REFERENCES conflictos(id),
    FOREIGN KEY (mediador_id) REFERENCES usuarios(id),
    INDEX idx_conflicto (conflicto_id),
    INDEX idx_mediador (mediador_id),
    INDEX idx_completada (completada),
    UNIQUE KEY unique_mediation_per_conflict (conflicto_id, mediador_id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================================
-- DATOS INICIALES
-- ============================================================================

-- Insertar Perfiles (Roles)
INSERT INTO perfiles (nombre, descripcion, activo) VALUES
('REPORTERO', 'Usuario que reporta conflictos', TRUE),
('MEDIADOR', 'Usuario que realiza la mediación de conflictos', TRUE),
('ADMINISTRADOR', 'Usuario administrador del sistema', TRUE),
('AUDITOR', 'Usuario auditor para monitoreo', TRUE)
ON DUPLICATE KEY UPDATE activo = VALUES(activo);

-- Insertar Estados de Conflicto (Workflow)
INSERT INTO estados_conflicto (nombre, descripcion, orden) VALUES
('REPORTADO', 'Conflicto recién reportado', 1),
('CLASIFICADO', 'Conflicto clasificado automáticamente', 2),
('EN_MEDIACION', 'Mediador asignado, mediación en proceso', 3),
('RESUELTO', 'Conflicto resuelto exitosamente', 4),
('ESCALADO', 'Conflicto escalado a autoridades', 5),
('CERRADO', 'Conflicto cerrado', 6)
ON DUPLICATE KEY UPDATE orden = VALUES(orden);

-- Insertar Tipos de Conflicto (Categorías)
INSERT INTO tipos_conflicto (nombre, descripcion, activo) VALUES
('RUIDO', 'Conflictos por ruido excesivo o música', TRUE),
('DAÑO_PROPIEDAD', 'Daño a propiedad ajena', TRUE),
('LÍMITES_TERRENO', 'Disputas por límites de terreno o propiedad', TRUE),
('SERVICIOS', 'Conflictos por servicios básicos (agua, electricidad)', TRUE),
('CONVIVENCIA', 'Problemas de convivencia y comportamiento', TRUE),
('ESTACIONAMIENTO', 'Conflictos por estacionamiento', TRUE),
('MASCOTAS', 'Conflictos relacionados con mascotas', TRUE),
('OTROS', 'Otros tipos de conflictos', TRUE)
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

-- Insertar Usuarios Iniciales (Mediadores y Administrador)
-- Contraseña de ejemplo: se debe cambiar en producción
INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id) 
SELECT 'Sistema', 'Administrador', 'admin@conciliaya.com', 'ADMIN001', '+34-900-000-000', TRUE, 
       (SELECT id FROM perfiles WHERE nombre = 'ADMINISTRADOR' LIMIT 1)
WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE email = 'admin@conciliaya.com');

INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id)
SELECT 'María', 'García', 'maria.garcia@conciliaya.com', 'MG001', '+34-901-111-111', TRUE,
       (SELECT id FROM perfiles WHERE nombre = 'MEDIADOR' LIMIT 1)
WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE email = 'maria.garcia@conciliaya.com');

INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id)
SELECT 'Juan', 'López', 'juan.lopez@conciliaya.com', 'JL001', '+34-902-222-222', TRUE,
       (SELECT id FROM perfiles WHERE nombre = 'MEDIADOR' LIMIT 1)
WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE email = 'juan.lopez@conciliaya.com');

INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id)
SELECT 'Carlos', 'Rodríguez', 'carlos.rodriguez@conciliaya.com', 'CR001', '+34-903-333-333', TRUE,
       (SELECT id FROM perfiles WHERE nombre = 'MEDIADOR' LIMIT 1)
WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE email = 'carlos.rodriguez@conciliaya.com');

-- ============================================================================
-- VISTAS ÚTILES (Opcional)
-- ============================================================================

-- Vista para consultar conflictos con información detallada
DROP VIEW IF EXISTS vista_conflictos_detalle;
CREATE VIEW vista_conflictos_detalle AS
SELECT 
    c.id,
    c.descripcion,
    c.ubicacion,
    c.prioridad,
    CONCAT(u.nombre, ' ', u.apellido) AS reportero,
    u.email AS email_reportero,
    tc.nombre AS tipo_conflicto,
    ec.nombre AS estado_conflicto,
    c.fecha_creacion,
    c.fecha_actualizacion
FROM conflictos c
JOIN usuarios u ON c.usuario_reportante_id = u.id
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id;

-- Vista para consultar mediaciones activas
DROP VIEW IF EXISTS vista_mediaciones_activas;
CREATE VIEW vista_mediaciones_activas AS
SELECT 
    m.id,
    c.descripcion AS conflicto,
    CONCAT(med.nombre, ' ', med.apellido) AS mediador,
    med.email AS email_mediador,
    tc.nombre AS tipo_conflicto,
    m.fecha_creacion,
    m.observaciones
FROM mediaciones m
JOIN conflictos c ON m.conflicto_id = c.id
JOIN usuarios med ON m.mediador_id = med.id
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
WHERE m.completada = FALSE;

-- Vista para estadísticas
DROP VIEW IF EXISTS vista_estadisticas_conflictos;
CREATE VIEW vista_estadisticas_conflictos AS
SELECT 
    tc.nombre AS tipo_conflicto,
    COUNT(*) AS total_conflictos,
    SUM(CASE WHEN ec.nombre = 'RESUELTO' THEN 1 ELSE 0 END) AS resueltos,
    SUM(CASE WHEN ec.nombre IN ('REPORTADO', 'CLASIFICADO') THEN 1 ELSE 0 END) AS pendientes,
    AVG(c.prioridad) AS promedio_prioridad,
    MAX(c.fecha_creacion) AS ultimo_conflicto
FROM conflictos c
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id
GROUP BY tc.id, tc.nombre;

-- ============================================================================
-- ÍNDICES ADICIONALES PARA OPTIMIZACIÓN
-- ============================================================================

-- Para búsquedas frecuentes
CREATE INDEX idx_conflictos_estado_prioridad ON conflictos(estado_conflicto_id, prioridad);
CREATE INDEX idx_conflictos_reportante_estado ON conflictos(usuario_reportante_id, estado_conflicto_id);
CREATE INDEX idx_mediaciones_activas ON mediaciones(conflicto_id, completada);

-- Para análisis
CREATE INDEX idx_conflictos_fecha_tipo ON conflictos(tipo_conflicto_id, fecha_creacion);

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================
-- Notas:
-- 1. Este script crea la estructura base de la base de datos
-- 2. Las credenciales por defecto deben ser cambiadas en producción
-- 3. Se incluyen vistas y índices para optimización
-- 4. Compatible con PostgreSQL y MySQL
-- 5. Para PostgreSQL, cambiar: AUTO_INCREMENT por SERIAL, ON UPDATE por triggers
-- ============================================================================
