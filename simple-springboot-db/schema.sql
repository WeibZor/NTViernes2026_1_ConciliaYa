-- ============================================================
-- ConciliaYa - Schema actualizado para Spring Boot
-- Compatible con simple-springboot-db
-- ============================================================

CREATE DATABASE IF NOT EXISTS conciliadb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE conciliadb;

-- Perfiles
CREATE TABLE IF NOT EXISTS perfil (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL,
  descripcion VARCHAR(300),
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  fecha_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Usuarios (con password para auth JWT)
CREATE TABLE IF NOT EXISTS usuario (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  tipo_documento VARCHAR(20),
  documento VARCHAR(60),
  correo VARCHAR(120) NOT NULL UNIQUE,
  password VARCHAR(255),
  telefono VARCHAR(30),
  perfil_id BIGINT,
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  fecha_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_usuario_perfil FOREIGN KEY (perfil_id) REFERENCES perfil(id)
);

-- Tipos de conflicto
CREATE TABLE IF NOT EXISTS tipo_conflicto (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(300),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Estados de conflicto
CREATE TABLE IF NOT EXISTS estado_conflicto (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL,
  codigo VARCHAR(30) NOT NULL,
  descripcion VARCHAR(300),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Conflictos
CREATE TABLE IF NOT EXISTS conflicto (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  usuario_demandante_id BIGINT NOT NULL,
  usuario_demandado_id BIGINT NOT NULL,
  tipo_conflicto_id BIGINT NOT NULL,
  estado_conflicto_id BIGINT NOT NULL,
  asunto VARCHAR(200) NOT NULL,
  descripcion VARCHAR(1000),
  fecha_inicio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_cierre DATETIME,
  resultado VARCHAR(200),
  monto_reclamado DOUBLE,
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  fecha_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_conflicto_demandante FOREIGN KEY (usuario_demandante_id) REFERENCES usuario(id),
  CONSTRAINT fk_conflicto_demandado FOREIGN KEY (usuario_demandado_id) REFERENCES usuario(id),
  CONSTRAINT fk_conflicto_tipo FOREIGN KEY (tipo_conflicto_id) REFERENCES tipo_conflicto(id),
  CONSTRAINT fk_conflicto_estado FOREIGN KEY (estado_conflicto_id) REFERENCES estado_conflicto(id)
);

-- Mediaciones
CREATE TABLE IF NOT EXISTS mediacion (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  conflicto_id BIGINT NOT NULL,
  usuario_mediador_id BIGINT NOT NULL,
  estado_conflicto_id BIGINT NOT NULL,
  fecha_programada DATETIME,
  lugar VARCHAR(200),
  observaciones VARCHAR(1000),
  resultado VARCHAR(200),
  fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  activo BOOLEAN NOT NULL DEFAULT TRUE,
  CONSTRAINT fk_mediacion_conflicto FOREIGN KEY (conflicto_id) REFERENCES conflicto(id),
  CONSTRAINT fk_mediacion_mediador FOREIGN KEY (usuario_mediador_id) REFERENCES usuario(id),
  CONSTRAINT fk_mediacion_estado FOREIGN KEY (estado_conflicto_id) REFERENCES estado_conflicto(id)
);

-- Publicaciones
CREATE TABLE IF NOT EXISTS publicacion (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT NOT NULL,
  contenido VARCHAR(2000),
  imagen VARCHAR(255),
  fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_publicacion_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- Notificaciones
CREATE TABLE IF NOT EXISTS notificacion (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT NOT NULL,
  mensaje VARCHAR(1000),
  leida BOOLEAN NOT NULL DEFAULT FALSE,
  fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_notificacion_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- Datos iniciales de perfiles
INSERT IGNORE INTO perfil (id, nombre, descripcion, activo) VALUES
  (1, 'Administrador', 'Acceso total al sistema', TRUE),
  (2, 'Mediador', 'Puede gestionar mediaciones', TRUE),
  (3, 'Usuario', 'Usuario regular del sistema', TRUE);

-- Datos iniciales de estados
INSERT IGNORE INTO estado_conflicto (id, nombre, codigo, descripcion, activo) VALUES
  (1, 'Abierto', 'ABIERTO', 'Conflicto recién registrado', TRUE),
  (2, 'En mediación', 'EN_MEDIACION', 'Proceso de mediación en curso', TRUE),
  (3, 'Resuelto', 'RESUELTO', 'Conflicto resuelto satisfactoriamente', TRUE),
  (4, 'Cerrado', 'CERRADO', 'Conflicto cerrado sin acuerdo', TRUE);

-- Datos iniciales de tipos
INSERT IGNORE INTO tipo_conflicto (id, nombre, descripcion, activo) VALUES
  (1, 'Laboral', 'Conflictos relacionados con el trabajo', TRUE),
  (2, 'Familiar', 'Conflictos de índole familiar', TRUE),
  (3, 'Comercial', 'Disputas comerciales o contractuales', TRUE),
  (4, 'Vecinal', 'Conflictos entre vecinos o comunidades', TRUE);
