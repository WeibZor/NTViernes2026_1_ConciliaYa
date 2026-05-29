import pandas as pd

# ==============================================================================
# 1. IMPORTS
# ==============================================================================

# Capa de Simulación (utils)
from utils.simulacion_estadoconflicto import generar_estadoConflictos
from utils.simulacion_perfil import generarPerfil
from utils.simulacion_usuario import generar_simulacion_usuarios
from utils.simulacion_tipoconflicto import generar_simulacion_tipoConflicto
from utils.simulacion_conflicto import generar_simulacion_conflicto
from utils.simulacion_mediacion import generar_simulacion_mediacion

# Capa de Limpieza (notebook)
from notebook.limpieza_estadoconflicto import limpiar_estadoConflictos
from notebook.limpieza_perfil import limpiar_perfil
from notebook.limpieza_usuraios import limpiar_usuarios       # respetando typo del archivo
from notebook.limpieza_tipoconflicto import limpiar_tipoConflicto
from notebook.limpieza_conflicto import limpiar_conflicto
from notebook.limpieza_mediacion import limpiar_mediacion

# Capa de Descripción (notebook)
from notebook.descripcion_estadoconflicto import describir_estadoConflictos
from notebook.descripcion_perfil import describir_perfil
from notebook.descripcion_usuario import describir_usuarios
from notebook.descripcion_tipoconflicto import describir_tipoConflicto
from notebook.descripcion_conflicto import describir_conflicto
from notebook.descripcion_mediacion import describir_mediacion

# Capa de Transformación (notebook)
from notebook.tranformacion_estadoconflicto import transformar_datos_estadoConflictos
from notebook.transformacion_perfil import transformar_datos_perfil
from notebook.transformacion_usuario import transformar_datos_usuarios
from notebook.transformacion_tipoconflicto import transformar_datos_tipoConflicto
from notebook.transformacion_conflicto import transformar_datos_conflicto
from notebook.transformacion_mediacion import transformar_datos_mediacion

# Capa de Graficación (notebook)
from notebook.graficar import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

# ==============================================================================
# REFERENCIA DE ENDPOINTS DEL SPRING BOOT
# GET /api/estados-conflicto  → DTO:    { id, nombre, codigo, descripcion, activo }
# GET /api/perfiles           → DTO:    { id, nombre, descripcion, activo }
#                               ⚠ PerfilDto NO expone fechaAlta
# GET /api/tipos-conflicto    → DTO:    { id, nombre, descripcion, activo }
# GET /api/usuarios           → Entidad:{ id, nombre, apellido, tipoDocumento,
#                                         documento, correo, telefono,
#                                         perfil:{id,nombre,descripcion,activo},
#                                         activo, fechaAlta }
# GET /api/conflictos         → Entidad:{ id, usuarioDemandante{...},
#                                         usuarioDemandado{...}, tipoConflicto{...},
#                                         estadoConflicto{...}, asunto, descripcion,
#                                         fechaInicio, fechaCierre, resultado,
#                                         montoReclamado, activo, fechaAlta }
# GET /api/mediaciones        → Entidad:{ id, conflicto{...}, usuarioMediador{...},
#                                         estadoConflicto{...}, fechaProgramada,
#                                         lugar, observaciones, resultado,
#                                         fechaRegistro, activo }
# ==============================================================================

# ==============================================================================
# 2. SIMULACIÓN (replica las respuestas reales del Spring Boot)
# ==============================================================================
print("=== CAPA 1: GENERANDO SIMULACIONES (1000 REGISTROS POR TABLA) ===")

simulacion_ec   = generar_estadoConflictos(1000)
simulacion_perf = generarPerfil(1000)
simulacion_user = generar_simulacion_usuarios(1000)
simulacion_tc   = generar_simulacion_tipoConflicto(1000)
simulacion_conf = generar_simulacion_conflicto(1000)
simulacion_med  = generar_simulacion_mediacion(1000)

df_ec_sucio   = pd.DataFrame(simulacion_ec)
df_perf_sucio = pd.DataFrame(simulacion_perf)
df_user_sucio = pd.DataFrame(simulacion_user)
df_tc_sucio   = pd.DataFrame(simulacion_tc)
df_conf_sucio = pd.DataFrame(simulacion_conf)
df_med_sucio  = pd.DataFrame(simulacion_med)

print("✔ Simulaciones cargadas en DataFrames sucios.\n")

# ==============================================================================
# 3. LIMPIEZA
#    - Aplana objetos anidados (usuario.perfil → perfilId, perfilNombre)
#    - Normaliza textos, booleanos y fechas
#    - Elimina registros con errores controlados
# ==============================================================================
print("=== CAPA 2: EJECUTANDO LIMPIEZA DE DATOS ===")

df_ec_limpio   = limpiar_estadoConflictos(df_ec_sucio)
df_perf_limpio = limpiar_perfil(df_perf_sucio)
df_user_limpio = limpiar_usuarios(df_user_sucio)
df_tc_limpio   = limpiar_tipoConflicto(df_tc_sucio)
df_conf_limpio = limpiar_conflicto(df_conf_sucio)
df_med_limpio  = limpiar_mediacion(df_med_sucio)

print("✔ Datos normalizados y registros corruptos eliminados.\n")

# ==============================================================================
# 4. DESCRIPCIÓN
# ==============================================================================
print("=== CAPA 3: DESCRIBIENDO DATOS LIMPIOS ===")

describir_estadoConflictos(df_ec_limpio)
describir_perfil(df_perf_limpio)
describir_usuarios(df_user_limpio)
describir_tipoConflicto(df_tc_limpio)
describir_conflicto(df_conf_limpio)
describir_mediacion(df_med_limpio)

print("\n✔ Descripciones impresas.\n")

# ==============================================================================
# 5. TRANSFORMACIÓN
# ==============================================================================
print("=== CAPA 4: APLICANDO AGRUPACIONES ===")

res_ec   = transformar_datos_estadoConflictos(df_ec_limpio)
res_perf = transformar_datos_perfil(df_perf_limpio)
res_user = transformar_datos_usuarios(df_user_limpio)
res_tc   = transformar_datos_tipoConflicto(df_tc_limpio)
res_conf = transformar_datos_conflicto(df_conf_limpio)
res_med  = transformar_datos_mediacion(df_med_limpio)

print("✔ Resúmenes creados.\n")

# ==============================================================================
# 6. GRAFICACIÓN — 6 gráficos con sentido de negocio real
#
# TABLA            | AGRUPACIÓN | COLUMNAS                              | TIPO
# -----------------|------------|---------------------------------------|----------
# EstadoConflicto  | ag2        | nombre, conteo                        | Torta
# Perfil           | ag1        | nombre, conteo                        | Barras
# TipoConflicto    | ag3        | nombre, conteo                        | Torta
# Usuario          | ag3        | tipoDocumento, perfilNombre, conteo   | Mapa Calor
# Conflicto        | ag3        | tipoConflictoNombre, estadoConf..., conteo | Mapa Calor
# Mediacion        | ag3        | lugar, resultado, conteo              | Mapa Calor
# ==============================================================================
print("=== CAPA 5: GENERANDO GRÁFICOS ESTADÍSTICOS EN EL FRONT ===")

# ------------------------------------------------------------------
# Gráfico 1 — EstadoConflicto → Torta
# ¿Qué proporción tienen los estados activos (Abierto / Cerrado / En Proceso)?
# Columnas: nombre | conteo
# ------------------------------------------------------------------
graficar_torta(
    res_ec["agrupacion2"],
    columna_etiquetas="nombre",
    columna_valores="conteo",
    titulo="Distribución de Estados de Conflicto Activos",
    nombre_archivo="torta_estado_conflicto_activos.png"
)

# ------------------------------------------------------------------
# Gráfico 2 — Perfil → Barras
# ¿Cuántos registros existen de cada tipo de perfil (administrador / gestor / usuario)?
# Columnas: nombre | conteo
# ------------------------------------------------------------------
graficar_barras(
    res_perf["agrupacion1"],
    columna_categorias="nombre",
    columna_valores="conteo",
    titulo="Cantidad de Registros por Tipo de Perfil",
    color_barras="#7E57C2",
    nombre_archivo="barras_perfiles_por_tipo.png"
)

# ------------------------------------------------------------------
# Gráfico 3 — TipoConflicto → Torta
# ¿Qué tipos de conflicto están activos y en qué proporción?
# Columnas: nombre | conteo
# ------------------------------------------------------------------
graficar_torta(
    res_tc["agrupacion3"],
    columna_etiquetas="nombre",
    columna_valores="conteo",
    titulo="Proporción de Tipos de Conflicto Activos",
    nombre_archivo="torta_tipos_conflicto_activos.png"
)

# ------------------------------------------------------------------
# Gráfico 4 — Usuario → Mapa de Calor
# ¿Qué combinación de tipo de documento × perfil es más frecuente?
# Permite detectar qué perfil predomina en cada tipo documental.
# Columnas: tipoDocumento | perfilNombre | conteo
# ------------------------------------------------------------------
graficar_mapa_calor(
    res_user["agrupacion3"],
    columna_filas="tipoDocumento",
    columna_columnas="perfilNombre",
    columna_valores="conteo",
    titulo="Usuarios: Tipo de Documento × Perfil Asignado",
    paleta_color="Blues",
    nombre_archivo="mapa_calor_usuarios_docperfil.png"
)

# ------------------------------------------------------------------
# Gráfico 5 — Conflicto → Mapa de Calor
# ¿En qué estado se encuentran los conflictos según su tipo?
# La celda más oscura indica la combinación más crítica del sistema.
# Columnas: tipoConflictoNombre | estadoConflictoNombre | conteo
# ------------------------------------------------------------------
graficar_mapa_calor(
    res_conf["agrupacion3"],
    columna_filas="tipoConflictoNombre",
    columna_columnas="estadoConflictoNombre",
    columna_valores="conteo",
    titulo="Conflictos: Tipo × Estado (Densidad de Casos)",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_conflictos_tipo_estado.png"
)

# ------------------------------------------------------------------
# Gráfico 6 — Mediación → Mapa de Calor
# ¿En qué sede se logran más acuerdos firmados y dónde fracasan más?
# Permite tomar decisiones sobre la asignación de sedes.
# Columnas: lugar | resultado | conteo
# ------------------------------------------------------------------
graficar_mapa_calor(
    res_med["agrupacion3"],
    columna_filas="lugar",
    columna_columnas="resultado",
    columna_valores="conteo",
    titulo="Mediaciones: Sede × Resultado (¿Dónde se logran más acuerdos?)",
    paleta_color="Greens",
    nombre_archivo="mapa_calor_mediaciones_sede_resultado.png"
)

print("\n✔ 6 gráficos exportados exitosamente al Front-End.")
print("=== PIPELINE TOTALMENTE FINALIZADO ===")
