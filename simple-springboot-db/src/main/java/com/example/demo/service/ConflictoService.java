package com.example.demo.service;

import com.example.demo.model.Conflicto;
import com.example.demo.repository.ConflictoRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ConflictoService {

    private final ConflictoRepository conflictoRepository;

    public ConflictoService(ConflictoRepository conflictoRepository) {
        this.conflictoRepository = conflictoRepository;
    }

    public List<Conflicto> findAll() { return conflictoRepository.findAll(); }
    public Optional<Conflicto> findById(Long id) { return conflictoRepository.findById(id); }
    public Conflicto save(Conflicto conflicto) { return conflictoRepository.save(conflicto); }
    public void deleteById(Long id) { conflictoRepository.deleteById(id); }
}
