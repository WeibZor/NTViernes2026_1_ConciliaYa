from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging
import json

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="ConciliaYa Classifier API",
    description="Microservicio de clasificación de conflictos vecinales",
    version="1.0.0"
)

# ==================== MODELOS ====================

class ClasificacionRequest(BaseModel):
    """Modelo para solicitud de clasificación."""
    descripcion: str = Field(..., min_length=20, description="Descripción del conflicto a clasificar")

    class Config:
        json_schema_extra = {
            "example": {
                "descripcion": "Mi vecino ha puesto música muy fuerte a las 3 de la mañana durante varios días, afectando mi descanso"
            }
        }


class ClasificacionResponse(BaseModel):
    """Modelo para respuesta de clasificación."""
    tipoConflictoId: int = Field(..., description="ID del tipo de conflicto identificado")
    tipoConflictoNombre: str = Field(..., description="Nombre del tipo de conflicto")
    confianza: float = Field(..., ge=0.0, le=1.0, description="Nivel de confianza de la clasificación (0-1)")
    justificacion: Optional[str] = Field(None, description="Explicación de por qué se clasificó así")

    class Config:
        json_schema_extra = {
            "example": {
                "tipoConflictoId": 1,
                "tipoConflictoNombre": "Ruido y molestias",
                "confianza": 0.95,
                "justificacion": "Se detectaron palabras clave: música, ruido, molestias. Horario nocturno indicado."
            }
        }


class HealthResponse(BaseModel):
    """Modelo para respuesta de salud del servicio."""
    status: str = Field(..., description="Estado del servicio")
    version: str = Field(..., description="Versión del servicio")


# ==================== DICCIONARIO DE CLASIFICACIÓN ====================

TIPOS_CONFLICTO = {
    1: "Ruido y molestias",
    2: "Estacionamiento",
    3: "Mascota",
    4: "Propiedad y límites",
    5: "Servicios e instalaciones",
    6: "Comportamiento molesto",
    7: "Construcción y reformas",
    8: "Basura y limpieza",
    9: "Mascotas",
    10: "Otros"
}

# Palabras clave para clasificación
PALABRAS_CLAVE = {
    1: [
        "ruido", "música", "sonido", "volumen", "bulla", "escándalo",
        "molestia", "dormir", "sueño", "descanso", "madrugada", "noche",
        "altavoz", "bocina", "parlante", "estrépito", "barullo"
    ],
    2: [
        "estacionamiento", "parqueo", "coche", "auto", "vehículo", "carro",
        "parqueado", "parked", "ocupado", "espacio", "prohibido", "zona azul",
        "multa", "denuncia", "delinea", "cochera"
    ],
    3: [
        "perro", "gato", "mascota", "animal", "ladridos", "ladra", "maullar",
        "mascota", "correa", "jaula", "heces", "orines", "excremento",
        "evacuación", "necesidades", "paseo"
    ],
    4: [
        "propiedad", "límite", "lindero", "frontera", "muro", "pared", "valla",
        "cerca", "invasión", "ocupación", "terreno", "lote", "colindancia",
        "amojonamiento", "servidumbre"
    ],
    5: [
        "agua", "luz", "electricidad", "gas", "tubería", "cañería", "alcantarilla",
        "desagüe", "fuga", "cortada", "corte", "servicio básico", "consumo",
        "medidor", "factura"
    ],
    6: [
        "comportamiento", "conducta", "grosería", "insulto", "amenaza", "agresión",
        "acoso", "hostigamiento", "molesto", "irritante", "desagradable",
        "intolerante", "falta de consideración"
    ],
    7: [
        "construcción", "reforma", "obra", "remodelación", "reparación", "ampliación",
        "demolición", "polvo", "escombro", "maquinaria", "ruido", "horario",
        "permiso", "autorización"
    ],
    8: [
        "basura", "desecho", "residuo", "basurero", "contenedor", "reciclaje",
        "limpieza", "suciedad", "mugre", "inmundicia", "plagas", "cucaracha",
        "rata", "higiene"
    ]
}


# ==================== FUNCIONES AUXILIARES ====================

def normalizar_texto(texto: str) -> str:
    """
    Normaliza el texto para búsqueda.
    Función pura sin efectos secundarios.
    """
    return texto.lower().strip()


def contar_palabras_clave(descripcion: str, palabras: list) -> int:
    """
    Cuenta cuántas palabras clave se encuentran en la descripción.
    Utiliza programación funcional (map, filter, reduce).
    """
    descripcion_norm = normalizar_texto(descripcion)
    palabras_encontradas = [
        palabra for palabra in palabras
        if palabra in descripcion_norm
    ]
    return len(palabras_encontradas)


def calcular_confianza(conteo: int, total_palabras: int) -> float:
    """
    Calcula la confianza basada en el conteo de palabras clave.
    Implementa lógica pura sin efectos secundarios.
    
    Args:
        conteo: Cantidad de palabras clave encontradas
        total_palabras: Total de palabras clave en la categoría
    
    Returns:
        Confianza entre 0 y 1
    """
    if total_palabras == 0:
        return 0.0
    
    confianza = min(conteo / total_palabras, 1.0)
    # Aplicar mínimo de 0.5 si se encuentra alguna palabra clave
    return max(confianza, 0.5) if conteo > 0 else 0.0


def clasificar_conflicto_puro(descripcion: str) -> dict:
    """
    Lógica pura de clasificación sin dependencias externas.
    Función pura: mismo input siempre da mismo output.
    Sin efectos secundarios.
    """
    descripcion_norm = normalizar_texto(descripcion)
    
    # Calcular puntuación para cada tipo
    puntuaciones = {}
    para_cada tipo, palabras in PALABRAS_CLAVE.items():
        conteo = contar_palabras_clave(descripcion_norm, palabras)
        confianza = calcular_confianza(conteo, len(palabras))
        puntuaciones[tipo] = {
            "conteo": conteo,
            "confianza": confianza
        }
    
    # Encontrar el tipo con mayor confianza
    mejor_tipo = max(
        puntuaciones.items(),
        key=lambda x: x[1]["confianza"]
    )
    
    tipo_id = mejor_tipo[0]
    confianza = mejor_tipo[1]["confianza"]
    
    # Si no hay palabras clave encontradas, clasificar como "Otros"
    if confianza == 0.0:
        tipo_id = 10
        confianza = 0.3  # Baja confianza
    
    return {
        "tipo_id": tipo_id,
        "confianza": confianza,
        "palabras_encontradas": mejor_tipo[1]["conteo"]
    }


def generar_justificacion(tipo_id: int, palabras_encontradas: int) -> str:
    """
    Genera una justificación para la clasificación.
    Función pura que mapea clasificación a explicación.
    """
    tipo_nombre = TIPOS_CONFLICTO.get(tipo_id, "Desconocido")
    
    if palabras_encontradas > 3:
        return f"Se detectaron palabras clave características de '{tipo_nombre}'. Clasificación con alta confiabilidad."
    elif palabras_encontradas > 0:
        return f"Se detectaron palabras relacionadas con '{tipo_nombre}'."
    else:
        return f"Clasificado como '{tipo_nombre}' por falta de palabras clave específicas."


# ==================== ENDPOINTS ====================

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Verifica la salud del servicio.
    GET /health
    """
    return HealthResponse(
        status="healthy",
        version="1.0.0"
    )


@app.post("/api/v1/classify-conflict", response_model=ClasificacionResponse, tags=["Classification"])
async def clasificar_conflicto(request: ClasificacionRequest) -> ClasificacionResponse:
    """
    Clasifica un conflicto vecinal basándose en su descripción.
    
    Args:
        request: ConflictoRequest con la descripción del conflicto
    
    Returns:
        ClasificacionResponse con el tipo de conflicto identificado
    
    Raises:
        HTTPException: Si la solicitud es inválida
    
    Ejemplo:
        POST /api/v1/classify-conflict
        {
            "descripcion": "Mi vecino ha puesto música muy fuerte a las 3 de la mañana"
        }
    """
    try:
        # Validar entrada
        if not request.descripcion or len(request.descripcion.strip()) < 20:
            raise HTTPException(
                status_code=400,
                detail="La descripción debe tener al menos 20 caracteres"
            )
        
        # Clasificar usando lógica pura
        resultado = clasificar_conflicto_puro(request.descripcion)
        
        tipo_id = resultado["tipo_id"]
        tipo_nombre = TIPOS_CONFLICTO[tipo_id]
        confianza = resultado["confianza"]
        palabras_encontradas = resultado["palabras_encontradas"]
        
        # Generar justificación
        justificacion = generar_justificacion(tipo_id, palabras_encontradas)
        
        logger.info(
            f"Conflicto clasificado: tipo={tipo_nombre}, confianza={confianza:.2f}"
        )
        
        return ClasificacionResponse(
            tipoConflictoId=tipo_id,
            tipoConflictoNombre=tipo_nombre,
            confianza=round(confianza, 2),
            justificacion=justificacion
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en clasificación: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error interno en el servicio de clasificación"
        )


@app.get("/api/v1/tipos-conflicto", tags=["Data"])
async def obtener_tipos_conflicto():
    """
    Obtiene la lista de tipos de conflicto disponibles.
    GET /api/v1/tipos-conflicto
    """
    tipos = [
        {"id": tipo_id, "nombre": nombre}
        for tipo_id, nombre in TIPOS_CONFLICTO.items()
    ]
    return {"tipos": tipos}


@app.get("/", tags=["Info"])
async def raiz():
    """
    Raíz de la API con información.
    """
    return {
        "nombre": "ConciliaYa Classifier API",
        "descripcion": "Microservicio de clasificación inteligente de conflictos vecinales",
        "version": "1.0.0",
        "endpoints": [
            "/health - Verificar salud del servicio",
            "/api/v1/classify-conflict - Clasificar un conflicto",
            "/api/v1/tipos-conflicto - Obtener tipos disponibles",
            "/docs - Documentación Swagger",
            "/redoc - Documentación ReDoc"
        ]
    }


# ==================== MANEJO DE ERRORES ====================

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    """Manejador global de excepciones."""
    logger.error(f"Error no capturado: {str(exc)}")
    return {
        "error": "Error interno del servidor",
        "detail": str(exc)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
