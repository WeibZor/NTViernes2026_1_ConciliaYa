"""Concilia package: Application, Domain, Infrastructure layers."""

__all__ = ["repositories", "services", "domain"]
"""Paquete de integración no destructiva para migración por capas.

Contiene wrappers para `services` y `repositories` que usan la lógica existente
en `usuario/`, `conflicto/`, `tipoconflicto/` sin mover archivos originales.
"""

__all__ = ["repositories", "services"]
