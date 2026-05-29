package com.example.demo.service;

import com.example.demo.model.Publicacion;
import com.example.demo.repository.PublicacionRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PublicacionService {

    private final PublicacionRepository publicacionRepository;

    public PublicacionService(PublicacionRepository publicacionRepository) {
        this.publicacionRepository = publicacionRepository;
    }

    public List<Publicacion> findAll() { return publicacionRepository.findAll(); }
    public Optional<Publicacion> findById(Long id) { return publicacionRepository.findById(id); }
    public Publicacion save(Publicacion publicacion) { return publicacionRepository.save(publicacion); }
    public void deleteById(Long id) { publicacionRepository.deleteById(id); }
}
