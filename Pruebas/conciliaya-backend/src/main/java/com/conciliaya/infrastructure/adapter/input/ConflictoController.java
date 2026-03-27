package com.conciliaya.infrastructure.adapter.input;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.TipoConflicto;
import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.usecase.CrearConflictoUseCase;
import com.conciliaya.domain.usecase.ObtenerConflictosUseCase;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import com.conciliaya.infrastructure.adapter.input.dto.ApiResponse;
import com.conciliaya.infrastructure.adapter.input.dto.ConflictoDTO;
import com.conciliaya.infrastructure.adapter.input.dto.ConflictoResponseDTO;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Controlador REST para operaciones de Conflicto.
 * Actúa como adaptador de entrada (input adapter).
 * 
 * Responsabilidades:
 * - Recibir solicitudes HTTP
 * - Validar datos con anotaciones
 * - Llamar a casos de uso
 * - Retornar respuestas HTTP
 * 
 * NO contiene lógica de negocio. La lógica está en los casos de uso.
 */
@RestController
@RequestMapping("/conflictos")
public class ConflictoController {

    private final CrearConflictoUseCase crearConflictoUseCase;
    private final ObtenerConflictosUseCase obtenerConflictosUseCase;
    private final ConflictoRepositoryPort conflictoRepository;

    public ConflictoController(CrearConflictoUseCase crearConflictoUseCase,
                              ObtenerConflictosUseCase obtenerConflictosUseCase,
                              ConflictoRepositoryPort conflictoRepository) {
        this.crearConflictoUseCase = crearConflictoUseCase;
        this.obtenerConflictosUseCase = obtenerConflictosUseCase;
        this.conflictoRepository = conflictoRepository;
    }

    /**
     * Crea un nuevo conflicto.
     * POST /api/conflictos
     */
    @PostMapping
    public ResponseEntity<ApiResponse<ConflictoResponseDTO>> crearConflicto(
            @Valid @RequestBody ConflictoDTO dto) {
        
        // Obtener usuario reportante (en una aplicación real, sería del contexto de seguridad)
        Usuario usuario = new Usuario();
        usuario.setId(dto.getUsuarioReportanteId());

        // Ejecutar caso de uso
        Conflicto conflicto = crearConflictoUseCase.ejecutar(
                dto.getTitulo(),
                dto.getDescripcion(),
                dto.getUbicacion(),
                usuario
        );

        ConflictoResponseDTO response = mapearAResponse(conflicto);
        ApiResponse<ConflictoResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Conflicto creado exitosamente");
        
        return ResponseEntity.status(HttpStatus.CREATED).body(respuesta);
    }

    /**
     * Obtiene un conflicto por su ID.
     * GET /api/conflictos/{id}
     */
    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<ConflictoResponseDTO>> obtenerConflicto(
            @PathVariable Long id) {
        
        Conflicto conflicto = obtenerConflictosUseCase.obtenerPorId(id);
        ConflictoResponseDTO response = mapearAResponse(conflicto);
        ApiResponse<ConflictoResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Conflicto obtenido exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Obtiene todos los conflictos.
     * GET /api/conflictos
     */
    @GetMapping
    public ResponseEntity<ApiResponse<List<ConflictoResponseDTO>>> obtenerTodos() {
        
        List<ConflictoResponseDTO> conflictos = obtenerConflictosUseCase.obtenerTodos()
                .stream()
                .map(this::mapearAResponse)
                .toList();
        
        ApiResponse<List<ConflictoResponseDTO>> respuesta = 
                ApiResponse.exitoso(conflictos, "Conflictos obtenidos exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Obtiene conflictos por estado.
     * GET /api/conflictos?estado={estadoId}
     */
    @GetMapping("/por-estado/{estadoId}")
    public ResponseEntity<ApiResponse<List<ConflictoResponseDTO>>> obtenerPorEstado(
            @PathVariable Long estadoId) {
        
        List<ConflictoResponseDTO> conflictos = obtenerConflictosUseCase.obtenerPorEstado(estadoId)
                .stream()
                .map(this::mapearAResponse)
                .toList();
        
        ApiResponse<List<ConflictoResponseDTO>> respuesta = 
                ApiResponse.exitoso(conflictos, "Conflictos por estado obtenidos");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Obtiene conflictos ordenados por prioridad.
     * GET /api/conflictos/por-prioridad
     */
    @GetMapping("/por-prioridad")
    public ResponseEntity<ApiResponse<List<ConflictoResponseDTO>>> obtenerPorPrioridad() {
        
        List<ConflictoResponseDTO> conflictos = obtenerConflictosUseCase.obtenerPorPrioridad()
                .stream()
                .map(this::mapearAResponse)
                .toList();
        
        ApiResponse<List<ConflictoResponseDTO>> respuesta = 
                ApiResponse.exitoso(conflictos, "Conflictos por prioridad obtenidos");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Actualiza un conflicto existente.
     * PUT /api/conflictos/{id}
     */
    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<ConflictoResponseDTO>> actualizarConflicto(
            @PathVariable Long id,
            @Valid @RequestBody ConflictoDTO dto) {
        
        // Obtener conflicto actual
        Conflicto conflicto = obtenerConflictosUseCase.obtenerPorId(id);
        
        // Actualizar campos
        conflicto.setTitulo(dto.getTitulo());
        conflicto.setDescripcion(dto.getDescripcion());
        conflicto.setUbicacion(dto.getUbicacion());
        conflicto.setPrioridad(dto.getPrioridad());
        
        // Guardar
        conflicto = conflictoRepository.save(conflicto);
        
        ConflictoResponseDTO response = mapearAResponse(conflicto);
        ApiResponse<ConflictoResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Conflicto actualizado exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Elimina un conflicto.
     * DELETE /api/conflictos/{id}
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<Void>> eliminarConflicto(@PathVariable Long id) {
        
        obtenerConflictosUseCase.obtenerPorId(id); // Validar existencia
        conflictoRepository.deleteById(id);
        
        ApiResponse<Void> respuesta = 
                ApiResponse.exitoso("Conflicto eliminado exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Mapea una entidad Conflicto a su DTO de respuesta.
     * Implementa conversión sin lógica de negocio.
     */
    private ConflictoResponseDTO mapearAResponse(Conflicto conflicto) {
        ConflictoResponseDTO dto = new ConflictoResponseDTO();
        dto.setId(conflicto.getId());
        dto.setTitulo(conflicto.getTitulo());
        dto.setDescripcion(conflicto.getDescripcion());
        dto.setUbicacion(conflicto.getUbicacion());
        dto.setFechaReporte(conflicto.getFechaReporte());
        dto.setFechaActualizacion(conflicto.getFechaActualizacion());
        dto.setPrioridad(conflicto.getPrioridad());
        dto.setObservaciones(conflicto.getObservaciones());
        
        // Mapear relacionados
        if (conflicto.getTipoConflicto() != null) {
            // Mapear TipoConflicto
        }
        if (conflicto.getEstadoConflicto() != null) {
            // Mapear EstadoConflicto
        }
        
        return dto;
    }
}
