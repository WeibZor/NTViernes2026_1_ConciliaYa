package com.conciliaya.domain.ports;

import com.conciliaya.domain.model.Mediacion;
import java.util.List;
import java.util.Optional;

/**
 * Puerto (interfaz) para operaciones de Mediacion.
 * Define el contrato que los adaptadores deben implementar.
 */
public interface MediacionRepositoryPort {

    /**
     * Guarda una nueva mediación o actualiza una existente.
     * @param mediacion la mediación a guardar
     * @return la mediación guardada
     */
    Mediacion save(Mediacion mediacion);

    /**
     * Busca una mediación por su ID.
     * @param id el ID de la mediación
     * @return un Optional con la mediación si existe
     */
    Optional<Mediacion> findById(Long id);

    /**
     * Obtiene todas las mediaciones.
     * @return lista de mediaciones
     */
    List<Mediacion> findAll();

    /**
     * Obtiene mediaciones por conflicto.
     * @param conflictoId el ID del conflicto
     * @return lista de mediaciones para ese conflicto
     */
    List<Mediacion> findByConflicto(Long conflictoId);

    /**
     * Obtiene mediaciones por mediador.
     * @param mediadorId el ID del mediador
     * @return lista de mediaciones asignadas a ese mediador
     */
    List<Mediacion> findByMediador(Long mediadorId);

    /**
     * Obtiene mediaciones completadas.
     * @return lista de mediaciones completadas
     */
    List<Mediacion> findByCompletada(Boolean completada);

    /**
     * Elimina una mediación.
     * @param id el ID de la mediación a eliminar
     */
    void deleteById(Long id);
}
