package com.example.demo.controller;

import com.example.demo.model.Usuario;
import com.example.demo.repository.PerfilRepository;
import com.example.demo.repository.UsuarioRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {

    private final UsuarioRepository usuarioRepository;
    private final PerfilRepository perfilRepository;

    public UsuarioController(UsuarioRepository usuarioRepository, PerfilRepository perfilRepository) {
        this.usuarioRepository = usuarioRepository;
        this.perfilRepository = perfilRepository;
    }

    @GetMapping
    public List<Usuario> getAll() {
        return usuarioRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Usuario> getById(@PathVariable Long id) {
        return usuarioRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Usuario> create(@RequestBody Usuario usuario) {
        if (usuario.getPerfil() != null && usuario.getPerfil().getId() != null) {
            perfilRepository.findById(usuario.getPerfil().getId()).ifPresent(usuario::setPerfil);
        }
        Usuario saved = usuarioRepository.save(usuario);
        return ResponseEntity.ok(saved);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Usuario> update(@PathVariable Long id, @RequestBody Usuario request) {
        return usuarioRepository.findById(id)
                .map(existing -> {
                    existing.setNombre(request.getNombre());
                    existing.setApellido(request.getApellido());
                    existing.setCorreo(request.getCorreo());
                    existing.setTelefono(request.getTelefono());
                    existing.setTipoDocumento(request.getTipoDocumento());
                    existing.setDocumento(request.getDocumento());
                    existing.setActivo(request.getActivo());
                    if (request.getPerfil() != null && request.getPerfil().getId() != null) {
                        perfilRepository.findById(request.getPerfil().getId()).ifPresent(existing::setPerfil);
                    }
                    return ResponseEntity.ok(usuarioRepository.save(existing));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        return usuarioRepository.findById(id)
                .map(existing -> {
                    usuarioRepository.delete(existing);
                    return ResponseEntity.noContent().<Void>build();
                })
                .orElse(ResponseEntity.notFound().build());
    }
}
