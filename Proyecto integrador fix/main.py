import pandas as pd

# ==============================================================================
# 1. IMPORTS DE TUS MÓDULOS (Según tu árbol de carpetas en VS Code)
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
from notebook.limpieza_usuraios import limpiar_usuarios  # Respetando typo del archivo
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

# Capa de Graficación Genérica (notebook)
from notebook.graficar import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

#2. CAPA DE SIMULACIÓN

print("=== CAPA 1: GENERANDO SIMULACIONES (1000 REGISTROS POR TABLA) ===")

simulacion_ec = generar_estadoConflictos(1000)
simulacion_perf = generarPerfil(1000)
simulacion_user = generar_simulacion_usuarios(1000)
simulacion_tc = generar_simulacion_tipoConflicto(1000)
simulacion_conf = generar_simulacion_conflicto(1000)
simulacion_med = generar_simulacion_mediacion(1000)

# Conversión inmediata a DataFrames crudos
df_ec_sucio = pd.DataFrame(simulacion_ec)
df_perf_sucio = pd.DataFrame(simulacion_perf)
df_user_sucio = pd.DataFrame(simulacion_user)
df_tc_sucio = pd.DataFrame(simulacion_tc)
df_conf_sucio = pd.DataFrame(simulacion_conf)
df_med_sucio = pd.DataFrame(simulacion_med)

print("✔ Todas las simulaciones han sido cargadas en DataFrames sucios.\n")

# 3. CAPA DE LIMPIEZA (Procesamiento y Filtro de Basura)

print("=== CAPA 2: EJECUTANDO LIMPIEZA DE DATOS ===")

df_ec_limpio = limpiar_estadoConflictos(df_ec_sucio)
df_perf_limpio = limpiar_perfil(df_perf_sucio)
df_user_limpio = limpiar_usuarios(df_user_sucio)
df_tc_limpio = limpiar_tipoConflicto(df_tc_sucio)
df_conf_limpio = limpiar_conflicto(df_conf_sucio)
df_med_limpio = limpiar_mediacion(df_med_sucio)

print("✔ Datos normalizados y filas corruptas eliminadas con éxito.\n")

# 4. CAPA DE TRANSFORMACIÓN (Preparación para Gráficos)

print("=== CAPA 3: APLICANDO QUERIES Y AGRUPACIONES (RESÚMENES) ===")

resumen_transformacion_ec = transformar_datos_estadoConflictos(df_ec_limpio)
resumen_transformacion_perf = transformar_datos_perfil(df_perf_limpio)
resumen_transformacion_user = transformar_datos_usuarios(df_user_limpio)
resumen_transformacion_tc = transformar_datos_tipoConflicto(df_tc_limpio)
resumen_transformacion_conf = transformar_datos_conflicto(df_conf_limpio)
resumen_transformacion_med = transformar_datos_mediacion(df_med_limpio)

print("✔ Diccionarios 'agrupacion_resumen' creados para cada entidad.\n")



# 5. CAPA DE GRAFICACIÓN (Un gráfico seleccionado por cada tabla)

print("=== CAPA 4: GENERANDO GRÁFICOS ESTADÍSTICOS EN EL FRONT ===")

# Gráfico 1 (Tabla: Estado Conflictos) -> ¡Gráfico de Torta!
graficar_torta(
    resumen_transformacion_ec["agrupacion3"],
    columna_etiquetas="nombre",
    columna_valores="conteo",
    titulo="Proporción de Nombres en Estados Activos (True)",
    nombre_archivo="torta_estados_activos.png"
)

# Gráfico 2 (Tabla: Perfil) -> ¡Gráfico de Líneas!
graficar_lineas(
    resumen_transformacion_perf["agrupacion2"],
    columna_eje_x="fecha",
    columna_eje_y="conteo",
    titulo="Tendencia de Creación de Perfiles Activos en el Tiempo",
    color_linea="#FF5722",
    nombre_archivo="lineas_perfiles_activos.png"
)

# Gráfico 3 (Tabla: Usuarios) -> ¡Gráfico de Barras!
graficar_barras(
    resumen_transformacion_user["agrupacion2"],
    columna_categorias="PerfilId",
    columna_valores="conteo",
    titulo="Cantidad de Usuarios con DNI asignados por Perfil",
    color_barras="#2196F3",
    nombre_archivo="barras_usuarios_dni.png"
)

# Gráfico 4 (Tabla: Tipo Conflicto) -> ¡Gráfico de Barras!
graficar_barras(
    resumen_transformacion_tc["agrupacion1"],
    columna_categorias="Descripcion",
    columna_valores="conteo",
    titulo="Frecuencia de Descripciones en Conflictos de Tipo Pago",
    color_barras="#4CAF50",
    nombre_archivo="barras_descripciones_pago.png"
)

# Gráfico 5 (Tabla: Conflicto) -> ¡Mapa de Calor!
graficar_mapa_calor(
    resumen_transformacion_conf["agrupacion3"],
    columna_filas="TipoConflictoId",
    columna_columnas="EstadoConflictoId",
    columna_valores="conteo",
    titulo="Densidad de Casos Activos: Tipo vs Estado del Conflicto",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_conflictos_activos.png"
)

# Gráfico 6 (Tabla: Mediación) -> ¡Gráfico de Torta!
graficar_torta(
    resumen_transformacion_med["agrupacion2"],
    columna_etiquetas="Resultado",
    columna_valores="conteo",
    titulo="Resultados de Mediaciones en Oficina Corrientes",
    nombre_archivo="torta_resultados_corrientes.png"
)

print("\n✔ Los 6 archivos de imágenes (.png) han sido exportados exitosamente al Front-End.")
print("=== PIPELINE TOTALMENTE FINALIZADO ===")