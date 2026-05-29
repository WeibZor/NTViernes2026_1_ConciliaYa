package com.example.demo.service;

import com.example.demo.model.Usuario;
import com.example.demo.repository.UsuarioRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UsuarioService {

    private final UsuarioRepository usuarioRepository;

    public UsuarioService(UsuarioRepository usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
    }

    public List<Usuario> findAll() { return usuarioRepository.findAll(); }
    public Optional<Usuario> findById(Long id) { return usuarioRepository.findById(id); }
    public Optional<Usuario> findByCorreo(String correo) { return usuarioRepository.findByCorreo(correo); }
    public Usuario save(Usuario usuario) { return usuarioRepository.save(usuario); }
    public void deleteById(Long id) { usuarioRepository.deleteById(id); }
}
