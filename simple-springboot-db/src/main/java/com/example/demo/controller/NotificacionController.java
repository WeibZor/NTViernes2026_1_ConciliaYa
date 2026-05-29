package com.example.demo.controller;

import com.example.demo.model.Notificacion;
import com.example.demo.service.NotificacionService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/notificaciones")
public class NotificacionController {

    private final NotificacionService notificacionService;

    public NotificacionController(NotificacionService notificacionService) {
        this.notificacionService = notificacionService;
    }

    @GetMapping
    public List<Notificacion> getAll() {
        return notificacionService.findAll();
    }

    @GetMapping("/usuario/{usuarioId}")
    public List<Notificacion> getByUsuario(@PathVariable Long usuarioId) {
        return notificacionService.findByUsuarioId(usuarioId);
    }
}
