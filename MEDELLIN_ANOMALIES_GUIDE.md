# 🇨🇴 Guía - Datos de Medellín con Anomalías Masivas

Documentación del script de prueba para **Medellín SOLO** con **200+ anomalías** detectables.

---

## 📊 Volumen de Datos - MEDELLÍN

| Concepto | Cantidad |
|----------|----------|
| **Usuarios Reporteros** | 50 |
| **Usuarios Mediadores** | 30 |
| **Administrador** | 1 |
| **Total Usuarios** | 81 |
| **Conflictos** | 2000+ |
| **Conflictos con anomalías** | 200+ |
| **Mediaciones** | 700+ |
| **TOTAL REGISTROS** | **2700+** |
| **Ciudades incluidas** | Solo MEDELLÍN |

---

## 🏙️ Comunas de Medellín Incluidas

```
Comuna 1  → Barrio Arví
Comuna 2  → Santo Domingo
Comuna 3  → Laureles-Estadio (La zona más residencial)
Comuna 4  → Junín
Comuna 5  → Castilla
Comuna 6  → Robledo
Comuna 7  → Flores
Comuna 8  → Villa Hermosa
Comuna 9  → Buenos Aires
Comuna 10 → Candelaria
Comuna 11 → Belén
Comuna 12 → San Javier
Comuna 13 → San Cristóbal
Comuna 14 → Chicó
Comuna 15 → Guayabal
Comuna 16 → Palmitas
```

**Distribución**: Conflictos aleatorios entre todas las comunas

---

## 🧹 Tipos de Anomalías (200+)

### Categoría 1: DESCRIPCIONES (20+)
```sql
-- Descripción completamente vacía
INSERT conflictos (descripcion='', ...)

-- Descripción muy larga (excede 2000 caracteres)
INSERT conflictos (descripcion='CONFLICTO REPETIDO. CONFLICTO REPETIDO... (x50)', ...)

-- Descripción NULL
INSERT conflictos (descripcion=NULL, ...)
```

**Impacto**: 
- Búsquedas sin resultados
- Formularios de edición con campos vacíos
- Validación fallida

### Categoría 2: UBICACIONES (30+)
```sql
-- Ubicación NULL
INSERT conflictos (ubicacion=NULL, ...)

-- Ubicación de otra ciudad (fuera del scope)
INSERT conflictos (ubicacion='Bogotá - Apto 15', ...)
INSERT conflictos (ubicacion='Cali - Apto 20', ...)
INSERT conflictos (ubicacion='Cartagena - Apto 10', ...)
INSERT conflictos (ubicacion='Barranquilla - Apto 5', ...)
```

**Impacto**:
- Filtro geográfico no funciona
- Reportes desviados
- Datos fuera de contexto

### Categoría 3: PRIORIDADES (40+)
```sql
-- Prioridad NULL
INSERT conflictos (prioridad=NULL, ...)

-- Prioridades negativas
INSERT conflictos (prioridad=-5, prioridad=-3, prioridad=-1, ...)

-- Prioridad cero
INSERT conflictos (prioridad=0, ...)

-- Prioridades extremas (>5)
INSERT conflictos (prioridad=6, prioridad=8, prioridad=10, 
                    prioridad=15, prioridad=20, prioridad=99, ...)
```

**Impacto**:
- Ordenamiento incorrecto
- Alertas mal categorizadas
- Violación de restricción CHECK

---

### Categoría 4: FECHAS (8+)
```sql
-- Fecha futura (conflicto reportado mañana o en el futuro)
INSERT conflictos (fecha_creacion=DATE_ADD(NOW(), INTERVAL 5 DAY), ...)
```

**Impacto**:
- Timeline anómala
- Reportes no incluyen conflictos
- Análisis temporal fallido

---

### Categoría 5: USUARIOS INVÁLIDOS (15+)
```sql
-- Usuario reportero inactivo
INSERT conflictos (usuario_reportante_id=(SELECT id FROM usuarios 
                   WHERE perfil_id=1 AND activo=FALSE), ...)
```

**Impacto**:
- Reporteros sin permisos generando conflictos
- Auditoría fallida
- Responsabilidad indeterminada

---

### Categoría 6: DUPLICADOS (10+)
```sql
-- Mismo conflicto insertado múltiples veces
-- Mismo conflicto con descripción exacta = 'Ruido excesivo...'
-- Mediación duplicada: mismo mediador, mismo conflicto
```

**Impacto**:
- Conteos inflados
- Trabajo duplicado de mediadores
- Estadísticas incorrectas

---

### Categoría 7: USUARIOS SIN CAMPOS (3+)
```sql
-- Usuario sin email
INSERT usuarios (email=NULL, ...)

-- Usuario sin teléfono
INSERT usuarios (telefono=NULL, ...)

-- Usuario sin documento
INSERT usuarios (numero_documento=NULL, ...)
```

---

### Categoría 8: MEDIACIONES CON ERRORES (20+)
```sql
-- Mediador inactivo asignado
INSERT mediaciones (mediador_id=(SELECT id FROM usuarios 
                    WHERE perfil_id=2 AND activo=FALSE), ...)

-- Mismo mediador para mismo conflicto (duplicado en mediaciones)
INSERT mediaciones (conflicto_id=5, mediador_id=1, ...)
INSERT mediaciones (conflicto_id=5, mediador_id=1, ...)
```

---

## 📋 Cómo Usar Este Dataset

### Paso 1: Cargar Datos
```bash
# Crear BD base
mysql -u root -p < database-init.sql

# Cargar SOLO Medellín con anomalías
mysql -u root -p conciliaya < database-seed-medelin.sql

# ✅ Resultado: 2700+ registros, todas anomalías en Medellín
```

### Paso 2: Verificar Anomalías
```sql
-- Conectarse
mysql -u root -p conciliaya

-- Ver todas las anomalías detectadas
SELECT * FROM (
    SELECT 'Descripciones vacías' AS tipo, COUNT(*) AS qty FROM conflictos WHERE descripcion = ''
    UNION ALL
    SELECT 'Ubicaciones NULL', COUNT(*) FROM conflictos WHERE ubicacion IS NULL
    UNION ALL
    SELECT 'Prioridades NULL', COUNT(*) FROM conflictos WHERE prioridad IS NULL
    UNION ALL
    SELECT 'Prioridades negativas', COUNT(*) FROM conflictos WHERE prioridad < 1
    UNION ALL
    SELECT 'Prioridades extremas', COUNT(*) FROM conflictos WHERE prioridad > 5
    UNION ALL
    SELECT 'Fechas futuras', COUNT(*) FROM conflictos WHERE fecha_creacion > NOW()
    UNION ALL
    SELECT 'Ubicaciones fuera Medellín', COUNT(*) FROM conflictos 
           WHERE ubicacion NOT LIKE 'Medellín %'
    UNION ALL
    SELECT 'Usuarios sin email', COUNT(*) FROM usuarios WHERE email IS NULL
    UNION ALL
    SELECT 'Usuarios sin teléfono', COUNT(*) FROM usuarios WHERE telefono IS NULL
    UNION ALL
    SELECT 'Usuarios inactivos', COUNT(*) FROM usuarios WHERE activo = FALSE
) AS anomalias
ORDER BY qty DESC;
```

**Salida esperada:**
```
Descripciones vacías           10
Ubicaciones NULL               8
Prioridades inválidas         10
Ubicaciones fuera Medellín     6
Prioridades extremas          10
Fechas futuras                8
Usuarios sin datos             6
...
TOTAL ANOMALÍAS             ~200+
```

---

## 🔍 Queries para Testing

### H1: Converfar Datos Sucios
```sql
-- Encontrar todos los conflictos problemáticos
SELECT 
    c.id,
    IF(c.descripcion = '' OR c.descripcion IS NULL, '❌ DESC', '✓') AS desc_ok,
    IF(c.ubicacion IS NULL, '❌ UBIC', '✓') AS ubic_ok,
    IF(c.prioridad IS NULL OR c.prioridad < 1 OR c.prioridad > 5, '❌ PRIO', '✓') AS prio_ok,
    IF(c.fecha_creacion > NOW(), '❌ FECHA', '✓') AS fecha_ok,
    c.descripcion,
    c.ubicacion,
    c.prioridad,
    c.fecha_creacion
FROM conflictos c
WHERE c.descripcion = '' 
   OR c.ubicacion IS NULL
   OR c.prioridad IS NULL
   OR c.prioridad < 1 OR c.prioridad > 5
   OR c.fecha_creacion > NOW()
LIMIT 20;
```

### H2: Validar Solo Medellín
```sql
-- Conflictos NO en Medellín (anomalía)
SELECT COUNT(*) AS conflictos_fuera_medellin
FROM conflictos
WHERE ubicacion NOT LIKE 'Medellín %'
  AND ubicacion IS NOT NULL;
```

**Resultado esperado**: ~6 conflictos (dato sucio)

### H3: Detectar Duplicados Exactos
```sql
-- Conflictos exactamente iguales
SELECT 
    descripcion,
    ubicacion,
    COUNT(*) AS veces_repetido
FROM conflictos
WHERE descripcion IS NOT NULL AND descripcion != ''
GROUP BY descripcion, ubicacion
HAVING COUNT(*) > 1
ORDER BY veces_repetido DESC;
```

### H4: Usuarios sin Información de Contacto
```sql
-- Usuarios incompletos
SELECT 
    id,
    nombre,
    apellido,
    email,
    telefono,
    numero_documento,
    activo,
    IF(email IS NULL OR telefono IS NULL OR numero_documento IS NULL, '⚠️ INCOMPLETO', '✓') AS estado
FROM usuarios
WHERE email IS NULL OR telefono IS NULL OR numero_documento IS NULL;
```

### H5: Mediaciones Problemáticas
```sql
-- Mediaciones con problemas
SELECT 
    m.id,
    m.conflicto_id,
    m.mediador_id,
    u.nombre,
    u.apellido,
    u.activo,
    IF(u.activo = FALSE, '❌ INACTIVO', '✓') AS mediador_activo,
    m.completada,
    m.observaciones
FROM mediaciones m
LEFT JOIN usuarios u ON m.mediador_id = u.id
WHERE u.activo = FALSE OR u.perfil_id != 2
LIMIT 20;
```

---

## 📈 Historias de Usuario para Testing

### HU-1: Validar Integridad de Datos

```gherkin
Escenario: Validar entrada de datos sucios
  Cuando el administrador ejecuta limpieza de datos
  Entonces debe identificar:
    - 10+ descripciones vacías
    - 8+ ubicaciones NULL
    - 10+ prioridades inválidas
    - 6+ conflictos fuera de Medellín
    - 8+ fechas futuras
  Y generar reporte de anomalías
  Y sugerir acciones correctivas
```

### HU-2: Filtrar Solo Medellín

```gherkin
Escenario: Filtrar conflictos por ciudad
  Cuando el usuario selecciona filtro "Medellín"
  Entonces debe mostrar ~2000 conflictos
  Y NO debe mostrar conflictos de Bogotá, Cali, etc.
  Y debe validar ubicación LIKE 'Medellín %'
```

### HU-3: Detectar Anomalías en Frontend

```gherkin
Escenario: Mostrar conflicto con datos incompletos
  Cuando carga conflicto con descripción vacía
  Entonces debe:
    - Mostrar placeholder "(sin descripción)"
    - Destacar en rojo
    - Sugerir editar
    - Permitir corrección rápida
```

### HU-4: Validar Prioridades

```gherkin
Escenario: Ordenar por prioridad
  Cuando ordena por prioridad
  Entonces debe:
    - Colocar prioridades válidas (1-5) primero
    - Luego prioridades NULL
    - Luego prioridades inválidas
    - Mostrar advertencia en inválidas
```

---

## 🎯 Casos de Prueba

| Test | Entrada | Esperado | Actual |
|------|---------|----------|--------|
| Desc vacía | descripcion='' | Error/Advertencia | ? |
| Ubicación NULL | ubicacion=NULL | Error/Advertencia | ? |
| Prioridad -5 | prioridad=-5 | Rechazado/Error | ? |
| Prioridad 99 | prioridad=99 | Rechazado/Error | ? |
| Fecha futura | fecha=+7 días | Rechazado/Error | ? |
| Fuera Medellín | ubicacion='Bogotá' | Filtro no muestra | ? |
| Usuario inactivo | activo=FALSE | No puede reportar | ? |
| Mediador inactivo | mediador.activo=FALSE | No puede mediar | ? |

---

## 💡 Recomendaciones para Limpieza

### Opción 1: Eliminar Anomalías
```sql
-- Eliminar conflictos con problemas críticos
DELETE FROM mediaciones WHERE conflicto_id IN (
    SELECT id FROM conflictos 
    WHERE descripcion = '' OR ubicacion IS NULL
);

DELETE FROM conflictos 
WHERE descripcion = '' OR ubicacion IS NULL;

-- Resultado: ~2700 → ~2400 registros limpios
```

### Opción 2: Corregir Automáticamente
```sql
-- Corregir prioridades inválidas
UPDATE conflictos 
SET prioridad = 3 
WHERE prioridad IS NULL OR prioridad < 1 OR prioridad > 5;

-- Corregir descripciones vacías
UPDATE conflictos 
SET descripcion = '(Sin descripción)' 
WHERE descripcion = '';

-- Resultado: Todos los registros válidos
```

### Opción 3: Marcar para Revisión
```sql
-- Agregar flag para revisión manual
ALTER TABLE conflictos ADD COLUMN requiere_revision BOOLEAN DEFAULT FALSE;

UPDATE conflictos 
SET requiere_revision = TRUE 
WHERE descripcion = '' 
   OR ubicacion IS NULL 
   OR prioridad BETWEEN -5 AND 0 
   OR prioridad > 5;

-- Resultado: 
SELECT COUNT(*) FROM conflictos WHERE requiere_revision = TRUE;
-- ~200+ conflictos marcados
```

---

## 📊 Métricas Esperadas

```
Total conflictos:           2000+
├─ Válidos:                 1800
├─ Descripciones vacías:       10
├─ Ubicaciones NULL:            8
├─ Prioridades inválidas:      10
├─ Fechas futuras:             8
├─ Fuera de Medellín:          6
└─ Otros problemas:           40

Tasa de calidad de datos:    85% (1700/2000)
Anomalías por corregir:      ~300 registros
Esfuerzo de limpieza:        ~30 minutos (automatizable)
```

---

## 🔧 Script de Limpieza Rápida

```sql
-- Script para limpiar datos problemáticos
BEGIN;

-- 1. Actualizar descripciones vacías
UPDATE conflictos SET descripcion = '(Sin descripción)' WHERE descripcion = '';

-- 2. Actualizar ubicaciones NULL
UPDATE conflictos SET ubicacion = 'Medellín - Comuna desconocida' WHERE ubicacion IS NULL;

-- 3. Corregir prioridades
UPDATE conflictos SET prioridad = 3 WHERE prioridad IS NULL OR prioridad < 1 OR prioridad > 5;

-- 4. Corregir fechas futuras
UPDATE conflictos SET fecha_creacion = NOW() WHERE fecha_creacion > NOW();

-- 5. Filtrar conflictos fuera de Medellín
UPDATE conflictos SET ubicacion = CONCAT('Medellín - ', ubicacion) 
WHERE ubicacion NOT LIKE 'Medellín %' AND ubicacion IS NOT NULL;

-- 6. Desactivar mediadores inactivos en mediaciones
DELETE FROM mediaciones WHERE mediador_id IN (
    SELECT id FROM usuarios WHERE perfil_id = 2 AND activo = FALSE
);

-- 7. Eliminar mediaciones duplicadas
DELETE m1 FROM mediaciones m1
INNER JOIN mediaciones m2 
WHERE m1.conflicto_id = m2.conflicto_id 
  AND m1.mediador_id = m2.mediador_id 
  AND m1.id > m2.id;

COMMIT;
```

---

## ✅ Validación Post-Limpieza

```sql
-- Ejecutar para verificar que todo está correcto
SELECT 
    (SELECT COUNT(*) FROM conflictos) AS total_conflictos,
    (SELECT COUNT(*) FROM conflictos WHERE descripcion IS NULL OR descripcion = '') AS desc_problemas,
    (SELECT COUNT(*) FROM conflictos WHERE ubicacion IS NULL) AS ubic_null,
    (SELECT COUNT(*) FROM conflictos 
     WHERE prioridad IS NULL OR prioridad < 1 OR prioridad > 5) AS prio_problemas,
    (SELECT COUNT(*) FROM conflictos WHERE fecha_creacion > NOW()) AS fechas_futuras,
    (SELECT COUNT(*) FROM conflictos 
     WHERE ubicacion NOT LIKE 'Medellín %' AND ubicacion IS NOT NULL) AS fuera_medellin;

-- Resultado esperado post-limpieza:
-- total_conflictos: 2000+
-- desc_problemas: 0
-- ubic_null: 0
-- prio_problemas: 0
-- fechas_futuras: 0
-- fuera_medellin: 0
```

---

**Versión**: 1.0 - Medellín con Anomalías
**Última actualización**: Marzo 2026
**Casos de prueba**: 20+
**Anomalías detectables**: 200+
