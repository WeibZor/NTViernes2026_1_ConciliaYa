package com.conciliaya.domain.usecase;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.EstadoConflicto;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import java.time.LocalDateTime;
import java.util.Optional;

/**
 * Caso de uso para obtener conflictos.
 * Implementa lógica de consulta de conflictos con filtros.
 */
public class ObtenerConflictosUseCase {

    private final ConflictoRepositoryPort conflictoRepository;

    public ObtenerConflictosUseCase(ConflictoRepositoryPort conflictoRepository) {
        this.conflictoRepository = conflictoRepository;
    }

    /**
     * Obtiene un conflicto por su ID.
     * 
     * @param id el ID del conflicto
     * @return el conflicto encontrado
     * @throws IllegalArgumentException si el conflicto no existe
     */
    public Conflicto obtenerPorId(Long id) {
        validarId(id);
        return conflictoRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Conflicto no encontrado: " + id));
    }

    /**
     * Obtiene todos los conflictos.
     * Usa programación funcional con Streams.
     * 
     * @return lista de todos los conflictos
     */
    public java.util.List<Conflicto> obtenerTodos() {
        return conflictoRepository.findAll()
                .stream()
                .peek(c -> c.setFechaActualizacion(LocalDateTime.now()))
                .toList();
    }

    /**
     * Obtiene conflictos por estado.
     * 
     * @param estadoId el ID del estado
     * @return lista de conflictos con ese estado
     */
    public java.util.List<Conflicto> obtenerPorEstado(Long estadoId) {
        validarId(estadoId);
        return conflictoRepository.findByEstado(estadoId)
                .stream()
                .filter(c -> c.getEstadoConflicto() != null)
                .toList();
    }

    /**
     * Obtiene conflictos por tipo.
     * 
     * @param tipoId el ID del tipo
     * @return lista de conflictos de ese tipo
     */
    public java.util.List<Conflicto> obtenerPorTipo(Long tipoId) {
        validarId(tipoId);
        return conflictoRepository.findByTipo(tipoId)
                .stream()
                .filter(c -> c.getTipoConflicto() != null)
                .toList();
    }

    /**
     * Obtiene conflictos de un usuario reportante.
     * 
     * @param usuarioId el ID del usuario
     * @return lista de conflictos reportados por ese usuario
     */
    public java.util.List<Conflicto> obtenerPorUsuarioReportante(Long usuarioId) {
        validarId(usuarioId);
        return conflictoRepository.findByUsuarioReportante(usuarioId)
                .stream()
                .filter(c -> c.getUsuarioReportante() != null)
                .toList();
    }

    /**
     * Obtiene conflictos ordenados por prioridad.
     * Implementa lógica de filtrado con funciones puras.
     * 
     * @return lista de conflictos ordenados por prioridad descendente
     */
    public java.util.List<Conflicto> obtenerPorPrioridad() {
        return conflictoRepository.findAll()
                .stream()
                .sorted((c1, c2) -> c2.getPrioridad().compareTo(c1.getPrioridad()))
                .toList();
    }

    /**
     * Cuenta el total de conflictos.
     * 
     * @return cantidad de conflictos
     */
    public long contarTotal() {
        return conflictoRepository.count();
    }

    /**
     * Valida que el ID sea válido.
     */
    private void validarId(Long id) {
        if (id == null || id <= 0) {
            throw new IllegalArgumentException("ID inválido: " + id);
        }
    }
}
