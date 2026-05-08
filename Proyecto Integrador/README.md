# Proyecto Integrador - ConciliaYa

Este directorio contiene la lógica de datos y los servicios Python para la integración con el frontend React.

## Qué hay aquí

- `api.py`: app FastAPI que expone la lógica de los HUs de Usuario.
- `main.py`: script local que ejecuta simulación, limpieza, descripción, consultas y agrupaciones.
- `requirements.txt`: dependencias Python necesarias.
- `usuario/`: módulos con generación, limpieza y análisis de datos de Usuario.

## Endpoints disponibles

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

## Cómo ejecutar el backend

```powershell
cd "c:\Users\User\Documents\2. FRONT\NTViernes2026_1_ConciliaYa\Proyecto Integrador"
python -m pip install -r requirements.txt
uvicorn api:app --reload --port 8000
```

## Integración con el frontend

- El frontend React se configura para consumir `http://localhost:8000/api`.
- El archivo `Front - Project/.env` contiene la variable `VITE_API_BASE_URL`.
- La lógica de usuario en React ahora usa la API backend con fallback local.

## Notas

- Si la API no está disponible, el frontend sigue funcionando con la base local simulada.
- El backend genera los datos sintéticos en memoria y los mantiene mientras la app está activa.
