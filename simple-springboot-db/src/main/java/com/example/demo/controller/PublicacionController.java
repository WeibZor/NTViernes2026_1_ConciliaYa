package com.example.demo.controller;

import com.example.demo.model.Publicacion;
import com.example.demo.repository.UsuarioRepository;
import com.example.demo.service.PublicacionService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/publicaciones")
public class PublicacionController {

    private final PublicacionService publicacionService;
    private final UsuarioRepository usuarioRepository;

    public PublicacionController(PublicacionService publicacionService,
                                  UsuarioRepository usuarioRepository) {
        this.publicacionService = publicacionService;
        this.usuarioRepository = usuarioRepository;
    }

    @GetMapping
    public List<Publicacion> getAll() {
        return publicacionService.findAll();
    }

    @PostMapping
    public ResponseEntity<Publicacion> create(@RequestBody Publicacion publicacion) {
        if (publicacion.getUsuario() != null && publicacion.getUsuario().getId() != null) {
            usuarioRepository.findById(publicacion.getUsuario().getId())
                    .ifPresent(publicacion::setUsuario);
        }
        return ResponseEntity.status(201).body(publicacionService.save(publicacion));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (publicacionService.findById(id).isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        publicacionService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
