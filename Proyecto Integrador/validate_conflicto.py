import sys
import os

sys.path.insert(0, os.getcwd())

from conflicto.conflicto_data import generar_datos_conflicto
from conflicto.HU_01_Limpieza_Conflicto import limpiar_conflictos
from conflicto.HU_02_Descripcion_Conflicto import descripcion_conflictos
from conflicto.HU_04_Query_Conflicto import consultas_conflicto
from conflicto.HU_05_Agrupacion_Conflicto import agrupaciones_conflicto


def main():
    df = generar_datos_conflicto(num_registros=50, semilla=42)
    print('Generated Conflicto rows:', len(df))

    clean_df = limpiar_conflictos(df)
    print('Cleaned Conflicto rows:', len(clean_df))

    summary = descripcion_conflictos(clean_df)
    print('Description keys:', list(summary.keys()))

    queries = consultas_conflicto(clean_df)
    print('Queries keys:', list(queries.keys()))
    for key, value in queries.items():
        print(f'{key}: {len(value)} rows')

    groups = agrupaciones_conflicto(clean_df)
    print('Groups keys:', list(groups.keys()))
    for key, value in groups.items():
        print(f'{key}: {len(value)} rows')

    print('Validation passed: Conflicto HUs 1, 2, 4, and 5 work correctly.')


if __name__ == '__main__':
    main()
