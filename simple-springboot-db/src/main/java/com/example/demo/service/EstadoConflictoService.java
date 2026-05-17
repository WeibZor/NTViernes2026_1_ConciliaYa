package com.example.demo.service;

import com.example.demo.model.EstadoConflicto;
import com.example.demo.repository.EstadoConflictoRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class EstadoConflictoService {

    private final EstadoConflictoRepository estadoConflictoRepository;

    public EstadoConflictoService(EstadoConflictoRepository estadoConflictoRepository) {
        this.estadoConflictoRepository = estadoConflictoRepository;
    }

    public List<EstadoConflicto> findAll() {
        return estadoConflictoRepository.findAll();
    }

    public Optional<EstadoConflicto> findById(Long id) {
        return estadoConflictoRepository.findById(id);
    }

    public EstadoConflicto save(EstadoConflicto estadoConflicto) {
        return estadoConflictoRepository.save(estadoConflicto);
    }

    public void deleteById(Long id) {
        estadoConflictoRepository.deleteById(id);
    }
}
