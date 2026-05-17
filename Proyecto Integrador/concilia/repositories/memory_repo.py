from collections import defaultdict
from copy import deepcopy


class MemoryRepository:
    def __init__(self):
        self._store = defaultdict(list)

    def list(self, key):
        return deepcopy(self._store.get(key, []))

    def get(self, key, id_):
        items = self._store.get(key, [])
        for item in items:
            if item.get("Id") == id_:
                return deepcopy(item)
        return None

    def save_all(self, key, records):
        self._store[key] = deepcopy(records)

    def add(self, key, record):
        self._store[key].append(deepcopy(record))

    def delete(self, key, id_):
        items = self._store.get(key, [])
        self._store[key] = [it for it in items if it.get("Id") != id_]


memory_repo = MemoryRepository()
"""Repositorio en memoria simple, usado como adaptador durante la migración.

API: list(key), get(key,id), save_all(key, records), add(key, record), delete(key,id)
Implementa un singleton `memory_repo` para uso directo en servicios.
"""
from threading import RLock
from typing import Any, Dict, List, Optional


class MemoryRepository:
    def __init__(self) -> None:
        self._store: Dict[str, List[Dict[str, Any]]] = {}
        self._lock = RLock()

    def list(self, key: str) -> List[Dict[str, Any]]:
        with self._lock:
            return list(self._store.get(key, []))

    def get(self, key: str, id_: Any) -> Optional[Dict[str, Any]]:
        with self._lock:
            return next((r for r in self._store.get(key, []) if r.get("id") == id_), None)

    def save_all(self, key: str, records: List[Dict[str, Any]]) -> None:
        with self._lock:
            self._store[key] = list(records)

    def add(self, key: str, record: Dict[str, Any]) -> None:
        with self._lock:
            self._store.setdefault(key, []).append(record)

    def delete(self, key: str, id_: Any) -> None:
        with self._lock:
            self._store[key] = [r for r in self._store.get(key, []) if r.get("id") != id_]


# Singleton instance for quick usage during migration
memory_repo = MemoryRepository()
