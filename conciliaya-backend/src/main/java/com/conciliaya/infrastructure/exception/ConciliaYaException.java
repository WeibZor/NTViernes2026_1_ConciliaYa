package com.conciliaya.infrastructure.exception;

/**
 * Excepción base para el dominio de ConciliaYa.
 */
public class ConciliaYaException extends RuntimeException {

    private final String codigo;

    public ConciliaYaException(String mensaje) {
        super(mensaje);
        this.codigo = "GENERIC_ERROR";
    }

    public ConciliaYaException(String codigo, String mensaje) {
        super(mensaje);
        this.codigo = codigo;
    }

    public ConciliaYaException(String codigo, String mensaje, Throwable causa) {
        super(mensaje, causa);
        this.codigo = codigo;
    }

    public String getCodigo() {
        return codigo;
    }
}
