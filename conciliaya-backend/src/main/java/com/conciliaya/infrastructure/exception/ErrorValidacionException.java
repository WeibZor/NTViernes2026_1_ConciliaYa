package com.conciliaya.infrastructure.exception;

/**
 * Excepción lanzada cuando hay error de validación en los datos.
 */
public class ErrorValidacionException extends ConciliaYaException {
    
    private final java.util.Map<String, String> errores;

    public ErrorValidacionException(String mensaje) {
        super("ERROR_VALIDACION", mensaje);
        this.errores = new java.util.HashMap<>();
    }

    public ErrorValidacionException(String mensaje, java.util.Map<String, String> errores) {
        super("ERROR_VALIDACION", mensaje);
        this.errores = errores;
    }

    public java.util.Map<String, String> getErrores() {
        return errores;
    }
}
