package com.example.demo.controller;

import com.example.demo.dto.EstadoConflictoDto;
import com.example.demo.model.EstadoConflicto;
import com.example.demo.service.EstadoConflictoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/estados-conflicto")
public class EstadoConflictoController {

    private final EstadoConflictoService estadoConflictoService;

    public EstadoConflictoController(EstadoConflictoService estadoConflictoService) {
        this.estadoConflictoService = estadoConflictoService;
    }

    @GetMapping
    public List<EstadoConflictoDto> getAll() {
        return estadoConflictoService.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public ResponseEntity<EstadoConflictoDto> getById(@PathVariable Long id) {
        return estadoConflictoService.findById(id)
                .map(this::toDto)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<EstadoConflictoDto> create(@RequestBody EstadoConflictoDto dto) {
        EstadoConflicto saved = estadoConflictoService.save(fromDto(dto));
        return ResponseEntity.ok(toDto(saved));
    }

    @PutMapping("/{id}")
    public ResponseEntity<EstadoConflictoDto> update(@PathVariable Long id, @RequestBody EstadoConflictoDto dto) {
        return estadoConflictoService.findById(id)
                .map(existing -> {
                    existing.setNombre(dto.getNombre());
                    existing.setCodigo(dto.getCodigo());
                    existing.setDescripcion(dto.getDescripcion());
                    existing.setActivo(dto.getActivo());
                    EstadoConflicto updated = estadoConflictoService.save(existing);
                    return ResponseEntity.ok(toDto(updated));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (estadoConflictoService.findById(id).isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        estadoConflictoService.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    private EstadoConflictoDto toDto(EstadoConflicto entity) {
        EstadoConflictoDto dto = new EstadoConflictoDto();
        dto.setId(entity.getId());
        dto.setNombre(entity.getNombre());
        dto.setCodigo(entity.getCodigo());
        dto.setDescripcion(entity.getDescripcion());
        dto.setActivo(entity.getActivo());
        return dto;
    }

    private EstadoConflicto fromDto(EstadoConflictoDto dto) {
        EstadoConflicto entity = new EstadoConflicto();
        entity.setNombre(dto.getNombre());
        entity.setCodigo(dto.getCodigo());
        entity.setDescripcion(dto.getDescripcion());
        entity.setActivo(dto.getActivo() == null ? true : dto.getActivo());
        return entity;
    }
}
