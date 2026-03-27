package com.conciliaya.domain.usecase;

import com.conciliaya.domain.model.Conflicto;
import com.conciliaya.domain.model.Mediacion;
import com.conciliaya.domain.model.Usuario;
import com.conciliaya.domain.ports.MediacionRepositoryPort;
import java.time.LocalDateTime;

/**
 * Caso de uso para asignar una mediación a un conflicto.
 * Responsabilidades:
 * - Validar que el conflicto existe
 * - Validar que el mediador es válido
 * - Crear y guardar la mediación
 */
public class AsignarMediacionUseCase {

    private final MediacionRepositoryPort mediacionRepository;

    public AsignarMediacionUseCase(MediacionRepositoryPort mediacionRepository) {
        this.mediacionRepository = mediacionRepository;
    }

    /**
     * Ejecuta el caso de uso de asignar mediación.
     * 
     * @param conflicto el conflicto a mediar
     * @param mediador el usuario mediador
     * @return la mediación creada
     * @throws IllegalArgumentException si los datos son inválidos
     */
    public Mediacion ejecutar(Conflicto conflicto, Usuario mediador) {
        // Validaciones
        validarDatos(conflicto, mediador);

        // Crear mediación
        Mediacion mediacion = new Mediacion(conflicto, mediador);
        mediacion.setFechaActualizacion(LocalDateTime.now());

        // Guardar y retornar
        return mediacionRepository.save(mediacion);
    }

    /**
     * Finaliza una mediación con resultado y acuerdos.
     * 
     * @param mediacionId el ID de la mediación
     * @param resultado el resultado de la mediación
     * @param acuerdos los acuerdos alcanzados
     * @return la mediación finalizada
     */
    public Mediacion finalizarMediacion(Long mediacionId, String resultado, String acuerdos) {
        validarId(mediacionId);
        
        Mediacion mediacion = mediacionRepository.findById(mediacionId)
                .orElseThrow(() -> new IllegalArgumentException("Mediación no encontrada: " + mediacionId));

        mediacion.setResultado(resultado);
        mediacion.setAcuerdos(acuerdos);
        mediacion.setFechaFinalizacion(LocalDateTime.now());
        mediacion.setCompletada(true);
        mediacion.setFechaActualizacion(LocalDateTime.now());

        return mediacionRepository.save(mediacion);
    }

    /**
     * Valida que los datos sean correctos.
     */
    private void validarDatos(Conflicto conflicto, Usuario mediador) {
        if (conflicto == null) {
            throw new IllegalArgumentException("El conflicto es requerido");
        }
        if (conflicto.getId() == null) {
            throw new IllegalArgumentException("El conflicto debe estar registrado en la base de datos");
        }
        if (mediador == null) {
            throw new IllegalArgumentException("El mediador es requerido");
        }
        if (mediador.getId() == null) {
            throw new IllegalArgumentException("El mediador debe estar registrado en la base de datos");
        }
    }

    /**
     * Valida que el ID sea válido.
     */
    private void validarId(Long id) {
        if (id == null || id <= 0) {
            throw new IllegalArgumentException("ID inválido: " + id);
        }
    }
}
