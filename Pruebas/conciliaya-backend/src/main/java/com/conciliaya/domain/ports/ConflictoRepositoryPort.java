package com.conciliaya.domain.ports;

import com.conciliaya.domain.model.Conflicto;
import java.util.List;
import java.util.Optional;

/**
 * Puerto (interfaz) para operaciones de Conflicto.
 * Define el contrato que los adaptadores deben implementar.
 */
public interface ConflictoRepositoryPort {

    /**
     * Guarda un nuevo conflicto o actualiza uno existente.
     * @param conflicto el conflicto a guardar
     * @return el conflicto guardado
     */
    Conflicto save(Conflicto conflicto);

    /**
     * Busca un conflicto por su ID.
     * @param id el ID del conflicto
     * @return un Optional con el conflicto si existe
     */
    Optional<Conflicto> findById(Long id);

    /**
     * Obtiene todos los conflictos.
     * @return lista de conflictos
     */
    List<Conflicto> findAll();

    /**
     * Obtiene conflictos por estado.
     * @param estadoId el ID del estado
     * @return lista de conflictos con ese estado
     */
    List<Conflicto> findByEstado(Long estadoId);

    /**
     * Obtiene conflictos por tipo.
     * @param tipoId el ID del tipo
     * @return lista de conflictos de ese tipo
     */
    List<Conflicto> findByTipo(Long tipoId);

    /**
     * Obtiene conflictos por usuario reportante.
     * @param usuarioId el ID del usuario
     * @return lista de conflictos reportados por ese usuario
     */
    List<Conflicto> findByUsuarioReportante(Long usuarioId);

    /**
     * Elimina un conflicto.
     * @param id el ID del conflicto a eliminar
     */
    void deleteById(Long id);

    /**
     * Cuenta el total de conflictos.
     * @return cantidad de conflictos
     */
    long count();
}
