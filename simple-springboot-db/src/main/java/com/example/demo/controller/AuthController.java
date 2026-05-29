package com.example.demo.controller;

import com.example.demo.dto.AuthResponse;
import com.example.demo.dto.LoginRequest;
import com.example.demo.dto.RegisterRequest;
import com.example.demo.model.Perfil;
import com.example.demo.model.Usuario;
import com.example.demo.repository.PerfilRepository;
import com.example.demo.repository.UsuarioRepository;
import com.example.demo.security.JwtUtil;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final UsuarioRepository usuarioRepository;
    private final PerfilRepository perfilRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;

    public AuthController(UsuarioRepository usuarioRepository,
                          PerfilRepository perfilRepository,
                          PasswordEncoder passwordEncoder,
                          JwtUtil jwtUtil) {
        this.usuarioRepository = usuarioRepository;
        this.perfilRepository = perfilRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtUtil = jwtUtil;
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@Valid @RequestBody LoginRequest request) {
        return usuarioRepository.findByCorreo(request.getCorreo())
                .map(user -> {
                    if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
                        return ResponseEntity.status(401).body("Contraseña incorrecta");
                    }
                    Long perfilId = user.getPerfil() != null ? user.getPerfil().getId() : null;
                    String token = jwtUtil.generateToken(user.getId(), perfilId);
                    return ResponseEntity.ok(new AuthResponse(
                            token, user.getId(),
                            user.getNombre() + " " + user.getApellido(),
                            user.getCorreo(), perfilId));
                })
                .orElse(ResponseEntity.status(401).body("Usuario no encontrado"));
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@Valid @RequestBody RegisterRequest request) {
        if (usuarioRepository.existsByCorreo(request.getCorreo())) {
            return ResponseEntity.badRequest().body("El correo ya está registrado");
        }

        // Perfil por defecto: id=3 (usuario normal), o el primero disponible
        Perfil perfilDefault = perfilRepository.findById(3L)
                .orElse(perfilRepository.findAll().stream().findFirst().orElse(null));

        Usuario usuario = new Usuario();
        usuario.setNombre(request.getNombre());
        usuario.setApellido(request.getApellido());
        usuario.setCorreo(request.getCorreo());
        usuario.setPassword(passwordEncoder.encode(request.getPassword()));
        usuario.setPerfil(perfilDefault);

        Usuario saved = usuarioRepository.save(usuario);
        Long perfilId = saved.getPerfil() != null ? saved.getPerfil().getId() : null;
        String token = jwtUtil.generateToken(saved.getId(), perfilId);

        return ResponseEntity.status(201).body(new AuthResponse(
                token, saved.getId(),
                saved.getNombre() + " " + saved.getApellido(),
                saved.getCorreo(), perfilId));
    }
}
