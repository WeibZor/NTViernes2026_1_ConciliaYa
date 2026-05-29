package com.example.demo.service;

import com.example.demo.model.Mediacion;
import com.example.demo.repository.MediacionRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MediacionService {

    private final MediacionRepository mediacionRepository;

    public MediacionService(MediacionRepository mediacionRepository) {
        this.mediacionRepository = mediacionRepository;
    }

    public List<Mediacion> findAll() { return mediacionRepository.findAll(); }
    public Optional<Mediacion> findById(Long id) { return mediacionRepository.findById(id); }
    public Mediacion save(Mediacion mediacion) { return mediacionRepository.save(mediacion); }
    public void deleteById(Long id) { mediacionRepository.deleteById(id); }
}
