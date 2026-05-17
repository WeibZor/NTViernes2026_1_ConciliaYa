package com.example.demo.service;

import com.example.demo.model.TipoConflicto;
import com.example.demo.repository.TipoConflictoRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TipoConflictoService {

    private final TipoConflictoRepository tipoConflictoRepository;

    public TipoConflictoService(TipoConflictoRepository tipoConflictoRepository) {
        this.tipoConflictoRepository = tipoConflictoRepository;
    }

    public List<TipoConflicto> findAll() {
        return tipoConflictoRepository.findAll();
    }

    public Optional<TipoConflicto> findById(Long id) {
        return tipoConflictoRepository.findById(id);
    }

    public TipoConflicto save(TipoConflicto tipoConflicto) {
        return tipoConflictoRepository.save(tipoConflicto);
    }

    public void deleteById(Long id) {
        tipoConflictoRepository.deleteById(id);
    }
}
