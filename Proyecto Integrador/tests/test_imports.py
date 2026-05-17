def test_can_import_services_and_repo():
    import concilia.repositories.memory_repo as repo
    import concilia.services.usuario_service as us
    import concilia.services.tipoconflicto_service as tc

    assert hasattr(repo, "memory_repo")
    assert hasattr(us, "initialize_users")
    assert hasattr(tc, "initialize_tipoconflictos")
def test_imports():
    # Smoke test: importar los servicios y el repositorio
    from concilia.services import initialize_users, list_users
    from concilia.repositories import memory_repo

    # Inicializar y comprobar que no lanza excepciones
    users = initialize_users(num_registros=10, semilla=42)
    assert isinstance(users, list)
    assert isinstance(list_users(), list)
    assert hasattr(memory_repo, "list")
