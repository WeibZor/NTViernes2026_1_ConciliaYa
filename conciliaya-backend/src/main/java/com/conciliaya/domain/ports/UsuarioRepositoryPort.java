package com.conciliaya.domain.ports;

import com.conciliaya.domain.model.Usuario;
import java.util.List;
import java.util.Optional;

/**
 * Puerto (interfaz) para operaciones de Usuario.
 * Define el contrato que los adaptadores deben implementar.
 * Separa la lógica de negocio de la implementación específica de persistencia.
 */
public interface UsuarioRepositoryPort {

    /**
     * Guarda un nuevo usuario o actualiza uno existente.
     * @param usuario el usuario a guardar
     * @return el usuario guardado
     */
    Usuario save(Usuario usuario);

    /**
     * Busca un usuario por su ID.
     * @param id el ID del usuario
     * @return un Optional con el usuario si existe
     */
    Optional<Usuario> findById(Long id);

    /**
     * Obtiene todos los usuarios activos.
     * @return lista de usuarios activos
     */
    List<Usuario> findAllActivos();

    /**
     * Busca un usuario por su email.
     * @param email el email del usuario
     * @return un Optional con el usuario si existe
     */
    Optional<Usuario> findByEmail(String email);

    /**
     * Busca usuarios por número de documento.
     * @param numeroDocumento el número de documento
     * @return un Optional con el usuario si existe
     */
    Optional<Usuario> findByNumeroDocumento(String numeroDocumento);

    /**
     * Elimina un usuario.
     * @param id el ID del usuario a eliminar
     */
    void deleteById(Long id);

    /**
     * Cuenta el total de usuarios activos.
     * @return cantidad de usuarios activos
     */
    long countActivos();
}
