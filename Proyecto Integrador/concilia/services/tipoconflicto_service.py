from concilia.repositories.memory_repo import memory_repo
from concilia.domain.conflicto.conflicto_data import generar_datos_conflicto


TIPOS_KEY = "tipos_conflicto"


def initialize_tipoconflictos(num=20, seed=None):
    df = generar_datos_conflicto(num_registros=num, semilla=seed)
    records = df.to_dict(orient="records")
    memory_repo.save_all(TIPOS_KEY, records)
    return records


def list_tipoconflictos():
    return memory_repo.list(TIPOS_KEY)
"""Wrappers de servicio para `tipoconflicto` que usan la lógica existente.
"""
from typing import Any, Dict, List, Optional
import pandas as pd

from concilia.repositories.memory_repo import memory_repo

from concilia.domain.tipoconflicto.tipoconflicto_data import generar_datos_tipoconflicto
from concilia.domain.tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto


KEY = "tipoconflictos"


def initialize_tipoconflictos(num_registros: int = 1000, semilla: int = 42) -> List[Dict[str, Any]]:
    existing = memory_repo.list(KEY)
    if existing:
        return existing

    df = limpiar_tipos_conflicto(generar_datos_tipoconflicto(num_registros=num_registros, semilla=semilla))
    records = df.where(pd.notnull(df), None).to_dict(orient="records")
    memory_repo.save_all(KEY, records)
    return records


def list_tipoconflictos() -> List[Dict[str, Any]]:
    return memory_repo.list(KEY)
