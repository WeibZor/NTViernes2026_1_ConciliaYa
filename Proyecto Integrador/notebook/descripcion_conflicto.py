def describir_conflicto(df):
    print("\n--- DESCRIPCIÓN: Conflicto ---")
    print(f"Registros limpios: {len(df)}")
    print(f"Columnas: {list(df.columns)}")
    print(df[["tipoConflictoNombre", "estadoConflictoNombre", "activo"]].value_counts().to_string())
    print(f"\nMonto reclamado - promedio: ${df['montoReclamado'].mean():,.2f}  |  max: ${df['montoReclamado'].max():,.2f}")
