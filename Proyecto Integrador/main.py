from typing import Annotated

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

# importar simulaciones EstadoConflicto
from utils.HU_8_Simulación_y_exportación_EstadoConflicto import generar_estadoConflictos

# importar limpiezas EstadoConflicto
from notebook.HU_6_Limpieza_EstadoConflicto import limpiar_estadosConflictos

# importar descripciones EstadoConflicto
from notebook.HU_7_Descripción_exploratoria_EstadoConflicto import descripcion_estado_conflicto

# importar simulaciones Usuario
from usuario.HU_28_Simulacion_Usuario import simular_y_exportar_usuarios, recargar_y_validar_usuarios

# importar limpieza Usuario
from usuario.HU_26_Limpieza_Usuario import limpiar_usuarios

# importar descripción Usuario
from usuario.HU_27_Descripcion_Usuario import descripcion_usuarios

# importar consultas Usuario
from usuario.HU_29_Query_Usuario import consultas_usuario

# importar agrupaciones Usuario
from usuario.HU_30_Agrupacion_Usuario import agrupaciones_usuario

# importar simulaciones TipoConflicto
from tipoconflicto.HU_23_Simulacion_TipoConflicto import simular_y_exportar_tipos_conflicto, recargar_y_validar_tipos_conflicto

# importar limpieza TipoConflicto
from tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto

# importar descripción TipoConflicto
from tipoconflicto.HU_22_Descripcion_TipoConflicto import descripcion_tipos_conflicto

# importar consultas TipoConflicto
from tipoconflicto.HU_24_Query_TipoConflicto import consultas_tipos_conflicto

# importar agrupaciones TipoConflicto
from tipoconflicto.HU_25_Agrupacion_TipoConflicto import agrupaciones_tipos_conflicto

# importar Conflicto
from conflicto.conflicto_data import generar_datos_conflicto
from conflicto.HU_01_Limpieza_Conflicto import limpiar_conflictos
from conflicto.HU_02_Descripcion_Conflicto import descripcion_conflictos
from conflicto.HU_04_Query_Conflicto import consultas_conflicto
from conflicto.HU_05_Agrupacion_Conflicto import agrupaciones_conflicto

#importar simulaciones del perfil
from utils.simulacionperfil import generarPerfil

#importar rutina de limpieza del prefil
from notebook.HU16_limpiezaperfil import limpiar_perfil

from usuario.usuario_data import generar_datos_usuario

app = FastAPI(
    title="ConciliaYa Data API",
    version="1.0.0",
    description="API para integrar la lógica de limpieza, exploración, simulación y análisis de Usuario, EstadoConflicto y Perfil con el frontend React."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

perfiles_ordenados=pd.DataFrame(perfiles)

simulaciones_perfil_limpias=limpiar_perfil(perfiles_ordenados)
print(simulaciones_perfil_limpias)


# crear simulaciones EstadoConflicto
simulacion_EstadoConflicto = generar_estadoConflictos(1000)

# ordenar simulaciones EstadoConflicto
simulacion_EstadoConflicto_ordenada = pd.DataFrame(simulacion_EstadoConflicto)

# limpiando los sets de datos EstadoConflicto
simulacion_EstadoConflicto_limpia = limpiar_estadosConflictos(simulacion_EstadoConflicto_ordenada)

# describiendo los datos EstadoConflicto
descripcion_estado_conflicto(simulacion_EstadoConflicto_limpia)


# crear simulación Usuario
usuario_original = simular_y_exportar_usuarios(num_registros=1000, semilla=42)

# recargar y validar Usuario
recargar_y_validar_usuarios(usuario_original)

# limpiar Usuario
usuario_limpio = limpiar_usuarios(usuario_original)

# describir Usuario
descripcion_usuarios(usuario_limpio)

# consultas Usuario
consultas_resultado = consultas_usuario(usuario_limpio)

# agrupaciones Usuario
agrupaciones_resultado = agrupaciones_usuario(usuario_limpio)


# crear simulación TipoConflicto
tipoconflicto_original = simular_y_exportar_tipos_conflicto(num_registros=1000, semilla=42)

# recargar y validar TipoConflicto
recargar_y_validar_tipos_conflicto(tipoconflicto_original)

# limpiar TipoConflicto
tipoconflicto_limpio = limpiar_tipos_conflicto(tipoconflicto_original)

# describir TipoConflicto
descripcion_tipos_conflicto(tipoconflicto_limpio)

# consultas TipoConflicto
consultas_tipoconflicto_resultado = consultas_tipos_conflicto(tipoconflicto_limpio)

# agrupaciones TipoConflicto
agrupaciones_tipoconflicto_resultado = agrupaciones_tipos_conflicto(tipoconflicto_limpio)

# crear simulación Conflicto
conflicto_original = generar_datos_conflicto(num_registros=1000, semilla=42)

# limpiar Conflicto
conflicto_limpio = limpiar_conflictos(conflicto_original)

# describir Conflicto
descripcion_conflictos(conflicto_limpio)

# consultas Conflicto
consultas_conflicto_resultado = consultas_conflicto(conflicto_limpio)

# agrupaciones Conflicto
agrupaciones_conflicto_resultado = agrupaciones_conflicto(conflicto_limpio)






# resultados finales
print("\nFlujo completo ejecutado: EstadoConflicto + Usuario + TipoConflicto + Conflicto")
print(f"EstadoConflicto limpio: {len(simulacion_EstadoConflicto_limpia)} registros")
print(f"Usuario limpio: {len(usuario_limpio)} registros")
print(f"TipoConflicto limpio: {len(tipoconflicto_limpio)} registros")
print(f"Conflicto limpio: {len(conflicto_limpio)} registros")
print(f"Consultas generadas: {list(consultas_resultado.keys())}")
print(f"Agrupaciones generadas: {list(agrupaciones_resultado.keys())}")
print(f"Consultas TipoConflicto generadas: {list(consultas_tipoconflicto_resultado.keys())}")
print(f"Agrupaciones TipoConflicto generadas: {list(agrupaciones_tipoconflicto_resultado.keys())}")
print(f"Consultas Conflicto generadas: {list(consultas_conflicto_resultado.keys())}")
print(f"Agrupaciones Conflicto generadas: {list(agrupaciones_conflicto_resultado.keys())}")