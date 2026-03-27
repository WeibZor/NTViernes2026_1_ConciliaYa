package com.conciliaya.infrastructure.adapter.output.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Repositorio Spring Data JPA para UsuarioEntity.
 * Proporciona métodos de consulta sin escribir SQL.
 */
@Repository
public interface UsuarioJpaRepository extends JpaRepository<UsuarioEntity, Long> {
    
    List<UsuarioEntity> findByActivoTrue();
    Optional<UsuarioEntity> findByEmail(String email);
    Optional<UsuarioEntity> findByNumeroDocumento(String numeroDocumento);
    long countByActivoTrue();
}
