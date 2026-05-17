package com.example.demo.controller;

import com.example.demo.dto.PerfilDto;
import com.example.demo.model.Perfil;
import com.example.demo.service.PerfilService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/perfiles")
public class PerfilController {

    private final PerfilService perfilService;

    public PerfilController(PerfilService perfilService) {
        this.perfilService = perfilService;
    }

    @GetMapping
    public List<PerfilDto> getAll() {
        return perfilService.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public ResponseEntity<PerfilDto> getById(@PathVariable Long id) {
        return perfilService.findById(id)
                .map(this::toDto)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<PerfilDto> create(@RequestBody PerfilDto dto) {
        Perfil perfil = fromDto(dto);
        Perfil saved = perfilService.save(perfil);
        return ResponseEntity.ok(toDto(saved));
    }

    @PutMapping("/{id}")
    public ResponseEntity<PerfilDto> update(@PathVariable Long id, @RequestBody PerfilDto dto) {
        return perfilService.findById(id)
                .map(existing -> {
                    existing.setNombre(dto.getNombre());
                    existing.setDescripcion(dto.getDescripcion());
                    existing.setActivo(dto.getActivo());
                    Perfil updated = perfilService.save(existing);
                    return ResponseEntity.ok(toDto(updated));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (perfilService.findById(id).isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        perfilService.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    private PerfilDto toDto(Perfil perfil) {
        PerfilDto dto = new PerfilDto();
        dto.setId(perfil.getId());
        dto.setNombre(perfil.getNombre());
        dto.setDescripcion(perfil.getDescripcion());
        dto.setActivo(perfil.getActivo());
        return dto;
    }

    private Perfil fromDto(PerfilDto dto) {
        Perfil perfil = new Perfil();
        perfil.setNombre(dto.getNombre());
        perfil.setDescripcion(dto.getDescripcion());
        perfil.setActivo(dto.getActivo() == null ? true : dto.getActivo());
        return perfil;
    }
}
