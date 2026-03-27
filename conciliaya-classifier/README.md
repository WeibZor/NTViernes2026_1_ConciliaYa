# ConciliaYa Classifier - Microservicio de Clasificación en Python

Este es el microservicio de clasificación de conflictos vecinales desarrollado con **FastAPI**.

## Descripción

Proporciona una API REST que clasifica automáticamente los conflictos vecinales basándose en su descripción utilizando análisis de palabras clave y procesamiento de lenguaje natural simple pero efectivo.

## Características

- ✅ Clasificación automática de conflictos en 8 categorías
- ✅ Cálculo de confianza en las predicciones
- ✅ Documentación automática con Swagger (Swagger UI)
- ✅ Código limpio con funciones puras
- ✅ Logging detallado
- ✅ Validación de datos con Pydantic
- ✅ Manejo de errores global

## Requisitos

- Python 3.9+
- pip (gestor de paquetes)

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

O directamente con uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en: `http://localhost:8000`

## Documentación de API

### Swagger UI
- URL: `http://localhost:8000/docs`
- Interfaz interactiva para testear endpoints

### ReDoc
- URL: `http://localhost:8000/redoc`
- Documentación de referencia

## Endpoints

### 1. Health Check

**GET** `/health`

Verifica si el servicio está funcionando.

**Respuesta:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### 2. Clasificar Conflicto

**POST** `/api/v1/classify-conflict`

Clasifica un conflicto basándose en su descripción.

**Solicitud:**
```json
{
  "descripcion": "Mi vecino ha puesto música muy fuerte a las 3 de la mañana durante varios días, afectando mi descanso"
}
```

**Respuesta:**
```json
{
  "tipoConflictoId": 1,
  "tipoConflictoNombre": "Ruido y molestias",
  "confianza": 0.95,
  "justificacion": "Se detectaron palabras clave características de 'Ruido y molestias'. Clasificación con alta confiabilidad."
}
```

**Códigos de estado HTTP:**
- `200`: Clasificación exitosa
- `400`: Solicitud inválida
- `500`: Error interno del servidor

### 3. Obtener Tipos de Conflicto

**GET** `/api/v1/tipos-conflicto`

Retorna la lista de tipos de conflicto disponibles para clasificación.

**Respuesta:**
```json
{
  "tipos": [
    {"id": 1, "nombre": "Ruido y molestias"},
    {"id": 2, "nombre": "Estacionamiento"},
    {"id": 3, "nombre": "Mascota"},
    {"id": 4, "nombre": "Propiedad y límites"},
    {"id": 5, "nombre": "Servicios e instalaciones"},
    {"id": 6, "nombre": "Comportamiento molesto"},
    {"id": 7, "nombre": "Construcción y reformas"},
    {"id": 8, "nombre": "Basura y limpieza"},
    {"id": 10, "nombre": "Otros"}
  ]
}
```

## Arquitectura

### Principios Aplicados

- **Funciones Puras**: Lógica sin efectos secundarios
- **Separación de Responsabilidades**: Funciones pequeñas y enfocadas
- **Validación de Datos**: Con Pydantic
- **Logging**: Sistema de registros detallado
- **Clean Code**: Nombres claros y descriptivos

### Componentes Principais

1. **Modelos Pydantic**: Validación automática de datos
2. **Funciones Puras**: Lógica de clasificación sin dependencias externas
3. **Endpoint Handlers**: Manejadores de solicitudes HTTP
4. **Global Exception Handler**: Manejo centralizado de errores

## Tipos de Conflicto Soportados

| ID | Tipo | Palabras Clave Ejemplo |
|---|---|---|
| 1 | Ruido y molestias | ruido, música, sonido, molestia, dormir |
| 2 | Estacionamiento | parqueo, estacionamiento, vehículo, coche |
| 3 | Mascota | perro, gato, mascota, ladridos, heces |
| 4 | Propiedad y límites | propiedad, límite, muro, pared, valla |
| 5 | Servicios e instalaciones | agua, luz, electricidad, gas, tubería |
| 6 | Comportamiento molesto | conducta, grosería, insulto, amenaza, acoso |
| 7 | Construcción y reformas | construcción, obra, reforma, demolición |
| 8 | Basura y limpieza | basura, desecho, residuo, suciedad |
| 10 | Otros | (sin palabras clave específicas) |

## Testing

Para testear los endpoints, puede usar:

### Con cURL

```bash
curl -X POST "http://localhost:8000/api/v1/classify-conflict" \
  -H "Content-Type: application/json" \
  -d '{
    "descripcion": "Mi vecino ha puesto música muy fuerte a las 3 de la mañana durante varios días"
  }'
```

### Con Python

```python
import requests

url = "http://localhost:8000/api/v1/classify-conflict"
data = {
    "descripcion": "Mi vecino ha puesto música muy fuerte a las 3 de la mañana durante varios días"
}

response = requests.post(url, json=data)
print(response.json())
```

### Con Swagger UI

1. Ir a `http://localhost:8000/docs`
2. Expandir el endpoint post
3. Hacer clic en "Try it out"
4. Ingresar la descripción
5. Ejecutar

## Mejoras Futuras

- [ ] Integración con modelos NLP avanzados (BERT, GPT)
- [ ] Machine Learning para mejor clasificación
- [ ] Análisis de sentimiento
- [ ] Base de datos de casos históricos
- [ ] Caché de clasificaciones
- [ ] Autenticación y autorización
- [ ] Rate limiting
- [ ] Métricas y monitoreo

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crear rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abrir Pull Request

## Licencia

MIT License

## Autor

ConciliaYa Team - 2024

## Contacto

Para preguntas o sugerencias, contacte al equipo de desarrollo.
