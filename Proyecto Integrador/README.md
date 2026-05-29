# Proyecto Integrador - ConciliaYa

Este directorio contiene la lógica de datos y los servicios Python para la integración con el frontend React.

## Requisitos de la Máquina Virtual

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes en tu máquina virtual:

### Python 3.8+
- Descarga desde: https://www.python.org/downloads/
- Verifica con: `python --version`

### Node.js 16+ y npm
- Descarga desde: https://nodejs.org/
- Verifica con: `node --version` y `npm --version`

### Git (opcional, para clonar repositorios)
- Descarga desde: https://git-scm.com/

## Instalación y Ejecución

### 1. Backend (Python/FastAPI)

```bash
# Navegar al directorio del backend
cd "Proyecto Integrador"

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor backend
uvicorn api:app --reload --port 8000
```

El backend estará disponible en: `http://localhost:8000`

#### Conexión opcional a MySQL / XAMPP

Si quieres usar una base de datos real en XAMPP, configura estas variables de entorno antes de iniciar la API:

```bash
set USE_MYSQL=true
set DB_HOST=127.0.0.1
set DB_PORT=3306
set DB_USER=root
set DB_PASSWORD=
set DB_NAME=conciliadb
```

La API intentará cargar usuarios desde la tabla `usuario` de MySQL y, si no está disponible, volverá a los datos sintéticos en memoria.

> No se requieren claves API para acceder al backend o al frontend. La autenticación de usuario en la aplicación usa correo y contraseña, no un token externo o clave de servicio.

### 2. Frontend (React/Vite)

```bash
# Navegar al directorio del frontend
cd "Front - Project"

# Instalar dependencias
npm install

# Ejecutar el servidor de desarrollo
npm run dev
```

El frontend estará disponible en: `http://localhost:5173` (o el puerto que indique la consola)

## Qué hay aquí

- `api.py`: app FastAPI que expone la lógica de los HUs de Usuario y TipoConflicto.
- `main.py`: script local que ejecuta simulación, limpieza, descripción, consultas y agrupaciones.
- `requirements.txt`: dependencias Python necesarias.
- `usuario/`: módulos con generación, limpieza y análisis de datos de Usuario.
- `tipoconflicto/`: módulos con generación, limpieza y análisis de datos de TipoConflicto.
- `conflicto/`: módulos con generación, limpieza y análisis de datos de Conflicto.

## Endpoints disponibles

### Usuario
- `GET /api/usuarios` — dataset Usuario limpio
- `GET /api/usuarios/raw` — dataset Usuario sintético original
- `GET /api/usuarios/filter` — filtrado por `search`, `activo`, `perfilId`, `tipoDocumento`, `desdeFechaAlta`
- `GET /api/usuarios/head-tail` — muestras `head` y `tail`
- `GET /api/usuarios/summary` — resumen estructural del dataset
- `GET /api/usuarios/queries` — resultados de las consultas con `query()`
- `GET /api/usuarios/groupings` — agrupaciones por perfil y tipo de documento
- `GET /api/usuarios/stats` — estadísticas agregadas de Usuario
- `POST /api/usuarios` — crea un nuevo usuario
- `PUT /api/usuarios/{usuario_id}` — actualiza usuario
- `DELETE /api/usuarios/{usuario_id}` — elimina usuario

### TipoConflicto
- `GET /api/tipoconflictos` — dataset TipoConflicto limpio
- `GET /api/tipoconflictos/raw` — dataset TipoConflicto sintético original
- `GET /api/tipoconflictos/filter` — filtrado por `search`, `activo`, `id`
- `GET /api/tipoconflictos/summary` — resumen estructural del dataset
- `GET /api/tipoconflictos/queries/{type}` — consultas específicas (activos, laborales, ultimos_180_dias)
- `GET /api/tipoconflictos/groupings/{type}` — agrupaciones (por_activo, por_nombre)
- `POST /api/tipoconflictos/simulate` — simula datos (parámetro `num_registros`)
- `POST /api/tipoconflictos/clean` — ejecuta limpieza de datos
- `POST /api/tipoconflictos` — crea un nuevo tipo de conflicto
- `PUT /api/tipoconflictos/{tipo_id}` — actualiza tipo de conflicto
- `DELETE /api/tipoconflictos/{tipo_id}` — elimina tipo de conflicto

### Conflicto
- `GET /api/conflictos/raw` — dataset Conflicto sintético original
- `GET /api/conflictos` — dataset Conflicto limpio
- `GET /api/conflictos/filter` — filtrado por `search`, `activo`, `tipoConflicto`, `estado`, `id`
- `GET /api/conflictos/head-tail` — muestras `head` y `tail`
- `GET /api/conflictos/summary` — resumen estructural del dataset
- `GET /api/conflictos/queries` — resultados de las consultas con `query()`
- `GET /api/conflictos/groupings` — agrupaciones por estado y tipo de conflicto
- `GET /api/conflictos/queries/{query_type}` — consulta específica devuelta por nombre de query
- `GET /api/conflictos/groupings/{group_type}` — agrupación específica devuelta por nombre de grupo
- `POST /api/conflictos/simulate` — simula datos (parámetro `num_registros`)
- `POST /api/conflictos/clean` — ejecuta limpieza de datos
- `POST /api/conflictos` — crea un nuevo conflicto
- `PUT /api/conflictos/{conflicto_id}` — actualiza conflicto
- `DELETE /api/conflictos/{conflicto_id}` — elimina conflicto

## Integración con el frontend

- El frontend React se configura para consumir `http://localhost:8000/api`.
- El archivo `Front - Project/.env` contiene la variable `VITE_API_BASE_URL`.
- La lógica de usuario y tipoconflicto en React usa la API backend con fallback local.
- Los cambios en el frontend (simular, limpiar, crear) se reflejan automáticamente en la UI y en el backend.

## Notas

- Si la API no está disponible, el frontend sigue funcionando con la base local simulada.
- El backend genera los datos sintéticos en memoria y los mantiene mientras la app está activa.
- Para desarrollo, ejecuta ambos servidores simultáneamente en terminales separadas.
