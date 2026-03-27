package com.conciliaya.infrastructure.adapter.output.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Repositorio Spring Data JPA para MediacionEntity.
 */
@Repository
public interface MediacionJpaRepository extends JpaRepository<MediacionEntity, Long> {
    
    List<MediacionEntity> findByConflictoId(Long conflictoId);
    List<MediacionEntity> findByMediadorId(Long mediadorId);
    List<MediacionEntity> findByCompletada(Boolean completada);
}
