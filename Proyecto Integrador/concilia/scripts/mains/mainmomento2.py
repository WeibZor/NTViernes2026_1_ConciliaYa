"""
Main de Prueba para Demostración al Profesor
Incluye simulación, limpieza y descripción para los módulos principales.
"""

from typing import Annotated

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

# Importaciones de módulos de EstadoConflicto
from concilia.domain.notebook.HU_6_Limpieza_EstadoConflicto import limpiar_estadosConflictos
from concilia.domain.notebook.HU_7_Descripción_exploratoria_EstadoConflicto import descripcion_estado_conflicto
from concilia.domain.utils.HU_8_Simulación_y_exportación_EstadoConflicto import generar_estadoConflictos

# Importaciones de módulos de Perfil
from concilia.domain.notebook.HU16_limpiezaperfil import limpiar_perfil
from concilia.domain.notebook.HU17_descripcion_perfil import descripcion_perfil
from concilia.domain.utils.simulacionperfil import generarPerfil

# Importaciones de módulos de TipoConflicto
from concilia.domain.tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto
from concilia.domain.tipoconflicto.HU_22_Descripcion_TipoConflicto import descripcion_tipos_conflicto
from concilia.domain.tipoconflicto.HU_23_Simulacion_TipoConflicto import simular_y_exportar_tipos_conflicto

# Importaciones de módulos de Usuario
from concilia.domain.usuario.HU_26_Limpieza_Usuario import limpiar_usuarios
from concilia.domain.usuario.HU_27_Descripcion_Usuario import descripcion_usuarios
from concilia.domain.usuario.HU_28_Simulacion_Usuario import simular_y_exportar_usuarios

# Importaciones de módulos de Conflicto
from concilia.domain.conflicto.HU_01_Limpieza_Conflicto import limpiar_conflictos
from concilia.domain.conflicto.HU_02_Descripcion_Conflicto import descripcion_conflictos
from concilia.domain.conflicto.conflicto_data import generar_datos_conflicto

# Configuración de FastAPI
app = FastAPI(
    title="ConciliaYa Data API - Demo",
    version="1.0.0",
    description="API de demostración para limpieza, simulación y descripción de datos."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def demo_procesamiento():
    """Función de demostración que ejecuta simulación, limpieza y descripción para cada módulo."""
    print("=== DEMO: Simulación, Limpieza y Descripción ===\n")

    # 1. EstadoConflicto
    print("1. EstadoConflicto:")
    simulacion_EstadoConflicto = generar_estadoConflictos(100)
    simulacion_EstadoConflicto_df = pd.DataFrame(simulacion_EstadoConflicto)
    simulacion_EstadoConflicto_limpia = limpiar_estadosConflictos(simulacion_EstadoConflicto_df)
    descripcion_estado_conflicto(simulacion_EstadoConflicto_limpia)
    print(f"Registros limpios: {len(simulacion_EstadoConflicto_limpia)}\n")

    # 2. Perfil
    print("2. Perfil:")
    perfiles = generarPerfil(100)
    perfiles_df = pd.DataFrame(perfiles)
    perfiles_limpios = limpiar_perfil(perfiles_df)
    descripcion_perfil(perfiles_limpios)
    print(f"Registros limpios: {len(perfiles_limpios)}\n")

    # 3. TipoConflicto
    print("3. TipoConflicto:")
    tipoconflicto_original = simular_y_exportar_tipos_conflicto(num_registros=100, semilla=42)
    tipoconflicto_limpio = limpiar_tipos_conflicto(tipoconflicto_original)
    descripcion_tipos_conflicto(tipoconflicto_limpio)
    print(f"Registros limpios: {len(tipoconflicto_limpio)}\n")

    # 4. Usuario
    print("4. Usuario:")
    usuario_original = simular_y_exportar_usuarios(num_registros=100, semilla=42)
    usuario_limpio = limpiar_usuarios(usuario_original)
    descripcion_usuarios(usuario_limpio)
    print(f"Registros limpios: {len(usuario_limpio)}\n")

    # 5. Conflicto
    print("5. Conflicto:")
    conflicto_original = generar_datos_conflicto(num_registros=100)
    conflicto_limpio = limpiar_conflictos(conflicto_original)
    descripcion_conflictos(conflicto_limpio)
    print(f"Registros limpios: {len(conflicto_limpio)}\n")

    print("=== DEMO COMPLETADA ===")


# Endpoints de la API para demostración

@app.get("/demo")
def ejecutar_demo():
    """Endpoint para ejecutar la demostración completa."""
    demo_procesamiento()
    return {"mensaje": "Demo ejecutada. Revisa la consola para los resultados."}

@app.get("/estado_conflicto/demo")
def demo_estado_conflicto():
    simulacion = generar_estadoConflictos(50)
    df = pd.DataFrame(simulacion)
    df_limpio = limpiar_estadosConflictos(df)
    descripcion_estado_conflicto(df_limpio)
    return {"registros_limpios": len(df_limpio)}

@app.get("/perfil/demo")
def demo_perfil():
    perfiles = generarPerfil(50)
    df = pd.DataFrame(perfiles)
    df_limpio = limpiar_perfil(df)
    descripcion_perfil(df_limpio)
    return {"registros_limpios": len(df_limpio)}

@app.get("/tipoconflicto/demo")
def demo_tipoconflicto():
    original = simular_y_exportar_tipos_conflicto(num_registros=50, semilla=42)
    df_limpio = limpiar_tipos_conflicto(original)
    descripcion_tipos_conflicto(df_limpio)
    return {"registros_limpios": len(df_limpio)}

@app.get("/usuario/demo")
def demo_usuario():
    original = simular_y_exportar_usuarios(num_registros=50, semilla=42)
    df_limpio = limpiar_usuarios(original)
    descripcion_usuarios(df_limpio)
    return {"registros_limpios": len(df_limpio)}

@app.get("/conflicto/demo")
def demo_conflicto():
    original = generar_datos_conflicto(num_registros=50)
    df_limpio = limpiar_conflictos(original)
    descripcion_conflictos(df_limpio)
    return {"registros_limpios": len(df_limpio)}


if __name__ == "__main__":
    demo_procesamiento()
    uvicorn.run(app, host="0.0.0.0", port=8001)
