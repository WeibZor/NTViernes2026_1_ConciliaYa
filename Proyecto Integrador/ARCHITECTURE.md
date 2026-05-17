# Arquitectura propuesta — Proyecto Integrador

Objetivo: organizar el backend para que sea modular, testeable y fácil de desplegar.

Propuesta de estructura (pasos de migración):

1. Convertir la carpeta en un paquete Python (`concilia` o `backend`) y mover la lógica allí:

   Proyecto Integrador/
   - conda/ o venv (opcional)
   - con‑package/ (nuevo nombre, p.ej. `concilia`)
     - __init__.py
     - api.py (o api/__init__.py + routes/)
     - services/
       - usuario.py
       - tipoconflicto.py
       - conflicto.py
     - utils/
   - notebooks/ (solo notebook y análisis, fuera del paquete productivo)
   - scripts/
     - run_backend.py
   - requirements.txt

2. Separar responsabilidades:
- `api.py`: solo definición de rutas y montaje de middlewares.
- `services/` o `processors/`: funciones de limpieza, simulación, queries y agrupaciones.
- `data/`: generación y fixtures (simulación de datos).

3. Imports: usar imports relativos dentro del paquete (p.ej. `from .services.usuario import limpiar_usuarios`).

4. Testing: añadir `tests/` para pruebas unitarias (smoke tests para cada servicio).

5. CI / Docker: agregar `Dockerfile` y pipeline básico para reproducibilidad.

Cambios mínimos ya aplicados:
- `run_backend.py` como entrypoint cross-platform (recomendado para ejecución desde IDE/Windows/WSL).
- Este documento: pasos y guía para continuar la refactorización.

Siguientes pasos sugeridos (puedo aplicarlos):
- Crear el paquete `concilia` y mover los módulos.
- Actualizar imports a relativos.
- Ejecutar pruebas de importación para validar.

Si quieres que siga, dime si prefieres que haga los cambios automáticamente (mover archivos y actualizar imports) o que primero genere un diff propuesto para revisar.
