package com.example.demo.controller;

import com.example.demo.model.Mediacion;
import com.example.demo.repository.ConflictoRepository;
import com.example.demo.repository.EstadoConflictoRepository;
import com.example.demo.repository.MediacionRepository;
import com.example.demo.repository.UsuarioRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/mediaciones")
public class MediacionController {

    private final MediacionRepository mediacionRepository;
    private final ConflictoRepository conflictoRepository;
    private final UsuarioRepository usuarioRepository;
    private final EstadoConflictoRepository estadoConflictoRepository;

    public MediacionController(MediacionRepository mediacionRepository,
                               ConflictoRepository conflictoRepository,
                               UsuarioRepository usuarioRepository,
                               EstadoConflictoRepository estadoConflictoRepository) {
        this.mediacionRepository = mediacionRepository;
        this.conflictoRepository = conflictoRepository;
        this.usuarioRepository = usuarioRepository;
        this.estadoConflictoRepository = estadoConflictoRepository;
    }

    @GetMapping
    public List<Mediacion> getAll() {
        return mediacionRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Mediacion> getById(@PathVariable Long id) {
        return mediacionRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Mediacion> create(@RequestBody Mediacion mediacion) {
        if (mediacion.getConflicto() != null && mediacion.getConflicto().getId() != null) {
            conflictoRepository.findById(mediacion.getConflicto().getId()).ifPresent(mediacion::setConflicto);
        }
        if (mediacion.getUsuarioMediador() != null && mediacion.getUsuarioMediador().getId() != null) {
            usuarioRepository.findById(mediacion.getUsuarioMediador().getId()).ifPresent(mediacion::setUsuarioMediador);
        }
        if (mediacion.getEstadoConflicto() != null && mediacion.getEstadoConflicto().getId() != null) {
            estadoConflictoRepository.findById(mediacion.getEstadoConflicto().getId()).ifPresent(mediacion::setEstadoConflicto);
        }
        return ResponseEntity.ok(mediacionRepository.save(mediacion));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Mediacion> update(@PathVariable Long id, @RequestBody Mediacion request) {
        return mediacionRepository.findById(id)
                .map(existing -> {
                    existing.setLugar(request.getLugar());
                    existing.setObservaciones(request.getObservaciones());
                    existing.setResultado(request.getResultado());
                    existing.setActivo(request.getActivo());
                    existing.setFechaProgramada(request.getFechaProgramada());
                    if (request.getConflicto() != null && request.getConflicto().getId() != null) {
                        conflictoRepository.findById(request.getConflicto().getId()).ifPresent(existing::setConflicto);
                    }
                    if (request.getUsuarioMediador() != null && request.getUsuarioMediador().getId() != null) {
                        usuarioRepository.findById(request.getUsuarioMediador().getId()).ifPresent(existing::setUsuarioMediador);
                    }
                    if (request.getEstadoConflicto() != null && request.getEstadoConflicto().getId() != null) {
                        estadoConflictoRepository.findById(request.getEstadoConflicto().getId()).ifPresent(existing::setEstadoConflicto);
                    }
                    return ResponseEntity.ok(mediacionRepository.save(existing));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        return mediacionRepository.findById(id)
                .map(existing -> {
                    mediacionRepository.delete(existing);
                    return ResponseEntity.noContent().<Void>build();
                })
                .orElse(ResponseEntity.notFound().build());
    }
}
