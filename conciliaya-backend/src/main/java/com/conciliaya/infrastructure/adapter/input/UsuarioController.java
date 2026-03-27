package com.conciliaya.infrastructure.adapter.input;

import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.ports.UsuarioRepositoryPort;
import com.conciliaya.infrastructure.adapter.input.dto.ApiResponse;
import com.conciliaya.infrastructure.adapter.input.dto.UsuarioDTO;
import com.conciliaya.infrastructure.adapter.input.dto.UsuarioResponseDTO;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Controlador REST para operaciones de Usuario.
 * Actúa como adaptador de entrada (input adapter).
 */
@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    private final UsuarioRepositoryPort usuarioRepository;

    public UsuarioController(UsuarioRepositoryPort usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
    }

    /**
     * Crea un nuevo usuario.
     * POST /api/usuarios
     */
    @PostMapping
    public ResponseEntity<ApiResponse<UsuarioResponseDTO>> crearUsuario(
            @Valid @RequestBody UsuarioDTO dto) {
        
        Usuario usuario = new Usuario(
                dto.getNombre(),
                dto.getApellido(),
                dto.getEmail(),
                dto.getNumeroDocumento()
        );
        usuario.setTelefono(dto.getTelefono());
        usuario.setDireccion(dto.getDireccion());
        
        usuario = usuarioRepository.save(usuario);
        
        UsuarioResponseDTO response = mapearAResponse(usuario);
        ApiResponse<UsuarioResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Usuario creado exitosamente");
        
        return ResponseEntity.status(HttpStatus.CREATED).body(respuesta);
    }

    /**
     * Obtiene un usuario por su ID.
     * GET /api/usuarios/{id}
     */
    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<UsuarioResponseDTO>> obtenerUsuario(
            @PathVariable Long id) {
        
        Usuario usuario = usuarioRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado: " + id));
        
        UsuarioResponseDTO response = mapearAResponse(usuario);
        ApiResponse<UsuarioResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Usuario obtenido exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Obtiene todos los usuarios activos.
     * GET /api/usuarios
     */
    @GetMapping
    public ResponseEntity<ApiResponse<List<UsuarioResponseDTO>>> obtenerTodos() {
        
        List<UsuarioResponseDTO> usuarios = usuarioRepository.findAllActivos()
                .stream()
                .map(this::mapearAResponse)
                .toList();
        
        ApiResponse<List<UsuarioResponseDTO>> respuesta = 
                ApiResponse.exitoso(usuarios, "Usuarios obtenidos exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Busca un usuario por email.
     * GET /api/usuarios/email/{email}
     */
    @GetMapping("/email/{email}")
    public ResponseEntity<ApiResponse<UsuarioResponseDTO>> obtenerPorEmail(
            @PathVariable String email) {
        
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado con email: " + email));
        
        UsuarioResponseDTO response = mapearAResponse(usuario);
        ApiResponse<UsuarioResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Usuario obtenido exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Actualiza un usuario existente.
     * PUT /api/usuarios/{id}
     */
    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<UsuarioResponseDTO>> actualizarUsuario(
            @PathVariable Long id,
            @Valid @RequestBody UsuarioDTO dto) {
        
        Usuario usuario = usuarioRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado: " + id));
        
        usuario.setNombre(dto.getNombre());
        usuario.setApellido(dto.getApellido());
        usuario.setEmail(dto.getEmail());
        usuario.setTelefono(dto.getTelefono());
        usuario.setDireccion(dto.getDireccion());
        
        usuario = usuarioRepository.save(usuario);
        
        UsuarioResponseDTO response = mapearAResponse(usuario);
        ApiResponse<UsuarioResponseDTO> respuesta = 
                ApiResponse.exitoso(response, "Usuario actualizado exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Elimina un usuario.
     * DELETE /api/usuarios/{id}
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<Void>> eliminarUsuario(@PathVariable Long id) {
        
        usuarioRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado: " + id));
        
        usuarioRepository.deleteById(id);
        
        ApiResponse<Void> respuesta = 
                ApiResponse.exitoso("Usuario eliminado exitosamente");
        
        return ResponseEntity.ok(respuesta);
    }

    /**
     * Mapea una entidad Usuario a su DTO de respuesta.
     */
    private UsuarioResponseDTO mapearAResponse(Usuario usuario) {
        UsuarioResponseDTO dto = new UsuarioResponseDTO();
        dto.setId(usuario.getId());
        dto.setNombre(usuario.getNombre());
        dto.setApellido(usuario.getApellido());
        dto.setEmail(usuario.getEmail());
        dto.setTelefono(usuario.getTelefono());
        dto.setDireccion(usuario.getDireccion());
        dto.setNumeroDocumento(usuario.getNumeroDocumento());
        dto.setNombreCompleto(usuario.getNombreCompleto());
        dto.setActivo(usuario.getActivo());
        
        return dto;
    }
}
