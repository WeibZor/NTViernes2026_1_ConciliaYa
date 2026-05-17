from concilia.repositories.memory_repo import memory_repo
from concilia.domain.entities.usuario.usuario_data import generar_datos_usuario


USERS_KEY = "usuarios"


def initialize_users(num=100, seed=None):
    df = generar_datos_usuario(num_registros=num, semilla=seed)
    records = df.to_dict(orient="records")
    memory_repo.save_all(USERS_KEY, records)
    return records


def list_users():
    return memory_repo.list(USERS_KEY)


def create_user(user_dict):
    users = memory_repo.list(USERS_KEY)
    next_id = 1 if not users else max(u.get("Id", 0) for u in users) + 1
    user = dict(user_dict)
    user["Id"] = next_id
    memory_repo.add(USERS_KEY, user)
    return user


def update_user(user_id, patch_dict):
    users = memory_repo.list(USERS_KEY)
    updated = None
    for u in users:
        if u.get("Id") == user_id:
            u.update(patch_dict)
            updated = u
            break
    if updated:
        memory_repo.save_all(USERS_KEY, users)
    return updated


def delete_user(user_id):
    memory_repo.delete(USERS_KEY, user_id)
"""Wrappers de servicio para `usuario` que usan la lógica existente.

Objetivo: exponer una API de servicio (Application layer) que use el dominio
actual sin mover archivos, y que almacene/gestione estado vía MemoryRepository.
"""
from typing import Any, Dict, List, Optional
import pandas as pd

from concilia.repositories.memory_repo import memory_repo

# Importar funciones existentes desde el dominio reorganizado
from concilia.domain.entities.usuario.usuario_data import generar_datos_usuario
from concilia.domain.entities.usuario.HU_26_Limpieza_Usuario import limpiar_usuarios


KEY = "usuarios"


def initialize_users(num_registros: int = 1000, semilla: int = 42) -> List[Dict[str, Any]]:
    existing = memory_repo.list(KEY)
    if existing:
        return existing

    df = limpiar_usuarios(generar_datos_usuario(num_registros=num_registros, semilla=semilla))
    records = df.where(pd.notnull(df), None).to_dict(orient="records")
    memory_repo.save_all(KEY, records)
    return records


def list_users() -> List[Dict[str, Any]]:
    return memory_repo.list(KEY)


def create_user(payload: Dict[str, Any]) -> Dict[str, Any]:
    usuarios = list_users()
    next_id = max((u.get("id", 0) for u in usuarios), default=0) + 1
    nuevo = {**payload, "id": next_id}
    if "activo" not in nuevo:
        nuevo["activo"] = True
    memory_repo.add(KEY, nuevo)
    return nuevo


def update_user(user_id: int, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    usuarios = list_users()
    usuario = next((u for u in usuarios if u.get("id") == user_id), None)
    if usuario is None:
        return None
    usuario.update(payload)
    memory_repo.save_all(KEY, usuarios)
    return usuario


def delete_user(user_id: int) -> bool:
    usuarios = list_users()
    nueva = [u for u in usuarios if u.get("id") != user_id]
    if len(nueva) == len(usuarios):
        return False
    memory_repo.save_all(KEY, nueva)
    return True
