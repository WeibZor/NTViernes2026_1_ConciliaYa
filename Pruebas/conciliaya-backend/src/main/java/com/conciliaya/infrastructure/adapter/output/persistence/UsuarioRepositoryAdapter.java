package com.conciliaya.infrastructure.adapter.output.persistence;

import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.ports.UsuarioRepositoryPort;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

/**
 * Adaptador que implementa el puerto UsuarioRepositoryPort.
 * Responsable de adaptar las operaciones de dominio a JPA.
 * Convierte entre entidades de dominio (Usuario) y entidades JPA (UsuarioEntity).
 */
@Component
public class UsuarioRepositoryAdapter implements UsuarioRepositoryPort {

    private final UsuarioJpaRepository jpaRepository;

    public UsuarioRepositoryAdapter(UsuarioJpaRepository jpaRepository) {
        this.jpaRepository = jpaRepository;
    }

    @Override
    public Usuario save(Usuario usuario) {
        UsuarioEntity entity = mapearAEntity(usuario);
        UsuarioEntity guardada = jpaRepository.save(entity);
        return mapearADominio(guardada);
    }

    @Override
    public Optional<Usuario> findById(Long id) {
        return jpaRepository.findById(id).map(this::mapearADominio);
    }

    @Override
    public List<Usuario> findAllActivos() {
        return jpaRepository.findByActivoTrue()
                .stream()
                .map(this::mapearADominio)
                .toList();
    }

    @Override
    public Optional<Usuario> findByEmail(String email) {
        return jpaRepository.findByEmail(email).map(this::mapearADominio);
    }

    @Override
    public Optional<Usuario> findByNumeroDocumento(String numeroDocumento) {
        return jpaRepository.findByNumeroDocumento(numeroDocumento).map(this::mapearADominio);
    }

    @Override
    public void deleteById(Long id) {
        jpaRepository.deleteById(id);
    }

    @Override
    public long countActivos() {
        return jpaRepository.countByActivoTrue();
    }

    /**
     * Convierte una entidad de dominio a entidad JPA.
     */
    private UsuarioEntity mapearAEntity(Usuario usuario) {
        UsuarioEntity entity = new UsuarioEntity();
        if (usuario.getId() != null) {
            entity.setId(usuario.getId());
        }
        entity.setNombre(usuario.getNombre());
        entity.setApellido(usuario.getApellido());
        entity.setEmail(usuario.getEmail());
        entity.setTelefono(usuario.getTelefono());
        entity.setDireccion(usuario.getDireccion());
        entity.setNumeroDocumento(usuario.getNumeroDocumento());
        entity.setActivo(usuario.getActivo());
        entity.setFechaCreacion(usuario.getFechaCreacion());
        entity.setFechaActualizacion(usuario.getFechaActualizacion());
        return entity;
    }

    /**
     * Convierte una entidad JPA a entidad de dominio.
     */
    private Usuario mapearADominio(UsuarioEntity entity) {
        Usuario usuario = new Usuario();
        usuario.setId(entity.getId());
        usuario.setNombre(entity.getNombre());
        usuario.setApellido(entity.getApellido());
        usuario.setEmail(entity.getEmail());
        usuario.setTelefono(entity.getTelefono());
        usuario.setDireccion(entity.getDireccion());
        usuario.setNumeroDocumento(entity.getNumeroDocumento());
        usuario.setActivo(entity.getActivo());
        usuario.setFechaCreacion(entity.getFechaCreacion());
        usuario.setFechaActualizacion(entity.getFechaActualizacion());
        return usuario;
    }
}
