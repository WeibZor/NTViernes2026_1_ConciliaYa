# Conflicto

Este directorio contiene los HUs para el análisis del dataset `Conflicto`.

## Épica
Análisis de datos de la tabla `Conflicto`.

## Backlog de historias de usuario

### HU-01: Limpieza del set de datos (`Conflicto`)
Como analista de datos quiero limpiar el conjunto de datos de la tabla `Conflicto` para asegurar que la información sea confiable antes del análisis.

Criterios de aceptación:
- [ ] Se identifican y reportan valores nulos por columna
- [ ] Se detectan y eliminan registros duplicados
- [ ] Se corrigen tipos de datos incorrectos
- [ ] Se normalizan textos
- [ ] Se documentan las transformaciones realizadas

### HU-02: Descripción exploratoria con Pandas (`Conflicto`)
Como analista de datos quiero describir la tabla `Conflicto` con Pandas para entender su estructura y calidad.

Criterios de aceptación:
- [ ] Dataset cargado correctamente
- [ ] Uso de `head()` y `tail()`
- [ ] Uso de `info()` y `describe()`
- [ ] Identificación de columnas
- [ ] Clasificación de variables

### HU-04: Transformación con `query()` (`Conflicto`)
Como analista de datos quiero aplicar `query()` en la tabla `Conflicto` para obtener subconjuntos útiles para el análisis.

Criterios de aceptación:
- [ ] Uso de `query()` en variables
- [ ] Tres consultas mínimo
- [ ] Resultados en `DataFrame`
- [ ] Validación de resultados

### HU-05: Agrupación y resumen (`Conflicto`)
Como analista de datos quiero agrupar datos de `Conflicto` para obtener indicadores y resúmenes.

Criterios de aceptación:
- [ ] Uso de `groupby()`
- [ ] Métricas agregadas
- [ ] Dos agrupaciones mínimo
- [ ] Resultados claros
