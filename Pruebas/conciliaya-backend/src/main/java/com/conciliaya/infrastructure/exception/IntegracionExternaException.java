package com.conciliaya.infrastructure.exception;

/**
 * Excepción lanzada cuando hay error en la integración con servicios externos.
 */
public class IntegracionExternaException extends ConciliaYaException {
    
    public IntegracionExternaException(String servicio, String mensaje) {
        super("ERROR_INTEGRACION_EXTERNA", 
              String.format("Error en servicio externo '%s': %s", servicio, mensaje));
    }

    public IntegracionExternaException(String servicio, String mensaje, Throwable causa) {
        super("ERROR_INTEGRACION_EXTERNA",
              String.format("Error en servicio externo '%s': %s", servicio, mensaje),
              causa);
    }
}
