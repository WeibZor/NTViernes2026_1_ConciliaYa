package com.conciliaya.domain.usecase;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.EstadoConflicto;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import java.time.LocalDateTime;

/**
 * Caso de uso para actualizar el estado de un conflicto.
 * Implementa la lógica de transición de estados.
 */
public class ActualizarEstadoConflictoUseCase {

    private final ConflictoRepositoryPort conflictoRepository;

    public ActualizarEstadoConflictoUseCase(ConflictoRepositoryPort conflictoRepository) {
        this.conflictoRepository = conflictoRepository;
    }

    /**
     * Actualiza el estado de un conflicto.
     * 
     * @param conflictoId el ID del conflicto
     * @param nuevoEstado el nuevo estado del conflicto
     * @param observaciones observaciones sobre el cambio de estado
     * @return el conflicto actualizado
     * @throws IllegalArgumentException si el conflicto no existe o estado es inválido
     */
    public Conflicto ejecutar(Long conflictoId, EstadoConflicto nuevoEstado, String observaciones) {
        // Validaciones
        validarDatos(conflictoId, nuevoEstado);

        // Obtener conflicto actual
        Conflicto conflicto = conflictoRepository.findById(conflictoId)
                .orElseThrow(() -> new IllegalArgumentException("Conflicto no encontrado: " + conflictoId));

        // Validar transición de estado
        validarTransicionEstado(conflicto.getEstadoConflicto(), nuevoEstado);

        // Actualizar estado
        conflicto.setEstadoConflicto(nuevoEstado);
        conflicto.setFechaActualizacion(LocalDateTime.now());
        
        if (observaciones != null && !observaciones.isBlank()) {
            conflicto.setObservaciones(observaciones);
        }

        // Guardar y retornar
        return conflictoRepository.save(conflicto);
    }

    /**
     * Valida que los datos sean correctos.
     */
    private void validarDatos(Long conflictoId, EstadoConflicto nuevoEstado) {
        if (conflictoId == null || conflictoId <= 0) {
            throw new IllegalArgumentException("ID de conflicto inválido");
        }
        if (nuevoEstado == null) {
            throw new IllegalArgumentException("El nuevo estado es requerido");
        }
    }

    /**
     * Valida que la transición de estado sea válida.
     * Implementa lógica de negocio sobre los estados permitidos.
     */
    private void validarTransicionEstado(EstadoConflicto estadoActual, EstadoConflicto estadoNuevo) {
        // Se permite cualquier transición (puede ser customizado según reglas de negocio)
        if (estadoNuevo == null) {
            throw new IllegalArgumentException("Estado no válido");
        }
    }
}
