package com.conciliaya.infrastructure.adapter.output.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Repositorio Spring Data JPA para ConflictoEntity.
 */
@Repository
public interface ConflictoJpaRepository extends JpaRepository<ConflictoEntity, Long> {
    
    List<ConflictoEntity> findByEstadoConflictoId(Long estadoId);
    List<ConflictoEntity> findByTipoConflictoId(Long tipoId);
    List<ConflictoEntity> findByUsuarioReportanteId(Long usuarioId);
}
