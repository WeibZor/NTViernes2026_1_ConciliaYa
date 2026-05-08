from typing import Annotated

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

# Importaciones de módulos de EstadoConflicto
from notebook.HU_6_Limpieza_EstadoConflicto import limpiar_estadosConflictos
from notebook.HU_7_Descripción_exploratoria_EstadoConflicto import descripcion_estado_conflicto
from utils.HU_8_Simulación_y_exportación_EstadoConflicto import generar_estadoConflictos

# Importaciones de módulos de Perfil
from notebook.HU16_limpiezaperfil import limpiar_perfil
from notebook.HU17_descripcion_perfil import descripcion_perfil
from notebook.HU19_query_perfil import consultas_perfil
from notebook.HU20_agrupacion_perfil import agrupaciones_perfil
from utils.simulacionperfil import generarPerfil

# Importaciones de módulos de TipoConflicto
from tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto
from tipoconflicto.HU_22_Descripcion_TipoConflicto import descripcion_tipos_conflicto
from tipoconflicto.HU_23_Simulacion_TipoConflicto import simular_y_exportar_tipos_conflicto, recargar_y_validar_tipos_conflicto
from tipoconflicto.HU_24_Query_TipoConflicto import consultas_tipos_conflicto
from tipoconflicto.HU_25_Agrupacion_TipoConflicto import agrupaciones_tipos_conflicto

# Importaciones de módulos de Usuario
from usuario.HU_26_Limpieza_Usuario import limpiar_usuarios
from usuario.HU_27_Descripcion_Usuario import descripcion_usuarios
from usuario.HU_28_Simulacion_Usuario import simular_y_exportar_usuarios, recargar_y_validar_usuarios
from usuario.HU_29_Query_Usuario import consultas_usuario
from usuario.HU_30_Agrupacion_Usuario import agrupaciones_usuario
from usuario.usuario_data import generar_datos_usuario

# Importaciones de módulos de Conflicto
from conflicto.HU_01_Limpieza_Conflicto import limpiar_conflictos
from conflicto.HU_02_Descripcion_Conflicto import descripcion_conflictos
from conflicto.HU_04_Query_Conflicto import consultas_conflicto
from conflicto.HU_05_Agrupacion_Conflicto import agrupaciones_conflicto
from conflicto.conflicto_data import generar_datos_conflicto

# Configuración de FastAPI
app = FastAPI(
    title="ConciliaYa Data API",
    version="1.0.0",
    description="API para integrar la lógica de limpieza, exploración, simulación y análisis de Usuario, EstadoConflicto, Perfil y Conflicto con el frontend React."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def ejecutar_procesamiento_completo():
    """Función que ejecuta todo el procesamiento de datos y muestra resultados."""
    # Procesamiento de Perfil
    perfiles = generarPerfil(1000)
    perfiles_ordenados = pd.DataFrame(perfiles)
    simulaciones_perfil_limpias = limpiar_perfil(perfiles_ordenados)
    print(simulaciones_perfil_limpias)

    # describir Perfil
    descripcion_perfil(simulaciones_perfil_limpias)

    # consultas Perfil
    consultas_resultado_perfil = consultas_perfil(simulaciones_perfil_limpias)

    # agrupaciones Perfil
    agrupaciones_resultado_perfil = agrupaciones_perfil(simulaciones_perfil_limpias)

    # Procesamiento de Conflicto
    conflicto_original = generar_datos_conflicto(num_registros=1000)
    conflicto_limpio = limpiar_conflictos(conflicto_original)
    descripcion_conflictos(conflicto_limpio)
    consultas_resultado_conflicto = consultas_conflicto(conflicto_limpio)
    agrupaciones_resultado_conflicto = agrupaciones_conflicto(conflicto_limpio)

    # Procesamiento de EstadoConflicto
    simulacion_EstadoConflicto = generar_estadoConflictos(1000)
    simulacion_EstadoConflicto_ordenada = pd.DataFrame(simulacion_EstadoConflicto)
    simulacion_EstadoConflicto_limpia = limpiar_estadosConflictos(simulacion_EstadoConflicto_ordenada)
    descripcion_estado_conflicto(simulacion_EstadoConflicto_limpia)

    # Procesamiento de Usuario
    usuario_original = simular_y_exportar_usuarios(num_registros=1000, semilla=42)
    recargar_y_validar_usuarios(usuario_original)
    usuario_limpio = limpiar_usuarios(usuario_original)
    descripcion_usuarios(usuario_limpio)
    consultas_resultado = consultas_usuario(usuario_limpio)
    agrupaciones_resultado = agrupaciones_usuario(usuario_limpio)

    # Procesamiento de TipoConflicto
    tipoconflicto_original = simular_y_exportar_tipos_conflicto(num_registros=1000, semilla=42)
    recargar_y_validar_tipos_conflicto(tipoconflicto_original)
    tipoconflicto_limpio = limpiar_tipos_conflicto(tipoconflicto_original)
    descripcion_tipos_conflicto(tipoconflicto_limpio)
    consultas_tipoconflicto_resultado = consultas_tipos_conflicto(tipoconflicto_limpio)
    agrupaciones_tipoconflicto_resultado = agrupaciones_tipos_conflicto(tipoconflicto_limpio)

    # Resultados finales
    print("\nFlujo completo ejecutado: EstadoConflicto + Usuario + TipoConflicto + Perfil + Conflicto")
    print(f"EstadoConflicto limpio: {len(simulacion_EstadoConflicto_limpia)} registros")
    print(f"Usuario limpio: {len(usuario_limpio)} registros")
    print(f"TipoConflicto limpio: {len(tipoconflicto_limpio)} registros")
    print(f"Perfil limpio: {len(simulaciones_perfil_limpias)} registros")
    print(f"Conflicto limpio: {len(conflicto_limpio)} registros")
    print(f"Consultas generadas: {list(consultas_resultado.keys())}")
    print(f"Agrupaciones generadas: {list(agrupaciones_resultado.keys())}")
    print(f"Consultas TipoConflicto generadas: {list(consultas_tipoconflicto_resultado.keys())}")
    print(f"Agrupaciones TipoConflicto generadas: {list(agrupaciones_tipoconflicto_resultado.keys())}")
    print(f"Consultas Perfil generadas: {list(consultas_resultado_perfil.keys())}")
    print(f"Agrupaciones Perfil generadas: {list(agrupaciones_resultado_perfil.keys())}")
    print(f"Consultas Conflicto generadas: {list(consultas_resultado_conflicto.keys())}")
    print(f"Agrupaciones Conflicto generadas: {list(agrupaciones_resultado_conflicto.keys())}")


# Endpoints de la API

@app.get("/perfil/simular")
def simular_perfil(num_registros: int = 100):
    perfiles = generarPerfil(num_registros)
    return {"perfiles": perfiles}

@app.get("/perfil/limpiar")
def limpiar_perfil_endpoint(num_registros: int = 100):
    perfiles = generarPerfil(num_registros)
    df = pd.DataFrame(perfiles)
    df_limpio = limpiar_perfil(df)
    return df_limpio.to_dict(orient="records")

@app.get("/perfil/descripcion")
def descripcion_perfil_endpoint(num_registros: int = 100):
    perfiles = generarPerfil(num_registros)
    df = pd.DataFrame(perfiles)
    df_limpio = limpiar_perfil(df)
    desc = descripcion_perfil(df_limpio)
    return desc

@app.get("/perfil/consultas")
def consultas_perfil_endpoint(num_registros: int = 100):
    perfiles = generarPerfil(num_registros)
    df = pd.DataFrame(perfiles)
    df_limpio = limpiar_perfil(df)
    consultas = consultas_perfil(df_limpio)
    return {k: v.to_dict(orient="records") for k, v in consultas.items()}

@app.get("/perfil/agrupaciones")
def agrupaciones_perfil_endpoint(num_registros: int = 100):
    perfiles = generarPerfil(num_registros)
    df = pd.DataFrame(perfiles)
    df_limpio = limpiar_perfil(df)
    agrup = agrupaciones_perfil(df_limpio)
    return {k: v.to_dict(orient="records") for k, v in agrup.items()}


@app.get("/conflicto/simular")
def simular_conflicto(num_registros: int = 100):
    conflictos = generar_datos_conflicto(num_registros=num_registros)
    return {"conflictos": conflictos.to_dict(orient="records")}

@app.get("/conflicto/limpiar")
def limpiar_conflicto_endpoint(num_registros: int = 100):
    conflictos = generar_datos_conflicto(num_registros=num_registros)
    df_limpio = limpiar_conflictos(conflictos)
    return df_limpio.to_dict(orient="records")

@app.get("/conflicto/descripcion")
def descripcion_conflicto_endpoint(num_registros: int = 100):
    conflictos = generar_datos_conflicto(num_registros=num_registros)
    df_limpio = limpiar_conflictos(conflictos)
    desc = descripcion_conflictos(df_limpio)
    return desc

@app.get("/conflicto/consultas")
def consultas_conflicto_endpoint(num_registros: int = 100):
    conflictos = generar_datos_conflicto(num_registros=num_registros)
    df_limpio = limpiar_conflictos(conflictos)
    consultas = consultas_conflicto(df_limpio)
    return {k: v.to_dict(orient="records") for k, v in consultas.items()}

@app.get("/conflicto/agrupaciones")
def agrupaciones_conflicto_endpoint(num_registros: int = 100):
    conflictos = generar_datos_conflicto(num_registros=num_registros)
    df_limpio = limpiar_conflictos(conflictos)
    agrup = agrupaciones_conflicto(df_limpio)
    return {k: v.to_dict(orient="records") for k, v in agrup.items()}


if __name__ == "__main__":
    ejecutar_procesamiento_completo()
    uvicorn.run(app, host="0.0.0.0", port=8000)
