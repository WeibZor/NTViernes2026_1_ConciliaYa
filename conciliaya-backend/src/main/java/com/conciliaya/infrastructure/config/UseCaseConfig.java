package com.conciliaya.infrastructure.config;

import com.conciliaya.domain.ports.ClasificadorConflictoPort;
import com.conciliaya.domain.ports.ConflictoRepositoryPort;
import com.conciliaya.domain.ports.MediacionRepositoryPort;
import com.conciliaya.domain.ports.UsuarioRepositoryPort;
import com.conciliaya.domain.usecase.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Configuración de los casos de uso e inyección de dependencias.
 * Define los beans para los casos de uso que serán inyectados en los controladores.
 */
@Configuration
public class UseCaseConfig {

    /**
     * Caso de uso para crear conflictos.
     */
    @Bean
    public CrearConflictoUseCase crearConflictoUseCase(
            ConflictoRepositoryPort conflictoRepository,
            ClasificadorConflictoPort clasificador) {
        return new CrearConflictoUseCase(conflictoRepository, clasificador);
    }

    /**
     * Caso de uso para obtener conflictos.
     */
    @Bean
    public ObtenerConflictosUseCase obtenerConflictosUseCase(
            ConflictoRepositoryPort conflictoRepository) {
        return new ObtenerConflictosUseCase(conflictoRepository);
    }

    /**
     * Caso de uso para actualizar estado de conflictos.
     */
    @Bean
    public ActualizarEstadoConflictoUseCase actualizarEstadoConflictoUseCase(
            ConflictoRepositoryPort conflictoRepository) {
        return new ActualizarEstadoConflictoUseCase(conflictoRepository);
    }

    /**
     * Caso de uso para asignar mediaciones.
     */
    @Bean
    public AsignarMediacionUseCase asignarMediacionUseCase(
            MediacionRepositoryPort mediacionRepository) {
        return new AsignarMediacionUseCase(mediacionRepository);
    }
}
