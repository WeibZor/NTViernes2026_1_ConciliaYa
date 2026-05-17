package com.example.demo.controller;

import com.example.demo.dto.TipoConflictoDto;
import com.example.demo.model.TipoConflicto;
import com.example.demo.service.TipoConflictoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/tipos-conflicto")
public class TipoConflictoController {

    private final TipoConflictoService tipoConflictoService;

    public TipoConflictoController(TipoConflictoService tipoConflictoService) {
        this.tipoConflictoService = tipoConflictoService;
    }

    @GetMapping
    public List<TipoConflictoDto> getAll() {
        return tipoConflictoService.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public ResponseEntity<TipoConflictoDto> getById(@PathVariable Long id) {
        return tipoConflictoService.findById(id)
                .map(this::toDto)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<TipoConflictoDto> create(@RequestBody TipoConflictoDto dto) {
        TipoConflicto saved = tipoConflictoService.save(fromDto(dto));
        return ResponseEntity.ok(toDto(saved));
    }

    @PutMapping("/{id}")
    public ResponseEntity<TipoConflictoDto> update(@PathVariable Long id, @RequestBody TipoConflictoDto dto) {
        return tipoConflictoService.findById(id)
                .map(existing -> {
                    existing.setNombre(dto.getNombre());
                    existing.setDescripcion(dto.getDescripcion());
                    existing.setActivo(dto.getActivo());
                    TipoConflicto updated = tipoConflictoService.save(existing);
                    return ResponseEntity.ok(toDto(updated));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (tipoConflictoService.findById(id).isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        tipoConflictoService.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    private TipoConflictoDto toDto(TipoConflicto entity) {
        TipoConflictoDto dto = new TipoConflictoDto();
        dto.setId(entity.getId());
        dto.setNombre(entity.getNombre());
        dto.setDescripcion(entity.getDescripcion());
        dto.setActivo(entity.getActivo());
        return dto;
    }

    private TipoConflicto fromDto(TipoConflictoDto dto) {
        TipoConflicto entity = new TipoConflicto();
        entity.setNombre(dto.getNombre());
        entity.setDescripcion(dto.getDescripcion());
        entity.setActivo(dto.getActivo() == null ? true : dto.getActivo());
        return entity;
    }
}
