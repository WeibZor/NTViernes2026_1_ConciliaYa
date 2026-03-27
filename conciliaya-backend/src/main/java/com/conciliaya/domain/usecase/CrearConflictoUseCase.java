package com.conciliaya.domain.usecase;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.TipoConflicto;
import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.ports.ClasificadorConflictoPort;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import java.time.LocalDateTime;

/**
 * Caso de uso para crear un nuevo conflicto.
 * Responsabilidades:
 * - Validar los datos del conflicto
 * - Clasificar automáticamente el conflicto
 * - Guardar el conflicto en la base de datos
 * 
 * Este caso de uso implementa la lógica pura de negocio sin dependencias de framework.
 */
public class CrearConflictoUseCase {

    private final ConflictoRepositoryPort conflictoRepository;
    private final ClasificadorConflictoPort clasificadorService;

    public CrearConflictoUseCase(ConflictoRepositoryPort conflictoRepository,
                                 ClasificadorConflictoPort clasificadorService) {
        this.conflictoRepository = conflictoRepository;
        this.clasificadorService = clasificadorService;
    }

    /**
     * Ejecuta el caso de uso de crear conflicto.
     * 
     * @param titulo título del conflicto
     * @param descripcion descripción detallada
     * @param ubicacion ubicación del conflicto
     * @param usuarioReportante usuario que reporta
     * @return el conflicto creado
     * @throws IllegalArgumentException si los datos son inválidos
     */
    public Conflicto ejecutar(String titulo, String descripcion, String ubicacion, Usuario usuarioReportante) {
        // Validaciones
        validarDatos(titulo, descripcion, ubicacion, usuarioReportante);

        // Crear conflicto
        Conflicto conflicto = new Conflicto(titulo, descripcion, ubicacion, usuarioReportante, null);
        conflicto.setFechaActualizacion(LocalDateTime.now());

        // Intentar clasificar automáticamente
        try {
            Long tipoConflictoId = clasificadorService.clasificarConflicto(descripcion);
            TipoConflicto tipoConflicto = new TipoConflicto();
            tipoConflicto.setId(tipoConflictoId);
            conflicto.setTipoConflicto(tipoConflicto);
        } catch (Exception e) {
            // Si falla la clasificación, dejar el tipo vacío para ser asignado manualmente
            System.err.println("Error clasificando conflicto: " + e.getMessage());
        }

        // Guardar y retornar
        return conflictoRepository.save(conflicto);
    }

    /**
     * Valida que los datos del conflicto sean válidos.
     * Implementa validaciones de negocio puras.
     */
    private void validarDatos(String titulo, String descripcion, String ubicacion, Usuario usuarioReportante) {
        if (titulo == null || titulo.isBlank()) {
            throw new IllegalArgumentException("El título del conflicto es requerido");
        }
        if (titulo.length() < 10) {
            throw new IllegalArgumentException("El título debe tener al menos 10 caracteres");
        }
        if (descripcion == null || descripcion.isBlank()) {
            throw new IllegalArgumentException("La descripción del conflicto es requerida");
        }
        if (descripcion.length() < 20) {
            throw new IllegalArgumentException("La descripción debe tener al menos 20 caracteres");
        }
        if (ubicacion == null || ubicacion.isBlank()) {
            throw new IllegalArgumentException("La ubicación del conflicto es requerida");
        }
        if (usuarioReportante == null) {
            throw new IllegalArgumentException("El usuario reportante es requerido");
        }
    }
}
