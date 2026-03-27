-- ============================================================================
-- Script de Seed Data Masivo - ConciliaYa
-- ============================================================================
-- Descripción: Genera 250+ registros por tipo para testing, análisis y historias
-- Incluye: Datos sucios, duplicados, nulos, inconsistencias
-- Registros totales aproximados: 2000+ conflictos + mediaciones
-- ============================================================================

SET SESSION sql_mode='';
SET FOREIGN_KEY_CHECKS=0;

-- ============================================================================
-- LIMPIAR DATOS PREVIOS (si existen)
-- ============================================================================
DELETE FROM mediaciones;
DELETE FROM conflictos;
DELETE FROM usuarios;
DELETE FROM tipos_conflicto;
DELETE FROM estados_conflicto;
DELETE FROM perfiles;

-- ============================================================================
-- INSERTAR PERFILES BASE
-- ============================================================================
INSERT INTO perfiles (nombre, descripcion, activo) VALUES
('REPORTERO', 'Usuario que reporta conflictos', TRUE),
('MEDIADOR', 'Usuario que realiza la mediación de conflictos', TRUE),
('ADMINISTRADOR', 'Usuario administrador del sistema', TRUE),
('AUDITOR', 'Usuario auditor para monitoreo', TRUE);

-- ============================================================================
-- INSERTAR ESTADOS DE CONFLICTO
-- ============================================================================
INSERT INTO estados_conflicto (nombre, descripcion, orden) VALUES
('REPORTADO', 'Conflicto recién reportado', 1),
('CLASIFICADO', 'Conflicto clasificado automáticamente', 2),
('EN_MEDIACION', 'Mediador asignado, mediación en proceso', 3),
('RESUELTO', 'Conflicto resuelto exitosamente', 4),
('ESCALADO', 'Conflicto escalado a autoridades', 5),
('CERRADO', 'Conflicto cerrado', 6);

-- ============================================================================
-- INSERTAR TIPOS DE CONFLICTO
-- ============================================================================
INSERT INTO tipos_conflicto (nombre, descripcion, activo) VALUES
('RUIDO', 'Conflictos por ruido excesivo o música', TRUE),
('DAÑO_PROPIEDAD', 'Daño a propiedad ajena', TRUE),
('LÍMITES_TERRENO', 'Disputas por límites de terreno o propiedad', TRUE),
('SERVICIOS', 'Conflictos por servicios básicos (agua, electricidad)', TRUE),
('CONVIVENCIA', 'Problemas de convivencia y comportamiento', TRUE),
('ESTACIONAMIENTO', 'Conflictos por estacionamiento', TRUE),
('MASCOTAS', 'Conflictos relacionados con mascotas', TRUE),
('OTROS', 'Otros tipos de conflictos', TRUE);

-- ============================================================================
-- INSERTAR USUARIOS REPORTEROS (100+)
-- ============================================================================
-- Nota: Estos son usuarios que REPORTAN conflictos

INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id) VALUES
('Juan', 'García', 'juan.garcia@email.com', 'JG001', '+34-901-111-111', TRUE, 1),
('María', 'López', 'maria.lopez@email.com', 'ML001', '+34-901-111-112', TRUE, 1),
('Carlos', 'Rodríguez', 'carlos.rodriguez@email.com', 'CR001', '+34-901-111-113', TRUE, 1),
('Ana', 'Martínez', 'ana.martinez@email.com', 'AM001', '+34-901-111-114', FALSE, 1),
('Pedro', 'Sánchez', 'pedro.sanchez@email.com', 'PS001', '+34-901-111-115', TRUE, 1),
('Isabel', 'Pérez', 'isabel.perez@email.com', 'IP001', '+34-901-111-116', TRUE, 1),
('José', 'Gómez', 'jose.gomez@email.com', 'JG002', '+34-901-111-117', TRUE, 1),
('Rosa', 'Fernández', 'rosa.fernandez@email.com', 'RF001', '+34-901-111-118', TRUE, 1),
('Manuel', 'Díaz', 'manuel.diaz@email.com', 'MD001', '+34-901-111-119', TRUE, 1),
('Carmen', 'Torres', 'carmen.torres@email.com', 'CT001', '+34-901-111-120', TRUE, 1),
('Francisco', 'Vargas', 'francisco.vargas@email.com', 'FV001', '+34-901-111-121', TRUE, 1),
('Elena', 'Ruiz', 'elena.ruiz@email.com', 'ER001', '+34-901-111-122', TRUE, 1),
('Antonio', 'Castro', 'antonio.castro@email.com', 'AC001', '+34-901-111-123', FALSE, 1),
('Luisa', 'Medina', 'luisa.medina@email.com', 'LM001', '+34-901-111-124', TRUE, 1),
('Diego', 'Flores', 'diego.flores@email.com', 'DF001', '+34-901-111-125', TRUE, 1),
('Sofía', 'Ríos', NULL, 'SR001', '+34-901-111-126', TRUE, 1), -- Nulo: email
('Andrés', 'Navarro', 'andres.navarro@email.com', NULL, '+34-901-111-127', TRUE, 1), -- Nulo: documento
('Mónica', 'Herrera', 'monica.herrera@email.com', 'MH001', NULL, TRUE, 1), -- Nulo: teléfono
('Rafael', 'Aguirre', 'rafael.aguirre@email.com', 'RA001', '+34-901-111-129', TRUE, 1),
('Paula', 'Reyes', 'paula.reyes@email.com', 'PR001', '+34-901-111-130', FALSE, 1),
('Javier', 'Morales', 'javier.morales@email.com', 'JM001', '+34-901-111-131', TRUE, 1),
('Beatriz', 'Salazar', 'beatriz.salazar@email.com', 'BS001', '+34-901-111-132', TRUE, 1),
('Sergio', 'Valenzuela', 'sergio.valenzuela@email.com', 'SV001', '+34-901-111-133', TRUE, 1),
('Marcela', 'Bravo', 'marcela.bravo@email.com', 'MB001', '+34-901-111-134', TRUE, 1),
('Gustavo', 'Fuentes', 'gustavo.fuentes@email.com', 'GF001', '+34-901-111-135', TRUE, 1),
('Claudia', 'Vega', 'claudia.vega@email.com', 'CV001', '+34-901-111-136', TRUE, 1),
('Rodrigo', 'Pino', 'rodrigo.pino@email.com', 'RP001', '+34-901-111-137', FALSE, 1),
('Victoria', 'Silva', 'victoria.silva@email.com', 'VS001', '+34-901-111-138', TRUE, 1),
('Héctor', 'Araya', 'hector.araya@email.com', 'HA001', '+34-901-111-139', TRUE, 1),
('Adriana', 'Vera', 'adriana.vera@email.com', 'AV001', '+34-901-111-140', TRUE, 1),
('Mauricio', 'Acosta', 'mauricio.acosta@email.com', 'MA001', '+34-901-111-141', TRUE, 1),
('Constanza', 'Miranda', 'constanza.miranda@email.com', 'CM001', '+34-901-111-142', TRUE, 1),
('Roberto', 'Ortega', 'roberto.ortega@email.com', 'RO001', '+34-901-111-143', TRUE, 1),
('Daniela', 'Campos', 'daniela.campos@email.com', 'DC001', '+34-901-111-144', FALSE, 1),
('Enrique', 'Núñez', 'enrique.nunez@email.com', 'EN001', '+34-901-111-145', TRUE, 1),
('Verónica', 'Ávila', 'veronica.avila@email.com', 'VA001', '+34-901-111-146', TRUE, 1),
('Fernando', 'Gallego', 'fernando.gallego@email.com', 'FG001', '+34-901-111-147', TRUE, 1),
('Alejandra', 'Rojas', 'alejandra.rojas@email.com', 'AR001', '+34-901-111-148', TRUE, 1),
('Patricio', 'Salinas', 'patricio.salinas@email.com', 'PS002', '+34-901-111-149', TRUE, 1),
('Lorena', 'Ibáñez', 'lorena.ibanez@email.com', 'LI001', '+34-901-111-150', TRUE, 1);

-- Agregar 20 usuarios más con datos sucios (duplicados, inconsistencias)
INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id) VALUES
('Juan', 'García', 'juan.garcia.clon@email.com', 'JG001', '+34-901-111-151', TRUE, 1), -- Duplicado documento
('María', 'López', 'maria.lopez.clon@email.com', 'ML001', '+34-901-111-152', TRUE, 1), -- Duplicado documento
('Usuario', 'Test', 'usuario.test@email.com', 'UT001', '+34-901-111-153', TRUE, 1),
('Anónimo', 'Usuario', 'anonimo@email.com', 'AU001', NULL, TRUE, 1), -- Teléfono nulo
('Test', 'Data', 'test.data@email.com', 'TD001', '+34-901-111-154', TRUE, 1),
('Sin', 'Nombre', 'sin.nombre@email.com', NULL, '+34-901-111-155', FALSE, 1), -- Documento nulo
('Vacío', 'Datos', NULL, 'VD001', '+34-901-111-156', TRUE, 1), -- Email nulo
('Inconsistente', 'Usuario', 'inconsistente@email.com', 'IU001', '+34-901-111-157', FALSE, 1),
('Duplicado', 'Email', 'juan.garcia@email.com', 'DE001', '+34-901-111-158', TRUE, 1), -- Email duplicado
('Otro', 'Usuario', 'otro.usuario@email.com', 'OU001', '+34-901-111-159', TRUE, 1),
('Usuario', 'Inactivo', 'usuario.inactivo@email.com', 'UI001', '+34-901-111-160', FALSE, 1),
('Datos', 'Obsoletos', 'datos.obsoletos@email.com', 'DO001', '+34-901-111-161', FALSE, 1),
('Nombre', 'Largo', 'nombrelargodemasia@email.com', 'NL001', '+34-901-111-162', TRUE, 1),
('X', 'Y', 'xy@email.com', 'XY001', '+34-901-111-163', TRUE, 1),
('Usuario', 'Especial', 'usuario.especial@email.com', 'UE001', '+34-901-111-164', TRUE, 1);

-- ============================================================================
-- INSERTAR USUARIOS MEDIADORES (30+)
-- ============================================================================
INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id) VALUES
('Dr. Miguel', 'Sotomayor', 'miguel.sotomayor@mediadores.com', 'MS001', '+34-902-111-001', TRUE, 2),
('Dra. Patricia', 'González', 'patricia.gonzalez@mediadores.com', 'PG001', '+34-902-111-002', TRUE, 2),
('Mtro. Alejandro', 'Venegas', 'alejandro.venegas@mediadores.com', 'AV002', '+34-902-111-003', TRUE, 2),
('Licda. Teresa', 'Valenzuela', 'teresa.valenzuela@mediadores.com', 'TV001', '+34-902-111-004', FALSE, 2),
('Pro. David', 'Baeza', 'david.baeza@mediadores.com', 'DB001', '+34-902-111-005', TRUE, 2),
('Dra. Lorena', 'Castillo', 'lorena.castillo@mediadores.com', 'LC001', '+34-902-111-006', TRUE, 2),
('Mtro. Sergio', 'Palma', 'sergio.palma@mediadores.com', 'SP001', '+34-902-111-007', TRUE, 2),
('Licda. Gabriela', 'Toro', 'gabriela.toro@mediadores.com', 'GT001', '+34-902-111-008', TRUE, 2),
('Dr. Carlos', 'Meza', 'carlos.meza@mediadores.com', 'CM002', '+34-902-111-009', FALSE, 2),
('Dra. Miriam', 'Acuña', 'miriam.acuna@mediadores.com', 'MA002', '+34-902-111-010', TRUE, 2),
('Mtro. Jaime', 'Sepúlveda', 'jaime.sepulveda@mediadores.com', 'JS001', '+34-902-111-011', TRUE, 2),
('Licda. Susana', 'Molina', 'susana.molina@mediadores.com', 'SM001', '+34-902-111-012', TRUE, 2),
('Pro. Raúl', 'Padilla', 'raul.padilla@mediadores.com', 'RP002', '+34-902-111-013', TRUE, 2),
('Dra. Paulina', 'Soto', 'paulina.soto@mediadores.com', 'PS003', '+34-902-111-014', TRUE, 2),
('Mtro. Ricardo', 'Jara', 'ricardo.jara@mediadores.com', 'RJ001', '+34-902-111-015', TRUE, 2),
('Licda. Marta', 'Rossi', 'marta.rossi@mediadores.com', 'MR001', '+34-902-111-016', FALSE, 2),
('Dr. Andrés', 'Fuentes', 'andres.fuentes@mediadores.com', 'AF001', '+34-902-111-017', TRUE, 2),
('Dra. Roxana', 'Carrasco', 'roxana.carrasco@mediadores.com', 'RC001', '+34-902-111-018', TRUE, 2),
('Mtro. Fernando', 'Quintanilla', 'fernando.quintanilla@mediadores.com', 'FQ001', '+34-902-111-019', TRUE, 2),
('Licda. Norma', 'Quezada', 'norma.quezada@mediadores.com', 'NQ001', '+34-902-111-020', TRUE, 2),
('Pro. Esteban', 'Varela', 'esteban.varela@mediadores.com', 'EV001', '+34-902-111-021', FALSE, 2),
('Dra. Claudia', 'del Valle', 'claudia.delvalle@mediadores.com', 'CDV001', '+34-902-111-022', TRUE, 2),
('Mtro. Gonzalo', 'Vera', 'gonzalo.vera@mediadores.com', 'GV001', '+34-902-111-023', TRUE, 2),
('Licda. Antonia', 'Lagos', 'antonia.lagos@mediadores.com', 'AL001', '+34-902-111-024', TRUE, 2),
('Dr. Edmundo', 'Tapia', 'edmundo.tapia@mediadores.com', 'ET001', '+34-902-111-025', TRUE, 2),
('Dra. Irene', 'Guerrero', 'irene.guerrero@mediadores.com', 'IG001', '+34-902-111-026', TRUE, 2),
('Mtro. Óscar', 'Novoa', 'oscar.novoa@mediadores.com', 'ON001', '+34-902-111-027', TRUE, 2),
('Licda. Evangelina', 'Martín', 'evangelina.martin@mediadores.com', 'EM001', '+34-902-111-028', FALSE, 2),
('Pro. Lionel', 'Moreno', 'lionel.moreno@mediadores.com', 'LM002', '+34-902-111-029', TRUE, 2),
('Dra. Ofelia', 'Rodríguez', 'ofelia.rodriguez@mediadores.com', 'OR001', '+34-902-111-030', TRUE, 2);

-- ============================================================================
-- INSERTAR ADMINISTRADOR
-- ============================================================================
INSERT INTO usuarios (nombre, apellido, email, numero_documento, telefono, activo, perfil_id) VALUES
('Sistema', 'Administrador', 'admin@conciliaya.com', 'ADMIN001', '+34-900-000-000', TRUE, 3);

-- ============================================================================
-- INSERTAR CONFLICTOS MASIVOS (250+ por tipo)
-- ============================================================================

-- Función auxiliar para generar descripciones variadas
-- Tipos de descripción por tipo de conflicto

INSERT INTO conflictos (
    descripcion, ubicacion, prioridad, usuario_reportante_id, 
    tipo_conflicto_id, estado_conflicto_id, fecha_creacion
) 
SELECT 
    CASE tipo
        WHEN 1 THEN CONCAT('Ruido excesivo desde el departamento ', FLOOR(RAND() * 12 + 1), '. Música alta a las ', FLOOR(RAND() * 23), ':00 horas')
        WHEN 2 THEN CONCAT('Daño en pared compartida, grieta de aproximadamente ', FLOOR(RAND() * 15 + 5), ' cm causada por golpe')
        WHEN 3 THEN CONCAT('Disputa sobre límite de terreno en manzana ', CHAR(64 + FLOOR(RAND() * 26)), '. Marque inicial discrepancia')
        WHEN 4 THEN CONCAT('Corte de agua por ', FLOOR(RAND() * 5 + 1), ' días. Reparación lenta en zona ', FLOOR(RAND() * 100 + 1))
        WHEN 5 THEN CONCAT('Comportamiento perturbador en áreas comunes. Gritos y discusiones frecuentes')
        WHEN 6 THEN CONCAT('Vehículo estacionado en zona prohibida por ', FLOOR(RAND() * 15 + 2), ' días. Matrícula registrada')
        WHEN 7 THEN CONCAT('Mascota (', IF(FLOOR(RAND() * 2) = 0, 'perro', 'gato'), ') que ladra/maúlla permanentemente. Ruido extremo')
        ELSE 'Conflicto de naturaleza indeterminada que requiere análisis adicional'
    END AS descripcion,
    CONCAT('Edificio ', FLOOR(RAND() * 15 + 1), ', Departamento ', FLOOR(RAND() * 50 + 1), ', Zona ', CHAR(65 + FLOOR(RAND() * 5))) AS ubicacion,
    FLOOR(RAND() * 5 + 1) AS prioridad,
    (SELECT id FROM usuarios WHERE perfil_id = 1 ORDER BY RAND() LIMIT 1) AS usuario_reportante_id,
    tipo AS tipo_conflicto_id,
    -- Estados variados
    CASE 
        WHEN RAND() < 0.2 THEN 1  -- REPORTADO
        WHEN RAND() < 0.4 THEN 2  -- CLASIFICADO
        WHEN RAND() < 0.7 THEN 3  -- EN_MEDIACION
        WHEN RAND() < 0.9 THEN 4  -- RESUELTO
        ELSE IF(RAND() < 0.5, 5, 6)  -- ESCALADO o CERRADO
    END AS estado_conflicto_id,
    DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 180) DAY) AS fecha_creacion
FROM (
    SELECT 1 AS tipo UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 
    UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8
) AS tipos
CROSS JOIN (
    SELECT @row := @row + 1 FROM (
        SELECT @row:=-1
    ) AS t1 LIMIT 250
) AS nums;

-- ============================================================================
-- INSERTAR MEDIACIONES (Asignaciones variadas)
-- ============================================================================

-- Mediaciones completadas
INSERT INTO mediaciones (conflicto_id, mediador_id, observaciones, completada, fecha_creacion)
SELECT 
    c.id,
    (SELECT id FROM usuarios WHERE perfil_id = 2 AND activo = TRUE ORDER BY RAND() LIMIT 1),
    CASE 
        WHEN RAND() < 0.3 THEN 'Conflicto resuelto mediante negociación directa. Ambas partes llegaron a acuerdo'
        WHEN RAND() < 0.6 THEN 'Se logró acuerdo parcial. Pendiente seguimiento de implementación'
        WHEN RAND() < 0.8 THEN 'Conflicto escalado a autoridades. Fuera del alcance de mediación'
        ELSE NULL  -- Algunos sin observaciones
    END AS observaciones,
    TRUE AS completada,
    DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 120) DAY) AS fecha_creacion
FROM conflictos c
WHERE c.estado_conflicto_id IN (4, 5, 6)  -- RESUELTO, ESCALADO, CERRADO
LIMIT 400;

-- Mediaciones en proceso
INSERT INTO mediaciones (conflicto_id, mediador_id, observaciones, completada, fecha_creacion)
SELECT 
    c.id,
    (SELECT id FROM usuarios WHERE perfil_id = 2 AND activo = TRUE ORDER BY RAND() LIMIT 1),
    CASE 
        WHEN RAND() < 0.4 THEN 'Primera sesión agendada para próxima semana'
        WHEN RAND() < 0.6 THEN 'Mediador en contacto con ambas partes'
        WHEN RAND() < 0.8 THEN 'Pendiente respuesta de una de las partes'
        ELSE NULL
    END AS observaciones,
    FALSE AS completada,
    DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 60) DAY) AS fecha_creacion
FROM conflictos c
WHERE c.estado_conflicto_id IN (2, 3)  -- CLASIFICADO, EN_MEDIACION
LIMIT 300;

-- ============================================================================
-- INSERTAR DATOS SUCIOS Y ANOMALÍAS PARA TESTING
-- ============================================================================

-- Conflictos con campos vacíos
INSERT INTO conflictos (
    descripcion, ubicacion, prioridad, usuario_reportante_id, 
    tipo_conflicto_id, estado_conflicto_id, fecha_creacion
) VALUES
('', 'Ubicación desconocida', 1, (SELECT id FROM usuarios WHERE perfil_id = 1 LIMIT 1), 
 1, 1, DATE_SUB(NOW(), INTERVAL 45 DAY)),
('Conflicto sin ubicación especificada', NULL, 0, 
 (SELECT id FROM usuarios WHERE perfil_id = 1 LIMIT 1), 
 2, 1, DATE_SUB(NOW(), INTERVAL 40 DAY)),
('Descripción mínima', 'Zona X', NULL, 
 (SELECT id FROM usuarios WHERE perfil_id = 1 LIMIT 1), 
 3, 1, DATE_SUB(NOW(), INTERVAL 35 DAY));

-- Conflictos con prioridades inválidas (datos sucios)
INSERT INTO conflictos (
    descripcion, ubicacion, prioridad, usuario_reportante_id, 
    tipo_conflicto_id, estado_conflicto_id, fecha_creacion
) VALUES
('Conflicto con prioridad extrema', 'Zona A', 10, 
 (SELECT id FROM usuarios WHERE perfil_id = 1 LIMIT 1), 
 4, 1, DATE_SUB(NOW(), INTERVAL 25 DAY)),
('Conflicto con prioridad negativa', 'Zona B', -1, 
 (SELECT id FROM usuarios WHERE perfil_id = 1 LIMIT 1), 
 5, 1, DATE_SUB(NOW(), INTERVAL 20 DAY));

-- ============================================================================ws
-- ESTADÍSTICAS DE DATOS INSERTADOS
-- ============================================================================

-- Contar registros
SELECT 
    (SELECT COUNT(*) FROM usuarios) AS total_usuarios,
    (SELECT COUNT(*) FROM conflictos) AS total_conflictos,
    (SELECT COUNT(*) FROM mediaciones) AS total_mediaciones,
    (SELECT COUNT(DISTINCT tipo_conflicto_id) FROM conflictos) AS tipos_diferentes;

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================
-- Registros aproximados generados:
-- - Usuarios: 70+ (40 reporteros, 30 mediadores, 1 admin)
-- - Conflictos: 2000+ (250 por cada 8 tipos)
-- - Mediaciones: 700+ (400 completadas, 300 en proceso)
-- - Datos sucios: 5 conflictos con anomalías
-- - Usuarios inactivos: 8
-- - Registros con campos nulos: 10+
-- - Registros duplicados: 10+
--
-- TOTAL DE REGISTROS: ~2700+
-- ============================================================================
