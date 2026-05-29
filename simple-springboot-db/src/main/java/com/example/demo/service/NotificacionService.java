package com.example.demo.service;

import com.example.demo.model.Notificacion;
import com.example.demo.repository.NotificacionRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NotificacionService {

    private final NotificacionRepository notificacionRepository;

    public NotificacionService(NotificacionRepository notificacionRepository) {
        this.notificacionRepository = notificacionRepository;
    }

    public List<Notificacion> findAll() { return notificacionRepository.findAll(); }
    public List<Notificacion> findByUsuarioId(Long usuarioId) { return notificacionRepository.findByUsuarioId(usuarioId); }
    public Notificacion save(Notificacion notificacion) { return notificacionRepository.save(notificacion); }
}
