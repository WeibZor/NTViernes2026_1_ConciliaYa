package com.example.demo.controller;

import com.example.demo.model.Conflicto;
import com.example.demo.repository.ConflictoRepository;
import com.example.demo.repository.EstadoConflictoRepository;
import com.example.demo.repository.TipoConflictoRepository;
import com.example.demo.repository.UsuarioRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/conflictos")
public class ConflictoController {

    private final ConflictoRepository conflictoRepository;
    private final UsuarioRepository usuarioRepository;
    private final TipoConflictoRepository tipoConflictoRepository;
    private final EstadoConflictoRepository estadoConflictoRepository;

    public ConflictoController(ConflictoRepository conflictoRepository,
                               UsuarioRepository usuarioRepository,
                               TipoConflictoRepository tipoConflictoRepository,
                               EstadoConflictoRepository estadoConflictoRepository) {
        this.conflictoRepository = conflictoRepository;
        this.usuarioRepository = usuarioRepository;
        this.tipoConflictoRepository = tipoConflictoRepository;
        this.estadoConflictoRepository = estadoConflictoRepository;
    }

    @GetMapping
    public List<Conflicto> getAll() {
        return conflictoRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Conflicto> getById(@PathVariable Long id) {
        return conflictoRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Conflicto> create(@RequestBody Conflicto conflicto) {
        if (conflicto.getUsuarioDemandante() != null && conflicto.getUsuarioDemandante().getId() != null) {
            usuarioRepository.findById(conflicto.getUsuarioDemandante().getId())
                    .ifPresent(conflicto::setUsuarioDemandante);
        }
        if (conflicto.getUsuarioDemandado() != null && conflicto.getUsuarioDemandado().getId() != null) {
            usuarioRepository.findById(conflicto.getUsuarioDemandado().getId())
                    .ifPresent(conflicto::setUsuarioDemandado);
        }
        if (conflicto.getTipoConflicto() != null && conflicto.getTipoConflicto().getId() != null) {
            tipoConflictoRepository.findById(conflicto.getTipoConflicto().getId())
                    .ifPresent(conflicto::setTipoConflicto);
        }
        if (conflicto.getEstadoConflicto() != null && conflicto.getEstadoConflicto().getId() != null) {
            estadoConflictoRepository.findById(conflicto.getEstadoConflicto().getId())
                    .ifPresent(conflicto::setEstadoConflicto);
        }
        return ResponseEntity.ok(conflictoRepository.save(conflicto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Conflicto> update(@PathVariable Long id, @RequestBody Conflicto request) {
        return conflictoRepository.findById(id)
                .map(existing -> {
                    existing.setAsunto(request.getAsunto());
                    existing.setDescripcion(request.getDescripcion());
                    existing.setMontoReclamado(request.getMontoReclamado());
                    existing.setResultado(request.getResultado());
                    existing.setActivo(request.getActivo());
                    if (request.getTipoConflicto() != null && request.getTipoConflicto().getId() != null) {
                        tipoConflictoRepository.findById(request.getTipoConflicto().getId())
                                .ifPresent(existing::setTipoConflicto);
                    }
                    if (request.getEstadoConflicto() != null && request.getEstadoConflicto().getId() != null) {
                        estadoConflictoRepository.findById(request.getEstadoConflicto().getId())
                                .ifPresent(existing::setEstadoConflicto);
                    }
                    if (request.getUsuarioDemandante() != null && request.getUsuarioDemandante().getId() != null) {
                        usuarioRepository.findById(request.getUsuarioDemandante().getId())
                                .ifPresent(existing::setUsuarioDemandante);
                    }
                    if (request.getUsuarioDemandado() != null && request.getUsuarioDemandado().getId() != null) {
                        usuarioRepository.findById(request.getUsuarioDemandado().getId())
                                .ifPresent(existing::setUsuarioDemandado);
                    }
                    return ResponseEntity.ok(conflictoRepository.save(existing));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        return conflictoRepository.findById(id)
                .map(existing -> {
                    conflictoRepository.delete(existing);
                    return ResponseEntity.noContent().<Void>build();
                })
                .orElse(ResponseEntity.notFound().build());
    }
}
