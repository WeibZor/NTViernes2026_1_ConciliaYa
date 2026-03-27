package com.conciliaya.infrastructure.adapter.output.persistence;

import com.conciliaya.domain.model.Mediacion;
import com.conciliaya.domain.ports.MediacionRepositoryPort;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

/**
 * Adaptador que implementa el puerto MediacionRepositoryPort.
 * Responsable de adaptar las operaciones de dominio a JPA.
 */
@Component
public class MediacionRepositoryAdapter implements MediacionRepositoryPort {

    private final MediacionJpaRepository jpaRepository;

    public MediacionRepositoryAdapter(MediacionJpaRepository jpaRepository) {
        this.jpaRepository = jpaRepository;
    }

    @Override
    public Mediacion save(Mediacion mediacion) {
        MediacionEntity entity = mapearAEntity(mediacion);
        MediacionEntity guardada = jpaRepository.save(entity);
        return mapearADominio(guardada);
    }

    @Override
    public Optional<Mediacion> findById(Long id) {
        return jpaRepository.findById(id).map(this::mapearADominio);
    }

    @Override
    public List<Mediacion> findAll() {
        return jpaRepository.findAll()
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Mediacion> findByConflicto(Long conflictoId) {
        return jpaRepository.findByConflictoId(conflictoId)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Mediacion> findByMediador(Long mediadorId) {
        return jpaRepository.findByMediadorId(mediadorId)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public List<Mediacion> findByCompletada(Boolean completada) {
        return jpaRepository.findByCompletada(completada)
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public void deleteById(Long id) {
        jpaRepository.deleteById(id);
    }

    /**
     * Convierte una entidad de dominio a entidad JPA.
     */
    private MediacionEntity mapearAEntity(Mediacion mediacion) {
        MediacionEntity entity = new MediacionEntity();
        if (mediacion.getId() != null) {
            entity.setId(mediacion.getId());
        }
        entity.setResultado(mediacion.getResultado());
        entity.setAcuerdos(mediacion.getAcuerdos());
        entity.setFechaInicio(mediacion.getFechaInicio());
        entity.setFechaFinalizacion(mediacion.getFechaFinalizacion());
        entity.setCompletada(mediacion.getCompletada());
        entity.setFechaCreacion(mediacion.getFechaCreacion());
        entity.setFechaActualizacion(mediacion.getFechaActualizacion());
        return entity;
    }

    /**
     * Convierte una entidad JPA a entidad de dominio.
     */
    private Mediacion mapearADominio(MediacionEntity entity) {
        Mediacion mediacion = new Mediacion();
        mediacion.setId(entity.getId());
        mediacion.setResultado(entity.getResultado());
        mediacion.setAcuerdos(entity.getAcuerdos());
        mediacion.setFechaInicio(entity.getFechaInicio());
        mediacion.setFechaFinalizacion(entity.getFechaFinalizacion());
        mediacion.setCompletada(entity.getCompletada());
        mediacion.setFechaCreacion(entity.getFechaCreacion());
        mediacion.setFechaActualizacion(entity.getFechaActualizacion());
        return mediacion;
    }
}
