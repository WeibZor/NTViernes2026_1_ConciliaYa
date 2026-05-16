import pandas as pd

def transformar_datos_servicio(data_frame_limpio):
    # Asegurar que los nombres de las columnas no tengan espacios en blanco
    df = data_frame_limpio.copy()
    
    # -------------------------------------------------------------------------
    # 1. Gráfico de Barras: Cantidad de registros por código solo para estados Activos
    # Ideal para: Comparar qué códigos tienen más presencia activa.
    # -------------------------------------------------------------------------
    filtro_1 = df.query("estado == 'Activo'")
    agrupacion_1 = filtro_1.groupby("codigo")["id"].count().reset_index(name="cuenta")
    
    # -------------------------------------------------------------------------
    # 2. Gráfico de Tortas (Pie): Distribución de estados para un código específico ('C01')
    # Ideal para: Ver el porcentaje de activos vs inactivos en un sector/código.
    # -------------------------------------------------------------------------
    filtro_2 = df.query("codigo == 'C01'")
    agrupacion_2 = filtro_2.groupby("estado")["id"].count().reset_index(name="porcentaje")
    
    # -------------------------------------------------------------------------
    # 3. Gráfico de Barras: Conteo de nombres únicos bajo descripciones críticas
    # Ideal para: Identificar qué actores o entidades están vinculados a descripciones específicas.
    # -------------------------------------------------------------------------
    filtro_3 = df.query("descripcion == 'Alerta Máxima' o descripcion == 'Conflicto Crítico'")
    agrupacion_3 = filtro_3.groupby("nombre")["id"].count().reset_index(name="total_casos")
    
    # -------------------------------------------------------------------------
    # 4. Gráfico de Líneas / Tendencia: Evolución por ID (asumiendo ID como orden correlativo)
    # Nota: Al no haber fecha, agrupamos por código y contamos estados para ver volumen.
    # -------------------------------------------------------------------------
    filtro_4 = df.query("estado == 'Inactivo'")
    agrupacion_4 = filtro_4.groupby("codigo")["id"].count().reset_index(name="historico_inactivos")
    
    # -------------------------------------------------------------------------
    # 5. Gráfico de Barras Agrupadas: Relación Nombre-Estado de los IDs mayores a 50
    # Ideal para: Analizar el comportamiento de los registros más recientes o con mayor peso (ID > 50).
    # -------------------------------------------------------------------------
    filtro_5 = df.query("id > 50")
    agrupacion_5 = filtro_5.groupby(["nombre", "estado"])["id"].count().reset_index(name="conteo_segmentado")
    
    # Retornamos los dataframes procesados para su posterior graficación
    return agrupacion_1, agrupacion_2, agrupacion_3, agrupacion_4, agrupacion_5