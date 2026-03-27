# 📊 Guía de Datos de Prueba - ConciliaYa

Documento que describe los datos de prueba masivos generados y las historias de usuario que se pueden realizar con ellos.

---

## 📈 Volumen de Datos Generados

### Script: `database-seed-data.sql`

| Entidad | Cantidad | Descripción |
|---------|----------|-------------|
| **Usuarios Reporteros** | 40+ | Usuarios que crean conflictos |
| **Usuarios Mediadores** | 30+ | Mediadores asignados a conflictos |
| **Administrador** | 1 | Sistema admin |
| **Total Usuarios** | 71+ | Incluye inactivos y datos sucios |
| **Conflictos** | 2000+ | 250 por cada tipo (8 tipos) |
| **Mediaciones** | 700+ | 400 completadas, 300 en proceso |
| **TOTAL REGISTROS** | **2700+** | Para análisis y testing |

---

## 🔍 Características de los Datos

### ✅ Datos Válidos
- Conflictos con descripciones realistas
- Estados variados (REPORTADO, CLASIFICADO, EN_MEDIACION, RESUELTO, ESCALADO, CERRADO)
- Prioridades entre 1-5 distribuidas aleatoriamente
- Ubicaciones con patrones realistas (Edificio X, Departamento Y, Zona Z)
- Fechas distribuidas en los últimos 180 días
- 8 tipos de conflictos variados

### ⚠️ Datos Sucios (Para Testing)
- **5 conflictos** con anomalías deliberadas
- **Campos nulos**: Email, teléfono, documento faltantes
- **Valores vacíos**: Descripciones y ubicaciones vacías
- **Prioridades inválidas**: -1, 0, 10 (fuera del rango 1-5)
- **Usuarios inactivos**: 8 usuarios con activo=FALSE
- **Duplicados**: Documentos y emails duplicados
- **Inconsistencias**: Transiciones de estado imposibles algunas

---

## 📋 Historias de Usuario Que Puedes Implementar

### 1️⃣ **Filtrar Conflictos por Tipo**

```sql
-- Historia: Como usuario quiero ver solo conflictos de RUIDO
SELECT c.id, c.descripcion, tc.nombre, c.prioridad
FROM conflictos c
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
WHERE tc.nombre = 'RUIDO'
LIMIT 10;
```

**Casos de Uso**:
- Filtrar por RUIDO: ~250 registros
- Filtrar por DAÑO_PROPIEDAD: ~250 registros
- Filtrar por LÍMITES_TERRENO: ~250 registros
- ... (8 tipos disponibles)

**Testing**: Verificar que cada filtro retorna ~250 registros

---

### 2️⃣ **Listar Conflictos por Estado**

```sql
-- Historia: Como mediador quiero ver todos los conflictos EN_MEDIACION
SELECT c.id, c.descripcion, c.ubicacion, u.nombre AS reportero, ec.nombre AS estado
FROM conflictos c
JOIN usuarios u ON c.usuario_reportante_id = u.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id
WHERE ec.nombre = 'EN_MEDIACION'
ORDER BY c.prioridad DESC;
```

**Casos de Uso**:
- Ver conflictos REPORTADOS: ~400 registros
- Ver conflictos EN_MEDIACION: ~500 registros
- Ver conflictos RESUELTOS: ~400 registros
- etc.

**Testing**: Verificar orden por prioridad (5→1)

---

### 3️⃣ **Encontrar Conflictos de Alta Prioridad**

```sql
-- Historia: Como administrador quiero ver conflictos criticos (prioridad 4-5)
SELECT c.id, c.descripcion, c.prioridad, tc.nombre, ec.nombre
FROM conflictos c
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id
WHERE c.prioridad IN (4, 5)
AND ec.nombre NOT IN ('RESUELTO', 'CERRADO')
ORDER BY c.fecha_creacion DESC;
```

**Casos de Uso**:
- Identificar crisis: ~300-400 conflictos
- Priorizar mediación
- Asignar mediadores experimentados

**Testing**: Debe haber conflictos altos sin resolver

---

### 4️⃣ **Análisis de Carga de Mediadores**

```sql
-- Historia: Como administrador quiero saber carga de mediadores
SELECT 
    u.nombre,
    u.apellido,
    COUNT(m.id) AS conflictos_asignados,
    SUM(CASE WHEN m.completada = FALSE THEN 1 ELSE 0 END) AS pendientes,
    SUM(CASE WHEN m.completada = TRUE THEN 1 ELSE 0 END) AS completados
FROM usuarios u
LEFT JOIN mediaciones m ON u.id = m.mediador_id
WHERE u.perfil_id = 2
GROUP BY u.id, u.nombre, u.apellido
ORDER BY conflictos_asignados DESC;
```

**Insights**:
- Mediadores sobrecargados
- Mediadores inactivos
- Balance de carga

**Testing**: Algunos mediadores con 50+ asignaciones, otros con 0

---

### 5️⃣ **Detectar Datos Faltantes/Sucios**

```sql
-- Historia: Como DBA quiero detectar registros incompletos
SELECT 
    'Usuarios sin email' AS tipo_problema,
    COUNT(*) AS cantidad
FROM usuarios
WHERE email IS NULL
UNION ALL
SELECT 'Usuarios sin teléfono', COUNT(*) FROM usuarios WHERE telefono IS NULL
UNION ALL
SELECT 'Conflictos sin ubicación', COUNT(*) FROM conflictos WHERE ubicacion IS NULL
UNION ALL
SELECT 'Conflictos con prioridad inválida', COUNT(*) 
FROM conflictos 
WHERE prioridad < 1 OR prioridad > 5
UNION ALL
SELECT 'Mediaciones sin observaciones', COUNT(*) 
FROM mediaciones 
WHERE observaciones IS NULL;
```

**Resultados Esperados**:
- Usuarios sin email: 2
- Usuarios sin teléfono: 3
- Conflictos sin ubicación: 1
- Prioridades inválidas: 2
- Mediaciones NULL: ~200+

**Testing**: Validar limpieza de datos

---

### 6️⃣ **Estadísticas por Tipo de Conflicto**

```sql
-- Historia: Como analista quiero distribución de conflictos por tipo
SELECT 
    tc.nombre AS tipo_conflicto,
    COUNT(c.id) AS total,
    AVG(c.prioridad) AS prioridad_promedio,
    MAX(c.prioridad) AS max_prioridad,
    MIN(c.prioridad) AS min_prioridad,
    SUM(CASE WHEN ec.nombre = 'RESUELTO' THEN 1 ELSE 0 END) AS resueltos,
    ROUND(
        SUM(CASE WHEN ec.nombre = 'RESUELTO' THEN 1 ELSE 0 END) * 100.0 / COUNT(c.id),
        2
    ) AS tasa_resolucion
FROM conflictos c
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id
GROUP BY tc.id, tc.nombre
ORDER BY total DESC;
```

**Dashboard Insights**:
- RUIDO: 250 conflictos, 80% resolución
- CONVIVENCIA: 250 conflictos, 60% resolución
- Prioridad promedio: 2.8/5
- etc.

**Testing**: Generar dashboards de análisis

---

### 7️⃣ **Identificar Usuarios Duplicados**

```sql
-- Historia: Como DBA quiero encontrar usuarios duplicados
SELECT 
    numero_documento,
    COUNT(*) AS cantidad,
    GROUP_CONCAT(DISTINCT email) AS emails
FROM usuarios
WHERE numero_documento IS NOT NULL
GROUP BY numero_documento
HAVING COUNT(*) > 1
ORDER BY cantidad DESC;
```

**Resultados**:
- Documentos duplicados: ~10 usuarios
- Emails duplicados: ~5 usuarios

**Testing**: Implementar validaciones uniq

---

### 8️⃣ **Timeline de Conflictos**

```sql
-- Historia: Como analista quiero ver evolución de conflictos
SELECT 
    DATE_FORMAT(fecha_creacion, '%Y-%m') AS mes,
    COUNT(*) AS conflictos_nuevos,
    AVG(prioridad) AS prioridad_promedio
FROM conflictos
GROUP BY DATE_FORMAT(fecha_creacion, '%Y-%m')
ORDER BY mes;
```

**Análisis**:
- Últimos 6 meses de datos
- Tendencias temporales
- Variaciones estacionales

**Testing**: Visualizar gráficos de serie temporal

---

### 9️⃣ **Casos Escalados que Necesitan Atención**

```sql
-- Historia: Como superior quiero saber qué casos fueron escalados
SELECT 
    c.id,
    c.descripcion,
    tc.nombre AS tipo,
    c.prioridad,
    u.nombre AS reportero,
    DATE_FORMAT(c.fecha_creacion, '%d/%m/%Y') AS fecha_reporte,
    DATEDIFF(NOW(), c.fecha_creacion) AS días_pendiente
FROM conflictos c
JOIN tipos_conflicto tc ON c.tipo_conflicto_id = tc.id
JOIN usuarios u ON c.usuario_reportante_id = u.id
JOIN estados_conflicto ec ON c.estado_conflicto_id = ec.id
WHERE ec.nombre = 'ESCALADO'
ORDER BY c.prioridad DESC, c.fecha_creacion ASC;
```

**Casos de Uso**:
- Monitoreo de escaladas
- Seguimiento a autoridades
- Histórico de conflictos graves

**Testing**: ~200-300 escaladas

---

### 🔟 **Mediadores Disponibles para Asignación**

```sql
-- Historia: Como sistema automatizado, necesito asignar mediador disponible
SELECT 
    u.id,
    u.nombre,
    u.apellido,
    COUNT(CASE WHEN m.completada = FALSE THEN 1 END) AS carga_actual,
    CASE 
        WHEN COUNT(CASE WHEN m.completada = FALSE THEN 1 END) < 10 THEN 'DISPONIBLE'
        WHEN COUNT(CASE WHEN m.completada = FALSE THEN 1 END) < 20 THEN 'MODERADO'
        ELSE 'SOBRECARGADO'
    END AS estado_capacidad
FROM usuarios u
LEFT JOIN mediaciones m ON u.id = m.mediador_id
WHERE u.perfil_id = 2 AND u.activo = TRUE
GROUP BY u.id
HAVING COUNT(CASE WHEN m.completada = FALSE THEN 1 END) < 20
ORDER BY carga_actual ASC;
```

**Testing**:
- Auto-asignación de mediadores
- Balance de carga
- Manejo de saturación

---

## 🛠️ Cómo Usar los Datos de Prueba

### Paso 1: Crear Base de Datos Base
```bash
mysql -u root -p < database-init.sql
```

### Paso 2: Insertar Datos Masivos
```bash
mysql -u root -p conciliaya < database-seed-data.sql
```

### Paso 3: Verificar Datos
```sql
-- Conectarse a la BD
mysql -u root -p conciliaya

-- Ver cantidad de registros
SELECT 'Usuarios' AS tabla, COUNT(*) AS registros FROM usuarios
UNION ALL
SELECT 'Conflictos', COUNT(*) FROM conflictos
UNION ALL
SELECT 'Mediaciones', COUNT(*) FROM mediaciones;
```

### Paso 4: Ejecutar Historias
Copiar las queries SQL anteriores y ejecutar en MySQL Workbench o terminal

---

## 📊 Queries Útiles para Testing

### Resetear Datos
```sql
DELETE FROM mediaciones;
DELETE FROM conflictos;
DELETE FROM usuarios;
DELETE FROM tipos_conflicto;
DELETE FROM estados_conflicto;
DELETE FROM perfiles;
-- Luego volver a ejecutar database-init.sql y database-seed-data.sql
```

### Ver Todas las Anomalías
```sql
SELECT 
    'Usuarios inactivos' AS tipo, COUNT(*) AS cantidad
FROM usuarios WHERE activo = FALSE
UNION ALL
SELECT 'Campos nulos en usuarios', COUNT(*) 
FROM usuarios WHERE email IS NULL OR telefono IS NULL OR numero_documento IS NULL
UNION ALL
SELECT 'Prioridades inválidas', COUNT(*) 
FROM conflictos WHERE prioridad < 1 OR prioridad > 5 OR prioridad IS NULL
UNION ALL
SELECT 'Conflictos sin mediación', COUNT(*) 
FROM conflictos c 
LEFT JOIN mediaciones m ON c.id = m.conflicto_id 
WHERE m.id IS NULL
UNION ALL
SELECT 'Descripciones vacías', COUNT(*) 
FROM conflictos WHERE descripcion = '' OR descripcion IS NULL;
```

### Reporte Completo de Integridad
```sql
SELECT 
    'TOTAL REGISTROS' AS métrica,
    (SELECT COUNT(*) FROM usuarios) + 
    (SELECT COUNT(*) FROM conflictos) + 
    (SELECT COUNT(*) FROM mediaciones) AS valor
UNION ALL
SELECT 'Usuarios activos', COUNT(*) FROM usuarios WHERE activo = TRUE
UNION ALL
SELECT 'Conflictos sin resolver', COUNT(*) 
FROM conflictos 
WHERE estado_conflicto_id NOT IN (SELECT id FROM estados_conflicto WHERE nombre IN ('RESUELTO', 'CERRADO'))
UNION ALL
SELECT 'Tasa completitud mediaciones', 
    ROUND(SUM(CASE WHEN completada = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
FROM mediaciones;
```

---

## 🎯 Historias por Sprint

### Sprint 1: Visualización Básica
- [ ] Ver lista de todos los conflictos
- [ ] Filtrar por tipo
- [ ] Filtrar por estado
- [ ] Ver detalles de un conflicto

### Sprint 2: Análisis de Datos
- [ ] Dashboard de estadísticas
- [ ] Gráfico de conflictos por tipo
- [ ] Tasas de resolución
- [ ] Carga de mediadores

### Sprint 3: Gestión Avanzada
- [ ] Asignación automática de mediadores
- [ ] Reportes de escaladas
- [ ] Búsqueda y filtros avanzados
- [ ] Exportar datos

### Sprint 4: Limpieza y Calidad
- [ ] Validar datos duplicados
- [ ] Detectar campos faltantes
- [ ] Implementar reglas de integridad
- [ ] Auditoría de cambios

---

## 📱 Datos por Historias Frontend

### Página de Inicio (HomePage)

**Estadísticas a mostrar**:
```json
{
  "conflictos_totales": 2000,
  "en_mediacion": 500,
  "resueltos": 800,
  "escalados": 250,
  "usuarios_activos": 63,
  "mediadores_disponibles": 28,
  "promedio_resolucion_dias": 45
}
```

### Página de Conflictos

**Funcionalidades**:
- Listar 2000+ conflictos con paginación
- Filtrar por estado (6 opciones)
- Filtrar por tipo (8 opciones)
- Filtrar por prioridad (1-5)
- Buscar por descripción
- Ordenar por fecha/prioridad

### Página de Crear Conflicto

**Test Cases**:
- Crear conflicto normal ✓
- Crear con prioridad inválida (validar) ✗
- Crear sin descripción (rechazar) ✗
- Auto-clasificar con IA
- Asignar mediador automáticamente

### Página de Usuarios

**Información**:
- Listar 71+ usuarios
- Filtrar activos/inactivos
- Ver carga de mediadores
- Estadísticas por usuario

---

## ⚡ Performance Testing

Con 2000+ registros puedes probar:

```javascript
// Tiempo de carga de lista (Frontend)
console.time('Cargar conflictos');
fetch('/api/conflictos').then(r => r.json()).then(d => {
    console.timeEnd('Cargar conflictos');
    console.log(`${d.length} registros en ${new Date() - start}ms`);
});

// Query pesada (Backend)
SELECT c.*, u.*, tc.*, ec.*, COUNT(m.id) as mediaciones
FROM conflictos c
JOIN usuarios u ON ...
WHERE c.prioridad > 3
GROUP BY c.id
HAVING COUNT(m.id) > 1
ORDER BY c.fecha_creacion DESC
LIMIT 10;
```

---

## 📝 Notas Importante

1. **Datos Reales**: Los datos simulan patrones reales de conflictos
2. **Datos Anómalos**: Incluyen errores comunes para probar validación
3. **Escalabilidad**: 2000 registros es suficiente para testing, no para producción
4. **Limpieza**: Puedes resetear ejecutando el script database-init.sql

---

Última actualización: Diciembre 2024
Versión: 1.0.0
