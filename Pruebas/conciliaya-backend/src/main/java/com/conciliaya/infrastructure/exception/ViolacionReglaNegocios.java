package com.conciliaya.infrastructure.exception;

/**
 * Excepción lanzada cuando hay una violación de regla de negocio.
 */
public class ViolacionReglaNegocios extends ConciliaYaException {
    
    public ViolacionReglaNegocios(String mensaje) {
        super("VIOLACION_REGLA_NEGOCIOS", mensaje);
    }

    public ViolacionReglaNegocios(String codigo, String mensaje) {
        super(codigo, mensaje);
    }
}
