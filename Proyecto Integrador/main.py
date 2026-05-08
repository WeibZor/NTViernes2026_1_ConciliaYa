import pandas as pd

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

#importar simulaciones del perfil
from utils.simulacionperfil import generarPerfil

#importar rutina de limpieza del prefil
from notebook.HU16_limpiezaperfil import limpiar_perfil


perfiles = generarPerfil(1000)

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






# resultados finales
print("\nFlujo completo ejecutado: EstadoConflicto + Usuario")
print(f"EstadoConflicto limpio: {len(simulacion_EstadoConflicto_limpia)} registros")
print(f"Usuario limpio: {len(usuario_limpio)} registros")
print(f"Consultas generadas: {list(consultas_resultado.keys())}")
print(f"Agrupaciones generadas: {list(agrupaciones_resultado.keys())}")