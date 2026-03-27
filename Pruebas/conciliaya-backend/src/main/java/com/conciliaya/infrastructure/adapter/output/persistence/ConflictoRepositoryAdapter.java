package com.conciliaya.infrastructure.adapter.output.persistence;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.EstadoConflicto;
import com.conciliaya.domain.model.TipoConflicto;
import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

/**
 * Adaptador que implementa el puerto ConflictoRepositoryPort.
 * Responsable de adaptar las operaciones de dominio a JPA.
 */
@Component
public class ConflictoRepositoryAdapter implements ConflictoRepositoryPort {

    private final ConflictoJpaRepository jpaRepository;

    public ConflictoRepositoryAdapter(ConflictoJpaRepository jpaRepository) {
        this.jpaRepository = jpaRepository;
    }

    @Override
    public Conflicto save(Conflicto conflicto) {
        ConflictoEntity entity = mapearAEntity(conflicto);
        ConflictoEntity guardada = jpaRepository.save(entity);
        return mapearADominio(guardada);
    }

    @Override
    public Optional<Conflicto> findById(Long id) {
        return jpaRepository.findById(id).map(this::mapearADominio);
    }

    @Override
    public List<Conflicto> findAll() {
        return jpaRepository.findAll()
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Conflicto> findByEstado(Long estadoId) {
        return jpaRepository.findByEstadoConflictoId(estadoId)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Conflicto> findByTipo(Long tipoId) {
        return jpaRepository.findByTipoConflictoId(tipoId)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Conflicto> findByUsuarioReportante(Long usuarioId) {
        return jpaRepository.findByUsuarioReportanteId(usuarioId)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public void deleteById(Long id) {
        jpaRepository.deleteById(id);
    }

    @Override
    public long count() {
        return jpaRepository.count();
    }

    /**
     * Convierte una entidad de dominio a entidad JPA.
     */
    private ConflictoEntity mapearAEntity(Conflicto conflicto) {
        ConflictoEntity entity = new ConflictoEntity();
        if (conflicto.getId() != null) {
            entity.setId(conflicto.getId());
        }
        entity.setTitulo(conflicto.getTitulo());
        entity.setDescripcion(conflicto.getDescripcion());
        entity.setUbicacion(conflicto.getUbicacion());
        entity.setPrioridad(conflicto.getPrioridad());
        entity.setObservaciones(conflicto.getObservaciones());
        entity.setFechaReporte(conflicto.getFechaReporte());
        entity.setFechaActualizacion(conflicto.getFechaActualizacion());
        return entity;
    }

    /**
     * Convierte una entidad JPA a entidad de dominio.
     */
    private Conflicto mapearADominio(ConflictoEntity entity) {
        Conflicto conflicto = new Conflicto();
        conflicto.setId(entity.getId());
        conflicto.setTitulo(entity.getTitulo());
        conflicto.setDescripcion(entity.getDescripcion());
        conflicto.setUbicacion(entity.getUbicacion());
        conflicto.setPrioridad(entity.getPrioridad());
        conflicto.setObservaciones(entity.getObservaciones());
        conflicto.setFechaReporte(entity.getFechaReporte());
        conflicto.setFechaActualizacion(entity.getFechaActualizacion());
        return conflicto;
    }
}
